count_merge_entity_align = function(input_file, rel_triples, test_data, output_path){
  rel_triples = rel_triples[rel_triples$V2 == "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",]
  indexes = which(rel_triples$V1 %in% test_data$V1)
  rel_triples = rel_triples[indexes,]
  table_rel_triples = data.frame(table(rel_triples$V3))
  colnames(table_rel_triples) = c("Entity", "Expected_entities")
  
  input_file = merge(input_file[,1], rel_triples[,-2], by = "V1")
  table_input = data.frame(table(input_file$V3))
  colnames(table_input) = c("Entity", "Obtained_entities")
  
  table = merge(table_rel_triples, table_input, by = "Entity")
  table = dplyr::mutate(table, Ratio = Obtained_entities/Expected_entities*100)
  write.table(table, output_path, col.names = T, row.names = F, quote = F, sep = "\t")
}

library(data.table)

#ECommerce L-L
input_file = fread("../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-BootEA/LLM-LLM", header = F)
rel_triples = fread("../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/rel_triples_1", header = F)
test_data = fread("../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/451_1fold/1/test_links", header = F)
output_path = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-BootEA/LLM-LLM_merged_count.tsv"
count_merge_entity_align(input_file, rel_triples, test_data, output_path)

input_file = fread("../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-AlignE/LLM-LLM", header = F)
output_path = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-AlignE/LLM-LLM_merged_count.tsv"
count_merge_entity_align(input_file, rel_triples, test_data, output_path)

input_file = fread("../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-SEA/LLM-LLM", header = F)
output_path = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-SEA/LLM-LLM_merged_count.tsv"
count_merge_entity_align(input_file, rel_triples, test_data, output_path)

