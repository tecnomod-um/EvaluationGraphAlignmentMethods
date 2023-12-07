# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:24:27 2023

@author: gines
"""
import re
import csv
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef



def create_pattern(dict_field, list_field, prefix_data):
    '''From a dictionary, a list of field names and a prefix
    this function creates a pattern'''
#    replacers = {' ':'%20', '!':'%21', '"':'%22', '#':'%23', '$':'%24',  '%':'%25', '&':'%26', "'":"%27", '(':'%28', ')':'%29', '*':'%2A', '+':'%2B', ',':'%2C', '/':'%2F',
#                 ':':'%3A', ';':'%3B', '=':'%3D', '?':'%3F', '@':'%40', '[':'%5B', ']':'%5D', }
    list_identifier = []
    identifier = ""

    if pd.isnull(dict_field[list_field[0]]):       ##When the field is a null value
        return ""
    elif len(list_field) == 1:                        ##Only there is one field [(field)]
        if re.findall('^https://',dict_field[list_field[0]]) or re.findall('^http://',dict_field[list_field[0]]):  
          identifier = dict_field[list_field[0]]
        else:
          identifier = dict_field[list_field[0]]
    else:                                           ##Multi-field  [(field1, field2), "string"]            
        for field in list_field[0]:
            list_identifier.append(dict_field[field])
        identifier = list_field[1].join(list_identifier)    
        
    pattern_id = URIRef(prefix_data + identifier)
    return pattern_id
        


## Input data

file_source = "../E-CommerceData/Mappings/ecommercedataLLM.nt"
file_target = "../E-CommerceData/Mappings/ecommercedataLLM.nt"
file_csv = "../E-CommerceData/SourceFiles/data20K.csv"

    #Entities to be aligned [prefix, class, list heads]


#### Gold-Basic  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"])]
## Target Dataset
#data2 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"])]

#### Object Properties
##Gold
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es/ontology/ecd/hasCountry"), URIRef("https://vocab.um.es/ontology/ecd/hasProduct"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesSpecification"), URIRef("https://vocab.um.es/ontology/ecd/hasCustomer"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesArticle"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesCountry")]
##Basic
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")]
##########

#### Gold-LLM  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"]), ("https://vocab.um.es/data/ecd/salesArticle_", "https://vocab.um.es/ontology/ecd/salesArticle", ["InvoiceNo_StockCode_pro"]), ("https://vocab.um.es/data/ecd/salesSpecification_", "https://vocab.um.es/ontology/ecd/SalesSpecification", ["Quantity_UnitPrice_Quantity_pro"])]
## Target Dataset
#data2 = [("https://vocab.um.es#invoice/", "https://vocab.um.es#invoice", ["InvoiceNo"]), ("https://vocab.um.es#salesArticle/", "https://vocab.um.es#salesArticle", ["StockCode_pro"]), ("http://schema.org/UnitPriceSpecification/", "http://schema.org/UnitPriceSpecification", ["UnitPrice"])]

#### Object Properties
##Gold
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es/ontology/ecd/hasCountry"), URIRef("https://vocab.um.es/ontology/ecd/hasProduct"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesSpecification"), URIRef("https://vocab.um.es/ontology/ecd/hasCustomer"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesArticle"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesCountry")]
##LLM
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es#hasSalesArticle"), URIRef("https://vocab.um.es#unitPriceSpecification")]
##########

#### Basic-LLM  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"])]
## Target Dataset
#data2 = [("https://vocab.um.es#invoice/", "https://vocab.um.es#invoice", ["InvoiceNo"])]

#### Object Properties
##Basic
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")]
##LLM
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es#hasSalesArticle"), URIRef("https://vocab.um.es#unitPriceSpecification")]
##########

#### Gold-Materials  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/salesArticle_", "https://vocab.um.es/ontology/ecd/salesArticle", ["InvoiceNo_StockCode_pro"]), ("https://vocab.um.es/data/ecd/product_", "https://vocab.um.es/ontology/ecd/Product", ["StockCode_pro"])]
## Target Dataset
#data2 = [("https://purl.org/ontologies/MT/data/salesArticle_", "https://purl.org/ontologies/MT/SalesArticle", ["InvoiceNo_StockCode_pro"]), ("https://purl.org/ontologies/MT/data/salesProduct_", "https://purl.org/ontologies/MT/sales_product", ["StockCode_pro"])]

#### Object Properties
##Gold
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es/ontology/ecd/hasCountry"), URIRef("https://vocab.um.es/ontology/ecd/hasProduct"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesSpecification"), URIRef("https://vocab.um.es/ontology/ecd/hasCustomer"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesArticle"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesCountry")]
##Materials
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://purl.org/ontologies/MT/containsProduct")]
##########

#### Materials-LLM  ###########
  ## Source Dataset
#data1 = [("https://purl.org/ontologies/MT/data/salesArticle_", "https://purl.org/ontologies/MT/SalesArticle", ["InvoiceNo_StockCode_pro"])]
## Target Dataset
#data2 = [("https://vocab.um.es#salesArticle/", "https://vocab.um.es#salesArticle", ["StockCode_pro"])]

#### Object Properties
##Materials
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://purl.org/ontologies/MT/containsProduct")]
##LLM
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es#hasSalesArticle"), URIRef("https://vocab.um.es#unitPriceSpecification")] 
##########

#### Materials-Materials  ###########
  ## Source Dataset
#data1 = [("https://purl.org/ontologies/MT/data/salesArticle_", "https://purl.org/ontologies/MT/SalesArticle", ["InvoiceNo_StockCode_pro"]), ("https://purl.org/ontologies/MT/data/salesProduct_", "https://purl.org/ontologies/MT/sales_product", ["StockCode_pro"])]
## Target Dataset
#data2 = [("https://purl.org/ontologies/MT/data/salesArticle_", "https://purl.org/ontologies/MT/SalesArticle", ["InvoiceNo_StockCode_pro"]), ("https://purl.org/ontologies/MT/data/salesProduct_", "https://purl.org/ontologies/MT/sales_product", ["StockCode_pro"])]

#### Object Properties
##Materials
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://purl.org/ontologies/MT/containsProduct")]
##Materials
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://purl.org/ontologies/MT/containsProduct")] 
##########

#### Gold-Gold  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/salesArticle_", "https://vocab.um.es/ontology/ecd/salesArticle", ["InvoiceNo_StockCode_pro"]), ("https://vocab.um.es/data/ecd/product_", "https://vocab.um.es/ontology/ecd/Product", ["StockCode_pro"]), ("https://vocab.um.es/data/ecd/country_", "https://vocab.um.es/ontology/ecd/Country", ["Country_pro"]), ("https://vocab.um.es/data/ecd/customer_", "https://vocab.um.es/ontology/ecd/Customer", ["CustomerID"]), ("https://vocab.um.es/data/ecd/salesSpecification_", "https://vocab.um.es/ontology/ecd/SalesSpecification", ["Quantity_UnitPrice_Quantity_pro"]), ("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"]) ]
## Target Dataset
#data2 = [("https://vocab.um.es/data/ecd/salesArticle_", "https://vocab.um.es/ontology/ecd/salesArticle", ["InvoiceNo_StockCode_pro"]), ("https://vocab.um.es/data/ecd/product_", "https://vocab.um.es/ontology/ecd/Product", ["StockCode_pro"]), ("https://vocab.um.es/data/ecd/country_", "https://vocab.um.es/ontology/ecd/Country", ["Country_pro"]), ("https://vocab.um.es/data/ecd/customer_", "https://vocab.um.es/ontology/ecd/Customer", ["CustomerID"]), ("https://vocab.um.es/data/ecd/salesSpecification_", "https://vocab.um.es/ontology/ecd/SalesSpecification", ["Quantity_UnitPrice_Quantity_pro"]), ("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"]) ]

#### Object Properties
##Gold
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es/ontology/ecd/hasCountry"), URIRef("https://vocab.um.es/ontology/ecd/hasProduct"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesSpecification"), URIRef("https://vocab.um.es/ontology/ecd/hasCustomer"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesArticle"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesCountry")]
##Materials
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es/ontology/ecd/hasCountry"), URIRef("https://vocab.um.es/ontology/ecd/hasProduct"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesSpecification"), URIRef("https://vocab.um.es/ontology/ecd/hasCustomer"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesArticle"), URIRef("https://vocab.um.es/ontology/ecd/hasSalesCountry")]
##########

#### Basic-Basic  ###########
  ## Source Dataset
#data1 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"])]
## Target Dataset
##data2 = [("https://vocab.um.es/data/ecd/invoice_", "https://vocab.um.es/ontology/ecd/Invoice", ["InvoiceNo"])]

#### Object Properties
##Basic
#obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")]
##Basic
#obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")]
##########

#### LLM-LLM  ###########
  ## Source Dataset
data1 = [("https://vocab.um.es#invoice/", "https://vocab.um.es#invoice", ["InvoiceNo"]), ("https://vocab.um.es#salesArticle/", "https://vocab.um.es#salesArticle", ["StockCode_pro"]), ("http://schema.org/UnitPriceSpecification/", "http://schema.org/UnitPriceSpecification", ["UnitPrice"])]
## Target Dataset
data2 = [("https://vocab.um.es#invoice/", "https://vocab.um.es#invoice", ["InvoiceNo"]), ("https://vocab.um.es#salesArticle/", "https://vocab.um.es#salesArticle", ["StockCode_pro"]), ("http://schema.org/UnitPriceSpecification/", "http://schema.org/UnitPriceSpecification", ["UnitPrice"])]

#### Object Properties
##LLM
obj_prop1 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es#hasSalesArticle"), URIRef("https://vocab.um.es#unitPriceSpecification")]
##LLM
obj_prop2 = [URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("https://vocab.um.es#hasSalesArticle"), URIRef("https://vocab.um.es#unitPriceSpecification")]
##########

## Output data

ent_links = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/ent_links"
ent_link_out = open(ent_links, "w", encoding="utf-8")

attr_triples_1 = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/attr_triples_1"
att_trip_1 = open(attr_triples_1, "w", encoding="utf-8")
attr_triples_2 = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/attr_triples_2"
att_trip_2 = open(attr_triples_2, "w", encoding="utf-8")

rel_triples_1 = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/rel_triples_1"
rel_trip_1 = open(rel_triples_1, "w", encoding="utf-8")
rel_triples_2 = "../E-CommerceData/Experiments/EntityAlignment/LLM-LLM/Input/rel_triples_2"
rel_trip_2 = open(rel_triples_2, "w", encoding="utf-8")


## Graphs
graph1 = Graph()
graph1.parse(file_source)
graph2 = Graph()
graph2.parse(file_target)

## Variables

list_ent_rel = []

for data_source, data_target in zip(data1, data2):

    ## Entity Data
    prefix1 = data_source[0]  
    prefix2 = data_target[0]
    class1 = URIRef(data_source[1])
    class2 = URIRef(data_target[1])  


## Generate entity links

    with open(file_csv, newline='', encoding='utf-8') as csvfile:       ##Dataset file (csv)
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            pattern_id1 = create_pattern(row, data_source[2], prefix1)
            pattern_id2 = create_pattern(row, data_target[2], prefix2)
            
            if pattern_id1 == "" or pattern_id2 == "": ##When there exist null values
              continue
                
            pattern_entity = pattern_id1 + "\t" + pattern_id2 + "\n"
            
            if pattern_entity not in list_ent_rel: 
              ent_link_out.write(pattern_entity)
              list_ent_rel.append(pattern_entity)

                    
## Close files
ent_link_out.close()


## Generate attributes triples
for subj, pred, obj in graph1:
    
    if (pred not in  obj_prop1): 
        pattern_trip1 = subj + "\t" + pred + "\t" + obj + "\n"
        att_trip_1.write(pattern_trip1)
    else:
        pattern_trip1 = subj + "\t" + pred + "\t" + obj + "\n"
        rel_trip_1.write(pattern_trip1)
        
for subj, pred, obj in graph2:
    if (pred not in  obj_prop2):
        pattern_trip2 = subj + "\t" + pred + "\t" + obj + "\n"    
        att_trip_2.write(pattern_trip2)
    else:
        pattern_trip2 = subj + "\t" + pred + "\t" + obj + "\n"
        rel_trip_2.write(pattern_trip2)
    
## Close files
att_trip_1.close()
att_trip_2.close()
rel_trip_1.close()
rel_trip_2.close()
