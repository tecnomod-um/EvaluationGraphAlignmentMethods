# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:02:59 2023

@author: gines
"""

import numpy as np
import os

######### Functions ###############

def load_alignment_pair(file_name):
    alignment_pair = []
    for line in open(file_name,'r', encoding="utf-8"):
        print(line)
        e1,e2 = line.split()
        alignment_pair.append((e1,e2))
    return alignment_pair

def load_data(lang,train_ratio, test_ratio):             
    
    alignment_pair = load_alignment_pair(lang)
    np.random.shuffle(alignment_pair)
    train_pair = alignment_pair[0:int(len(alignment_pair)*train_ratio)]
    test_pair = alignment_pair[int(len(alignment_pair)*(train_ratio)):int(len(alignment_pair)*(train_ratio+test_ratio))]
    val_pair = alignment_pair[int(len(alignment_pair)*(train_ratio+test_ratio)):]

    return train_pair, test_pair, val_pair

#####################################################

## Input data
ent_links = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/ent_links"


## Output data
path_base = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/451_1fold/"

train_links = "train_links"   
test_links = "test_links"
valid_links = "valid_links"

##← Variables
ratio_train = 0.5
ratio_test = 0.4

list_dir_out = [1, 2, 3, 4, 5]

for dir_out in list_dir_out:
    
    train_ent, test_ent, val_ent = load_data(ent_links, ratio_train, ratio_test)

    with open(path_base + str(dir_out) + "/" + train_links, "w", encoding='utf-8') as train_file:
        for pair_train in train_ent:
            pattern_train = pair_train[0] + "\t" + pair_train[1]+ "\n" 
            train_file.write(pattern_train)
            
    with open(path_base + str(dir_out) + "/" + test_links, "w", encoding='utf-8') as test_file:
        for pair_test in test_ent:
            pattern_test = pair_test[0] + "\t" + pair_test[1]+ "\n" 
            test_file.write(pattern_test)
            
    with open(path_base + str(dir_out) + "/" + valid_links, "w", encoding='utf-8') as val_file:
        for pair_val in val_ent:
            pattern_val = pair_val[0] + "\t" + pair_val[1]+ "\n" 
            val_file.write(pattern_val)





