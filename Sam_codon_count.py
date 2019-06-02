import os
import re 
import sys

nucleotide_count1 = {}
sam_file = open(sys.argv[1])
for line in sam_file:
	if line.startswith("D"):
		split = line.split("\t")
		sequence = split[9]	
		codon = sequence[0:3]
		current_count = nucleotide_count1.get(codon,0)
		new_count = current_count + 1
		nucleotide_count1[codon] = new_count


for codon, count in nucleotide_count1.items():
	print(codon + " : " + str(count) + ",")
