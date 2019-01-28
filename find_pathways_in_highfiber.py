#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import metquest
from collections import Counter
import os
import gzip
import pickle

def find_pathways_in_highfiber(graphname, seed_mets_nonmodel):
    print(graphname)
    filename = path_name +  graphname
    G = nx.read_gpickle(filename)
    path_name_to_write = '/data/Aarthi/raborgs/pathway_analysis_raborgs_highfiberdiet_jan32019/'
    seed_mets = set([])
    splitfilenames = graphname.split('-twopple-')
    graphname1 = splitfilenames[0]
    graphname2 = splitfilenames[1].split('.gpickle')[0]
    for mets in seed_mets_nonmodel:
        #seed_mets.add(mets)
        renamed_seedmets_1 = graphname1 + ' ' + mets
        renamed_seedmets_2 = graphname2 + ' ' + mets
        seed_mets.add(renamed_seedmets_1)
        seed_mets.add(renamed_seedmets_2)
    path_len_cutoff = 30
    pathway_table, cyclic_pathways, scope = metquest.find_pathways(G, seed_mets, path_len_cutoff)
    ptable_fname = graphname1 + '-twopple-' + graphname2 + '.pickle'
    with gzip.open(path_name_to_write + ptable_fname, 'wb') as f:
        pickle.dump(pathway_table, f)

path_name = '/data/Aarthi/raborgs/rab_combined_graphs/'
with open('high_fiber_seed.txt', 'r') as f:
    seed_mets_nonmodel = f.read().splitlines()
for graphname in os.listdir(path_name):
    if graphname.endswith('.gpickle'):
        find_pathways_in_highfiber(graphname, seed_mets_nonmodel)
