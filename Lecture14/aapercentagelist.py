#!/usr/bin/env python3

import sys

protein_seq = sys.argv[1]
aa_list = sys.argv[2]
#default_aa_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']

def get_percentage_list(protein_seq, aa_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
	for residue in aa_list:
		count = protein_seq.count(residue)
		print(count)

get_percentage_list(protein_seq, aa_list)
