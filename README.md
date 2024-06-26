# NuPhylo: NCLDV Phylogenetic marker tree creator
A tool for making quick phylogenetic trees of Nucleocytoviricota marker genes. Just input a fasta file of your own marker proteins, select your chosen NCLDV marker gene, and NuPhylo will align your sequences to reference sequences and build a tree so that you can determine phylogenetic placement. To ensure your tree is not overwhelmed by reference sequences, a representative set of 5 references for each NCLDV family has been curated and annotated here to use in tree building. For certain markers, there are no representatives for certain families due to that family not having that specific marker gene. 


![alt text](https://github.com/BenMinch/NuPhylo/blob/main/logo.png)


## Installation

### Dependencies
1. Fasttree (newest version)
2. Python 3+
3. mafft (v 7.453)
4. Trimal (v 1.4)
5. catfasta2phyml for concat feature (https://github.com/nylander/catfasta2phyml)

### Installing NuPhylo

It is as easy as cloning this directory with `git clone https://github.com/BenMinch/NuPhylo`. 

## Using NuPhylo

1. Get a set of marker genes from your metagenomic dataset. This can be done using [NCLDV Markersearch](https://github.com/faylward/ncldv_markersearch) after you predict proteins with a program like Prodigal.
2. After getting marker genes, you are now ready to run NuPhylo.
3. Run the command `python NuPhylo.py -i yoursequences.faa -m MCP -o Output_folder`

### Flags

1. -i: Your input fasta file
2. -m: Marker to make a tree (Choices are MCP, PolB, A32, SF2, Topo2, RNAPL, RNAPS, TF2B, VLTF3)
3. -o: Output folder to store the results.
4. -cat: Create a concatenated alignment with multiple marker genes
5. -e: Using this flag is optional, but when used it will align your sequences with an extended phylogeny that includes plant, animal, bacteria, archaeal, and fungal sequences. (Only avaliable for PolB, Topo2, RNAPL, RNAPS, and TF2B markers).

### Outputs
1. allseqs.aln: An alignment file with all of your sequences aligned with reference sequences.
2. allseqs.nwk: The tree file that you can use to upload to a program like iTOL to visualize.

### Visualizing your tree

A csv file titled NuPhylo_itol_colors.csv has been provided to make annotating your tree in itol very easy. Just go into your tree in iTOL and create a new colorstrip dataset. You can then paste data from this csv file into your new dataset to visualize unique colors for each order and family.

### New Feature: Concatenated alignment

If you want to make a tree of the concatenated alignment of multiple marker genes, you can do so with the -cat flag. In order to do this you will have to list multiple marker genes in the -m flag and multiple input files with the -i flag. Make sure the order of these matches and your genome name is consistent across all your marker gene files. 

Example: `python NuPhylo.py -i Genome_MCP.faa,Genome_PolB.faa -m MCP,PolB -o Output_folder -cat`

Some warnings
1. You cannot use -cat with the -e flag.
2. By default, it will only include sequences in the concatenated alignment where all marker genes are present within a genome.
3. If you are looking to do this, you should only have one copy of each marker per genome. To do this, you should not use the -a flag in NCLDV Markersearch.

# Copyright
NuPhylo Copyright (C) 2023 Benjamin Minch

This program is free software: you can redistribute it and/or modify it under the terms of the MIT License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the MIT License for more details.
