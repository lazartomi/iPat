# iPat
Physicochemical patterns of residues in protein-proteins interfaces


Script desciptions:

calc_properties.py

This script enables to recaluclate the physicochemical patterning preferences for interfaces and non-interfaces for a given dataset. The input is a list of PDB id codes in a simple text file (the structures will be use automatically downloaded). The output is a flat file with rows summarizing how many properties of which type can be found around a given residue in a structure.
Dependencies: python modules: os, numpy, re + STRIDE


iPatBaselineParserFast.py

This script can calculate the contributions of the potential coming from a given property pair. The input for this program is the output of calc_properties.py, and the output is the statistics and potential values calculated on the dataset going to the standard output.
Dependencies: python modules: numpy, pandas


localPotentialQuick.py

This script calculates potentials from the physicochemical property environments. The default potentals are hard-coded in the script but these can be changed to the output of iPatBaselineParserFast.py. The input file is the flat file output of calc_properties.py, and the output is a similar flat file with potentials values for each residue.
This script has no dependencies.

