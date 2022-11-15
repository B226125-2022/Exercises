#!/usr/bin/env python3
import re

gene_accession = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

for gene_no in gene_accession:
	contains_five = re.search(r'5', gene_no)
	if contains_five:
		print(gene_no, 'contains 5')
	contains_de = re.search(r'(d|e)', gene_no)
	if contains_de:
		print(gene_no, 'contains d or e')
	contains_de_ordered = re.search(r'de', gene_no)
	if contains_de_ordered:
		print(gene_no, 'contains d and e in sequential order')
	contains_de_letter = re.search(r'd[a-z]e', gene_no)
	if contains_de_letter:
		print(gene_no, 'contains a letter between d and e')
	contains_de_any = re.search(r'd', gene_no) and re.search(r'e', gene_no)
	if contains_de_any:
		print(gene_no, 'contains d and e in any order')
	starts_xy = re.search(r'^[xy]', gene_no)
	if starts_xy:
		print(gene_no, 'starts with x or y')
	starts_xy_end_e = re.search(r'^[xy]', gene_no) and re.search(r'e$', gene_no)
	if starts_xy_end_e:
		print(gene_no, 'starts with x or y and ends with e')

