#!/usr/bin/env python3

# EXAMPLE:  mutation.py /FASTA/A0202.fasta /FASTA/A0203.txt

import os,sys

# File containing sequences; must be in same directory
file_1 = sys.argv[1]
file_2 = sys.argv[2]

# split file's name to recover juste the name
f1_split = (file_1.split("/")[-1]).split(".")[0]
f2_split = (file_2.split("/")[-1]).split(".")[0]

# Openning files
with open (file_1, "r") as f1, open (file_2,"r") as f2:
    
    # Delete spaces and tabulations
    seq_1 = f1.read().replace(" ","").replace("\n","")
    seq_2 = f2.read().replace(" ","").replace("\n","")
    
    i = 0 # counter
    list_mut = [] # mutation list
    
    # Alignment to same position[i] /!\MUST BE PERFORMED/!\ 
    while i < len(seq_1) and i < len(seq_2):
        if (seq_1[i] != seq_2[i]):
            
            # pos_i correspond to the real position in prot sequence without
            # peptide signal (-24) ; and (+1) because python counts from i = 0 
            pos_i = ((i - 24) + 1)

            # Make unique mutation depends on alphabetic order
            if (seq_1[i] < seq_2[i]):
                mut = str(pos_i)+""+seq_1[i]+""+seq_2[i]
            else:
                mut = str(pos_i)+""+seq_2[i]+""+seq_1[i]

            # Adding every mutation in list_mut
            list_mut.append(mut) 
        # Next mutation    
        i = i + 1

    # Creating new file for saving mutations    
    with open (f1_split+"--"+f2_split,"w") as op_mut:
        for mut in list_mut:
            op_mut.write(mut+"\n")
        