import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys


def open_and_parse_fasta_file_func (path_dir):
    amino_acid_list = ["G","A","L","M","F","W","K","Q","E","S","P","V","I","C","Y","H","R","N","D","T"]
    counter_list = [0] * 20
    
    parent_path = Path(path_dir)
    parent_path = parent_path.parents[0]
    #new_path = str(parent_path) + "\\" + file_name + ".png"
    new_path = "D:/EIGENE DATEIEN/Documents/!UNI/Coding/Advanced Python/Exercise_1/" + "barplot.png"
    #output_df = pd.Dataframe(columns = ["AminoAcids":amino_acid_list,"Counter":zero_list])
    with open(path_dir) as input_data:
        for line in input_data:
            if line.startswith(">"):
                a = 0
            else:
                for i in range(len(amino_acid_list)):
                    stripped_line = line.strip("\n")
                    count_single_AA_list = re.findall(amino_acid_list[i], stripped_line)
                    counter_list[i] += len(count_single_AA_list)
         
    
    

    plt.bar(amino_acid_list, counter_list, color ='maroon') 
    plt.xlabel("AA")
    plt.ylabel("Counts")
    plt.title("Barplot")
    plt.savefig(new_path)

open_and_parse_fasta_file_func(sys.argv[0])