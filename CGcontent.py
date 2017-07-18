#Author: Ruqian Lyu
#Data 18 July 2017
#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;

import pysam

dna = pysam.FastxFile("dna.fa")
gcRate = {}
maxRate = 0
name = ''
for read in dna:
    gcRate[read.name] = (float)(read.sequence.count("C")+read.sequence.count("G"))/len(read.sequence)

for query in gcRate:
    if gcRate[query] > maxRate:
        maxRate = gcRate[query]
        name = query

print name,'\n',100 * maxRate