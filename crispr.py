#!/usr/bin/env python

#dictionary

from Bio import SeqIO

Seaurchin_dict = SeqIO.to_dict(SeqIO.parse('seaurchinscaffolds.fa','fasta'))
print(Seaurchin_dict['Scaffold670'] [107650:107840])





 
