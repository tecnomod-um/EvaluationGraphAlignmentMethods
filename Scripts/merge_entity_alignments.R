merge_entity_align = function(main_path_results, methods, pairs, path_save){
  library(data.table)
  for (pair in pairs){
    ent_match = data.frame()
    for (method in methods){
      files = list.files(paste0(main_path_results, method, "/", pair), recursive = T)
      index = grep("ent_match", files)
      if (length(index) > 0) {
        path = paste0(main_path_results, method, "/", pair, "/", files[index])
        ent_match_file = fread(path, header = F)
        ent_match = rbind(ent_match, ent_match_file)
      }
    }
    ent_match = ent_match[!duplicated(ent_match),]
    fwrite(ent_match, paste0(path_save, pair), col.names = F, row.names = F, sep = "\t", quote = F)
  }
}

#Ecommerce
main_path_results = "$PATH"
path_save = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-BootEA"
methods = c("AttrE", "BootEA") 
pairs = c("LLM-LLM")
merge_entity_align(main_path_results, methods, pairs)

path_save = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-AlignE"
methods = c("AttrE", "AlignE") 
merge_entity_align(main_path_results, methods, pairs)

path_save = "../E-CommerceData/Experiments/EntityAlignment/merged_methods/AttrE-SEA"
methods = c("AttrE", "SEA") 
merge_entity_align(main_path_results, methods, pairs)