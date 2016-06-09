#!/usr/bin/env python

#dictionary: search from desired sequence
#input sequence as [scaffold000] and define range [0:0]

from Bio import SeqIO

import re

Seaurchin_dict = SeqIO.to_dict(SeqIO.parse('seaurchinscaffolds.fa','fasta'))
sequences = (Seaurchin_dict['Scaffold670'] [107800:107840])
print(sequences.seq)
output_handle = open ('DNA_Scaffold', 'w') 
SeqIO.write(sequences, output_handle,'fasta')
output_handle.close()

#PAM finder + 20nt
new_sequences = 'TAGAGACGCGCCGAAAAGAACTGTACGGACTGTAGCCACC'

for m in re.finditer('[ATGC]CC', new_sequences):
	print('PAM found', m.start(), m.end())
	print(new_sequences[m.start()-20:m.end()])

#pat = re.compile ('[ATGC]CC')
#match = pat.search (new_sequences)

         


'''
how to find all occurnces
if len(new_sequences)-match.start() < 20:
	continue
else:
	print()
'''