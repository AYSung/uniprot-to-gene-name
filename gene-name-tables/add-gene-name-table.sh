#!/bin/bash
for PREFIX in $@
do
    wget https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/${PREFIX}_idmapping.dat.gz
    gunzip ${PREFIX}_idmapping.dat.gz
    grep 'Gene_Name' ${PREFIX}_idmapping.dat | awk -F '\t' '{print $1"\t"$3}' > ${PREFIX}_gene_names.txt
    rm ${PREFIX}*.dat
done