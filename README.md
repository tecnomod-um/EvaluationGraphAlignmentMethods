# Evaluation of 25 OpenEA knowledge graph alignment methods

## Overview

This repository contains the data, scripts and results of evaluating 25 methods offered by the OpenEA package for the alignment of datasets related to product, sales and user satisfaction. Through this study we aim to identify:

* Which methods give the best performance in our domain of interest?
* Which is the impact of the structure of the ontologies in the results?
* Which is the impact of combining the best performing methods in the results?

 The next figure describes the approach followed. The experiments included seven datasets related to our domain of interest: six datasets have been selected from Kaggle and the other one was provided by the chemical company BASF SE as an RDF knowledge graph. 

The datasets were represented in RDF using different ontologies, which have the following origin:

* Basic ontology (B). Dataset-dependent ontology, created by a member of our team, which implements a canonical representation of the CSV file, in which the ontology has one class, and the columns are represented as datatype properties of the class, because they are strings, dates and numeric data.

* Gold ontology (G). Dataset-dependent ontology, created by a member of our team. The gold ontology includes the definition of different classes that are related to each other through object properties, as well as attributes included as datatype properties.

* LLM ontology (L). Dataset-dependent ontology. This ontology corresponds to the schema returned by OntoGenix \cite{ontogenix}, an LLM algorithm based on ChatGPT4.0 which has been given guidelines to generate an ontology from a CSV dataset.

* Materials (M) and Transactions (T), dataset-independent ontologies. These ontologies, which are called BASF ontologies or application ontologies (AP), was previously developed by BASF SE domain experts for the modeling of business entities related to commercial activity.

<figcaption><strong>Figure 1.</strong> Method Overview.</figcaption>

![Overview Figure](./FiguresAndTables/graphicalAbstract.png "Overview Figure")

## Pipeline OpenEA

We have designed a pipeline for standardizing our process for obtaining the alignments between pairs of knowledge graphs, which is described in the next figure. 

Each experiment consists of finding the alignment between two KGs generated from the information stored in the same CSV file (dataset) but structured with two different ontologies. 

See the [instructions](./Scripts/README.md) for reproducing the experiments.

<figcaption><strong>Figure 2.</strong> Entity Alignment OpenEA Pipeline .</figcaption>

![Entity Alignment OpenEA Pipeline](./FiguresAndTables/graphicalAlignment-pipeline.png "Entity Alignment OpenEA Pipeline")

## Experiments performed

A total of 49 alignment experiments were carried out using 25 different methods. Alignments were carried out whenever the schemas had compatible entities to align. 

<figcaption><strong>Table 1.</strong> Experiments Performed.</figcaption>

| Approach       |   AirlinesCustomerSatisfaction |   AmazonRatings |   BigBasketProducts |   BrazilianE-commerce |   E-CommerceData | Customer Satisfaction |
|:---------------|-------------------------------:|----------------:|--------------------:|----------------------:|-----------------:|----------------------:|
| Basic-Basic | X | X | X | X | X | X |
| Basic-Gold | X | X | X | X | X | X |
| Basic-LLM | X | X | X | X | X | X |
| Basic-AP |  | X | X |  |  |  |
| Gold-Gold | X | X | X | X | X | X |
| Gold-LLM | X | X | X | X | X | X |
| Gold-AP |  | X | X | X | X |  |
| LLM-LLM | X | X | X | X | X | X |
| LLM-AP |  | X | X |  | X |  |
| AP-AP |  | X | X | X | X |  |

## Results

The results have been analyzed at three levels, from higher to lower resolution. At the individual class level, at the method level and at the experiment type level. 
The detailed results by dataset can be accessed by clicking on the name of the dataset. 

* [AirlinesCustomerSatisfaction](./AirlinesCustomerSatisfaction/AirlinesCustomerSatisfaction.md)

* [AmazonRatings](./AmazonRatings/AmazonRatings.md)

* [BigBasketProducts](./BigBasketProducts/bigBasketProducts.md)

* [BrazilianE-commerce](./BrazilianE-Commerce/brazilianEcommerce.md)

* [CustomerComplaintDatabase](./CustomerComplaintDatabase/CustomerComplaintDatabase.md)

* [E-Commerce Data](./E-CommerceData/eCommerceData.md)

* [Materials](./Materials/materials.md)

Next, we present some tables and figures that summarize the results obtained in terms of Hits@1, runtime and errors 

<figcaption><strong>Figure 3.</strong> Distribution of OpenEA methods according to the average Hits@1 score obtained between datasets and the average execution time obtained between datasets, scaled between 0 and 1 for each experiment. The average percentage of failed experiments between datasets is included in the label. Modules with an error rate of 1 are not shown.</figcaption>

![Modules distribution by averages](./FiguresAndTables/plotMeansModules.png "Modules distribution by averages")

<figcaption><strong>Table 2.</strong> Mean Hits@1 metric ([0,100]) obtained by each method</figcaption>

|    | Approach       |   AirlinesCustomerSatisfaction |   AmazonRatings |   BigBasketProducts |   BrazilianE-commerce |   E-CommerceData |   CustomerComplaintDatabase |    meanH@1 |
|---:|:---------------|-------------------------------:|----------------:|--------------------:|----------------------:|-----------------:|----------------------------:|-----------:|
|  0 | AlignE(0.0)    |                     15.1167    |         35.397  |             29.568  |              24.1625  |          31.8589 |                  22.8033    |  26.4844   |
|  1 | AliNet(0.57)   |                     68.34      |         59.0583 |             55.52   |              70.28    |          60.0125 |                  40.7633    |  58.9957   |
|  2 | AttrE(0.0)     |                     41.495     |         68.017  |             60.927  |              59.01    |          42.6556 |                  58.8867    |  55.1652   |
|  3 | BootEA(0.0)    |                     16.2817    |         37.884  |             30.609  |              26.3525  |          31.8378 |                  23.24      |  27.7008   |
|  4 | BootEA-R(0.0)  |                     16.115     |         37.049  |             29.894  |              25.7637  |          32.1722 |                  22.7267    |  27.2868   |
|  5 | BootEA-T(1.0)  |                    nan         |        nan      |            nan      |             nan       |         nan      |                 nan         | nan        |
|  6 | Conve(1.0)     |                    nan         |        nan      |            nan      |             nan       |         nan      |                 nan         | nan        |
|  7 | GCN_Align(0.0) |                     12.6167    |         37.839  |             28.626  |              25.1512  |          29.7511 |                  21.9283    |  25.9854   |
|  8 | GMNN(0.69)     |                    nan         |        nan      |             86.41   |             100       |          99.7783 |                 nan         |  95.3961   |
|  9 | HolE(0.0)      |                      9.565     |         31.424  |             21.849  |              19.115   |          25.9356 |                  17.4533    |  20.8903   |
| 10 | IMUSE(0.16)    |                     26.5817    |         56.8243 |             44.3389 |              89.925   |          57.0533 |                  31.1383    |  50.9769   |
| 11 | IPTransE(0.93) |                    nan         |        nan      |            nan      |             nan       |          33.035  |                 nan         |  33.035    |
| 12 | JAPE(0.21)     |                      0.473333  |         26.9567 |             23.4478 |              22.1033  |          16.0225 |                  14.3017    |  17.2175   |
| 13 | KDCoE(1.0)     |                    nan         |        nan      |            nan      |             nan       |         nan      |                 nan         | nan        |
| 14 | MTransE(0.0)   |                      1.955     |         31.3    |             24.849  |              19.7     |          13.96   |                  12.3517    |  17.3526   |
| 15 | MultiKE(1.0)   |                    nan         |        nan      |            nan      |             nan       |         nan      |                 nan         | nan        |
| 16 | ProjE(0.04)    |                      5.36667   |         15.732  |             12.722  |               6.85125 |          24.5429 |                  11.12      |  12.7225   |
| 17 | RDGCN(0.07)    |                      0.005     |          0.009  |             72.8244 |              34.8486  |          19.6678 |                   0.034     |  21.2315   |
| 18 | RotatE(0.16)   |                      0.0166667 |         30.48   |             28.801  |              24.3987  |          31.4356 |                   2.0275    |  19.5266   |
| 19 | RSN4EA(0.7)    |                    nan         |         56.1    |             58.0875 |              63.4267  |          61.2425 |                 nan         |  59.7142   |
| 20 | SEA(0.0)       |                     16.2483    |         35.707  |             29.059  |              24.575   |          32.2056 |                  21.8917    |  26.6144   |
| 21 | SimplE(0.0)    |                      0.0916667 |         27.732  |             22.209  |              20.775   |          23.4344 |                   5.025     |  16.5445   |
| 22 | TransD(0.02)   |                     13.1267    |         33.621  |             26.36   |              19.73    |          29.6863 |                  21.16      |  23.9473   |
| 23 | TransH(0.0)    |                     13.3217    |         33.702  |             26.211  |              21.3675  |          29.2789 |                  21.4       |  24.2135   |
| 24 | TransR(0.0)    |                      0.015     |          0.036  |              0.08   |               0.03875 |           0.39   |                   0.0466667 |   0.101069 |

<figcaption><strong>Table 3.</strong> Mean Runtime ([0,1]) for each module.</figcaption>

|    | Approach   |   AirlinesCustomerSatisfaction |   AmazonRatings |   BigBasketProducts |   BrazilianE-commerce |   E-CommerceData |   CustomerComplaintDatabase |    meanTime |
|---:|:-----------|-------------------------------:|----------------:|--------------------:|----------------------:|-----------------:|----------------------------:|------------:|
|  0 | AlignE     |                     0.383452   |       0.398477  |          0.140399   |            0.217742   |       0.308854   |                  0.420449   |   0.311562  |
|  1 | AliNet     |                     0.29239    |       0.413501  |          0.128083   |            0.70534    |       0.176202   |                  0.503721   |   0.369873  |
|  2 | AttrE      |                     0.586099   |       0.329858  |          0.175498   |            0.334752   |       0.166925   |                  0.625912   |   0.369841  |
|  3 | BootEA     |                     0.434692   |       0.570226  |          0.148005   |            0.312151   |       0.297753   |                  0.420206   |   0.363839  |
|  4 | BootEA-R   |                     0.68202    |       0.85052   |          0.319472   |            0.575235   |       0.539029   |                  0.747011   |   0.618881  |
|  5 | BootEA-T   |                   nan          |     nan         |        nan          |          nan          |     nan          |                nan          | nan         |
|  6 | Conve      |                   nan          |     nan         |        nan          |          nan          |     nan          |                nan          | nan         |
|  7 | GCN_Align  |                     0.058169   |       0.0232482 |          0.00354892 |            0.00614488 |       0.00766333 |                  0.0205908  |   0.0198942 |
|  8 | GMNN       |                   nan          |     nan         |          1          |            1          |       0.853034   |                nan          |   0.951011  |
|  9 | HolE       |                     0.476202   |       0.6037    |          0.350937   |            0.388389   |       0.505976   |                  0.604757   |   0.488327  |
| 10 | IMUSE      |                     0.168226   |       0.0723632 |          0.017393   |            0.0208482  |       0.0119694  |                  0.09483    |   0.0642716 |
| 11 | IPTransE   |                   nan          |     nan         |        nan          |          nan          |       0.0682923  |                nan          |   0.0682923 |
| 12 | JAPE       |                     0.346894   |       0.0985859 |          0.0333028  |            0.0554822  |       0.0379448  |                  0.250169   |   0.137063  |
| 13 | KDCoE      |                   nan          |     nan         |        nan          |          nan          |     nan          |                nan          | nan         |
| 14 | MTransE    |                     0.0652884  |       0.0196702 |          0.00771234 |            0.0231861  |       0.0155308  |                  0.0644053  |   0.0326322 |
| 15 | MultiKE    |                   nan          |     nan         |        nan          |          nan          |     nan          |                nan          | nan         |
| 16 | ProjE      |                     0.42183    |       0.284093  |          0.13603    |            0.225391   |       0.322763   |                  0.400854   |   0.298493  |
| 17 | RDGCN      |                     0.331012   |       0.109752  |          0.337565   |            0.468765   |       0.510758   |                  0.916327   |   0.445697  |
| 18 | RotatE     |                     0.415271   |       0.317508  |          0.146911   |            0.196299   |       0.257131   |                  0.452141   |   0.297543  |
| 19 | RSN4EA     |                   nan          |       0.804311  |          0.275658   |            0.778985   |       0.88147    |                nan          |   0.685106  |
| 20 | SEA        |                     0.0729613  |       0.031018  |          0.00693881 |            0.0286398  |       0.0295775  |                  0.0288212  |   0.0329928 |
| 21 | SimplE     |                     0.00655595 |       0.0134017 |          0.0136943  |            0.0152445  |       0.0206047  |                  0.00147042 |   0.0118286 |
| 22 | TransD     |                     0.143617   |       0.103602  |          0.0398369  |            0.0595628  |       0.0886751  |                  0.205873   |   0.106861  |
| 23 | TransH     |                     0.11547    |       0.0678725 |          0.0253032  |            0.0604899  |       0.0898547  |                  0.151213   |   0.0850337 |
| 24 | TransR     |                     0.182317   |       0.122178  |          0.066497   |            0.0796253  |       0.126292   |                  0.144497   |   0.120235  |

<figcaption><strong>Table 4.</strong> Mean Error rate ([0,1]) for each module.</figcaption>

|   | Approach   |   AirlinesCustomerSatisfaction |   AmazonRatings |   BigBasketProducts |   BrazilianE-commerce |   E-CommerceData |   CustomerComplaintDatabase |   meanError |
|---:|:-----------|-------------------------------:|----------------:|--------------------:|----------------------:|-----------------:|----------------------------:|------------:|
|  0 | AlignE     |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
|  1 | AliNet     |                       0.833333 |             0.4 |                 0.5 |                 0.625 |         0.555556 |                    0.5      |        0.57 |
|  2 | AttrE      |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
|  3 | BootEA     |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
|  4 | BootEA-R   |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
|  5 | BootEA-T   |                       1        |             1   |                 1   |                 1     |         1        |                    1        |        1    |
|  6 | Conve      |                       1        |             1   |                 1   |                 1     |         1        |                    1        |        1    |
|  7 | GCN_Align  |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
|  8 | GMNN       |                       1        |             1   |                 0.3 |                 0.5   |         0.333333 |                    1        |        0.69 |
|  9 | HolE       |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
| 10 | IMUSE      |                       0        |             0.3 |                 0.1 |                 0.25  |         0.333333 |                    0        |        0.16 |
| 11 | IPTransE   |                       1        |             1   |                 1   |                 1     |         0.555556 |                    1        |        0.93 |
| 12 | JAPE       |                       0        |             0.4 |                 0.1 |                 0.625 |         0.111111 |                    0        |        0.21 |
| 13 | KDCoE      |                       1        |             1   |                 1   |                 1     |         1        |                    1        |        1    |
| 14 | MTransE    |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
| 15 | MultiKE    |                       1        |             1   |                 1   |                 1     |         1        |                    1        |        1    |
| 16 | ProjE      |                       0        |             0   |                 0   |                 0     |         0.222222 |                    0        |        0.04 |
| 17 | RDGCN      |                       0        |             0   |                 0.1 |                 0.125 |         0        |                    0.166667 |        0.07 |
| 18 | RotatE     |                       0.5      |             0.1 |                 0   |                 0     |         0        |                    0.333333 |        0.16 |
| 19 | RSN4EA     |                       1        |             0.4 |                 0.6 |                 0.625 |         0.555556 |                    1        |        0.7  |
| 20 | SEA        |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
| 21 | SimplE     |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
| 22 | TransD     |                       0        |             0   |                 0   |                 0     |         0.111111 |                    0        |        0.02 |
| 23 | TransH     |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |
| 24 | TransR     |                       0        |             0   |                 0   |                 0     |         0        |                    0        |        0    |

<figcaption><strong>Table 5.</strong> P-value of the two-sided t-test statistic between trivial graph alignment experiments, considering the Hits@1 of all methods. Assuming normality, sample independence and not considering Nan values.</figcaption>

| |AlignE|AliNet|AttrE|BootEA|BootEA_R|GCN_A|GMNN|HolE|IMUSE|IPTransE|JAPE|MTransE|ProjE|RDGCN|RotatE|RSN4EA|SEA|SimplE|TransD|TransH|TransR|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|AlignE|1.0|||||||||||||||||||||
|AliNet|2.709E-05|1.0||||||||||||||||||||
|AttrE|1.105E-04|0.790|1.0|||||||||||||||||||
|BootEA|0.851|7.452E-05|2.872E-04|1.0||||||||||||||||||
|BootEA_R|0.901|5.419E-05|2.2130E-04|0.950|1.0|||||||||||||||||
|GCN_A|0.960|2.300E-05|9.410E-05|0.813|0.862|1.0||||||||||||||||
|GMNN|2.558E-11|1.828E-05|9.856E-06|4.738E-11|3.820E-11|2.237E-11|1.0|||||||||||||||
|HolE|0.358|3.990E-07|1.447E-06|0.275|0.302|0.387|3.870E-12|1.0||||||||||||||
|IMUSE|0.001|0.298|0.458|0.003|0.002|0.001|8.131E-07|2.796E-05|1.0|||||||||||||
|IPTransE|0.824|0.338|0.370|0.865|0.851|0.813|0.062|0.651|0.482|1.0||||||||||||
|JAPE|0.090|2.966E-08|7.574E-08|0.066|0.074|0.101|9.794E-13|0.390|1.722E-06|0.523|1.0|||||||||||
|MTransE|0.129|3.021E-08|5.946E-08|0.094|0.105|0.145|3.570E-12|0.549|1.594E-06|0.566|0.736|1.0||||||||||
|ProjE|0.006|1.098E-09|2.003E-10|0.004|0.005|0.007|7.212E-12|0.047|8.170E-09|0.424|0.344|0.129|1.0|||||||||
|RDGCN|0.544|8.402E-06|3.256E-05|0.443|0.477|0.576|6.805E-12|0.840|3.671E-04|0.692|0.355|0.481|0.074|1.0||||||||
|RotatE|0.618|5.428E-06|2.181E-05|0.502|0.540|0.654|8.316E-12|0.706|2.855E-04|0.721|0.249|0.350|0.032|0.890|1.0|||||||
|RSN4EA|9.289E-06|0.854|0.663|2.707E-05|1.932E-05|7.858E-06|2.468E-05|1.304E-07|0.212|0.318|1.103E-08|1.240E-08|1.189E-09|3.020E-06|1.851E-06|1.0||||||
|SEA|0.986|3.090E-05|1.251E-04|0.866|0.915|0.946|2.713E-11|0.351|0.001|0.828|0.089|0.127|0.006|0.535|0.608|1.068E-05|1.0|||||
|SimplE|0.118|2.835E-08|6.347E-08|0.086|0.096|0.132|2.102E-12|0.501|1.637E-06|0.553|0.812|0.921|0.182|0.443|0.320|1.086E-08|0.116|1.0||||
|TransD|0.673|3.743E-06|1.551E-05|0.546|0.588|0.712|9.322E-12|0.614|2.301E-04|0.739|0.187|0.267|0.015|0.814|0.921|1.213E-06|0.662|0.243|1.0|||
|TransH|0.712|4.551E-06|1.900E-05|0.580|0.624|0.751|1.027E-11|0.576|2.765E-04|0.749|0.170|0.243|0.013|0.777|0.881|1.474E-06|0.699|0.221|0.957|1.0||
|TransR|3.190E-07|4.875E-11|3.488E-14|3.705E-07|3.770E-07|4.260E-07|1.318E-11|1.113E-06|2.681E-12|0.226|9.832E-05|5.334E-07|3.855E-07|6.728E-05|6.478E-06|3.522E-10|3.612E-07|3.104E-06|5.522E-07|4.258E-07|1.0|

<figcaption><strong>Table 6.</strong> P-value of the two-sided t-test statistic between trivial graph alignment experiments, considering the Hits@1 of all methods. Assuming normality, sample independence and not considering Nan values.</figcaption>

|   | G-G | B-B | L-L | AP-AP | G-B | G-L | G-AP | B-L | B-AP | L-AP |
|:-:|:---:|:---:|:---:|:-----:|:---:|:---:|:---:|:-----:|:---:|:-----:|
|G-G|1.0||||
|B-B|7.49E-30|1.0|||
|L-L|3.84E-07|9.90e-14|1.0||
|AP-AP|3.06E-08|6.98E-08|0.195|1.0|
|G-B|7.67E-38|0.305|||1.0||||||
|G-L|1.02E-23||1.95E-07||8.57E-07|1.0|||||
|G-AP|3.13E-13|||0.209|4.60E-09|0.050|1.0||||
|B-L||0.025|6.13E-25||0.198|1.23E-11||1.0|||
|B-AP||0.236||7.99E-08|0.648||2.50E-06|0.724|1.0||
|L-AP|||2.35E-07|1.20E-03||0.743|0.032|1.00E-08|5.58E-04|1.0|

<figcaption><strong>Figure 4.</strong> Bar chart containing the average increase in Hits@1 value when combining the AttrE module with either BootEA or Align-E or SEA, with respect to the module of each pair with the highest Hits@1 value. For the 4 types of experiments G-G, B-B, L-L and AP-AP. This is the average obtained from the averages obtained from all the classes aligned in each of the six datasets individually.</figcaption>

![Modules distribution by averages](./FiguresAndTables/barchartMethodsAccumulated.png "Combined Improvement Hits@1")