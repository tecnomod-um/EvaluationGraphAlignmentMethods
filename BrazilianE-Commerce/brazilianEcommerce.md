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
|[Basic](./Mappings/mappingBasic.csv.yml)|processed_olist_customers_dataset_20K.csv|[120000 triples](./Mappings/brazilianecommerceBasic.nt)|[100000 triples](./Experiments/EntityAlignment/Basic-Basic/Input/attr_triples_1)|[20000 triples](./Experiments/EntityAlignment/Basic-Basic/Input/rel_triples_1)|
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
|AlignE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AlignE/1/nohup_gold-basic_aligne.txt)|0.01|0.05|0.11|4007|0.00|9023|1 (0.01%)|
|AliNet|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AliNet/1/error_output_gold-basic_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/AttrE/1/nohup_gold-basic_attre.txt)|82.84|97.88|99.15|1|0.89|20589|6627 (82.84%)|
|BootEA|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA/1/nohup_gold-basic_bootea.txt)|0.03|0.13 |0.21 |3947|0.00|9179|2 (0.03%)|
|BootEA_RotatE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_RotatE/1/nohup_gold-basic_bootea_rotate.txt)|0.00|0.05|0.10 |3993|0.00|21939|-|
|BootEA_TransH|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_TransH/1/error_output_gold-basic_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/ConvE/1/error_output_gold-basic_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/GCN_Align/1/nohup_gold-basic_gcnalign.txt)|0.01|0.06|0.10|3993|0.00|1051|-|
|GMNN|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/GMNN/1/error_output_gold-basic_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/HolE/1/nohup_gold-basic_hole.txt)|0.00|0.06 |0.16|4017|0.00|12261|-|
|IMUSE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/IMUSE/1/nohup_gold-basic_imuse.txt)|95.86|96.65|96.90|185|0.96|2383|-|
|IPTransE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/IPTransE/1/error_output_gold-basic_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/JAPE/1/nohup_gold-basic_jape.txt)|0.01|0.09 |0.10|3956|0.00|2805|-|
|KDCoE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/KDCoE/1/error_output_gold-basic_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/MTransE/1/nohup_gold-basic_mtranse.txt)|0.03|0.06 |0.11|4004|0.00|1896|-|
|MultiKE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/MultiKE/1/error_output_gold-basic_multike.txt)|E|r|r|o|r|||
|ProjE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/ProjE/1/nohup_gold-basic_proje.txt)|0.00|0.04 |0.10|4026|0.00|12037|-|
|RDGCN|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/RDGCN/1/nohup_gold-basic_rdgcn.txt)|55.78|55.81|55.88|790|0.56|20120|-|
|RotatE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/RotatE/1/nohup_gold-basic_rotate.txt)|0.01|0.05 |0.10|4009|0.00|11038|-|
|RSN4EA|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/RSN4EA/1/error_output_gold-basic_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/SEA/1/nohup_gold-basic_sea.txt)|0.01|0.09|0.18|3982|0.00|679|1 (0.01%)|
|SimplE|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/SimplE/1/nohup_gold-basic_simple.txt)|0.01|0.08|0.16|3983|0.00|521|-|
|TransD|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/TransD/1/nohup_gold-basic_transd.txt)|0.03|0.08|0.15|4009|0.00|1761|-|
|TransH|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/TransH/1/nohup_gold-basic_transh.txt)|0.04|0.09|0.11|3978|0.00|1382|-|
|TransR|1|[8000](./Experiments/EntityAlignment/Gold-Basic/Output/TransR/1/nohup_gold-basic_transr.txt)|0.01|0.10|0.15|3969|0.00|4884|-|

## [Gold - LLM](./Experiments/EntityAlignment/Gold-LLM/)

![Graph Gold-LLM](./Figures/BrazilianEcommerce-Gold-LLM.png "Graph Gold-LLM")

### [Input](./Experiments/EntityAlignment/Gold-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-LLM/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerIdOrder> - <https://vocab.um.es#Customer>| 20000 (64.49%)|7991 (64.42%)
|<https://vocab.um.es/ontology/bre/ZipCodePrefix> - <https://vocab.um.es#ZipCodePrefix>| 8740 (28.18%)|3528 (28.44%)
|<https://vocab.um.es/ontology/bre/City> - <https://vocab.um.es#City>| 2247 (7.24%)|875 (7.05%)
|<https://vocab.um.es/ontology/bre/State> - <https://vocab.um.es#State>| 27 (0.09%)|11 (0.09%)
| Total related entities |31014|12405

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-LLM/Input/451_1fold/1/)|15507|12405|3102|

### [Output](./Experiments/EntityAlignment/Gold-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | CustomerIdOrder (#/%) |ZipCodePrefix (#/%) |City (#/%) |State (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/AlignE/1/nohup_gold-llm_aligne.txt)|61.00|83.86|87.06|152|0.71|20913|4091 (51.20%)|2708 (76.76%)|757 (86.51%)|11 (100%)
|AliNet|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/AliNet/1/nohup_gold-llm_alinet.txt)|62.61|85.26|87.36|279|0.72|24381|-|-|-|-|
|AttrE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/AttrE/1/nohup_gold-llm_attre.txt)|72.54|82.47|83.77|82|0.77|25731|5633 (70.49%)|2631 (74.57%)|723 (82.63%)|11 (100%)
|BootEA|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA/1/nohup_gold-llm_bootea.txt)|62.93|86.56|89.94|102|0.73|31157|4249 (53.17%)|2779 (78.77%)|768 (87.77%)|11 (100%)
|BootEA_RotatE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA_RotatE/1/nohup_gold-llm_bootea_rotate.txt)|62.48|87.05|90.62|24|0.73|37592|-|-|-|-|
|BootEA_TransH|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/BootEA_TransH/1/error_output_gold-llm_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/ConvE/1/error_output_gold-llm_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/GCN_Align/1/nohup_gold-llm_gcnalign.txt)|60.25|81.81|83.99|326|0.70|2570|-|-|-|-|
|GMNN|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/GMNN/1/error_output_gold-llm_gmnn.txt)|E|r|r|o|r|||
|HolE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/HolE/1/nohup_gold-llm_hole.txt)|40.70|59.28|63.52|572|0.49|41036|-|-|-|-|
|IMUSE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/IMUSE/1/error_output_gold-llm_imuse.txt)|E|r|r|o|r|||
|IPTransE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/IPTransE/1/error_output_gold-llm_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/JAPE/1/error_output_gold-llm_jape.txt)|E|r|r|o|r|||
|KDCoE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/KDCoE/1/error_output_gold-llm_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/MTransE/1/nohup_gold-llm_mtranse.txt)|47.57|62.92|64.94|821|0.54|4847|-|-|-|-|
|MultiKE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/MultiKE/1/error_output_gold-llm_multike.txt)|E|r|r|o|r|||
|ProjE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/ProjE/1/nohup_gold-llm_proje.txt)|0.24|1.02|1.87|4215|0.01|22175|-|-|-|-|
|RDGCN|1|[12405](./Experiments/EntityAlignment//Gold-LLM/Output/RDGCN/1/nohup_gold-llm_rdgcn.txt)|48.14|55.24|56.80|1223|0.51|42698|-|-|-|-|
|RotatE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/RotatE/1/nohup_gold-llm_rotate.txt)|61.15|85.75|89.63|34|0.72|20979|-|-|-|-|
|RSN4EA|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/RSN4EA/1/nohup_gold-llm_rsn4ea.txt)|59.65|82.35|85.18|240|0.70|41051|-|-|-|-|
|SEA|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/SEA/1/nohup_gold-llm_sea.txt)|61.17|84.41|88.29|88|0.71|6376|4164 (52.11%)|2669 (75.65%)|744 (85.03%)|11 (100%)
|SimplE|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/SimplE/1/nohup_gold-llm_simple.txt)|48.65|69.18|72.08|494|0.58|5598|-|-|-|-|
|TransD|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/TransD/1/nohup_gold-llm_transd.txt)|48.95|64.53|67.54|531|0.56|10902|-|-|-|-|
|TransH|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/TransH/1/nohup_gold-llm_transh.txt)|43.60|56.07|57.86|843|0.49|4975|-|-|-|-|
|TransR|1|[12405](./Experiments/EntityAlignment/Gold-LLM/Output/TransR/1/nohup_gold-llm_transr.txt)|0.07|0.32|0.62|4071|0.00|8490|-|-|-|-|

## [Gold - Transactions](./Experiments/EntityAlignment/Gold-Transactions/)

![Graph Gold-Transactions](./Figures/BrazilianEcommerce-Gold-Transactions.png "Graph Gold-Transactions")

### [Input](./Experiments/EntityAlignment/Gold-Transactions/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Transactions/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerAccount> - <https://purl.org/ontologies/BPA/CustomerAccount>| 19843 (100%)|7937 (100%)
| Total related entities |19843|7937

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-Transactions/Input/451_1fold/1/)|9921|7937|1985|


### [Output](./Experiments/EntityAlignment/Gold-Transactions/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time |CustomerAccount (#/%)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/AlignE/1/nohup_gold-transactions_aligne.txt)|0.00|0.08|0.09|3955|0.00|4833|0 (0.0%)|
|AliNet|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/AliNet/1/error_output_gold-transactions_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/AttrE/1/nohup_gold-transactions_attre.txt)|3.89|13.03|21.09|125|0.10|4965|309 (3.89)|
|BootEA|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/BootEA/1/nohup_gold-transactions_bootea.txt)|0.01|0.04|0.11|3981|0.00|5258|1 (0.01%)|
|BootEA_RotatE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/BootEA_RotatE/1/nohup_gold-transactions_bootea_rotate.txt)|0.00|0.04|0.10|3995|0.00|12665|-|
|BootEA_TransH|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/BootEA_TransH/1/)|E|r|r|o|r|||
|Conve|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/ConvE/1/error_output_gold-transactions_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/GCN_Align/1/nohup_gold-transactions_gcnalign.txt)|0.03|0.09|0.14|3983|0.00|374|-|
|GMNN|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/GMNN/1/nohup_gold-transactions_gmnn.txt)|100|100|100|1|1.00|36384|-|
|HolE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/HolE/1/nohup_gold-transactions_hole.txt)|0.01|0.03|0.08|3935|0.00|4755|-|
|IMUSE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/IMUSE/1/nohup_gold-transactions_imuse.txt)|100|100|100|1|1.00|684|-|
|IPTransE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/IPTransE/1/error_output_gold-transactions_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/JAPE/1/error_output_gold-transactions_jape.txt)|E|r|r|o|r|||
|KDCoE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/KDCoE/1/error_output_gold-transactions_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/MTransE/1/nohup_gold-transactions_mtranse.txt)|0.03|0.06|0.18|4002|0.00|882|-|
|MultiKE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/MultiKE/1/error_output_gold-transactions_multike.txt)|E|r|r|o|r|||
|ProjE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/ProjE/1/nohup_gold-transactions_proje.txt)|0.05|0.10|0.16|3971|0.00|5720|-|
|RDGCN|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/RDGCN/1/nohup_gold-transactions_rdgcn.txt)|0.69|0.76|0.84|3961|0.01|13089|-|
|RotatE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/RotatE/1/nohup_gold-transactions_rotate.txt)|0.01|0.10|0.19|3973|0.00|5468|-|
|RSN4EA|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/RSN4EA/1/error_output_gold-transactions_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/SEA/1/nohup_gold-transactions_sea.txt)|0.00|0.03|0.10|3936|0.00|498|0 (0.00%)|
|SimplE|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/SimplE/1/nohup_gold-transactions_simple.txt)|0.01|0.04|0.06|3976|0.00|370|-|
|TransD|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/TransD/1/nohup_gold-transactions_transd.txt)|0.01|0.06|0.11|3990|0.00|1058|-|
|TransH|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/TransD/1/nohup_gold-transactions_transd.txt)|0.01|0.10|0.18|3953|0.00|925|-|
|TransR|1|[7937](./Experiments/EntityAlignment/Gold-Transactions/Output/TransR/1/nohup_gold-transactions_transr.txt)|0.03|0.08|0.11|3987|0.00|3285|-|


## [Basic - LLM](./Experiments/EntityAlignment/Basic-LLM/)

![Graph Basic-LLM](./Figures/BrazilianEcommerce-Basic-LLM.png "Graph Basic-LLM")

### [Input](./Experiments/EntityAlignment/Basic-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Basic-LLM/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bre/CustomerOrder> <https://vocab.um.es#Customer>| 20000 (100%)|8000 (100%)
| Total related entities |20000|8000

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Basic-LLM/Input/451_1fold/1/)|10000|8000|2000|

### [Output](./Experiments/EntityAlignment/Basic-LLM/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | CustomerOrder (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/AlignE/1/nohup_basic-llm_aligne.txt)|0.00|0.06|0.11|3950|0.00|3438|0 (0.00%)|
|AliNet|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/AliNet/1/error_output_basic-llm_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/AttrE/1/nohup_basic-llm_attre.txt)|14.91|32.96|43.11|96|0.24|6869|1193 (14.91%)|
|BootEA|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/BootEA/1/nohup_basic-llm_bootea.txt)|0.01|0.05|0.09|4048|0.00|3521|1 (0.01%)|
|BootEA_RotatE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/BootEA_RotatE/1/nohup_basic-llm_bootea_rotate.txt)|0.00|0.09|0.15|3989|0.00|8743|-|
|BootEA_TransH|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/BootEA_TransH/1/error_output_basic-llm_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/ConvE/1/error_output_basic-llm_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/GCN_Align/1/nohup_basic-llm_gcnalign.txt)|0.00|0.11|0.19|4012|0.00|126|-|
|GMNN|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/GMNN/1/nohup_basic-llm_gmnn.txt)|100|100 |100|1|1.00|45951|-|
|HolE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/HolE/1/nohup_basic-llm_hole.txt)|0.01|0.08|0.18|3986|0.00|2762|-|
|IMUSE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/IMUSE/1/error_output_basic-llm_imuse.txt)|E|r|r|o|r|||
|IPTransE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/IPTransE/1/error_output_basic-llm_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/JAPE/1/error_output_basic-llm_jape.txt)|E|r|r|o|r|||
|KDCoE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/KDCoE/1/error_output_basic-llm_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/MTransE/1/nohup_basic-llm_mtranse.txt)|0.00|0.06|0.09|3969|0.00|366|-|
|MultiKE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/MultiKE/1/error_output_basic-llm_multike.txt)|E|r|r|o|r|||
|ProjE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/ProjE/1/nohup_basic-llm_proje.txt)|0.03|0.09|0.15|4028|0.00|2001|-|
|RDGCN|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/RDGCN/1/nohup_basic-llm_rdgcn.txt)|56.04|56.06|56.16|774|0.56|6698|-|
|RotatE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/RotatE/1/nohup_basic-llm_rotate.txt)|0.01|0.06|0.14|3990|0.00|2647|-|
|RSN4EA|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/RSN4EA/1/error_output_basic-llm_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/SEA/1/nohup_basic-llm_sea.txt)|0.04|0.15|0.19|3975|0.00|541|3 (0.04%)|
|SimplE|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/SimplE/1/nohup_basic-llm_simple.txt)|0.00|0.05|0.14|4005|0.00|346|-|
|TransD|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/TransD/1/nohup_basic-llm_transd.txt)|0.01|0.06|0.15|4001|0.00|845|-|
|TransH|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/TransH/1/nohup_basic-llm_transh.txt)|0.04|0.06|0.13|3946|0.00|704|-|
|TransR|1|[8000](./Experiments/EntityAlignment/Basic-LLM/Output/TransR/1/nohup_basic-llm_transr.txt)|0.01|0.06|0.08|4036|0.00|2282|-|

## Results

![Modules Boxplot Brazilian E-Commerce](./Figures/boxplotApproaches.png "Modules Boxplot Brazilian E-Commerce")

![Modules Clusters Brazilian E-Commerce](./Figures/clusterApproaches.png "Modules Clusters Brazilian E-Commerce")

![Datasets Boxplot Brazilian E-Commerce](./Figures/boxplotDatasetsPairs.png "Datasets Boxplot Brazilian E-Commerce")

![Datasets Clusters Brazilian E-Commerce](./Figures/clusterDataset.png "Datasets Clusters Brazilian E-Commerce")

![Datasets Cluster AttrE-BootEA Brazilian E-Commerce](./Figures/clusterDatasetAttBoot.png "Datasets Cluster AttrE-BootEA Brazilian E-Commerce")

![BarChart Comparisons Modules Brazilian E-Commerce](./Figures/barComparison.png "BarChart Comparisons Modules Brazilian E-Commerce")

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
