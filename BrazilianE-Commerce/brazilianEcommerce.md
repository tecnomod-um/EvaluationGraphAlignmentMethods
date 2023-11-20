# Brazilian E-Commerce

* URL: <https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce>
* Format: CSV
* Description: This is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

## Datasets

* [olist_customers_dataset.csv](./SourceFiles/olist_customers_dataset.csv)
  * 99441 rows x 5 columns
* [processed_olist_customers_dataset_20K.csv](./SourceFiles/processed_olist_customers_dataset_20K.csv)
  * 20000 rows x 10 columns
  * Selected the first 20000 rows of the above file
  * Processing of identifiers for five classes
![Counts processed_olist_customers_dataset_20K.csv](./Figures/count_data.JPG "Counts processed_olist_customers_dataset_20K.csv")

* No field has null values
* "customer_id" is the only field that has all unique values

![Fields cardinality processed_olist_customers_dataset_20K.csv](./Figures/card_data.JPG "Fields cardinality processed_olist_customers_dataset_20K.csv")

* (0,0) No relationship between values in the row and column fields
* (0,1) One value in the row field is related to at most one value in the column field
* (0,2) One value in the row field can be related to none, one or several values in the column field
* (1,1) One value in the row filed is only related to one value in the column field
* (1,2) One value in the row field can be related to one or several values in the column field
* Inconsistencies:
  * A value of a "customer_city" should only be associated with a value of a "customer_state"

## Ontologies

* [Basic](./Ontologies/)
* [LLM](./Ontologies/)
* [Gold standard](./Ontologies//)
* [Transactions](./Ontologies/)

## Mapping

|Mapping |Dataset| RDF | attr_triples | rel_triples |
|:-:|:-:|:-:|:-:|:-:|
|[Basic](./Mappings/mappingBasic.csv.yml)|processed_olist_customers_dataset_20K.csv|[120000 triples](./Mappings/brazilianecommerceBasic.nt)|[10000 triples](./Experiments/EntityAlignment/Basic-Basic/Input/attr_triples_1)|[20000 triples](./Experiments/EntityAlignment/Basic-Basic/Input/rel_triples_1)|
|[Gold](./Mappings/mappingGold.csv.yml)|processed_olist_customers_dataset_20K.csv|[152758 triples](./Mappings/brazilianecommerceGold.nt)|[50857 triples](./Experiments/EntityAlignment/Gold-Gold/Input/attr_triples_1)|[101901 triples](./Experiments/EntityAlignment/Gold-Gold/Input/rel_triples_1)|
|[LLM](./Mappings/mappingLLM.csv.ttl)|processed_olist_customers_dataset_20K.csv|[84357 triples](./Mappings/brazilianecommerceLLM.nt)|[20000 triples](./Experiments/EntityAlignment/LLM-LLM/Input/attr_triples_1)|[64357 triples](./Experiments/EntityAlignment/LLM-LLM/Input/rel_triples_1)|
|[Transactions](./Mappings/mappingTransactions.csv.yml)|processed_olist_customers_dataset_20K.csv|[39686 triples](./Mappings/brazilianecommerceTransactions.nt)|[19843 triples](./Experiments/EntityAlignment/Transactions-Transactions/Input/attr_triples_1)|[19843 triples](./Experiments/EntityAlignment/Transactions-Transactions/Input/rel_triples_1)|

## [Gold - Gold](./Experiments/EntityAlignment/Gold-Gold/)

![Graph Gold](./Figures/BrazilianEcommerce-Gold.png "Graph Gold")

### [Input](./Experiments/EntityAlignment/Gold-Gold/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Gold/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerIdOrder> <https://vocab.um.es/ontology/bre/CustomerIdOrder>| 20000 (39.33%)|8015 (39.40%)
|<https://vocab.um.es/ontology/bre/CustomerAccount> <https://vocab.um.es/ontology/bre/CustomerAccount>|19843 (39.02%)| 7903 (38.85%)|
|<https://vocab.um.es/ontology/bre/State> <https://vocab.um.es/ontology/bre/State>| 27 (0.05%)| 12 (0.06%)|
|<https://vocab.um.es/ontology/bre/City> <https://vocab.um.es/ontology/bre/City>| 2247 (4.42%)| 900 (4.42%)|
|<https://vocab.um.es/ontology/bre/ZipCodePrefix> <https://vocab.um.es/ontology/bre/ZipCodePrefix>| 8740 (17.18%)| 3513 (17.27%)|
| Total related entities |50857|20343

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-Gold/Input/451_1fold/1/)|25428|20343|5086|

### [Output](./Experiments/EntityAlignment/Gold-Gold/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | CustomerIdOrder (#/%) | CustomerAccount (#/%) | ZipCodePrefix (#/%) | City (#/%) | State (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/AlignE/1/nohup_gold-gold_aligne.txt)|71.69|86.29 |88.40 |151|0.78|45471|5619 (70.11%)|5069 (64.14%)|3083 (87.76%)|800 (88.89%)|12 (100%)
|AliNet|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/AliNet/1/nohup_gold-gold_alinet.txt)|85.27|95.33|96.10|14|0.90|166191|-|-|-|-|-
|AttrE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/AttrE/1/nohup_gold-gold_attre.txt)|96.23|99.01|99.54|1|0.97|59878|7731 (96.46%)|7580 (95.91%)|3382 (96.27%)|871 (96.78%)|12 (100%)
|BootEA|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA/1/nohup_gold-gold_bootea.txt)|85.46|95.05|96.33 |54|0.90|104864|6709 (83.71%)|6586 (83.34%)|3233 (92.03%)|845 (93.89%)|12 (100%)
|BootEA_RotatE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA_RotatE/1/nohup_gold-gold_bootea_rotate.txt)|81.33|95.66|96.95 |10|0.88|146977|-|-|-|-|-
|BootEA_TransH|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA_TransH/1/error_output_gold-gold_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/ConvE/1/error_output_gold-gold_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/GCN_Align/1/nohup_gold-gold_gcnalign.txt)|79.97|90.28 |91.39|124|0.85|15364|-|-|-|-|-
|GMNN|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/GMNN/1/error_output_gold-gold_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/HolE/1/nohup_gold-gold_hole.txt)|63.89|73.10|75.70|489|0.68|179720|-|-|-|-|-
|IMUSE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/IMUSE/1/nohup_gold-gold_imuse.txt)|95.07|98.85|99.10|2|0.97|11628|-|-|-|-|-
|IPTransE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/IPTransE/1/error_output_gold-gold_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/JAPE/1/nohup_gold-gold_jape.txt)|66.27|75.95|77.88|523|0.70|19948|-|-|-|-|-
|KDCoE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/KDCoE/1/error_output_gold-gold_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/MTransE/1/nohup_gold-gold_mtranse.txt)|61.34|68.10|69.75|695|0.64|17384|-|-|-|-|-
|MultiKE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/MultiKE/1/error_output_gold-gold_multike.txt)|E|r|r|o|r|||
|ProjE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/ProjE/1/nohup_gold-gold_proje.txt)|31.14|43.10|45.98|1881|0.36|86923|-|-|-|-|-
|RDGCN|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/RDGCN/1/error_output_gold-gold_rdgcn.txt)|E|r|r|o|r|||
|RotatE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/RotatE/1/nohup_gold-gold_rotate.txt)|73.81|93.71|95.80|25|0.82|46838|-|-|-|-|-
|RSN4EA|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/RSN4EA/1/nohup_gold-gold_rsn4ea.txt)|70.77|80.38|82.05|535|0.75|155310|-|-|-|-|-
|SEA|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/SEA/1/nohup_gold-gold_sea.txt)|74.49|92.25|94.07|59|0.82|18675|5650 (70.49%)|5571 (70.49%)|3112 (88.59%)|808 (89.78%)|12 (100%)
|SimplE|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/SimplE/1/nohup_gold-gold_simple.txt)|63.56|80.31|83.12|247|0.71|11721|-|-|-|-|-
|TransD|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/TransD/1/nohup_gold-gold_transd.txt)|60.58|65.66|66.73|727|0.63|18137|-|-|-|-|-
|TransH|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/TransH/1/nohup_gold-gold_transh.txt)|69.11|80.34|82.36|303|0.74|43002|-|-|-|-|-
|TransR|1|[20343](./Experiments/EntityAlignment/Gold-Gold/Output/TransR/1/nohup_gold-gold_transr.txt)|0.07|0.28|0.41|6546|0.00|15842|-|-|-|-|-

## [Basic - Basic](./Experiments/EntityAlignment/Basic-Basic/)

![Graph Basic](./Figures/BrazilianEcommerce-Basic.png "Graph Basic")

### [Input](./Experiments/EntityAlignment/Basic-Basic/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Basic-Basic/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerOrder> <https://vocab.um.es/ontology/bre/CustomerOrder>| 20000 (100%)|8000 (100%)
| Total related entities |20000|8000

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Basic-Basic/Input/451_1fold/1/)|10000|8000|2000|

### [Output](./Experiments/EntityAlignment/Basic-Basic/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | CustomerIdOrder (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/AlignE/1/nohup_basic-basic_aligne.txt)|0.04|0.09 |0.11 |4001|0.00|2186|3 (0.04%)|
|AliNet|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/AliNet/1/error_output_basic-basic_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/AttrE/1/nohup_basic-basic_attre.txt)|99.55|99.99|99.99|1|1.00|4950|7964 (99.55)|
|BootEA|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/BootEA/1/nohup_basic-basic_bootea.txt)|0.04|0.06 |0.13 |4017|0.00|3780|3 (0.04%)|
|BootEA_RotatE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/BootEA_RotatE/1/nohup_basic-basic_bootea_rotate.txt)|0.01|0.08|0.14 |4003|0.00|6949|-|
|BootEA_TransH|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/BootEA_TransH/1/error_output_basic-basic_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/ConvE/1/error_output_basic-basic_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/GCN_Align/1/nohup_basic-basic_gcnalign.txt)|0.00|0.04 |0.06|3994|0.00|300|-|
|GMNN|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/GMNN/1/nohup_basic-basic_gmnn.txt)|100|100 |100|1|1.00|69502|-|
|HolE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/HolE/1/nohup_basic-basic_hole.txt)|0.04|0.09 |0.15|3989|0.00|1852|-|
|IMUSE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/IMUSE/1/nohup_basic-basic_imuse.txt)|49.01|49.03|49.04|2075|0.49|1076|-|
|IPTransE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/IPTransE/1/error_output_basic-basic_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/JAPE/1/nohup_basic-basic_jape.txt)|0.03|0.05 |0.11|4010|0.00|871|-|
|KDCoE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/KDCoE/1/error_output_basic-basic_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/MTransE/1/nohup_basic-basic_mtranse.txt)|0.01|0.06 |0.11|4007|0.00|305|-|
|MultiKE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/MultiKE/1/error_output_basic-basic_multike.txt)|E|r|r|o|r|||
|ProjE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/ProjE/1/nohup_basic-basic_proje.txt)|0.01|0.04 |0.09|4023|0.00|1525|-|
|RDGCN|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/RDGCN/1/nohup_basic-basic_rdgcn.txt)|55.36|55.41|55.48|799|0.55|9609|-|
|RotatE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/RotatE/1/nohup_basic-basic_rotate.txt)|0.00|0.04 |0.14|3993|0.00|2249|-|
|RSN4EA|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/RSN4EA/1/error_output_basic-basic_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/SEA/1/nohup_basic-basic_sea.txt)|0.03|0.05|0.15|3967|0.00|156|2 (0.03%)|
|SimplE|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/SimplE/1/nohup_basic-basic_simple.txt)|0.00|0.05|0.13|4007|0.00|188|-|
|TransD|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/TransD/1/nohup_basic-basic_transd.txt)|0.00|0.06|0.10|3975|0.00|319|-|
|TransH|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/TransH/1/nohup_basic-basic_transh.txt)|0.00|0.04|0.06|3923|0.00|289|-|
|TransR|1|[8000](./Experiments/EntityAlignment/Basic-Basic/Output/TransR/1/nohup_basic-basic_transr.txt)|0.00|0.03|0.11|4035|0.00|790|-|

## [LLM - LLM](./Experiments/EntityAlignment/LLM-LLM/)

![Graph LLM](./Figures/BrazilianEcommerce-LLM.png "Graph LLM")

### [Input](./Experiments/EntityAlignment/LLM-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/LLM-LLM/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es#Customer> <https://vocab.um.es#Customer>| 20000 (64.49%)|8021 (64.66%)
|<https://vocab.um.es#ZipCodePrefix> <https://vocab.um.es#ZipCodePrefix>| 8740 (28.18%)| 3502 (28.23%)
|<https://vocab.um.es#City> <https://vocab.um.es#City>| 2247 (7.24%)| 871 (7.02%)
|<https://vocab.um.es#State> <https://vocab.um.es#State>| 27 (0.09%)| 11 (0.09%)
| Total related entities |31014|12405

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/LLM-LLM/Input/451_1fold/1/)|15507|12405|3102|

### [Output](./Experiments/EntityAlignment/LLM-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | Customer (#/%) | ZipCodePrefix (#/%) | City (#/%)|State (#/%)
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/AlignE/1/nohup_llm-llm_aligne.txt)|60.55|83.20|86.77|130|0.71|13869|4125 (51.43%)|2614 (74.64%)|761 (87.37%)|11 (100%)
|AliNet|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/AliNet/1/nohup_llm-llm_alinet.txt)|62.96|86.17|88.48|196|0.73|23199|-|-|-|-|
|AttrE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/AttrE/1/nohup_llm-llm_attre.txt)|87.55|92.79|94.41|8|0.90|11215|7257 (90.48%)|2832 (80.87%)|760 (87.26%)|11 (100%)
|BootEA|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/BootEA/1/nohup_llm-llm_bootea.txt)|62.33|85.74|89.20|104|0.73|16214|4249 (52.97%)|2703 (77.18%)|769 (88.29%)|11 (100%)
|BootEA_RotatE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/BootEA_RotatE/1/nohup_llm-llm_bootea_rotate.txt)|62.28|87.35|90.79|22|0.73|35216|-|-|-|-|
|BootEA_TransH|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/BootEA_TransH/1/error_output_llm-llm_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/ConvE/1/error_output_llm-llm_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/GCN_Align/1/nohup_llm-llm_gcnalign.txt)|60.94|82.90|84.96|105|0.70|588|-|-|-|-|
|GMNN|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/GMNN/1/error_output_llm-llm_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/HolE/1/nohup_llm-llm_hole.txt)|48.26|66.72|70.65|387|0.57|12489|-|-|-|-|
|IMUSE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/IMUSE/1/nohup_llm-llm_imuse.txt)|99.61|99.96|99.98|1|1.00|948|-|-|-|-|
|IPTransE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/IPTransE/1/error_output_llm-llm_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/JAPE/1/error_output_llm-llm_jape.txt)|E|r|r|o|r|||
|KDCoE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/KDCoE/1/error_output_llm-llm_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/MTransE/1/nohup_llm-llm_mtranse.txt)|48.59|65.19|67.22|750|0.56|770|-|-|-|-|
|MultiKE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/MultiKE/1/error_output_llm-llm_multike.txt)|E|r|r|o|r|||
|ProjE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/ProjE/1/nohup_llm-llm_proje.txt)|23.33|23.52|23.77|3623|0.24|2721|-|-|-|-|
|RDGCN|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/RDGCN/1/nohup_llm-llm_rdgcn.txt)|27.27|31.67|33.94|2389|0.30|16257|-|-|-|-|
|RotatE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/RotatE/1/nohup_llm-llm_rotate.txt)|60.20|84.51|88.88|30|0.71|4564|-|-|-|-|
|RSN4EA|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/RSN4EA/1/nohup_llm-llm_rsn4ea.txt)|59.86|82.60|85.01|282|0.70|18706|-|-|-|-|
|SEA|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/SEA/1/nohup_llm-llm_sea.txt)|60.86|84.20|88.26|61|0.71|2961|4192 (52.26%)|2592 (74.01%)|755 (86.68%)|11 (100%)
|SimplE|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/SimplE/1/nohup_llm-llm_simple.txt)|53.97|76.03|78.57|119|0.64|1949|-|-|-|-|
|TransD|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/TransD/1/nohup_llm-llm_transd.txt)|48.26|63.64|66.73|574|0.55|4989|-|-|-|-|
|TransH|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/TransH/1/nohup_llm-llm_transh.txt)|58.14|78.89|81.36|292|0.67|6148|-|-|-|-|
|TransR|1|[12405](./Experiments/EntityAlignment/LLM-LLM/Output/TransR/1/nohup_llm-llm_transr.txt)|0.11|0.28|0.56|4223|0.00|3887|-|-|-|-|

## [Transactions - Transactions](./Experiments/EntityAlignment/Transactions-Transactions/)

![Graph Transactions](./Figures/BrazilianEcommerce-Transactions.png "Graph Transactions")

### [Input](./Experiments/EntityAlignment/Transactions-Transactions/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Transactions-Transactions/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://purl.org/ontologies/BPA/CustomerAccount> <https://purl.org/ontologies/BPA/CustomerAccount>| 19843 (100%)|7937 (100%)
| Total related entities |19843|7937

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Transactions-Transactions/Input/451_1fold/1/)|9921|7937|1985|

### [Output](./Experiments/EntityAlignment/Transactions-Transactions/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time |CustomerAccount (#/%)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/AlignE/1/nohup_transactions-transactions_aligne.txt)|0.01|0.09|0.16|3985|0.00|1890|1 (0.01%)|
|AliNet|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/AliNet/1/error_output_transactions-transactions_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/AttrE/1/nohup_transactions-transactions_attre.txt)|14.57|39.75|55.44|22|0.27|5339|1156 (14.57%)|
|BootEA|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/BootEA/1/nohup_transactions-transactions_bootea.txt)|0.01|0.06|0.11|3950|0.00|2704|1 (0.01%)|
|BootEA_RotatE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/BootEA_RotatE/1/nohup_transactions-transactions_bootea_rotate.txt)|0.01|0.06|0.14|3973|0.00|6975|-|
|BootEA_TransH|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/BootEA_TransH/1/)|E|r|r|o|r|||
|Conve|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/ConvE/1/error_output_transactions-transactions_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/GCN_Align/1/nohup_transactions-transactions_gcnalign.txt)|0.01|0.04|0.13|3987|0.0|90|-|
|GMNN|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/GMNN/1/nohup_transactions-transactions_gmnn.txt)|100|100|100|1|1.00|23309|-|
|HolE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/HolE/1/nohup_transactions-transactions_hole.txt)|0.01|0.10|0.16|3987|0.00|1320|-|
|IMUSE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/IMUSE/1/nohup_transactions-transactions_imuse.txt)|100|100|100|1|1.00|224|-|
|IPTransE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/IPTransE/1/error_output_transactions-transactions_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/JAPE/1/error_output_transactions-transactions_jape.txt)|E|r|r|o|r|||
|KDCoE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/KDCoE/1/error_output_transactions-transactions_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/MTransE/1/nohup_transactions-transactions_mtranse.txt)|0.03|0.05|0.13|3944|0.00|170|-|
|MultiKE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/MultiKE/1/error_output_transactions-transactions_multike.txt)|E|r|r|o|r|||
|ProjE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/ProjE/1/nohup_transactions-transactions_proje.txt)|0.01|0.05|0.05|3950|0.00|1440|-|
|RDGCN|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/RDGCN/1/nohup_transactions-transactions_rdgcn.txt)|0.66|0.71|0.77|3918|0.01|6612|-|
|RotatE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/RotatE/1/nohup_transactions-transactions_rotate.txt)|0.00|0.03|0.04|3967|0.00|1705|-|
|RSN4EA|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/RSN4EA/1/error_output_transactions-transactions_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/SEA/1/nohup_transactions-transactions_sea.txt)|0.00|0.13|0.19|3944|0.00|179|0 (0.0%)|
|SimplE|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/SimplE/1/nohup_transactions-transactions_simple.txt)|0.00|0.05|0.09|3971|0.00|122|-|
|TransD|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/TransD/1/nohup_transactions-transactions_transd.txt)|0.00|0.10|0.19|3982|0.00|276|-|
|TransH|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/TransH/1/nohup_transactions-transactions_transh.txt)|0.00|0.13|0.20|3994|0.00|244|-|
|TransR|1|[7937](./Experiments/EntityAlignment/Transactions-Transactions/Output/TransR/1/nohup_transactions-transactions_transr.txt)|0.01|0.05|0.08|3978|0.00|747|-|

## [Gold - Basic](./Experiments/EntityAlignment/Gold-Basic/)

![Graph Gold-Basic](./Figures/BrazilianEcommerce-Gold-Basic.png "Graph Gold-Basic")

### [Input](./Experiments/EntityAlignment/Gold-Basic/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Basic/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerIdOrder> <https://vocab.um.es/ontology/bre/CustomerOrder>| 20000 (100%)|8000 (100%)
| Total related entities |20000|8000

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-Basic/Input/451_1fold/1/)|10000|8000|2000|

### [Output](./Experiments/EntityAlignment/Gold-Basic/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | CustomerIdOrder (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AlignE/1/nohup_gold-basic_aligne.txt)|0.01|0.05|0.11|4007|0.00|9023|0 (0.0%)|
|AliNet|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AliNet/1/error_output_gold-basic_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AttrE/1/nohup_gold-basic_attre.txt)|82.84|97.88|99.15|1|0.89|20589|0 (1.60)|
|BootEA|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA/1/nohup_gold-basic_bootea.txt)|0.03|0.13 |0.21 |3947|0.00|9179|0 (0.0%)|
|BootEA_RotatE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_RotatE/1/nohup_gold-basic_bootea_rotate.txt)|0.00|0.05|0.10 |3993|0.00|21939|-|
|BootEA_TransH|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_TransH/1/error_output_gold-basic_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/ConvE/1/error_output_gold-basic_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/GCN_Align/1/nohup_gold-basic_gcnalign.txt)|0.01|0.06|0.10|3993|0.00|1051|-|
|GMNN|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/GMNN/1/error_output_gold-basic_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/HolE/1/nohup_gold-basic_hole.txt)|0.03|0.06 |0.18|1631|0.00|3975|0 (0.0%)|
|IMUSE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/IMUSE/1/nohup_gold-basic_imuse.txt)|50.26|57.14 |59.52|466|0.54|609|0 (0.0%)|
|IPTransE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/IPTransE/1/error_output_gold-basic_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/JAPE/1/nohup_gold-basic_jape.txt)|0.03|0.12 |0.24|1646|0.00|1057|0 (0.0%)|
|KDCoE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/KDCoE/1/error_output_gold-basic_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/MTransE/1/nohup_gold-basic_mtranse.txt)|0.03|0.34 |0.43|1642|0.00|471|0 (0.0%)|
|MultiKE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/MultiKE/1/error_output_gold-basic_multike.txt)|E|r|r|o|r|||
|ProjE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/ProjE/1/nohup_gold-basic_proje.txt)|0.00|0.09 |0.27|1637|0.00|3045|0 (0.0%)|
|RDGCN|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RDGCN/1/nohup_gold-basic_rdgcn.txt)|100|100 |100|1|1.00|4100|0 (0.0%)|
|RotatE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RotatE/1/nohup_gold-basic_rotate.txt)|0.00|0.12 |0.21|1615|0.00|1227|0 (0.0%)|
|RSN4EA|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RSN4EA/1/error_output_gold-basic_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/SEA/1/nohup_gold-basic_sea.txt)|0.12|0.27 |0.37|1641|0.00|218|0 (0.0%)|
|SimplE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/SimplE/1/nohup_gold-basic_simple.txt)|0.12|0.21|0.31|1646|0.00|199|0 (0.0%)|
|TransD|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransD/1/nohup_gold-basic_transd.txt)|0.06|0.27|0.61|1597|0.00|552|0 (0.0%)|
|TransH|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransH/1/nohup_gold-basic_transh.txt)|0.09|0.18|0.31|1612|0.00|488|0 (0.0%)|
|TransR|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransR/1/nohup_gold-basic_transr.txt)|0.12|0.21|0.31|1639|0.00|1899|0 (0.0%)|

## [Gold - LLM](./Experiments/EntityAlignment/Gold-LLM/)

![Graph Gold-LLM](./Figures/bigBasketProducts-Gold-LLM.png "Graph Gold-LLM")

### [Input](./Experiments/EntityAlignment/Gold-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-LLM/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bbp/SalesArticle> - <https://vocab.um.es/sales_product/>| 8208 (50.18%)|3282 (50.17%)
|<https://vocab.um.es/ontology/bbp/SalesSpecification> - <http://schema.org/Offer/>| 8148 (49.82%)|3260 (49.83%)
| Total related entities |16356|6542

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-LLM/Input/451_1fold/1/)|8178|6542|1636|

### [Output](./Experiments/EntityAlignment/Gold-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | SalesArticle (#/%) |SalesSpecification (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/AlignE/1/nohup_gold-llm_aligne.txt)|38.96|57.63 |60.07 |1045|0.47|5252|0 (0.0%)|
|AliNet|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/AliNet/1/nohup_gold-llm_alinet.txt)|31.31|45.55|46.73|1412|0.37|2247||
|AttrE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/AttrE/1/nohup_gold-llm_attre.txt)|48.88|70.18|76.93|28|0.59|4867|6 (1.60)|
|BootEA|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA/1/nohup_gold-llm_bootea.txt)|39.94|57.93 |60.33 |1026|0.48|4895|0 (0.0%)|
|BootEA_RotatE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA_RotatE/1/nohup_gold-llm_bootea_rotate.txt)|36.46|57.87|60.59 |1496|0.46|8585|0 (0.0%)|
|BootEA_TransH|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA_TransH/1/error_output_gold-llm_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/ConvE/1/error_output_gold-llm_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/GCN_Align/1/nohup_gold-llm_gcnalign.txt)|24.21|40.31 |44.25|2170|0.31|771|0 (0.0%)|
|GMNN|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/GMNN/1/error_output_gold-llm_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/HolE/1/nohup_gold-llm_hole.txt)|22.64|39.03 |44.42|1337|0.30|13156|0 (0.0%)|
|IMUSE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/IMUSE/1/nohup_gold-llm_imuse.txt)|33.78|55.06 |59.46|818|0.43|1184|0 (0.0%)|
|IPTransE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/IPTransE/1/error_output_gold-llm_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/JAPE/1/nohup_gold-llm_jape.txt)|24.20|37.62 |41.49|1082|0.30|1182|0 (0.0%)|
|KDCoE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/KDCoE/1/error_output_gold-llm_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/MTransE/1/nohup_gold-llm_mtranse.txt)|23.53|33.57 |36.76|609|0.28|802|0 (0.0%)|
|MultiKE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/MultiKE/1/error_output_gold-llm_multike.txt)|E|r|r|o|r|||
|ProjE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/ProjE/1/nohup_gold-llm_proje.txt)|21.92|30.14 |30.85|2747|0.26|4979|0 (0.0%)|
|RDGCN|1|[6542](./Experiments/EntityAlignment//Gold-LLM/Output/RDGCN/1/nohup_gold-llm_rdgcn.txt)|14.34|20.99 |23.39|1898|0.18|14291|0 (0.0%)|
|RotatE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/RotatE/1/nohup_gold-llm_rotate.txt)|30.66|53.30 |58.19|1969|0.40|5016|0 (0.0%)|
|RSN4EA|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/RSN4EA/1/error_output_gold-llm_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/SEA/1/nohup_gold-llm_sea.txt)|35.60|54.66 |58.67|1166|0.44|921|0 (0.0%)|
|SimplE|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/SimplE/1/nohup_gold-llm_simple.txt)|19.66|36.52|41.35|1299|0.27|982|0 (0.0%)|
|TransD|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/TransD/1/nohup_gold-llm_transd.txt)|33.23|48.88|51.73|1360|0.40|2184|0 (0.0%)|
|TransH|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/TransH/1/nohup_gold-llm_transh.txt)|33.02|50.44|53.63|1078|0.41|2262|0 (0.0%)|
|TransR|1|[6542](./Experiments/EntityAlignment/Gold-LLM/Output/TransR/1/nohup_gold-llm_transr.txt)|0.18|0.70|1.10|2454|0.01|2231|0 (0.0%)|

## [Gold - Materials](./Experiments/EntityAlignment/Gold-Materials/)

![Graph Gold-Materials](./Figures/bigBasketProducts-Gold-Materials.png "Graph Gold-Materials")

### [Input](./Experiments/EntityAlignment/Gold-Materials/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Materials/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bbp/SalesArticle> - <https://purl.org/ontologies/MT/SalesArticle>| 8208 (54.54%)|3276 (54.42%)
|<https://vocab.um.es/ontology/bbp/Product> - <https://purl.org/ontologies/MT/sales_product>| 6842 (45.46%)|2744 (45.58%)
| Total related entities |15050|6020

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-Materials/Input/451_1fold/1/)|7525|6020|1505|

### [Output](./Experiments/EntityAlignment/Gold-Materials/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | SalesArticle (#/%) |Product (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/AlignE/1/nohup_gold-materials_aligne.txt)|53.31|56.66 |57.03 |573|0.55|5237|0 (0.0%)|
|AliNet|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/AliNet/1/nohup_gold-materials_alinet.txt)|53.92|57.06|57.28|445|0.56|5172||
|AttrE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/AttrE/1/nohup_gold-materials_attre.txt)|52.82|59.02|62.03|287|0.56|2788|6 (1.60)|
|BootEA|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/BootEA/1/nohup_gold-materials_bootea.txt)|53.79|56.89 |57.03 |638|0.55|5297|0 (0.0%)|
|BootEA_RotatE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/BootEA_RotatE/1/nohup_gold-materials_bootea_rotate.txt)|53.69|56.94|57.03 |651|0.55|10599|0 (0.0%)|
|BootEA_TransH|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/BootEA_TransH/1/error_output_gold-materials_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/ConvE/1/error_output_gold-materials_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/GCN_Align/1/nohup_gold-materials_gcnalign.txt)|53.87|57.04|57.16|655|0.55|677|0 (0.0%)|
|GMNN|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/GMNN/1/nohup_gold-materials_gmnn.txt)|100|100|100|1|1.00|42545||
|HolE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/HolE/1/nohup_gold-materials_hole.txt)|51.55|55.43|55.83|984|0.53|18212|0 (0.0%)|
|IMUSE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/IMUSE/1/nohup_gold-materials_imuse.txt)|52.43|60.52 |60.98|659|0.56|1412|0 (0.0%)|
|IPTransE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/IPTransE/1/error_output_gold-materials_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/JAPE/1/nohup_gold-materials_jape.txt)|50.57|53.70 |54.14|901|0.52|1315|0 (0.0%)|
|KDCoE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/KDCoE/1/error_output_gold-materials_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/MTransE/1/nohup_gold-materials_mtranse.txt)|46.11|50.52 |51.41|846|0.48|1025|0 (0.0%)|
|MultiKE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/MultiKE/1/error_output_gold-materials_multike.txt)|E|r|r|o|r|||
|ProjE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/ProjE/1/nohup_gold-materials_proje.txt)|28.21|31.43 |31.65|1401|0.30|5533|0 (0.0%)|
|RDGCN|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/RDGCN/1/nohup_gold-materials_rdgcn.txt)|73.42|75.60 |77.11|101|0.75|8926|0 (0.0%)|
|RotatE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/RotatE/1/nohup_gold-materials_rotate.txt)|52.64|56.89 |56.99|745|0.55|7471|0 (0.0%)|
|RSN4EA|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/RSN4EA/1/nohup_gold-materials_rsn4ea.txt)|51.96|55.32|55.93|1306|0.54|7380||
|SEA|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/SEA/1/nohup_gold-materials_sea.txt)|53.49|56.78 |57.01|649|0.55|1036|0 (0.0%)|
|SimplE|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/SimplE/1/nohup_gold-materials_simple.txt)|49.49|56.10|56.53|817|0.53|2971|0 (0.0%)|
|TransD|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/TransD/1/nohup_gold-materials_transd.txt)|50.53|52.97|53.37|606|0.52|2536|0 (0.0%)|
|TransH|1|[6020](./Experiments/EntityAlignment//Gold-Materials/Output/TransH/1/nohup_gold-materials_transh.txt)|50.68|53.14|53.44|695|0.52|1677|0 (0.0%)|
|TransR|1|[6020](./Experiments/EntityAlignment/Gold-Materials/Output/TransR/1/nohup_gold-materials_transr.txt)|0.10|0.30|0.52|2311|0.00|2934|0 (0.0%)|


## [Basic - LLM](./Experiments/EntityAlignment/Basic-LLM/)

![Graph Basic-LLM](./Figures/bigBasketProducts-Basic-LLM.png "Graph Basic-LLM")

### [Input](./Experiments/EntityAlignment/Basic-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Basic-LLM/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bbp/SalesProduct> <https://vocab.um.es/sales_product/>| 8208 (100%)|3283 (100%)
| Total related entities |8208|3283

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Basic-LLM/Input/451_1fold/1/)|4104|3283|821|

### [Output](./Experiments/EntityAlignment/Basic-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | SalesProduct (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/AlignE/1/nohup_gold-basic_aligne.txt)|0.06|0.15 |0.27 |1665|0.00|2139|0 (0.0%)|
|AliNet|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/AliNet/1/error_output_gold-basic_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/AttrE/1/nohup_gold-basic_attre.txt)|86.05|99.30|99.97|1|0.92|5238|0 (1.60)|
|BootEA|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA/1/nohup_gold-basic_bootea.txt)|0.00|0.09 |0.18 |1638|0.00|2160|0 (0.0%)|
|BootEA_RotatE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_RotatE/1/nohup_gold-basic_bootea_rotate.txt)|0.03|0.18|0.37 |1653|0.00|5720|0 (0.0%)|
|BootEA_TransH|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_TransH/1/error_output_gold-basic_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/ConvE/1/error_output_gold-basic_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/GCN_Align/1/nohup_gold-basic_gcnalign.txt)|0.00|0.09 |0.21|1647|0.00|269|0 (0.0%)|
|GMNN|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/GMNN/1/nohup_gold-basic_gmnn.txt)|100|100 |100|1|1.00|19927|0 (0.0%)|
|HolE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/HolE/1/nohup_gold-basic_hole.txt)|0.03|0.06 |0.18|1631|0.00|3975|0 (0.0%)|
|IMUSE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/IMUSE/1/nohup_gold-basic_imuse.txt)|50.26|57.14 |59.52|466|0.54|609|0 (0.0%)|
|IPTransE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/IPTransE/1/error_output_gold-basic_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/JAPE/1/nohup_gold-basic_jape.txt)|0.03|0.12 |0.24|1646|0.00|1057|0 (0.0%)|
|KDCoE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/KDCoE/1/error_output_gold-basic_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/MTransE/1/nohup_gold-basic_mtranse.txt)|0.03|0.34 |0.43|1642|0.00|471|0 (0.0%)|
|MultiKE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/MultiKE/1/error_output_gold-basic_multike.txt)|E|r|r|o|r|||
|ProjE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/ProjE/1/nohup_gold-basic_proje.txt)|0.00|0.09 |0.27|1637|0.00|3045|0 (0.0%)|
|RDGCN|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RDGCN/1/nohup_gold-basic_rdgcn.txt)|100|100 |100|1|1.00|4100|0 (0.0%)|
|RotatE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RotatE/1/nohup_gold-basic_rotate.txt)|0.00|0.12 |0.21|1615|0.00|1227|0 (0.0%)|
|RSN4EA|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/RSN4EA/1/error_output_gold-basic_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/SEA/1/nohup_gold-basic_sea.txt)|0.12|0.27 |0.37|1641|0.00|218|0 (0.0%)|
|SimplE|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/SimplE/1/nohup_gold-basic_simple.txt)|0.12|0.21|0.31|1646|0.00|199|0 (0.0%)|
|TransD|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransD/1/nohup_gold-basic_transd.txt)|0.06|0.27|0.61|1597|0.00|552|0 (0.0%)|
|TransH|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransH/1/nohup_gold-basic_transh.txt)|0.09|0.18|0.31|1612|0.00|488|0 (0.0%)|
|TransR|1|[3283](./Experiments/EntityAlignment/Gold-Basic/Output/TransR/1/nohup_gold-basic_transr.txt)|0.12|0.21|0.31|1639|0.00|1899|0 (0.0%)|

## Metrics

|Alignment|Approach|Split|h@1 (%)|h@5 (%)|h@10 (%)|MR|MRR [0,1]|Run Time (s)|
|:------:|:------:|:---:|:-:|:-:|:--:|:-:|:-:|:-:|
|Gold-Basic|BootEA|1|0.0|1.60|2.67|188|0.02|759|
|Gold-Basic|AttrE|1|1.60|4.80|9.60|136|0.05|352|

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
