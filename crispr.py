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
	
	OutFile.write('>location_in_search_query|'+ str(m.start()) + '|' + str(m.end()) + '|' + '\n' + new_sequences[m.start()-20:m.end()] + '\n')
	
	print('NGG PAM found', m.start(), m.end()) 
	
	print(new_sequences[m.start()-20:m.end()]) 

OutFile.close()


OutFile = open('CCN_gRNA', 'w')


for m in re.finditer('CC[ATGC]', new_sequences): 
	
	OutFile.write('>location_in_search_query|'+ str(m.start()) + '|' + str(m.end()) + '|' + '\n' + new_sequences[m.start():m.end()+20] + '\n')
	
	print('CCN PAM found', m.start(), m.end()) 
	
	print(new_sequences[m.start():m.end()+20])


OutFile.close()

#PAM BLAST - this finds the blast sequence with maximum 15/20 mismatches 

from Bio.Blast.Applications import NcbiblastnCommandline
help(NcbiblastnCommandline)

blastn_cline = NcbiblastnCommandline(query='CCN_gRNA', db='sp_purpuratus', evalue=0.001, outfmt=5, out='gRNA_aligments')

blastn_cline

NcbiblastnCommandline(cmd='blastn', out='gRNA_aligments', outfmt=5, query='CCN_gRNA', db='sp_purpuratus', evalue=0.001)

print(blastn_cline)

blastn -out gRNA_aligments -outfmt 5 -query CCN_gRNA -db purple sea urchin -evalue 0.001

stdout, stderr = blastn_cline()


#pat = re.compile ('[ATGC]CC')
#match = pat.search (new_sequences)
