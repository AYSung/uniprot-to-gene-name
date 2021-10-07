# UniProt to Gene Name Mapper

## Running the script

Executing the script involves the following command line statement
`python uniprot-to-gene-name.py species list`

* `species` is one of `human`, `mouse`, `rat`, `yeast`
*  `list` is the path to the list of UniProtIDs to be mapped

e.g. to map the list of uniprot mouse IDs called 'list_of_uniprot_IDs.txt' to gene names, use the following command:

`python uniprot-to-gene-name.py mouse ./list_of_uniprot_IDs.txt`

Note: file directory paths in Windows use the `\` character, file directory paths in Linux/MacOS use `/`

You can map multiple lists of IDs by either passing in multiple file paths or using wildcard matching

e.g., to map the three lists `uniprot_IDs_1.txt`, `uniprot_IDs_2.txt`, `uniprot_IDs_3.txt` you could use either

`python uniprot-to-gene-name.py mouse ./uniprot_IDs_1.txt ./uniprot_IDs_2.txt ./uniprot_IDs_3.txt`

or

`python uniprot-to-gene-name.py mouse ./uniprot_IDs*.txt`

## Dependencies
This script requires `Pandas` and its dependencies to run properly. If you have a recent version of Pandas already installed, either through `pip` or `conda`, this should work fine. If not, navigate to the directory of the script and build an Anaconda environment using the command

`conda env create`

This will create an Anaconda environment named `uniprot-to-gene-name`. Activate this environment if it is not activated with the command

`conda activate uniprot-to-gene-name`

The script should now be able to run

## To generate mapping tables for other species
* Download `.dat.gz` from https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/ on Oct. 6, 2021
* Unzip file and place in /uniprot-id-tables directory
* Open `uniprot-to-gene-name.ipynb` Jupyter notebook. 
* Uncomment call to function `create_mapping()` and replace argument with prefix for .dat file (e.g., HUMAN_9606, MOUSE_10090)
* Run cell - there should now be a new file in the /gene-name-tables directory with the name `<prefix>_gene_names.txt`