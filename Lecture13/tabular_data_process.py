#!/usr/bin/env python3

import sys
import os

#Print out gene names for all genes from the species Drosophila
#melanogaster or simulans

input = sys.argv[1]

fh = open(input)
data1 = fh.readlines()

for line in data1 :
	gene_data = line.split(",")
	species = gene_data[0]
	sequence = gene_data[1]
	gene_name = gene_data[2]
	expression_level = gene_data[3]
	if species == "Drosophila melanogaster" or species == "Drosophila simulans" :
		print(species, gene_name)
	if len(sequence) > 90 and len(sequence) < 110 :
		print(species, gene_name)
	if 


