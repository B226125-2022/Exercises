#!/usr/bin/env python3

import sys

dna_seq = sys.argv[1]
threshold = sys.argv[2]

def proportion_base(dna_seq, threshold):
	a_count = dna_seq.upper().count('A')
	t_count = dna_seq.upper().count('T')
	g_count = dna_seq.upper().count('G')
	c_count = dna_seq.upper().count('C')
	percentage = ((a_count+t_count+g_count+c_count)/len(dna_seq))*100
	if percentage < int(threshold):
		print("TRUE")
	else:
		print("FALSE")

proportion_base(dna_seq, threshold)
