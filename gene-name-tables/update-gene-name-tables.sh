#!/bin/bash
for PREFIX in ${@:-'HUMAN_9606' 'MOUSE_10090' 'YEAST_559292'}
do
    wget https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/${PREFIX}_idmapping.dat.gz
    gunzip ${PREFIX}_idmapping.dat.gz
    grep 'Gene_Name' ${PREFIX}_idmapping.dat | awk '{print $1"\t"$3}' > ${PREFIX}_gene_names.txt
done
rm *.dat