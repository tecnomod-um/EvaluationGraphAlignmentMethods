# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:24:27 2023

@author: gines
"""

## Input data
dataset_path = "$PATH"
pair_dataset = "LLM-LLM"

file_test_link = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/451_1fold/1/test_links"
file_align_result = "$PATH" + "/alignment_results_12"
file_kg1_ids = "$PATH" + "/kg1_ent_ids"
file_kg2_ids = "$PATH" + "/kg2_ent_ids"
file_kg1_rel = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/451_1fold/1/rel_triples_1"


## Output data

file_count_align = "$PATH" + "/count_aligned_ent"
file_ent_match = "$PATH" + "/ent_match"

count_align = open(file_count_align, "w", encoding= "utf-8")
ent_match = open(file_ent_match, "w", encoding= "utf-8")

##variables

pattern1 = ""
pattern2 = ""
pattern_align = ""
dict_classes = {}
dict_matches = {}
count_class_total = 0
count_class_match = 0

## Get the IRI of each alignment

align_results = open(file_align_result, "r", encoding="utf-8")

list_align_id = align_results.readlines()

for each_line_align in list_align_id:    
    
    id_1, id_2 = each_line_align.split("\t")
    id_2 = id_2.rstrip()
    
    with open(file_kg1_ids, encoding='utf-8') as file_id_1:
        while True:
            line_id_1 = file_id_1.readline()
            colum_1, colum_2 = line_id_1.split("\t")
            colum_2 = colum_2.rstrip()
            if id_1 == colum_2:
                pattern1 = colum_1 
                break
    with open(file_kg2_ids, encoding='utf-8') as file_id_2:
        while True:
            line_id_2 = file_id_2.readline()
            colum_1, colum_2 = line_id_2.split("\t")
            colum_2 = colum_2.rstrip()
            if id_2 == colum_2:
                pattern2 = colum_1
                break
    
    pattern_align = pattern1 + "\t" + pattern2 + "\n"    ## Match IRIs entities
    count_class_total += 1    

## Identify the class of entity
    with open(file_kg1_rel, encoding='utf-8') as file_rel_1:
        while True:
            line_rel_1 = file_rel_1.readline()
            subject, predicate, obj = line_rel_1.split("\t")
            obj = obj.rstrip()
            if subject == pattern1 and predicate == "http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
                if obj not in list(dict_classes):   ## Identify all classes aligned
                    dict_classes[obj] = 1
                    dict_matches[obj] = 0
                else:
                    dict_classes[obj] += 1       ##Count the type of class
                break
        
        print(dict_matches)    
## Verify the match

    with open(file_test_link, encoding='utf-8') as file_test:
        list_test = file_test.readlines()
        if pattern_align in list_test:
          dict_matches[obj] += 1       ##Count the match class
          ent_match.write(pattern_align)
            

## Write the counts
count_align.write("class\ttotal_count\tmatch_count\t%_match\n")
for class_match in list(dict_classes): 
    class_line = class_match + "\t" + str(dict_classes[class_match]) + "\t" + str(dict_matches[class_match]) + "\t" + str((dict_matches[class_match]/dict_classes[class_match])*100) + "\n"   
    count_align.write(class_line)    

    
count_align.close()
ent_match.close()