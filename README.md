# UniProt to Gene Name Mapper

## Running the script

Executing the script involves the following command line statement
`python uniprot-to-gene-name.py species list`

* `species` is one of `human`, `mouse`, `rat`, `yeast`
* `list` is the path to the list of UniProtIDs to be mapped

e.g. to map the list of uniprot mouse IDs called 'list_of_uniprot_IDs.txt' to gene names, use the following command:

`python uniprot-to-gene-name.py mouse ./list_of_uniprot_IDs.txt`

Note: file directory paths in Windows use the `\` character, file directory paths in Linux/MacOS use `/`

You can map multiple lists of IDs by either passing in multiple file paths or using wildcard matching

e.g., to map the three lists `uniprot_IDs_1.txt`, `uniprot_IDs_2.txt`, `uniprot_IDs_3.txt` you could use either

`python uniprot-to-gene-name.py mouse ./uniprot_IDs_1.txt ./uniprot_IDs_2.txt ./uniprot_IDs_3.txt`

or

`python uniprot-to-gene-name.py mouse ./uniprot_IDs*.txt`

results of the mapping are saved in a new file with the suffix `_result.csv`

## Dependencies
This script requires `Pandas` and its dependencies to run properly. If you have a recent version of Pandas already installed, either through `pip` or `conda`, this should work fine. If not, navigate to the directory of the script and build an Anaconda environment using the command

`conda env create`

This will create an Anaconda environment named `uniprot-to-gene-name`. Activate this environment if it is not activated with the command

`conda activate uniprot-to-gene-name`

The script should now be able to run in the terminal/command line. (Remember to activate the environment any time you open up a new terminal window)

## To add new mapping tables (Linux/MacOS only, or WSL on Windows to use)
* Go to https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/ to find the prefix for a `_idmapping.dat.gz` file for the species you want.
* Open bash shell / terminal
* Navigate to `./gene-name-tables/` directory
* Give executable permission to `add-gene-name-tables.sh` with the command `chmod +x add-gene-name-tables.sh` (Should only need to do this once)
* Run the bash script with the command `./add-gene-name-tables.sh <prefix>`, where prefix is something like HUMAN_9606 or MOUSE_10090. You can put as many prefixes in a row as you want `./add-gene-name-tables.sh ECOLI_83333 RAT_10116` will add tables for both *E. coli* and Rat.
* Note: using this script to add a species for which there is already a `_gene_names.txt` file will overwrite it (probably won't do anything bad, can be used to update a gene name table if UniProt ever releases a new `_idmapping.dat.gz`).