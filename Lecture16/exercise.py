#!/usr/bin/env Python3

import os, sys, subprocess
import numpy as np
import pandas as pd

df = pd.read_csv('eukaryotes.txt', sep="\t")

# genomes bigger than 100Mb, fungal species

df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1)]
len(df[df.apply( lambda x: x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis = 1)])


#how many of each kingdom/group (plants, animals, fungi and protists)
#have been sequenced?

for i in df['Group'].unique():
	len(df[df.apply( lambda x: x['Group], axis=1)]

