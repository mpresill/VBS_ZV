#!/usr/bin/env python
# coding: utf-8
import ROOT as R
R.gROOT.SetBatch(True)
import argparse
import os
from pprint import pprint
import pandas as pd 


import latinos_rdf as lrdf

parser = argparse.ArgumentParser()
parser.add_argument("--config-dir", type=str, help="Latinos config dir")
parser.add_argument("--cut", type=str, help="Cut to output")
parser.add_argument("-o","--outputdir", type=str, help="Output dir")
parser.add_argument("--vers", type=str, help="Version")
parser.add_argument("-s","--samples", type=str, nargs="+", help="Samples to output")
parser.add_argument("--discard-negative-weights",action="store_true", help="Remove negative weighted events", default=False)
parser.add_argument("--debug", action="store_true", help="Debug output")
args = parser.parse_args()

keep_negative_weights = not args.discard_negative_weights

R.ROOT.EnableImplicitMT() # only for ROOT rdf
print(f"Running with {R.ROOT.GetImplicitMTPoolSize()} threads")

R.gInterpreter.ProcessLine(".L headers.hh")

# sample version
version = args.vers
# input: plot config tag
config_dir = args.config_dir

#cut = "res_sig_mjjincl"
cut = args.cut

# Samples to output
samples = args.samples

# output: samples directory
output_basedir = args.outputdir
output_dir = os.path.join(output_basedir, config_dir, cut, "samples", version)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

config = lrdf.ConfigReader(config_dir, version)

### List of variables to output: 
# The name of the variable is: cut_variablename
output_columns = [ cut+"_"+c for c in config.variables]
output_columns += ["weight_"]

print("Output columns: ", output_columns)

'''
The LatinoRDF lib creates the RootDataFrame trees to be run. 
One "job" is created for each group of files with the base weights. 
This means that each sample can be splitted in more than one "job". 
'''
joblist = []

for sample in samples:
    print(sample)
    try:
        trees, nfiles = lrdf.build_dataframe(config_dir, version, sample, R, "root", keep_negative_weights) # ROOT RDF "interactive"
    except Exception as e:
        print("Error!", e)
        exit(1)

    for tree, nfile in zip(trees,nfiles):
        joblist.append((tree,nfile))
        
######## Now sort by number of files
jobslist = sorted(joblist, key=lambda v: v[1], reverse=True)

# ########
# dfs = {}
# for tree,_ in jobslist:
#     print("\n\n>>>> Working on tree: ", tree.name)
#     if args.debug: print(tree)

#     df = pd.DataFrame(tree[cut].rdf_node.AsNumpy(columns=output_columns))
#     print("Output array: ", tree.name, df.shape)
    
#     if tree.name in dfs:
#         df.to_pickle(os.path.join(output_dir, tree.name + "_part{}.pkl".format(dfs[tree.name]+1)))
#         dfs[tree.name] +=1
#     else:
#         df.to_pickle(os.path.join(output_dir, tree.name +"_part1.pkl"))
#         dfs[tree.name] =1
        

# print("DONE!")
