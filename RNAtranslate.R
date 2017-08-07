# Title     : translate RNA into Amino Acid sequences
# Objective :
# Created by: ruqianlyu
# Created on: 7/8/17

#use the function provided in Biostrings to easily translate RNA into AA
source("http://www.bioconductor.org/biocLite.R")
biocLite("Biostrings")

rna <- RNAString("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

translate(rna)
