@echo off
setlocal
cd /d "%~dp0"
set "PYRUN="
py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
if not errorlevel 1 set "PYRUN=py -3"
if defined PYRUN goto ready
python -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
if not errorlevel 1 set "PYRUN=python"
if defined PYRUN goto ready
echo Python 3.10 or newer was not found. No settings were changed.
echo See START_HERE.md for the requirements.
pause
exit /b 2
:ready
%PYRUN% room_tools.py verify
pause
