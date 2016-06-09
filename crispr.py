#!/usr/bin/env python

#dictionary: search from desired sequence
#input sequence as [scaffold000] and define range [0:0]

from Bio import SeqIO
import re

'''

Seaurchin_dict = SeqIO.to_dict(SeqIO.parse('seaurchinscaffolds.fa','fasta'))
sequences = (Seaurchin_dict['Scaffold670'] [107780:107850])
print(sequences.seq)
output_handle = open ('DNA_Scaffold', 'w') 
SeqIO.write(sequences, output_handle,'fasta')
output_handle.close()
'''
#PAM finder + 20nt
#new_sequences = raw_input ('enter DNA for gRNA scan: ')
new_sequences = 'ACTAAGTACTGAGCTACTCCTAGAGACGCGCCGAAAAGAACTGTACGGACTGTAGCCACCCTATGACGTC'

OutFile = open('NGG_gRNA', 'w')

for m in re.finditer('[ATGC]GG', new_sequences): 
	OutFile.write('NGG PAM found '+ str(m.start())+ str(m.end()) + new_sequences[m.start()-20:m.end()])
	print('NGG PAM found', m.start(), m.end()) 

#if len(new_sequences)-m.start() > 20:
	print(new_sequences[m.start()-20:m.end()]) 
	
#else:
	#print('NGG no valid sequence match')  

for m in re.finditer('CC[ATGC]', new_sequences): 
	OutFile.write('CCN PAM found '+ str(m.start())+ str(m.end()) + new_sequences[m.start()-20:m.end()])
	print('CCN PAM found', m.start(), m.end()) 
#if len(new_sequences)-m.end() > 20:	
	print(new_sequences[m.start():m.end()+20])

#else: 	
	#print('CCN no valid sequence match')

OutFile.close()

#PAM BLAST - this finds the blast sequence with maximum 15/20 mismatches 

#pat = re.compile ('[ATGC]CC')
#match = pat.search (new_sequences)
'''
how to find all occurnces
if len(new_sequences)-match.start() < 20:
	continue
else:
	print()
'''