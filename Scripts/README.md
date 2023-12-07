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

* RDF data generation:
  1. Indicate the YML file ([config.ini](./config.ini))
  2. Indicate the output RDF nt file ([csv2rdf-morph-kgc-rdflib.py](./csv2rdf-morph-kgc-rdflib.py))
	3. Generates the RDF nt file for each ontology-csv:
  ```
  nohup python3 csv2rdf-morph-kgc-rdflib.py &
  ```

* Data preparation ([processingRDF.py](processingRDF.py)):
  1. Indicate the two RDF nt files and the CSV file
	2. Indicate the Entities to be aligned
	3. Indicate the Object properties for each knowledge graph
	4. Indicate the output directory and files
  ```
  nohup python3 processingRDF.py &
  ```

* Training sets ([randomPairs.py](randomPairs.py)):
  1. Indicate the input directory and "ent_links" file
  2. Indicate the output directories
  3. Indicate the ratios of training, testing and validation
  4. Create the corresponding split folders and and code execution:
  ```
  nohup python3 randomPairs.py &
  ```

* Entity alignment:
  1. Edit arg file: "training_data", "output", "dataset_division". [Example](./attre_args_15K.json)
  ```
  cd ~/OpenEA/run
  nohup python main_from_args.py <arg.json> <training_data> <dataset_division> &
  ```
  Example:
  ```
  nohup python main_from_args.py ./args/attre_args_15K.json LLM-LLM/Input 451_1fold/1/ &
  ```
  2. nohup.out indicates the statistics
 
* Evaluation
  1. Entity count per class([countingAlignment.py](countingAlignment.py))
     1. Indicate the inputs: dataset, approach, test_links result, alignment_results_12 result, rel_triples1 result, kg1_ent_ids result and kg2_ent_ids result
     2. Indicate the outputs: count_aligned_ent file and ent_match file
     3. Generates the count file by class and the entity matching:
    ```
    nohup python3 countingAlignment.py &
    ```
  2. Merge results to combine ([merge_entity_alignments](./merge_entity_alignments.R))
     1. Indicate the inputs: the path of results for each method (main_path_results), methods and pairwise alignments to combine (methods and pairs)
     2. Indicate the outputs: the path to save the results (path_save)
     2. Generate the merger:
    ```
    Rscript merge_entity_alignments.R
    ```
  3. Merged entity count per class ([count_merge_entity_alignments](./count_merge_entity_alignments.R))
     1. Indicate the inputs: the previously merged file (input_file), and the original file with relations(rel_triples1) and test file (test_links)
     2. Indicate the output (file with count): output_path
     3. Generate the count:
    ```
    Rscript count_merge_entity_alignments.R
    ```
    
