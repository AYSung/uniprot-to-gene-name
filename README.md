# UniProt to Gene Name Mapper

## Running the script

Executing the script involves the following command line statement
`python uniprot-to-gene-name.py species list`

where `species` is one of `human`, `mouse`, `rat`, `yeast`

and `list` is the path to the list of UniProtIDs to be mapped


e.g.
`python uniprot-gene-name.py mouse ./sample_input_list.txt`

Note: file directory paths in Windows use the `\` character, file directory paths in Linux/MacOS use `/`

## Dependencies
This script requires `Pandas` to run properly.

## To generate mapping tables for other species
* Download `.dat.gz` from https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/ on Oct. 6, 2021
* Unzip file and place in /uniprot-id-tables directory
* Open `uniprot-to-gene-name.ipynb` Jupyter notebook. 
* Uncomment call to function `create_mapping()` and replace argument with prefix for .dat file (e.g., HUMAN_9606, MOUSE_10090)
* Run cell - there should now be a new file in the /gene-name-tables directory with the name `<prefix>_gene_names.txt`