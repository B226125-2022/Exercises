#!/usr/bin/env python3

import sys
protein_seq = sys.argv[1]
aa_code = sys.argv[2]

def get_percentage(protein_seq, aa_code):
	length = len(protein_seq)
	count = protein_seq.upper().count(aa_code.upper())
	percent = (count/length)*100
	#print("The percentage of", aa_code, "in", protein_seq, "is", round(percent), "%")
	return round(percent)

get_percentage(str(protein_seq), str(aa_code))

print("Testing Assertions, if there are no errors, there will be no further statements:")
if sys.argv[2] == "M":
	assert round(get_percentage(protein_seq, aa_code)) == round(5)
elif sys.argv[2] == "r":
	assert round(get_percentage(protein_seq, aa_code)) == round(10)
elif sys.argv[2] == "L":
	assert round(get_percentage(protein_seq, aa_code)) == round(50)
elif sys.argv[2] == "Y":
	assert round(get_percentage(protein_seq, aa_code)) == round(0)
print("Assertions complete")



