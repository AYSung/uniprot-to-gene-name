import argparse
import pandas as pd
from pathlib import Path


def main(args):
    mappers = {
        'human': Path('gene-name-tables/HUMAN_9606_gene_names.txt'),
        'mouse': Path('gene-name-tables/MOUSE_10090_gene_names.txt'),
        'rat': Path('gene-name-tables/RAT_10116_gene_names.txt'),
        'yeast': Path('gene-name-tables/YEAST_559292_gene_names.txt'),
        # Add path to mappers for other species here if desired
    }
    
    format = INPUT_FORMATS[args.format]
    uniprot_to_genename = dict(pd.read_csv(mappers[args.species], delimiter='\t').to_records(index=False))
 
    for path in args.list:
        (pd.read_csv(path, **format)
         .assign(GeneName=lambda x: x.UniProtID.map(uniprot_to_genename))
         .to_csv(path.with_name(f'{path.stem}_result').with_suffix('.csv'), index=False))

if __name__ == '__main__':
    INPUT_FORMATS = {
        'list': {'delimiter':'\t', 'header':None, 'names':['UniProtID']},
        'maxquant': {},
    }
    
    parser = argparse.ArgumentParser(
        prog='uniprot-to-genename', 
        description='Map list of UniProtIDs to Gene Names')

    # add other species here after creating a mapper in the /gene-name-tables director
    species = ['human','mouse','rat','yeast']

    ## TODO: maxquant/proteome discoverer support
    parser.add_argument('-f', '--format',
        metavar='input_format',
        default='list',
        type=str,
        choices=INPUT_FORMATS.keys(),
        dest='format',
        help='data format'
        )
    parser.add_argument('species',
        metavar='species',
        choices=species,
        type=str,
        help='species to use for ID mapping, choose from [ human | mouse | rat | yeast ]',)
    parser.add_argument('list',
        metavar='ID_list',
        nargs='+',
        type=Path,
        help='list of UniProtIDs, separated by newline',)
    args = parser.parse_args()
    main(args)