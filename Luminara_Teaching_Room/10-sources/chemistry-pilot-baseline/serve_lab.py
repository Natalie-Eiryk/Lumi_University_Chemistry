#!/usr/bin/env python3
"""Small, read-only, loopback-only host for the Luminara Bioethics lab.

Python 3.10+; standard library only. Does not touch browser profiles, learner
records, registry keys, firewall rules, or browser policy. No directory server.
The immutable app snapshot is taken at startup; restart after an app update.
"""
from __future__ import annotations
import argparse
import hashlib
import http.server
import json
import os
from pathlib import Path
import socket
import sys
import threading
import urllib.error
import urllib.request
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = '127.0.0.1'
PORT = 47831  # Keep this stable: the port is part of the browser storage origin.
ORIGIN = f'http://{HOST}:{PORT}'
APP_PATH = '/bioethics/'
APP_ID = 'luminara-bioethics-stable-local'
RELEASE = '1.2.0-chemistry-pilot'
STATE_KEYS = (
    'luminara-key-terms-ch1-3-v1',
    'luminara-bioethics-cases-1-4-v1',
    'luminara-learning-circuits-v1',
    'luminara-principle-observatory-v1',
    'luminara-bioethics-context-reader-v1',
    'luminara-bioethics-beside-v1',
)
CSP = ("default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; "
       "img-src data:; connect-src 'none'; font-src 'none'; object-src 'none'; "
       "base-uri 'none'; form-action 'none'; frame-ancestors 'none'")


def app_metadata(payload: bytes, root: Path = ROOT) -> dict:
    return {
        'application': APP_ID, 'launcherVersion': RELEASE,
        'origin': ORIGIN, 'appPath': APP_PATH,
        'htmlSha256': hashlib.sha256(payload).hexdigest(),
        'installationId': hashlib.sha256(str(root.resolve()).encode()).hexdigest()[:24],
        'backend': 'native browser localStorage; no server-side learner database',
        'stateKeys': list(STATE_KEYS), 'readOnlyServer': True,
        'policyChanges': False, 'lumiOsIntegrated': False,
    }


def load_resources(root: Path = ROOT) -> tuple[dict, dict]:
    app = (root / 'web' / 'index.html').read_bytes()
    if not app or len(app) > 20 * 1024 * 1024:
        raise ValueError('Missing or oversized study application.')
    metadata = app_metadata(app, root)
    room = (root / 'web' / 'room.html').read_bytes()
    if not room or len(room) > 2 * 1024 * 1024:
        raise ValueError('Missing or oversized teaching room.')
    metadata['teachingRoomPath'] = '/room/'
    metadata['roomSha256'] = hashlib.sha256(room).hexdigest()
    metadata['privateArchiveRoutes'] = False
    chemistry_file = root / 'web' / 'chemistry.html'
    chemistry = chemistry_file.read_bytes() if chemistry_file.is_file() else b''
    if len(chemistry) > 2 * 1024 * 1024:
        raise ValueError('Oversized chemistry pilot.')
    metadata['chemistryPath'] = '/chemistry/' if chemistry else None
    metadata['chemistryHtmlSha256'] = hashlib.sha256(chemistry).hexdigest() if chemistry else None
    metadata['chemistryStateKey'] = 'luminara-chem1117-workbook-pilot-v1' if chemistry else None
    metadata['chemistrySourceScope'] = 'One recovered workbook; requested Windows folder not inspected' if chemistry else None
    source = root / '30-modules' / '174.2-bioethics' / 'source' / 'index.html'
    metadata['sourceHtmlSha256'] = hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None
    metadata['sourceMatchesServedApp'] = metadata['sourceHtmlSha256'] == metadata['htmlSha256'] if metadata['sourceHtmlSha256'] else None
    metadata['resourceBundleSha256'] = hashlib.sha256(app + room + (root / 'web' / 'diagnostics.html').read_bytes() + chemistry).hexdigest()
    resources = {
        APP_PATH: ('text/html; charset=utf-8', app),
        '/room/': ('text/html; charset=utf-8', room),
        '/diagnostics/': ('text/html; charset=utf-8', (root / 'web' / 'diagnostics.html').read_bytes()),
        '/health': ('application/json; charset=utf-8', json.dumps(metadata).encode()),
        '/favicon.ico': ('image/x-icon', b''),
    }
    if chemistry:
        resources['/chemistry/'] = ('text/html; charset=utf-8', chemistry)
    return resources, metadata


class LocalServer(http.server.ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = os.name != 'nt'

    def server_bind(self) -> None:
        # A second process must not share our fixed Windows port.
        if os.name == 'nt' and hasattr(socket, 'SO_EXCLUSIVEADDRUSE'):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def make_server(root: Path = ROOT, port: int = PORT) -> LocalServer:
    resources, metadata = load_resources(root)
    # port=0 exists only for isolated server tests, never a launcher fallback.
    class Handler(http.server.BaseHTTPRequestHandler):
        server_version = 'LuminaraLocal/1'
        sys_version = ''
        protocol_version = 'HTTP/1.0'

        def setup(self) -> None:
            super().setup()
            self.connection.settimeout(10)

        def log_message(self, fmt: str, *args: object) -> None:
            # Do not record full request URLs or personal local paths.
            return

        def reply(self, status: int, content: bytes = b'', mime: str = 'text/plain; charset=utf-8', location: str | None = None) -> None:
            self.send_response(status)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('Content-Security-Policy', CSP)
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('Cross-Origin-Resource-Policy', 'same-origin')
            self.send_header('Permissions-Policy', 'camera=(), microphone=(), geolocation=()')
            if location is not None:
                self.send_header('Location', location)
            self.end_headers()
            if self.command != 'HEAD' and content:
                self.wfile.write(content)

        def get(self) -> None:
            authority = f'{HOST}:{self.server.server_port}'
            if self.headers.get_all('Host', []) != [authority]:
                self.reply(403, b'Use the launcher address exactly; hostname aliases are not accepted.')
                return
            # Fail closed on cross-site embedding. No cross-origin read/write API.
            if self.headers.get('Sec-Fetch-Site') == 'cross-site' and self.headers.get('Sec-Fetch-Mode') != 'navigate':
                self.reply(403, b'Cross-site resource request refused.')
                return
            if self.path in ('/', '/bioethics', '/bioethics/index.html', '/index.html'):
                self.reply(302, location=APP_PATH)
                return
            if self.path in ('/room', '/room/index.html'):
                self.reply(302, location='/room/')
                return
            if self.path in ('/chemistry', '/chemistry/index.html') and '/chemistry/' in resources:
                self.reply(302, location='/chemistry/')
                return
            if self.path == '/diagnostics':
                self.reply(302, location='/diagnostics/')
                return
            # No path-to-disk conversion, URL unquoting, directory listing or symlink traversal.
            item = resources.get(self.path)
            if item is None:
                self.reply(404, b'Not a published lab resource.')
                return
            mime, content = item
            self.reply(204 if self.path == '/favicon.ico' else 200, content, mime)

        def do_GET(self) -> None:
            self.get()

        def do_HEAD(self) -> None:
            self.get()

        def unsupported(self) -> None:
            self.reply(405, b'This local host does not accept writes.')

        do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = unsupported

    server = LocalServer((HOST, port), Handler)
    server.metadata = metadata
    return server


def running_instance(expected: dict) -> tuple[bool, str]:
    # Never use configured HTTP proxies for a loopback health check.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(ORIGIN + '/health', timeout=2) as response:
            payload = response.read(32769)
        if len(payload) > 32768:
            return False, 'Unexpected service response.'
        actual = json.loads(payload)
        if not isinstance(actual, dict):
            return False, 'Unexpected service response.'
        if actual.get('application') != APP_ID:
            return False, 'Another application uses the fixed port.'
        if actual.get('installationId') != expected['installationId']:
            return False, 'A different lab folder is running. Stop its launcher first.'
        if actual.get('htmlSha256') != expected['htmlSha256']:
            return False, 'An older app snapshot is running. Stop that launcher and start again.'
        if actual.get('resourceBundleSha256') != expected.get('resourceBundleSha256'):
            return False, 'An older room or diagnostic snapshot is running. Stop its launcher first.'
        return True, 'The same installation and exact served resources are already running.'
    except (OSError, ValueError, urllib.error.URLError):
        return False, 'The fixed port is busy or unavailable; no matching lab was identified.'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics', action='store_true', help='Open the native storage check instead of the study page.')
    parser.add_argument('--room', action='store_true', help='Open the unified teaching room; the lab keeps its existing address.')
    parser.add_argument('--chemistry', action='store_true', help='Open the source-limited chemistry pilot.')
    parser.add_argument('--no-browser', action='store_true', help='Start the host and print its address only.')
    args = parser.parse_args()
    if sum((args.room, args.diagnostics, args.chemistry)) > 1:
        parser.error('Choose exactly one opening view.')
    from room_tools import require_external_room
    try:
        require_external_room(ROOT)
    except ValueError as exc:
        parser.error(str(exc))
    try:
        _, expected = load_resources()
    except (OSError, ValueError) as exc:
        print(f'Cannot load the complete package; extract all files first: {exc}', file=sys.stderr)
        return 2
    if args.chemistry and expected.get('chemistryPath') is None:
        print('Chemistry pilot missing. Extract the full updated package.', file=sys.stderr)
        return 2
    try:
        server = make_server()
    except OSError as exc:
        ok, detail = running_instance(expected)
        print(detail)
        if ok:
            if not args.no_browser:
                webbrowser.open(ORIGIN + ('/diagnostics/' if args.diagnostics else '/room/' if args.room else '/chemistry/' if args.chemistry else APP_PATH))
            return 0
        print(f'No settings were changed and no alternative port was selected. Detail: {exc}', file=sys.stderr)
        return 2
    target = ORIGIN + ('/diagnostics/' if args.diagnostics else '/room/' if args.room else '/chemistry/' if args.chemistry else APP_PATH)
    print('\nMS. LUMINARA - stable local study home')
    print(f'Teaching:    {ORIGIN}/room/')
    print(f'Study:       {ORIGIN}{APP_PATH}')
    print(f'Chemistry:   {ORIGIN}/chemistry/')
    print(f'Save check:  {ORIGIN}/diagnostics/')
    print(f'HTML SHA256: {expected["htmlSha256"]}')
    print('\nUse the same regular browser/profile each time. Import your private backup once.')
    print('Keep this window open while studying. Ctrl+C stops the host.')
    print('No cloud, no policy changes, no automatic learner-data uploads.\n', flush=True)
    if not args.no_browser:
        threading.Timer(0.35, lambda: webbrowser.open(target)).start()
    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        print('\nLocal host stopped. Browser-stored notes were not deleted.')
    finally:
        server.server_close()
    return 0

if __name__ == '__main__':
    if sys.version_info < (3, 10):
        raise SystemExit('Python 3.10 or newer is required.')
    raise SystemExit(main())
