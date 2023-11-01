# BigBasket Products

* URL: <https://www.kaggle.com/datasets/chinmayshanbhag/big-basket-products>
* Format: CSV
* Description: Dataset containing the products listed on the website of online grocery store Big Basket.

## Datasets

* [data.csv](./SourceFiles/data.csv)
  * 8208 rows x 9 columns
* [processed_data20K.csv](./SourceFiles/processed_data.csv)
  * 8208 rows x 19 columns
  * Processing of identifiers for five classes
![Counts processed_data.csv](./Figures/counts_data.JPG "Counts processed_data.csv")

* No field has null values
* "Absolute_Url" is the only field that has all unique values

![Fields cardinality data20K.csv](./Figures/counts_data.JPG "Fields cardinality data20K.csv")

* (0,0) No relationship between values in the row and column fields
* (0,1) One value in the row field is related to at most one value in the column field
* (0,2) One value in the row field can be related to none, one or several values in the column field
* (1,1) One value in the row filed is only related to one value in the column field
* (1,2) One value in the row field can be related to one or several values in the column field
* Inconsistencies:

## Ontologies

* [Basic](./Ontologies/eCommerceOntology.owl)
* [LLM](./Ontologies/eCommerceOntologyLLM.owl)
* [Gold standard](./Ontologies/eCommerceOntologyII.owl)
* [Materials](./Ontology/materials_anony_v2.owl)

## Mapping

|Mapping |Dataset| RDF | attr_triples | rel_triples |
|:-:|:-:|:-:|:-:|:-:|
|[Basic](./Mappings/mappingBasic.csv.yml)|processed_data.csv|[82080 triples](./Mappings/bigbasketproductsBasic.nt)|[73872 triples](./Experiments/EntityAlignment/Basic-Basic/Input/attr_triples_1)|[8208 triples](./Experiments/EntityAlignment/Basic-Basic/Input/rel_triples_1)|
|[Gold](./Mappings/mappingGold.csv.yml)|processed_data.csv|[92422 triples](./Mappings/bigbasketproductsGold.nt)|[47597 triples](./Experiments/EntityAlignment/Gold-Gold/Input/attr_triples_1)|[44825 triples](./Experiments/EntityAlignment/Gold-Gold/Input/rel_triples_1)|
|[LLM](./Mappings/mappingLLM.csv.ttl)|processed_data20K.csv|[69428 triples](./Mappings/bigbasketproductsLLM.nt)|[61288 triples](./Experiments/EntityAlignment/LLM-LLM/Input/attr_triples_1)|[8140 triples](./Experiments/EntityAlignment/LLM-LLM/Input/rel_triples_1)|
|[Materials](./Mappings/mappingMaterials.csv.yml)|processed_data20K.csv|[45150 triples](./Mappings/bigbasketproductsMaterials.nt)|[21892 triples](./Experiments/EntityAlignment/Materials-Materials/Input/attr_triples_1)|[23258 triples](./Experiments/EntityAlignment/Materials-Materials/Input/rel_triples_1)|

[Gold](./Mappings/mappingGold.csv.yml) - processed_data.csv
|Property |Number|
|:-:|:-:|
|<https://vocab.um.es/ontology/bbp/image>|8208|
|<https://vocab.um.es/ontology/bbp/url>|8208|
|<https://vocab.um.es/ontology/bbp/productQuantity>|8208|
|<https://vocab.um.es/ontology/bbp/productName>|6842|
|<https://vocab.um.es/ontology/bbp/brandName>|6842|
|<https://vocab.um.es/ontology/bbp/priceArticle>|4472|
|<https://vocab.um.es/ontology/bbp/discount_price>|4472|
|<https://vocab.um.es/ontology/bbp/subCategoryName>|334|
|<https://vocab.um.es/ontology/bbp/categoryName>|11|
|**Total Attr_Triples**|47597|
|<https://vocab.um.es/ontology/bbp/belongsToSubCategory>|8208|
|<https://vocab.um.es/ontology/bbp/hasProduct>|8208|
|<https://vocab.um.es/ontology/bbp/hasSalesSpecification>|8208|
|<http://www.w3.org/2000/01/rdf-schema#subClassOf>|334|
|<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>|19867|
|**Total Rel_Triples**|44825|
|**Total Graph Gold**|92422|

## [Gold - Gold](./Experiments/EntityAlignment/Gold-Gold/)

![Graph Gold](./Figures/bigBasketProducts-Gold.png "Graph Gold")

### [Input](./Experiments/EntityAlignment/Gold-Gold/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Gold/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/bbp/SalesArticle> <https://vocab.um.es/ontology/bbp/SalesArticle>| 8208 (41.31%)|3311 (41.66%)
|<https://vocab.um.es/ontology/bbp/Product> <https://vocab.um.es/ontology/bbp/Product>|6842 (34.44%)| 2703 (34.01%)|
|<https://vocab.um.es/ontology/bbp/Category> <https://vocab.um.es/ontology/bbp/Category>| 11 (0.06%)| 3 (0.04%)|
|<https://vocab.um.es/ontology/bbp/SubCategory> <https://vocab.um.es/ontology/bbp/SubCategory>| 334 (1.68%)| 124 (1.56%)|
|<https://vocab.um.es/ontology/bbp/SalesSpecification> <https://vocab.um.es/ontology/bbp/SalesSpecification>| 4472 (22.51%)| 1806 (22.73%)|
| Total related entities |19867|7947

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-Gold/Input/451_1fold/1/)|9933|7947|1987|

### [Output](./Experiments/EntityAlignment/Gold-Gold/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | SalesArticle (#/%) | Product (#/%) | Category (#/%) | SubCategory (#/%) | SalesSpecification (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/AlignE/1/nohup_gold-gold_aligne.txt)|80.86|90.90 |93.63 |8|0.85|8714|0 (0.0%)|
|AliNet|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/AliNet/1/nohup_gold-gold_alinet.txt)|84.25|92.01|93.09|26|0.88|10335||
|AttrE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/AttrE/1/nohup_gold-gold_attre.txt)|94.56|99.64|99.99|1|0.97|7575|6 (1.60)|
|BootEA|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA/1/nohup_gold-gold_bootea.txt)|89.67|95.36 |96.82 |4|0.92|13386|0 (0.0%)|
|BootEA_RotatE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA_RotatE/1/nohup_gold-gold_bootea_rotate.txt)|86.30|95.45|97.09 |3|0.91|17748|0 (0.0%)|
|BootEA_TransH|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/BootEA_TransH/1/error_output_gold-gold_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/ConvE/1/error_output_gold-gold_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/GCN_Align/1/nohup_gold-gold_gcnalign.txt)|85.53|93.14 |94.56|13|0.89|1023|0 (0.0%)|
|GMNN|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/GMNN/1/nohup_gold-gold_gmnn.txt)|100|100 |100|1|1.00|64433|0 (0.0%)|
|HolE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/HolE/1/nohup_gold-gold_hole.txt)|67.01|75.22 |78.06|145|0.71|26733|0 (0.0%)|
|IMUSE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/IMUSE/1/nohup_gold-gold_imuse.txt)|68.10|91.47 |93.90|13|0.79|2007|0 (0.0%)|
|IPTransE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/IPTransE/1/error_output_gold-gold_iptranse.txt)|E|r|r|o|r|||
|JAPE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/JAPE/1/nohup_gold-gold_jape.txt)|67.56|76.14 |77.98|200|0.71|2945|0 (0.0%)|
|KDCoE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/KDCoE/1/error_output_gold-gold_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/MTransE/1/nohup_gold-gold_mtranse.txt)|58.76|64.91 |66.57|305|0.62|1560|0 (0.0%)|
|MultiKE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/MultiKE/1/error_output_gold-gold_multike.txt)|E|r|r|o|r|||
|ProjE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/ProjE/1/nohup_gold-gold_proje.txt)|32.78|38.14 |39.65|686|0.35|11090|0 (0.0%)|
|RDGCN|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/RDGCN/1/nohup_gold-gold_rdgcn.txt)|99.85|99.91 |99.94|1|1.00|13264|0 (0.0%)|
|RotatE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/RotatE/1/nohup_gold-gold_rotate.txt)|82.02|93.91 |96.00|4|0.87|3800|0 (0.0%)|
|RSN4EA|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/RSN4EA/1/nohup_gold-gold_rsn4ea.txt)|76.14|85.01|86.90|92|0.80|23671||
|SEA|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/SEA/1/nohup_gold-gold_sea.txt)|82.28|93.00 |95.60|3|0.87|2866|0 (0.0%)|
|SimplE|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/SimplE/1/nohup_gold-gold_simple.txt)|61.19|77.69|82.43|34|0.69|1469|0 (0.0%)|
|TransD|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/TransD/1/nohup_gold-gold_transd.txt)|65.47|72.13|74.93|120|0.69|4137|0 (0.0%)|
|TransH|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/TransH/1/nohup_gold-gold_transh.txt)|63.58|69.02|70.76|155|0.66|2403|0 (0.0%)|
|TransR|1|[7947](./Experiments/EntityAlignment/Gold-Gold/Output/TransR/1/nohup_gold-gold_transr.txt)|0.09|0.58|1.02|2453|0.01|3722|0 (0.0%)|

## [Gold - LLM](./Experiments/EntityAlignment/Gold-LLM/)

![Graph Gold-LLM](./Figures/bigBasketProducts-Gold-LLM.png "Graph Gold-LLM")

### [Input](./Experiments/EntityAlignment/Gold-LLM/Input/)

|ent_links| [Related Entities](./Experiments/EntityAlignment/Gold-Basic/Input/ent_links)|Split 1 Test|
|:-:|:-:|:-:|
|<https://vocab.um.es/ontology/ecd/Invoice> - <https://vocab.um.es#invoice>| 938 (4.31%)|364 (4.18%)
|<https://vocab.um.es/ontology/ecd/salesArticle> - <https://vocab.um.es#salesArticle>| 19425 (89.23%)|7802 (89.60%)
|<https://vocab.um.es/ontology/ecd/SalesSpecification> - <http://schema.org/UnitPriceSpecification>| 1407 (6.46%)|542 (6.22%)
| Total related entities |21770|8708

|Split|Training (50%) | Test (40%) | Validation (10%) |
|:-:|:-:|:-:|:-:|
|[1](./Experiments/EntityAlignment/Gold-LLM/Input/451_1fold/1/)|10885|8708|2177|

### [Output](./Experiments/EntityAlignment/Gold-Basic/Output/)

|Approach|Split|Aligned Ent|H@1 (%)|H@5 (%)|H@10 (%)|MR|MRR [0,1]|Run time | Invoice (#/%) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|AlignE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/AlignE/1/nohup_gold-basic_aligne.txt)|0.8|1.33 |2.40 |180|0.02|2123|0 (0.0%)|
|AliNet|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/AliNet/1/error_output_gold-basic_alinet.txt)|E|r|r|o|r|||
|AttrE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/AttrE/1/nohup_gold-basic_attre.txt)|1.33|5.33|11.2|132|0.05|1254|6 (1.60)|
|BootEA|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA/1/nohup_gold-basic_bootea.txt)|0.0|1.07 |1.60 |193|0.01|2117|0 (0.0%)|
|BootEA_RotatE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_RotatE/1/nohup_gold-basic_bootea_rotate.txt)|0.8|2.13|3.20 |188|0.02|6864|0 (0.0%)|
|BootEA_TransH|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/BootEA_TransH/1/nohup_gold-basic_bootea_transh.txt)|E|r|r|o|r|||
|Conve|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/ConvE/1/error_output_gold-basic_conve.txt)|E|r|r|o|r|||
|GCN_Align|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/GCN_Align/1/nohup_gold-basic_gcnalign.txt)|0.0|1.60 |3.20|188|0.02|215|0 (0.0%)|
|GMNN|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/GMNN/1/nohup_gold-basic_gmnn.txt)|98.67|100 |100|1|0.99|20177|0 (0.0%)|
|HolE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/HolE/1/nohup_gold-basic_hole.txt)|0.27|1.60 |3.20|187|0.02|4278|0 (0.0%)|
|IMUSE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/IMUSE/1/nohup_gold-basic_imuse.txt)|52.27|60.53 |64.53|60|0.56|449|0 (0.0%)|
|IPTransE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/IPTransE/1/nohup_gold-basic_iptranse.txt)|0.0|1.01 |1.87|187|0.01|731|0 (0.0%)|
|JAPE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/JAPE/1/nohup_gold-basic_jape.txt)|0.53|1.33 |2.93|187|0.02|747|0 (0.0%)|
|KDCoE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/KDCoE/1/error_output_gold-basic_kdcoe.txt)|E|r|r|o|r|||
|MTransE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/MTransE/1/nohup_gold-basic_mtranse.txt)|0.53|1.33 |2.40|190|0.02|659|0 (0.0%)|
|MultiKE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/MultiKE/1/error_output_gold-basic_multike.txt)|E|r|r|o|r|||
|ProjE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/ProjE/1/nohup_gold-basic_proje.txt)|0.27|1.60 |1.87|181|0.02|3128|0 (0.0%)|
|RDGCN|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/RDGCN/1/nohup_gold-basic_rdgcn.txt)|0.27|1.33 |3.47|166|0.02|1847|0 (0.0%)|
|RotatE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/RotatE/1/nohup_gold-basic_rotate.txt)|0.27|1.33 |2.40|184|0.02|3800|0 (0.0%)|
|RSN4EA|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/RSN4EA/1/error_output_gold-basic_rsn4ea.txt)|E|r|r|o|r|||
|SEA|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/SEA/1/nohup_gold-basic_sea.txt)|0.27|0.53 |1.87|184|0.02|266|0 (0.0%)|
|SimplE|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/SimplE/1/nohup_gold-basic_simple.txt)|0.0|2.13|4.0|187|0.02|237|0 (0.0%)|
|TransD|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/TransD/1/nohup_gold-basic_transd.txt)|0.53|1.60|2.40|187|0.02|796|0 (0.0%)|
|TransH|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/TransH/1/nohup_gold-basic_transh.txt)|0.0|1.07|2.13|186|0.01|696|0 (0.0%)|
|TransR|1|[375](./Experiments/EntityAlignment/Gold-Basic/Output/TransR/1/nohup_gold-basic_transr.txt)|0.53|2.40|3.47|194|0.01|2197|0 (0.0%)|

## [Basic - LLM](./Experiments/EntityAlignment/Basic-LLM/)

![Graph Basic-LLM](./Figures/bigBasketProducts-Basic-LLM.png "Graph Basic-LLM")

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
