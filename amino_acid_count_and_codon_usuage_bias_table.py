#! /usr/bin/env Python3

"""
Created on Fri Nov 24 04:52:41 2023

@author: Chinaza

Python code for counting amino acid and generation of codon usage bias table. Dictionary was used in keeping track of the several counts in the codon usage bias table function
"""

import os
from prettytable import PrettyTable #importing PrettyTable for better visualization of the result

#to check the current working directory
print(os.getcwd())

#to change the directory
os.chdir("G:/My Drive/school_and_programming/scripts_for_minor_task_completed")

print(os.getcwd())
#----------------------------------------------------------------------------------------------------

#amino acid_codon dictionary
aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}

#function for reading in fasta file and putting it in a dictionary
def read_fasta():
    fasta_dict = {}
    header = ""
    sequence = ""
    
    #with open("data/Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa") as fh:
    with open("data/MDomestica-short.fa") as fh: #shorter version of fasta file can be used in testing the script    
        for line in fh:
            line = line.strip()

            if line.startswith(">"):
                if len(header) > 0:
                    fasta_dict[header] = sequence
                    sequence = ""
                header = line
            else:
                sequence += line
        fasta_dict[header] = sequence
    return fasta_dict


# =============================================================================
# Part 1: function for getting amino acid counts
# =============================================================================
def countAAs(fasta_file, frame):
   
    if frame not in (0,1,2):
        raise ValueError
    
    for header,seq in fasta_file.items(): #looping through dictionary of sequence
        counts = {} #creating an empty dictionary
        
        #making the keys of the empty dictionary (counts) to be same as the keys of aa_dict dictionary and setting the counts to zero
        for key in aa_dict.keys():
            counts[key] = 0
        
        seqLen = len(seq)
        
        #looping through the sequences from fasta_file, getting amino acid count and storing it in "counts" dictionary
        for start in range(frame,seqLen,3):
            codon = seq[start:start+3]

            for AA,codon_lst in aa_dict.items():
                if codon in codon_lst:
                    counts[AA] += 1

        #printing result
        print(f"AA counts for {header}")
        for key,val in counts.items():
            if val>0:
                print(f'\t{key}: {val}')
                
                
# =============================================================================
# Part 2: function for codon usage bias table
# =============================================================================
def codon_usage_bias_table():
    
    #creating a human readable file (codon_bias_table.txt) for storing the result and adding an header
    fout = open("result/codon_bias_table.txt", 'w')
    result_header = "Codon, Amino acid, Codon count, Fraction \n"
    fout.write(result_header)
    fout.close
    
    fout = open("result/codon_bias_table.txt", 'a') #this will be used to append the result at the end of this function to codon_bias_table.txt file 
    
    combined_seq = "" #creating an empty string variable that will be used for storing all the sequences together
    
    fasta_dict = read_fasta() #reading in the fasta file as a dictionary
    
    #combining all the sequences into one
    for header,seq in fasta_dict.items(): 
        combined_seq += seq

    seqLen = len(combined_seq) #getting the length of all the sequences, this will be used later
    codon_count = {} #creating an empty dictionary that will be used for storing codon counts
    
    #making codons aa_dict.values() keys in codon_count dictionary and setting the count to zero
    for key,val in aa_dict.items():
        for codon in val:
            codon_count[codon] = 0
    
    #looping through the sequences from "combined_seq" and getting codon frequency
    for start in range(0,seqLen,3):
        cd = combined_seq[start:start+3]
        
        #getting codon frequency and storing it in codon_count dictionary
        for codon,count in codon_count.items():
            if cd == codon:
                codon_count[codon] += 1
    
    #creating a new dictionary (combined_dict) that comprise of aa_dict and codon_count
    combined_dict = {}
    for aa, codons in aa_dict.items():
        combined_dict[aa] = {'codon_count': {codon: codon_count[codon] for codon in codons}}
    
    #creating an empty PrettyTable for easy visualization of result
    table = PrettyTable(['Codon', 'Amino Acid', 'Codon Count', 'Fraction'])
    
    #getting the fractional count of each codon (this is in relative to the amino acid it codes for)
    for amino_acid, data in combined_dict.items():
        
        protein_count = sum(combined_dict[amino_acid]['codon_count'].values()) #getting protein count by summing up the codons
        
        fraction_dict = {} #dictionary for storing codon fractional counts
        
        #calculating codon fractional count based on the amino acid it codes for and storing this in a dictionary (fraction_dict)
        for codon,codon_count in combined_dict[amino_acid]['codon_count'].items(): 
            relative_fraction = codon_count/protein_count        
            fraction_dict[codon] = relative_fraction
        
        #adding the fraction_dict dictionary to combined_dict
        combined_dict[amino_acid]['fraction'] = fraction_dict
        
        #codes below store result in PrettyTable for easy visualization
        codon_count = data['codon_count'] #accessing codon_count dictionary in combined_dict
        fraction = data['fraction'] #accessing fraction dictionary in combined_dict
        
        #iterating through codon_count dictionary, extracting fraction_value from fraction dictionary based on key (codon) from codon_count dictionary, putting the result in PrettyTable and writing it out to codon_bias_table.txt
        for codon, count in codon_count.items():
            fraction_value = fraction[codon]
            table.add_row([codon, amino_acid, count, fraction_value])
            
            #saving result in a human readable file (codon_bias_table.txt)
            result = (f"{codon}, {amino_acid}, {count}, {fraction_value}\n")
            fout.write(result)
        fout.close
        
    print(table) #printing the PrettyTable
   
    
def main():
    
    #un-comment the codes below if you want to get the amino acid counts
    #frame = int(input("Welcome user, what frame do you want to run the amino acid count on? (can only select from 0,1,2: "))
    #fasta_file = read_fasta()
    #countAAs(fasta_file, frame)
    
    codon_usage_bias_table()
    
if __name__ == "__main__":
	main()
    
    