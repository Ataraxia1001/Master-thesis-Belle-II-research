import os
import sys
import pandas as pd
import argparse
import ROOT 
ROOT.PyConfig.IgnoreCommandLineOptions = True
from root_pandas import read_root
from root_numpy import list_trees

import basf2_mva

parser = argparse.ArgumentParser()
parser.add_argument('filenames', help='Ntuple files', nargs='+')

parser.add_argument('-t','--tree', help='Tree name',
        default='my_ttree')
parser.add_argument('-x','--xml', help='XML file path',
        type=str, required=True)


args = parser.parse_args()
var_name = os.path.basename(args.xml).split('_')[0]
tag_name = os.path.basename(args.xml).split('_')[1][:-4]
print(var_name)
for filename in args.filenames:
    initial_base =  os.path.basename(filename).split('.')[0]
    tmp_filename = f'.tmp_{initial_base}_{var_name}-{tag_name}.root'
    treename = args.tree
    if not treename:
        treename = list_trees(filename)[0]
    print(f'{filename}: {treename}')
    basf2_mva.expert(basf2_mva.vector(args.xml),
                    basf2_mva.vector(filename),
                    treename, tmp_filename)
    expert_df = read_root(tmp_filename).reset_index()
    target_df = read_root(filename, key=treename).reset_index()
    target_df[var_name] = expert_df[expert_df.columns[1]]
    if  'level_0' in target_df.columns:
        target_df.drop(['level_0'], axis=1, in_place=True)
    target_df.drop(['index'], axis=1).to_root(f'{filename[:-5]}_{var_name}-{tag_name}.root', key=treename)
