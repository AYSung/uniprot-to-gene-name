import argparse
import pandas as pd
from pathlib import Path


# return dictionary with UniProtID: Gene Name key-value-pairs
def get_map(species):
    MAPPERS = {
        'human': Path('gene-name-tables/HUMAN_9606_gene_names.txt'),
        'mouse': Path('gene-name-tables/MOUSE_10090_gene_names.txt'),
        'yeast': Path('gene-name-tables/YEAST_559292_gene_names.txt'),
        # Add key and path to _gene_names.txt for other species here if desired
    }
    map = pd.read_csv(MAPPERS[species], delimiter='\t', names=['UniProtID','GeneName'])
    return dict(zip(map['UniProtID'], map['GeneName']))


# Creates new column with gene name corresponding to UniProtID and saves in a *_result.csv file
def map_ids(species, list_paths):
    mapper = get_map(species)
    for path in list_paths:
        df = pd.read_csv(path, delimiter='\n', header=None, names=['UniProtID'])
        df['GeneName'] = df['UniProtID'].map(mapper)
        df.to_csv(path.with_name(f'{path.stem}_result').with_suffix('.csv'), index=False)


def main(args):
    map_ids(args.species, args.list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='uniprot-to-genename', 
        description='Map list of UniProtIDs to Gene Names')

    # add other species here after creating a mapper in the /gene-name-tables director
    species = ['human','mouse','yeast']

    parser.add_argument('species',
        metavar='species',
        choices=species,
        type=str,
        help='species to use for ID mapping',)
    parser.add_argument('list',
        metavar='ID_list',
        nargs='+',
        type=Path,
        help='list of UniProtIDs, separated by newline',)
    args = parser.parse_args()
    main(args)