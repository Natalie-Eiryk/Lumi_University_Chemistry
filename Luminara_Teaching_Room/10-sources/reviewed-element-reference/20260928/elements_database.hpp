/**
 * @file elements_database.hpp
 * @brief Complete Periodic Table Database
 * @codon 924.00
 *
 * THE TRICORDER MANDATE: All C++ files integrate with the tricorder system.
 * Reports: element properties, orbital occupancies, bonding states.
 *
 * Comprehensive element data from authoritative sources:
 * - Atomic properties: NIST Atomic Spectra Database
 * - Physical properties: CRC Handbook of Chemistry and Physics (97th ed)
 * - Optical constants: Palik, "Handbook of Optical Constants of Solids"
 * - Electronic structure: Kittel, "Introduction to Solid State Physics"
 *
 * VALIDATION STATUS:
 * - NOT_VALIDATED: No experimental comparison performed
 * - PARTIALLY_VALIDATED: Some properties verified
 * - VALIDATED: Computed values match experiment within tolerance
 * - VALIDATION_FAILED: Computed values deviate beyond tolerance
 *
 * @author LUMI-OS Quantum Division
 * @version 2026-04-03
 * @lifecycle CANONICAL
 */

#ifndef LUMI_924_00_ELEMENTS_DATABASE_HPP
#define LUMI_924_00_ELEMENTS_DATABASE_HPP

#include <array>
#include <cstdint>
#include "../../000XX/000.00-tricorder.hpp"
#include "../../904.30-universal_physics_module/universal_physics_module.hpp"

namespace lumi {
namespace elements {

// =============================================================================
// ENUMERATIONS
// =============================================================================

enum class Phase : uint8_t {
    SOLID = 0,
    LIQUID = 1,
    GAS = 2,
    UNKNOWN = 3
};

enum class Category : uint8_t {
    ALKALI_METAL = 0,
    ALKALINE_EARTH = 1,
    TRANSITION_METAL = 2,
    POST_TRANSITION = 3,
    METALLOID = 4,
    NONMETAL = 5,
    HALOGEN = 6,
    NOBLE_GAS = 7,
    LANTHANIDE = 8,
    ACTINIDE = 9,
    UNKNOWN = 10
};

enum class ValidationStatus : uint8_t {
    NOT_VALIDATED = 0,
    PARTIALLY_VALIDATED = 1,
    VALIDATED = 2,
    VALIDATION_FAILED = 3
};

enum class CrystalStructure : uint8_t {
    BCC = 0,    // Body-centered cubic
    FCC = 1,    // Face-centered cubic
    HCP = 2,    // Hexagonal close-packed
    DIAMOND = 3,
    SC = 4,     // Simple cubic
    ORTHO = 5,  // Orthorhombic
    TETRA = 6,  // Tetragonal
    MONO = 7,   // Monoclinic
    TRIC = 8,   // Triclinic
    RHOMBO = 9, // Rhombohedral
    UNKNOWN = 10
};

// =============================================================================
// ELEMENT STRUCTURE
// =============================================================================

/**
 * @brief Complete element data
 *
 * All values in SI units unless otherwise noted.
 * NaN or 0 indicates unknown/not applicable.
 */
struct Element {
    // Identity
    uint8_t Z;                  // Atomic number
    char symbol[4];             // Chemical symbol
    char name[16];              // Element name

    // Periodic table position
    uint8_t period;             // 1-7
    uint8_t group;              // 1-18 (0 for lanthanides/actinides)
    Category category;

    // Atomic properties
    float atomic_mass;          // g/mol (standard atomic weight)
    float atomic_radius_pm;     // Empirical atomic radius (pm)
    float covalent_radius_pm;   // Covalent radius (pm)
    float vdw_radius_pm;        // Van der Waals radius (pm)

    // Electronic structure
    uint8_t electrons[7];       // Electrons per shell [K, L, M, N, O, P, Q]
    float electronegativity;    // Pauling scale
    float first_ionization_eV;  // First ionization energy (eV)
    float electron_affinity_eV; // Electron affinity (eV)

    // Physical properties (at STP unless noted)
    Phase phase_stp;
    float density_kg_m3;        // Density (kg/m^3)
    float melting_point_K;      // Melting point (K)
    float boiling_point_K;      // Boiling point (K)
    float specific_heat_J_kgK;  // Specific heat capacity
    float thermal_cond_W_mK;    // Thermal conductivity

    // Crystal structure (for solids)
    CrystalStructure crystal;
    float lattice_a_pm;         // Lattice parameter a (pm)
    float lattice_c_pm;         // Lattice parameter c (pm, for HCP/tetra)

    // Optical properties (polished surface, visible range)
    // These are COMPUTED values to be validated
    float reflectance_550nm;    // Normal incidence reflectance at 550nm
    std::array<float, 3> color_srgb;  // Computed sRGB color

    // Validation
    ValidationStatus validation;
    float optical_error;        // Max relative error vs Palik
    float color_delta_e;        // CIE76 delta-E vs reference

    // Source flags (which properties have experimental backing)
    uint32_t validated_flags;   // Bitfield of validated properties
};

// Property validation flags
constexpr uint32_t VAL_DENSITY      = 1 << 0;
constexpr uint32_t VAL_MELTING      = 1 << 1;
constexpr uint32_t VAL_OPTICAL_N    = 1 << 2;
constexpr uint32_t VAL_OPTICAL_K    = 1 << 3;
constexpr uint32_t VAL_COLOR        = 1 << 4;
constexpr uint32_t VAL_BAND_WIDTH   = 1 << 5;
constexpr uint32_t VAL_BAND_CENTER  = 1 << 6;
constexpr uint32_t VAL_WORK_FUNC    = 1 << 7;

// =============================================================================
// COMPLETE PERIODIC TABLE
// All 118 elements with known properties
// =============================================================================

constexpr int NUM_ELEMENTS = 118;

// Element data array - indexed by Z-1
// Data from CRC Handbook 97th edition, NIST, Palik
extern const Element PERIODIC_TABLE[NUM_ELEMENTS];

// =============================================================================
// ACCESS FUNCTIONS
// =============================================================================

inline const Element* get_element(int Z) {
    if (Z < 1 || Z > NUM_ELEMENTS) return nullptr;
    return &PERIODIC_TABLE[Z - 1];
}

inline const Element* get_element(const char* symbol) {
    for (int i = 0; i < NUM_ELEMENTS; ++i) {
        // Simple strcmp
        const char* s1 = PERIODIC_TABLE[i].symbol;
        const char* s2 = symbol;
        bool match = true;
        while (*s1 && *s2) {
            if (*s1++ != *s2++) { match = false; break; }
        }
        if (match && *s1 == *s2) return &PERIODIC_TABLE[i];
    }
    return nullptr;
}

// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

// Get period and group from Z
inline void get_position(int Z, int& period, int& group) {
    // Standard periodic table layout
    if (Z <= 2) { period = 1; group = (Z == 1) ? 1 : 18; }
    else if (Z <= 10) { period = 2; group = (Z <= 4) ? Z - 2 : Z + 8; }
    else if (Z <= 18) { period = 3; group = (Z <= 12) ? Z - 10 : Z - 4; }
    else if (Z <= 36) { period = 4; group = (Z <= 30) ? Z - 18 : Z - 22; }
    else if (Z <= 54) { period = 5; group = (Z <= 48) ? Z - 36 : Z - 40; }
    else if (Z <= 86) {
        period = 6;
        if (Z <= 56) group = Z - 54;
        else if (Z <= 71) group = 0;  // Lanthanides
        else group = Z - 68;
    }
    else {
        period = 7;
        if (Z <= 88) group = Z - 86;
        else if (Z <= 103) group = 0;  // Actinides
        else group = Z - 100;
    }
}

// Check if element is a metal
inline bool is_metal(const Element& e) {
    return e.category == Category::ALKALI_METAL ||
           e.category == Category::ALKALINE_EARTH ||
           e.category == Category::TRANSITION_METAL ||
           e.category == Category::POST_TRANSITION ||
           e.category == Category::LANTHANIDE ||
           e.category == Category::ACTINIDE;
}

// Check if element has optical data in Palik
inline bool has_palik_data(int Z) {
    // Elements with optical constants in Palik Vol 1-3
    constexpr int palik_elements[] = {
        3, 4, 6, 11, 12, 13, 14, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 55, 56, 57, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
        90, 92
    };
    for (int pz : palik_elements) {
        if (pz == Z) return true;
    }
    return false;
}

}  // namespace elements
}  // namespace lumi

#endif // LUMI_924_00_ELEMENTS_DATABASE_HPP
