# Instructions for reproducing the experiments

The scripts for the execution of the experiments have been implemented in Python (3.6). You will require to have [OpenEA](https://github.com/nju-websoft/OpenEA) installed, also [Morph-KGC](https://github.com/morph-kgc/morph-kgc).

## Python packages required
The file [requirements.txt](./requirements.txt) include the Python packages needed for executing the experiments.

You can install them using  

pip install -r requirements.txt

## Execution

Next, we illustrate how to run an experiment, which requires to use one dataset, two ontologies and two mapping files. The concrete example is eCommerce LLM-LLM.

### The scripts
All the scripts needed are available in the [scripts](./) folder. Next, we explain the task carried out by each script:

Hay que añadir el nombre de los ficheros

* RDF data generation ([csv2rdf-morph-kgc-rdflib.py](./csv2rdf-morph-kgc-rdflib.py)): Generation of the RDF data using Morph-KGC with the previously defined mapping rules.

* Data preparation ([processingRDF.py](processingRDF.py)): Splitting the RDF files required by OpenEA for the alignments, that is, files with triples representing the attributes (attr), the relations (rel) and the aligned entities (ent).

* Training sets ([randomPairs.py](randomPairs.py)): Randomly split the set of aligned entities in three files, containing: links for training the model, links for the validation of the model, and links for testing.

* Entity alignment ([main_from_args.py](https://github.com/nju-websoft/OpenEA/blob/master/run/main_from_args.py)): Run the entity alignment experiment with a graph alignment method.

* Evaluation ([countingAlignment.py](countingAlignment.py)): Generation of metrics for evaluating the results.


### The commands



