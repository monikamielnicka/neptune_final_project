#!/usr/bin/env python

#dictionary: search from desired sequence
#input sequence as [scaffold000] and define range [0:0]

from Bio import SeqIO
import re

#Bio.Blast.NCBIWWW
from Bio.Blast import NCBIWWW
#help(NCBIWWW.qblast)

from Bio.Blast import NCBIXML

# optional: shows the scaffolds and nt positions of desired PAM seq search - takes time to load. 
# saves the result to file


Seaurchin_dict = SeqIO.to_dict(SeqIO.parse('seaurchinscaffolds.fa','fasta'))
sequences = (Seaurchin_dict['Scaffold670'] [107780:107850])

print(sequences.seq)

output_handle = open ('DNA_Scaffold', 'w') 
SeqIO.write(sequences, output_handle,'fasta')
output_handle.close()

# PAM finder + 20nt in scaffold sequence
# optional feature: swap new_sequences = '' to new_sequences = raw_input ('enter DNA for gRNA scan: ') to add customised DNA sequence search query

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

# the blast search entrez_query for sea urchin (see ORGN number on online blast if in doubt)
# to add extra features to search go to entrez BLAST NCBI webpage
# format_type set to a text file for convenience
# add one fasta per quert to the blast search if have multipe gRNA aligments

record = SeqIO.read("gRNA_searchfile", format="fasta")
result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq, entrez_query='txid7668[ORGN]', format_type='Text', expect=100.0)
#print (result_handle)

save_file = open('magic_blast', 'w')
save_file.write(result_handle.read())
save_file.close()
result_handle.close()

#to search results open wildcards (Identities\s.\snumber.+)