import os
import sys
import argparse
import pandas as pd


import numpy as np
from sklearn.model_selection import train_test_split
sys.path.append(os.path.dirname(sys.path[0]))


# import mplconfig

import ROOT 
ROOT.PyConfig.IgnoreCommandLineOptions = True
from root_pandas import read_root
from root_pandas import readwrite



def replace(df: pd.DataFrame):
    ltp_variables = ['extraInfoMuPCMS', 'extraInfoEPCMS']
    ltcos_variables = ['extraInfoMuCosTheta', 'extraInfoECosTheta']
    dt_variables = ['DeltaT', 'DeltaTErr']
    #df[ltp_variables] = df[ltp_variables].fillna(0)
    #df[ltcos_variables] = df[ltcos_variables].fillna(-1)
    #df[dt_variables] = df[dt_variables].fillna(-15)
    cut = '(extraInfoMuTag > 0 or extraInfoETag > 0)'
    return df.query(cut)

if __name__ == '__main__':
    #cuts = mplconfig.getCuts('m2')
    #print(cuts)

    parser = argparse.ArgumentParser(description="Script to split train test")
    parser.add_argument('filenames', nargs='+', help="Input MC file names")
    parser.add_argument('-r','--ratio', type=float, default=0.3, help="Test to train ratio")
    parser.add_argument('-t','--tree', type=str, default='my_ttree', help="Tree to use") 
    parser.add_argument('-tag','--tag_name', type=str, default='ltmva', help="Tag name for output files")
    

    args = parser.parse_args()

    df = read_root(args.filenames, key=args.tree)
    # df = replace(df)
    folder = os.path.dirname(args.filenames[0])
    df_train, df_test = train_test_split(df, test_size=args.ratio, random_state=42)
    print(f'Saving output to: {folder}')
    df_train.to_root(f'train-{args.tag_name}.root',key=args.tree)
    df_test.to_root(f'test-{args.tag_name}.root',key=args.tree)
