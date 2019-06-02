#!/usr/bin/env python3

# EXAMPLE RUN :  mutation.py A0202.fasta 

import os,sys

# File containing ref sequence; must be in same directory
file_ref = sys.argv[1]

# FUNCTION FOR GUETTING MUTATIONS BETWEEN REF AND EVERY FILE IN THE DIRECTORY 
def mut_ref_file(file):

    # split file's name to recover juste the name
    f_ref_split = (file_ref.split("/")[-1]).split(".")[0]    
    f_split = (file.split("/")[-1]).split(".")[0]

    # Openning files
    with open (file_ref, "r") as f_ref, open (file,"r") as f:
        
        # Delete spaces and tabulations
        seq_1 = f_ref.read().replace(" ","").replace("\n","")
        seq_2 = f.read().replace(" ","").replace("\n","")
        
        i = 0 # counter
        list_mut = [] # mutation list
        
        # Alignment to same position[i] /!\MUST BE PERFORMED/!\ 
        while i < len(seq_1) and i < len(seq_2):
            if (seq_1[i] != seq_2[i]):
                
                # pos_i correspond to the real position in prot sequence without
                # peptide signal (-24) ; and (+1) because python counts from i = 0 
                pos_i = ((i - 24) + 1)

                # Corresponding unique mutation depending on alphabetic order: exp 43RQ <=> 43QR 
                if (seq_1[i] < seq_2[i]):
                    mut = str(pos_i)+""+seq_1[i]+""+seq_2[i]
                else:
                    mut = str(pos_i)+""+seq_2[i]+""+seq_1[i]

                # Adding every mutation in list_mut
                list_mut.append(mut) 
            # Next mutation    
            i = i + 1

        # Creating new file for saving mutations
        res = f_ref_split+"--"+f_split    
        with open (res,"w") as op_mut:
            for mut in list_mut:
                op_mut.write(mut+"\n")

# RUN MUT_REF_FILE FOR EACH FILE IN DIRECTORY 
for file in os.listdir():
    if os.path.isfile(file):
        # If file is different to the ref and the script name 
          if file != sys.argv[1] and  file != sys.argv[0].split("./")[1]:
              mut_ref_file(file)