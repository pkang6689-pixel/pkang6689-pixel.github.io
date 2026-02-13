#!/usr/bin/env python3
"""Rename Archive files from topic-name format to Lesson X.Y (TopicName)_Type.html format."""

import os
import shutil

ARCHIVE = "/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/Archive"

# Mapping: archive_prefix -> (lesson_number, readable_topic_name)
# Built from cross-referencing lesson titles with archive filenames
PREFIX_MAP = {
    # Unit 1
    "statesofmatter": ("1.1", "States of Matter"),
    "heatingcoolingcurves": ("1.2", "Phase Changes"),
    "intensivevsextensiveproperties": ("1.3", "Intensive vs Extensive Properties"),
    "densitycalculations": ("1.4", "Density Calculations"),
    "heterogeneousvshomogeneousmixtures": ("1.5a", "Heterogeneous vs Homogeneous Mixtures"),
    "mixturesheterogeneousvshomogeneous": ("1.5b", "Mixtures"),
    "puresubstancesvsmixtures": ("1.5c", "Pure Substances vs Mixtures"),
    "physicalvschemicalproperties": ("1.6", "Physical vs Chemical Properties"),
    "physicalvschemicalchanges": ("1.7", "Physical vs Chemical Changes"),

    # Unit 2
    "scientificnotation": ("2.1", "Scientific Notation"),
    "significantfiguressigfigs": ("2.2", "Significant Figures"),
    "accuracyvsprecision": ("2.3", "Accuracy vs Precision"),
    "themetricsystemsiunits": ("2.4", "Metric System"),
    "unitconversionsdimensionalanalysis": ("2.5", "Unit Conversions"),

    # Unit 3
    "subatomicparticlesprotonsneutronselectrons": ("3.1", "Subatomic Particles"),
    "atomicnumbermassnumber": ("3.2a", "Atomic Number Mass Number"),
    "theatomicnucleus": ("3.2b", "The Atomic Nucleus"),
    "quantummechanicalmodelorbitals": ("3.3", "Quantum Mechanical Model"),
    "thebohrmodel": ("3.4", "The Bohr Model"),
    "nuclearchemistrystabilityradioactivity": ("3.5", "Nuclear Chemistry Stability"),
    "isotopesaverageatomicmass": ("3.6", "Isotopes Average Atomic Mass"),

    # Unit 4
    "groupsperiods": ("4.2a", "Groups and Periods"),
    "historyoftheperiodictable": ("4.2b", "History of the Periodic Table"),
    "metalsnonmetalsmetalloids": ("4.2c", "Metals Nonmetals Metalloids"),
    "valenceelectrons": ("4.3", "Valence Electrons"),
    "electronconfiguration": ("4.5", "Electron Configuration"),
    "periodictrendsatomicradius": ("4.6a", "Periodic Trends Atomic Radius"),
    "periodictrendselectronegativity": ("4.6b", "Periodic Trends Electronegativity"),
    "periodictrendsionizationenergy": ("4.6c", "Periodic Trends Ionization Energy"),
    "vseprtheorymoleculargeometry": ("4.8", "VSEPR Molecular Geometry"),

    # Unit 5A
    "octetruleionformation": ("5A.2", "Octet Rule Ion Formation"),
    "introductiontochemicalbonds": ("5A.3", "Introduction to Chemical Bonds"),
    "ionicbonding": ("5A.4", "Ionic Bonding"),
    "namingioniccompounds": ("5A.6", "Naming Ionic Compounds"),
    "polyatomicions": ("5A.7", "Polyatomic Ions"),

    # Unit 5B
    "covalentbonding": ("5B.1a", "Covalent Bonding"),
    "lewisstructures": ("5B.1b", "Lewis Structures"),
    "polarityintermolecularforces": ("5B.1c", "Polarity Intermolecular Forces"),
    "namingcovalentcompounds": ("5B.2", "Naming Covalent Compounds"),
    "metallicbonding": ("5B.3", "Metallic Bonding"),

    # Unit 6
    "synthesisdecompositionreactions": ("6.1a", "Synthesis Decomposition Reactions"),
    "singledoublereplacementreactions": ("6.1b", "Single Double Replacement Reactions"),
    "combustionreactions": ("6.2", "Combustion Reactions"),
    "redoxreactionsintroduction": ("6.3", "Redox Reactions"),
    "collisiontheory": ("6.4", "Collision Theory"),
    "balancingchemicalequations": ("6.5a", "Balancing Chemical Equations"),
    "chemicalequationsconservationofmass": ("6.5b", "Conservation of Mass"),
    "factorsaffectingreactionrates": ("6.6", "Factors Affecting Reaction Rates"),
    "chemicalequilibrium": ("6.7a", "Chemical Equilibrium"),
    "lechateliersprinciple": ("6.7b", "Le Chateliers Principle"),
    "equilibriumconstantskeq": ("6.7c", "Equilibrium Constants"),

    # Unit 7
    "molarmasscalculations": ("7.2", "Molar Mass Calculations"),
    "themoleconceptavogadrosnumber": ("7.3", "Avogadros Number"),
    "molemassparticleconversions": ("7.4", "Mole Mass Particle Conversions"),
    "empiricalmolecularformulas": ("7.5a", "Empirical Molecular Formulas"),
    "percentcomposition": ("7.5b", "Percent Composition"),
    "limitingreactant": ("7.6", "Limiting Reactant"),
    "stoichiometrymoleratios": ("7.7", "Stoichiometry Mole Ratios"),
    "theoreticalpercentyield": ("7.8", "Theoretical Percent Yield"),

    # Unit 8
    "gaspressureunits": ("8.2", "Gas Pressure Units"),
    "kineticmoleculartheory": ("8.3", "Kinetic Molecular Theory"),
    "boyleslaw": ("8.4", "Boyles Law"),
    "charlesslaw": ("8.5", "Charles Law"),
    "gaylussacslaw": ("8.6", "Gay-Lussacs Law"),
    "thecombinedgaslaw": ("8.7", "Combined Gas Law"),
    "idealgaslaw": ("8.8", "Ideal Gas Law"),
    "daltonslawofpartialpressures": ("8.x", "Daltons Law of Partial Pressures"),
    "grahamslawofeffusion": ("8.x2", "Grahams Law of Effusion"),

    # Unit 9
    "solutessolventssolutioncreation": ("9.1", "Solutes Solvents Solution Creation"),
    "concentrationmolarity": ("9.2", "Concentration Molarity"),
    "dilutions": ("9.3", "Dilutions"),
    "solubilitysaturation": ("9.5", "Solubility Saturation"),
    "factorsaffectingsolubility": ("9.6", "Factors Affecting Solubility"),
    "colligativeproperties": ("9.7", "Colligative Properties"),

    # Unit 10
    "propertiesofacidsbases": ("10.1", "Properties of Acids Bases"),
    "arrheniusvsbronstedlowrydefinitions": ("10.4", "Arrhenius vs Bronsted-Lowry"),
    "strongvsweakacidsbases": ("10.5", "Strong vs Weak Acids Bases"),
    "neutralizationreactions": ("10.6a", "Neutralization Reactions"),
    "netionicequations": ("10.6b", "Net Ionic Equations"),
    "titrations": ("10.6c", "Titrations"),
    "buffers": ("10.8", "Buffers"),
    "phpohscale": ("10.9", "pH pOH Scale"),
    "calculatingph": ("10.10", "Calculating pH"),

    # Unit 11
    "energyheattemperature": ("11.1a", "Energy Heat Temperature"),
    "endothermicvsexothermic": ("11.1b", "Endothermic vs Exothermic"),
    "energychangesendothermicexothermic": ("11.1c", "Energy Changes"),
    "specificheatcapacity": ("11.2", "Specific Heat Capacity"),
    "calorimetry": ("11.4", "Calorimetry"),
    "enthalpythermochemicalequations": ("11.5", "Enthalpy Thermochemical Equations"),
    "hessslaw": ("11.6", "Hess Law"),
}

# The archive files have patterns like:
# topicnamepractice_Practice.html  (type word embedded in prefix)
# topicname_Practice.html          (clean separator)
# topicname_Video.html
# topicname_Video_DUP.html

TYPES = ["_Video", "_Summary", "_Practice", "_Quiz"]

def extract_prefix_and_type(filename):
    """Extract the topic prefix and file type from an archive filename."""
    base = filename.replace(".html", "")
    
    # Handle _DUP suffix
    is_dup = "_DUP" in base
    base = base.replace("_DUP", "")
    
    # Try to match against known types
    for t in TYPES:
        if base.endswith(t):
            prefix = base[:-len(t)]
            return prefix, t, is_dup
    
    return None, None, False

def find_prefix_match(raw_prefix):
    """Try to match a raw prefix (which may have the type word embedded) to our mapping."""
    # Direct match
    if raw_prefix in PREFIX_MAP:
        return raw_prefix
    
    # The prefix might have the type word appended, e.g. "statesofmatterpractice"
    # Try removing common suffixes
    for suffix in ["practice", "quiz", "summary", "video"]:
        if raw_prefix.endswith(suffix):
            stripped = raw_prefix[:-len(suffix)]
            if stripped in PREFIX_MAP:
                return stripped
    
    return None

def main():
    renamed = 0
    skipped = []
    
    files = sorted(os.listdir(ARCHIVE))
    
    for fname in files:
        full_path = os.path.join(ARCHIVE, fname)
        if not os.path.isfile(full_path) or not fname.endswith(".html"):
            continue
        
        # Skip unit test files - they're already named fine
        if fname.startswith("Unit") and "Test" in fname:
            continue
        
        raw_prefix, ftype, is_dup = extract_prefix_and_type(fname)
        
        if raw_prefix is None or ftype is None:
            skipped.append(fname)
            continue
        
        matched = find_prefix_match(raw_prefix)
        
        if matched is None:
            skipped.append(fname)
            continue
        
        lesson_num, topic_name = PREFIX_MAP[matched]
        dup_suffix = " DUP" if is_dup else ""
        
        # New name: Lesson X.Y (TopicName)_Type.html
        new_name = f"Lesson {lesson_num} ({topic_name}){ftype}{dup_suffix}.html"
        new_path = os.path.join(ARCHIVE, new_name)
        
        if full_path != new_path:
            os.rename(full_path, new_path)
            print(f"  {fname}")
            print(f"    → {new_name}")
            renamed += 1
    
    print(f"\nRenamed: {renamed}")
    if skipped:
        print(f"Skipped ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s}")

if __name__ == "__main__":
    main()
