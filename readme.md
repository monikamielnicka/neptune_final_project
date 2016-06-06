# Neptune Computational Biology - CRISPR gRNA search tool for Sp.purpuratus 

# Title of my project
# CRISPR gRNA seq search

## Introduction and Goals

The goal is to create a tool for gRNA search in purple sea urchin: 

The tool will be looking for a PAM sequence in genomic DNA defined as NGG (positive strand) or CCN (negative strand) within the gene/region of interest. Then it will locate a 20 nt at 5' end of NGG or 3' end of CCN. In summary, the whole DNA product to be indentified will look like N20-NGG or CCN-N20.

Then this sequence will be matched across the genome for potential mismatches sites - to find the N20 matching sites with minimum of 15/20 nt matches. 

Then the tool search whether at 3' end NGG is present or CCN at 5' is present.

Then will it pool the results with location in the genome with numerical location of a scaffold and nt.


The data I will use are sp.purpuratus DNA sequence from echinobase.org 

## Methods

The tools I used were... See analysis files at (links to analysis files).

## Results

![Figure 1](./Figure1.png?raw=true)

In Figure 1...

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


