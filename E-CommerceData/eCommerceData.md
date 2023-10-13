# E-Commerce Data

* URL: https://www.kaggle.com/datasets/carrie1/ecommerce-data
* Format: CSV
* Description: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

## Datasets

* [data.csv](./SourceFiles/data.csv)
  * 541909 rows x 8 columns
* [data_proper_encoding_bad_columns.csv](../../../data_proper_encoding_bad_columns.csv)
  * 541909 rows x 8 columns
  * Removal of the pound sign
  * Removal of quotes
* [data50K.csv](../../../data50K.csv)
  * 50000 rows x 8 columns
  * From above, selection of the first 50000 rows
  * Removal of extra commas in the "Description" field
* [data20K.csv](../../../data20K.csv)
  * 20000 rows x 8 columns
  * From above, selection of the first 20000 rows
  * Replacement of "United Kingdom" by "United_Kingdom"

## Ontologies

* [Basic](./Ontologies/eCommerceOntology.owl)
* [LLM](./Ontologies/eCommerceOntologyLLM.owl)
* [Gold standard](./Ontologies/eCommerceOntologyII.owl)
* [Materials](./Ontology/materials_anony_v2.owl)

## Mapping

|Mapping | RDF | attr_triples | rel_triples |
|:------:|:---:|:------------:|:-----------:|
|[Basic](../../../Mappings/mapping.csv.yml)|[164370 triples](../../../Mappings/eCommerce20K.nt)|[61921 triples](./Basic-LLM/Input/attr_triples_1)|[102449 triples](./Basic-LLM/Input/rel_triples_1)|
[LLM](../../../Mappings/mappingLLM.csv.yml)| [121621 triples](../../../Mappings/eCommerceLLM20K.nt)|[81277 triples](./Basic-LLM/Input/attr_triples_2)|[40344 triples](./Basic-LLM/Input/rel_triples_2)|
|[Gold](../../../Mappings/mappingGold.csv.yml)|[168290 triples](../../../Mappings/eCommerceGold20K.nt)|[65841 triples](./Gold-LLM/Input/attr_triples_1)|[102449 triples](./Gold-LLM/Input/rel_triples_1)|
|[Materials](../../../Mappings/mappingMaterials.csv.yml)|[41256 triples](../../../Mappings/eCommerceMaterials20K.nt)|[0 triples](./LLM-Materials/Input/attr_triples_2)|[41256 triples](./LLM-Materials/Input/rel_triples_2)|
|[Gold II](../../../Mappings/mappingGoldII.csv.yml)|[207068 triples](../../../Mappings/eCommerceGoldII20K.nt)|[104619 triples](./GoldII-MaterialsII/Input/attr_triples_1)|[102449 triples](./GoldII-MaterialsII/Input/rel_triples_1)|
|[Materials II](../../../Mappings/mappingMaterialsII.csv.yml)|[84848 triples](../../../Mappings/eCommerceMaterialsII20K.nt)|[43592 triples](./GoldII-MaterialsII/Input/attr_triples_2)|[41256 triples](./GoldII-MaterialsII/Input/rel_triples_2)

## [Basic - LLM](./Basic-LLM/)

![Graph Basic - LLM](../Figures/eCommerce-Basic-LLM.png "Graph Basic - LLM")

### [Input](./Basic-LLM/Input/)

|[ent_links](./Basic-LLM/Input/ent_links)| Related Entities | Split 1 - Test| Split 2 - Test|
|:-:|:-:|:-:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://vocab.um.es#Product>| 19424 (92.84%)  | 11629 (92.64%) | 11663 (92.92%) |
<https://schema.org/Invoice> - <https://vocab.um.es#Invoice>|  937 (4.48%)  | 581 (4.62%) | 562 (4.48%) | 
|<https://vocab.um.es/Customer> - <https://vocab.um.es#Customer> |  560 (2.68%)  | 342 (2.72%) | 327 (2.61%) |
| Total related entities |  20921 | 12552 | 12552 |

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Basic-LLM/Input/631_2fold/1/)|6276|12552|2093|
|[2](./Basic-LLM/Input/631_2fold/2/)|6276|12552|2093|

### [Output](./Basic-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Invoice (#/%) | Customer (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[12552](./Basic-LLM/Output/BootEA/1/alignment_results_12)|8.6|25.1 |39.7 |92|0.18|2688|621 (5.34%) | 429 (73.83%) | 1 (0.29%)|
|BootEA|2|[12551](./Basic-LLM/Output/BootEA/2/alignment_results_12)|8.4|25.1 |39.7 |100|0.18|2606|607 (5.20%)|431 (76.69%)|1 (0.31%)|
|BootEA Rotate|1|[12552](./Basic-LLM/Output/BooteaRotatE/1/alignment_results_12)|9.1|26.1 |41.1 |104|0.18|11444|679(5.84%)|432 (74.35%)|2 (0.58%)|
|BootEA Rotate|2|[12551](./Basic-LLM/Output/BooteaRotatE/2/alignment_results_12)|8.8|26.4 |41.3 |105|0.18|11793|642 (5.50%)|433 (77.05%)|0 (0.0%)
|RSN4EA|1|[12552](./Basic-LLM/Output/RSN4EA/1/alignment_results_12)|8.9|26.6 |41.5 |215|0.18|4048|662 (5.69%) | 433 (74.53%)|0 (0.0%)
|AttrE|1|[12552](./Basic-LLM/Output/AttrE/1/alignment_results_12)|74.9|91.5|94.1 |7|0.82|3271|7840 (67.42%)|420 (72.29%)|3 (0.88%))

## [Gold - LLM](./Gold-LLM/)

![Graph Gold-LLM](../Figures/eCommerce-Gold-LLM.png "Graph Gold-LLM")

### [Input](./Gold-LLM/Input/)

|[ent_links](./Gold-LLM/Input/ent_links)| Related Entities |Split 1 - Test| Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://vocab.um.es#Product>| 19424 (92.84%)  | 11651 (92.82%) |11645 (92.77%)|
<https://schema.org/Invoice> - <https://vocab.um.es#Invoice>|  937 (4.48%)  | 571 (4.55%) |567 (4.52%)| 
|<https://vocab.um.es/Customer> - <https://vocab.um.es#Customer> |  560 (2.68%)  |330 (2.63%) |340 (2.71%)|
| Total related entities |  20921 |12552|12552|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Gold-LLM/Input/631_2fold/1/)|6276|12552|2093|
|[2](./Gold-LLM/Input/631_2fold/2/)|6276|12552|2093|

### [Output](./Gold-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Invoice (#/%) | Customer (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[12551](./Gold-LLM/Output/BootEA/1/alignment_results_12)|8.8|26.1 |41.3 |75|0.18|5037|640 (5.49%)|432 (75.66%) | 0 (0.0%)|
|BootEA|2|[12551](./Gold-LLM/Output/BootEA/2/alignment_results_12)|8.8|25.7 |40.9 |81|0.18|4794|661 (5.68%)|430 (75.84%)|3 (0.89%)|
|RSN4EA|1|[12551](./Gold-LLM/Output/RSN4EA/1/alignment_results_12)|8.8|25.8 |41.0 |261|0.18|3060|640 (5.49%)|431 (75.48%)|0 (0.0%)|
|AttrE|1|[12551](./Gold-LLM/Output/AttrE/1/alignment_results_12)|81.8|94.9|96.5|3|0.88|3967|8847 (75.93%)|423 (74.08%)|16 (4.86%)|


## [Gold - Basic](./Gold-Basic/)

![Graph Gold-Basic](../Figures/eCommerce-Gold-Basic.png "Graph Gold-Basic")

### [Input](./Gold-Basic/Input/)

|[ent_links](./Gold-Basic/Input/ent_links)| Related Entities |Split 1 - Test|
|:--------------:|:----------------:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://purl.org/ontologies/MT/salesArticle>| 19424 (45.39%) |11611 (45.23%)|
<https://schema.org/Invoice> - <https://schema.org/Invoice>|  937 (2.19%)  |550 (2.14%)|
|<https://vocab.um.es/Customer> - <https://vocab.um.es/Customer> |  560 (1.31%) |328 (1.28%)
<https://schema.org/Country> - <https://schema.org/Country>|  16 (0.04%) |11 (0.04)
<https://schema.org/UnitPriceSpecification> - <https://schema.org/UnitPriceSpecification>|  19449 (45.45%)  |11706 (45.60%)
<https://schema.org/Product> - <https://schema.org/Product>|  2404 (5.62%) |1466 (5.71%)
| Total related entities |  42790 |25673|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Gold-Basic/Input/631_2fold/1/)|12837|25673|4280|
|[2](./Gold-Basic/Input/631_2fold/2/)|12837|25673|4280|

### [Output](./Gold-Basic/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Invoice (#/%) | Customer (#/%) |Product (#/%)|Country (#/%)|UnitPriceSpecification (#/%)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[25672](./Gold-Basic/Output/BootEA/1/alignment_results_12)|98.1|99.1 |99.3 |2|0.99|18498|11428 (98.42%)|538 (97.82%)|327 (99.70%)|1374 (93.72%)|11 (100%)|11481 (98.08%)|
|RSN4EA|1|[25672](./Gold-Basic/Output/RSN4EA/1/alignment_results_12)|72.9|81.0|83.4|166|0.77|19296|10134 (87.28%)|472 (85.82%)|249 (75.91%)|1076 (73.40%)|5 (45.45%)|5648 (48.25%)|
|AttrE|1|[25672](./Gold-Basic/Output/AttrE/1/alignment_results_12)|98.1|99.6|99.8|1|0.99|10127|11381 (98.02)| 528 (96.00)|313 (95.43%)|1430 (97.54%)|4 (36.36%)|11143 (95.19%)|

## [LLM - Materials](./LLM-Materials/)

![Graph LLM - Materials](../Figures/eCommerce-LLM-Materials.png "Graph LLM - Materials")

### [Input](./LLM-Materials/Input/)

|[ent_links](./LLM-Materials/Input/ent_links)| Related Entities |Split 1 - Test|Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://vocab.um.es#Product> - <https://purl.org/ontologies/MT/salesArticle>| 19424  |11654|11654|
| Total related entities |  19424 | 11654|11654|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./LLM-Materials/Input/631_2fold/1/)|5827|11654|1943|
|[2](./LLM-Materials/Input/631_2fold/2/)|5827|11654|1943|

### [Output](./LLM-Materials/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|Product (#/%)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[11654](./LLM-Materials/Output/BootEA/1/alignment_results_12)|0.0|0.0 |0.0 |5948|0.00|928|0 (0.0%)
|BootEA|2|[11654](./LLM-Materials/Output/BootEA/2/alignment_results_12)|0.0|0.0 |0.0 |5928|0.00|964|0 (0.0%)|
|RSN4EA|1||E|r |r |o|r||
|AttrE|1|[11654](./LLM-Materials/Output/AttrE/1/alignment_results_12)|0.2|1.1 |2.0 |2850|0.01|464|30 (0.26%)|

## [LLM - Materials(P)](./LLM-Materials(P)/)


### [Input](./LLM-Materials(P)/Input/)

|[ent_links](./LLM-Materials(P)/Input/ent_links)| Related Entities |Split 1 - Test|Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://vocab.um.es#Product> - <https://purl.org/ontologies/MT/sales_product>| 19424  |11654|11654|
| Total related entities |  19424 |11654|11654|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./LLM-Materials(P)/Input/631_2fold/1/)|5827|11654|1943|
|[2](./LLM-Materials(P)/Input/631_2fold/2/)|5827|11654|1943|

### [Output](./LLM-Materials(P)/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|Product (#/%)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[11654](./LLM-Materials(P)/Output/BootEA/1/alignment_results_12)|0.0|0.0 |0.0 |5976|0.00|1392|0 (0.0%)|
|BootEA|2|[11654](./LLM-Materials(P)/Output/BootEA/2/alignment_results_12)|0.0|0.0 |0.0 |5911|0.00|1425|0 (0.0%)|
|AttrE|1|[11654](./LLM-Materials(P)/Output/AttrE/1/alignment_results_12)|2.0|7.6 |12.4 |1289|0.05|811|829 (7.11%)|

## [Basic - Materials](./Basic-Materials/)

![Graph Basic - Materials](../Figures/eCommerce-Basic-Materials.png "Graph Basic - Materials")

### [Input](./Basic-Materials/Input/)

|[ent_links](./Basic-Materials/Input/ent_links)| Related Entities |Split 1 - Test|Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://purl.org/ontologies/MT/salesArticle>| 19424 (88.97%)  |11678 (89.15%)|11676 (89.14%)|
|<https://schema.org/Product> - <https://purl.org/ontologies/MT/sales_product>| 2408 (11.03%) | 1421 (10.85%)| 1423 (10.86%)|
| Total related entities |  21832 | 13099|13099|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Basic-Materials/Input/631_2fold/1/)|6549|13099|2184|
|[2](./Basic-Materials/Input/631_2fold/2/)|6549|13099|2184|

### [Output](./Basic-Materials/Output/)

Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Product (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[13099](./Basic-Materials/Output/BootEA/1/alignment_results_12)|19.8|50.7 |69.0 |177|0.34|4292|929 (7.96%)|622 (43.80%)|
|BootEA|2|[13099](./Basic-Materials/Output/BootEA/2/alignment_results_12)|20.2|51.3 |69.9 |187|0.35|3970|966 (8.27%)|655 (46.06%)
|RSN4EA|1|[13099](./Basic-Materials/Output/RSN4EA/1/alignment_results_12)|20.7|50.9 |67.0 |570|0.34|5757|1642 (14.13%)|1038 (70.37%)|
|AttrE|1|[13099](./Basic-Materials/Output/AttrE/1/alignment_results_12)|15.0|33.8|45.9 |627|0.24|2129|884 (7.61%)|970 (65.76%)|

## [Gold - Materials](./Gold-Materials/)    

![Graph Gold - Materials](../Figures/eCommerce-Gold-Materials.png "Graph Gold - Materilas")

### [Input](./Gold-Materials/Input/)

|[ent_links](./Gold-Materials/Input/ent_links)| Related Entities |Split 1 - Test|Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://purl.org/ontologies/MT/salesArticle>| 19424 (88.97%) |11655 (88.98%)|11641 (88.87%)|
|<https://schema.org/Product> - <https://purl.org/ontologies/MT/sales_product>| 2408 (11.03%) | 1444 (11.02%)|1458 (11.13%)|
| Total related entities |  21832 | 13099 |13099|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Gold-Materials/Input/631_2fold/1/)|6549|13099|2184|
|[2](./Gold-Materials/Input/631_2fold/2/)|6549|13099|2184|

### [Output](./Gold-Materials/Output/)

Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Product (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[13099](./Gold-Materials/Output/BootEA/1/alignment_results_12)|19.7|49.6 |68.2 |195|0.34|3691|1503 (12.90%)|1016 (70.51%)
|BootEA|2|[13099](./Gold-Materials/Output/BootEA/2/alignment_results_12)|19.9|50.9 |69.3 |189|0.34|4120|1561 (13.41%)|1020 (70.01%)|
|RSN4EA|1|[13099](./Gold-Materials/Output/RSN4EA/1/alignment_results_12)|20.5|51.8 |70.4 |556|0.35|3318|1615 (13.87%) | 1022 (70.92%(|))
|AttrE|1|[13099](./Gold-Materials/Output/AttrE/1/alignment_results_12)|51.6|75.2 |80.9|43|0.62|3164|4633 (39.75%)|1004 (69.67%)|

## [Gold(II) - Materials(II)](./GoldII-MaterialsII/)

![Graph Gold II - Materials II](../Figures/eCommerce-GoldII-MaterialsII.png "Graph Gold II - Materials II")

### [Input](./GoldII-MaterialsII/Input/)

|[ent_links](./GoldII-MaterialsII/Input/ent_links)| Related Entities |Split 1 - Test|Split 2 - Test|
|:--------------:|:----------------:|:-:|:-:|
|<https://purl.org/ontologies/MT/salesArticle> - <https://purl.org/ontologies/MT/salesArticle>| 19424 (88.97%)  | 11628 (88.77%) |11675 (89.13%)|
|<https://schema.org/Product> - <https://purl.org/ontologies/MT/sales_product>| 2408 (11.03%) | 1471 (11.23%) |1424 (10.87%)|
| Total related entities |  21832 | 13099|

|Split|Training (30%) | Test (60%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./GoldII-MaterialsII/Input/631_2fold/1/)|6549|13099|2184|
|[2](./GoldII-MaterialsII/Input/631_2fold/2/)|6549|13099|2184|

### [Output](./GoldII-MaterialsII/Output/)

Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time (s)|salesArticle (#/%) | Product (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|BootEA|1|[13099](./GoldII-MaterialsII/Output/BootEA/1/alignment_results_12)|20.5|49.9 |68.2 |197|0.34|3265|1567 (13.48%)|1061 (72.13%)|
|BootEA|2|[13099](./GoldII-MaterialsII/Output/BootEA/2/alignment_results_12)|19.3|48.7|67.5 |221|0.33|3142|1510 (12.93%)|985 (69.17%)|
|RSN4EA|1|[13099](./GoldII-MaterialsII/Output/RSN4EA/1/alignment_results_12)|21.2|52.8|70.4|498|0.36|3265|1662 (14.29%) |1067 (72.54%)|
|AttrE|1|[13099](./GoldII-MaterialsII/Output/AttrE/1/alignment_results_12)|56.0|79.8|84.6|34|0.67|3918|5244 (45.10%)| 1054 (71.65%)|

## Metrics

|Alignment|Approach|Split|h@1 (%)|h@5 (%)|h@10 (%)|MR|MRR [0,1]|Run Time (s)|
|:------:|:------:|:---:|:-:|:-:|:--:|:-:|:-:|:-:|
|Basic-LLM|Bootea|1|8.6|25.1 |39.7 |92|0.18|2688|
|Basic-LLM|Bootea|2|8.4|25.1 |39.7 |100|0.18|2606|
|Basic-LLM|BooteaRoot|1|9.1|26.1 |41.1 |104|0.18|11444|
|Basic-LLM|BooteaRoot|2|8.8|26.4 |41.3 |105|0.18|11793|
|Basic-LLM|RSN4EA|1|8.9|26.6 |41.5 |215|0.18|4048|
|Basic-LLM|AttrE|1|74.9|91.5|94.1 |7|0.82|3271|
|Gold-LLM|Bootea|1|8.8|26.1 |41.3 |75|0.18|5037|
|Gold-LLM|Bootea|2|8.8|25.7 |40.9 |81|0.18|4794|
|Gold-LLM|RSN4EA|1|8.8|25.8 |41.0 |261|0.18|3060|
|Gold-LLM|AttrE|1|81.8|94.9|96.5|3|0.88|3967|
|LLM-Gold*|Bootea|1|9.0|26.2 |40.2 |99|0.18|3457|
|Gold-Basic|Bootea|1|98.1|99.1 |99.3 |2|0.99|18498|
|Gold-Basic|RSN4EA|1|72.9|81.0|83.4|166|0.77|19296|
|Gold-Basic|AttrE|1|98.1|99.6|99.8|1|0.99|10127|
|LLM-Materials|Bootea|1|0.0|0.0 |0.0 |5948|0.00|928|
|LLM-Materials|Bootea|2|0.0|0.0 |0.0 |5928|0.00|964|
|LLM-Materials|RSN4EA|2|E|r|r|o|r|||
|LLM-Materials|AttrE|1|0.2|1.1 |2.0 |2850|0.01|464|
|LLMII**-Materials|Bootea|1|0.0|0.0 |0.0 |5915|0.00|1001|
|LLM-Materials(P)***|Bootea|1|0.0|0.0 |0.0 |5976|0.00|1392|
|LLM-Materials(P)***|Bootea|2|0.0|0.0 |0.0 |5911|0.00|1425|
|LLM-Materials(P)***|AttrE|1|2.0|7.6 |12.4 |1289|0.05|811|
|LLM-MaterialsII|Bootea|1|0.0|0.0 |0.1 |5935|0.00|974|
|LLM-MaterialsII|AttrE|1|0.6|1.8 |3.0|2163|0.02|668|
|Basic-Materials|Bootea|1|19.8|50.7 |69.0 |177|0.34|4292|
|Basic-Materials|Bootea|2|20.2|51.3 |69.9 |187|0.35|3970|
|Basic-Materials|RSN4EA|1|20.7|50.9 |67.0 |570|0.34|5757|
|Basic-Materials|AttrE|1|15.0|33.8|45.9 |627|0.24|1857|
|Gold-Materials|Bootea|1|19.7|49.6 |68.2 |195|0.34|3691|
|Gold-Materials|Bootea|2|19.9|50.9 |69.3 |189|0.34|4120|
|Gold-Materials|RSN4EA|1|20.5|51.8 |70.4 |556|0.35|3318|
|Gold-Materials|AttrE|1|51.6|75.2 |80.9|43|0.62|3164|
|GoldII-MaterialsII|Bootea|1|20.5|49.9 |68.2 |197|0.34|3265|
|GoldII-MaterialsII|Bootea|2|19.3|48.7|67.5 |221|0.33|3142|
|GoldII-MaterialsII|RSN4EA|1|21.2|52.8|70.4|498|0.36|3265|
|GoldII-MaterialsII|AttrE|1|56.0|79.8|84.6|34|0.67|3918|

*LLM-Gold, to verify that the algorithm is symmetric

**LLMII, the instance identifier has been changed (from "StockCode_InvoiceNo" to "InvoiceNo_StockCode") to match with the instance identifier of Materials ("InvoiceNo_StockCode")

***Materials(P), the algorithm attemps to align the mt:sales_product entities of Materials. One mt:sales_product entity aligns with several um:Product entities of LLM.



### Discussion

1. LLM mapping uses only the "StockCode" as identifier. It is not suitable for modulating n-ary relationships (price, quantity, sales item).
2. "Materials" has only two classes and one object property between them. 
3. Increasing attributes in Materials II and Gold II.
4. BottEA and RSN4EA show similar results for Basic and Gold versus LLM. However, AttrE shows much better results in these cases, being even better with Gold than with Basic.
5. In general, the best result is between Bacic and Gold, generating the worst result RSN4EA 
6. In general, the worst result is between LLM and Materials. Bootea and RSN4EA show similar results for LLM versus Materials. With AttrE showing a slight improvement, but still slightly better with LLM-MaterialsII. 
7. Bottea and RSN4EA show similar results for Basic and Gold versus Materials, even for GoldII-MaterialsII, showing that increasing the number of attributes (data properties) by both Gold and Materials does not affect the performance of these algorithms. 
the  However, AttrE shows much better results in these cases, being even better with Gold than with Basic.
8. However, for AttrE, while it performs worse in Basic-Materials than the other two algorithms, it improves substantially in Gold-Materials. The results for GoldII-MaterialsII are even better. Demostrating that this algorithm is indeed susceptible to the number of attributes present in the KGs. 
9. According to the results obtained between the different datasets and alignment methods used, which take into account both the structure of relationships between classes and the attributes that describe the elements of each of them, it is observed that there is a greater similarity between the semantic schemas of Basic and Gold with LLM than with Materials or even MaterialsII.
10. According to the classes to which the aligned entities belong:
    1. Basic-LLM and Gold-LLM. The Invoice class with 75% achieves the most alignments, while the second one is around 5% for the BootEA and RSN4EA methods. However, AttrE maintains this percentage with Invoice but improves the salesArticle class to 67% and 76% for Basic and Gold respectively. 
    2. While for the other methods there is no difference between the different LLM-Materials formats, AttrE does manage to increase the alignment between the one representing the LLM salesArticle class (um:Product) and the one representing the Materials Product class (mt:sales_product). Although these two classes should not be aligned according to the general pattern followed in this dataset. This indicates a lack of semantic expressiveness.
    3. In Basic-Materials, the Product class is the one that gets the most alignment in all methods with respect to the salesArticle. The same is true for Gold. Although in the latter, the alignment improvements for AttrE occur with the salesArticle class.

### Conclusions

1. To improve the alignment of entities between knowledge graphs, it is important to identify the underlying patterns and sub-patterns between both graphs. One objective would be the development of reference patterns on which the developed ontologies are based.
2. These algorithms are not based on the text of entities, relationships or attributes. 
Bootea, Bootea Rotate and RSN4EA are based on the structure of the relationships between nodes, especially those corresponding to object properties.
3. AttrE is more influenced by data properties than the object properties
4. In the case of dealing with simple ontologies, whith few object properties and data properties AttrE presents worse results, but as the number of data properties increases, they improve significantly.
5. In the absence of more in-depth studies, the results of both Bootea (object properties) and AttrE (data properties) could be used to determine the structural similarity between two KGs by means of entity alignment analysis for a given dataset.  
6. Among the semantic schemes of LLM, Basic and Gold, the last two are the ones with which AttrE and BootEA achieve the best alignment, very close to the optimum, due to the great similarity in the structure of these schemas.
    * In both Basic-LLM and Gold-LLM pairs, the improvement of the results of AttrE over BootEA is due to the "salesArticle" class, as the other two classes to be aligned maintain their results in both methods. Mainly due to the high number of attributes that this class presents.
7. The Materials semantic schema has been reduced to the two classes whose entities can be aligned according to the CSV file. The results are not very good when comparing this schema with LLM or Basic, but do well with Gold, as these classes lack a clear structure both in terms of attributes and relationships between classes.
    * It is only when we enrich classes with attributes, not with relationships between classes, that we see an improvement in the percentage of aligned entities for AttrE
    * Looking at the LLM-Materials pair, it can be concluded that in the face of poor or too simple schemes, both AttrE and BootEA are not able to align entities.

### Notes

1. The metrics indicated in the tables refer to the CSLS method, while the data on the number of entities per class refer to the Greedy method (data that appear in the respective nohup.out file).
2. [Sun et al.](http://www.vldb.org/pvldb/vol13/p2326-sun.pdf) are comparing two different methods for entity alignment in the context of knowledge graph embeddings. The two methods being compared are "Greedy" and "CSLS" (Cross-Domain Similarity Local Scaling). The results are reported using the Hits@1 metric for various models on the D-Y-15K (V1) dataset. Here are the main differences between the results obtained using Greedy and CSLS:
    1. Greedy:
        * The Greedy method uses a nearest neighbor search strategy to perform entity alignment between two knowledge graphs.
        * For each entity in the source knowledge graph (KG), it finds its nearest neighbor in the target KG based on a similarity metric (e.g., cosine similarity).
        * The entity alignment is performed in a local manner, considering only the immediate nearest neighbor for each entity.
    2. CSLS (Cross-Domain Similarity Local Scaling):
        * CSLS is an alternative metric used to enhance the conventional distance metrics (such as cosine similarity) used in entity alignment.
        * It normalizes the similarity of source and target entity embeddings based on the density of their embedding neighbors.
        * The CSLS function is defined as: $$CSLS(xs, xt) = 2 * cos(xs, xt) − ψt(xs) − ψs(xt)$$, where cos(xs, xt) is the cosine similarity between source entity xs and target entity xt, and ψt(xs) and ψs(xt) are the average similarities of xs and xt with their top-k nearest neighbors in the target and source KGs, respectively.
        * CSLS reduces the similarities between hub entities (entities with many neighbors) and other entities. It also gives fair consideration to some isolated entities (entities with few neighbors) during testing, as they receive less similarity penalization.
    3. Results Comparison:
        * The authors report the Hits@1 results for different models using both Greedy and CSLS methods.
        * Based on the reported results in Table 6, it is evident that using CSLS significantly improves the performance of the Greedy strategy in entity alignment for most of the models. The Hits@1 scores are generally higher when using CSLS compared to the Greedy method alone.
    4. In summary, CSLS is a metric that enhances the conventional distance metrics used in entity alignment, and when combined with the Greedy strategy, it leads to better alignment results in terms of the Hits@1 metric across different models on the D-Y-15K (V1) dataset.