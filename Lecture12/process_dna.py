#!/usr/bin/env python3

import sys
import os

#Processing DNA in a file
input = sys.argv[1]

fh = open(input)
data1 = fh.readlines()

with open("cleaned.txt", "w") as the_file:
	for line_no, line in enumerate(data1, start = 1) :
		#print("Line number", line_no)
		#print("Full_line", line_no, line.strip())
		#output_list = line[14:] #line.split('ATTCGATTATAAGC')
		the_file.write(str(len(line[14:]))+"\n")
		the_file.write(line[14:])


