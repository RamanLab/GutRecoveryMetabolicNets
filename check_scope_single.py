#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 12:42:35 2018

@author: aarthi
"""

import networkx as nx
import metquest
from collections import Counter
import os
import pdb
import pickle
#import re
#from joblib import Parallel, delayed


def check_scope(graphname, seed_mets_nonmodel):
    print(graphname)
    filename = path_name +  graphname
    G = nx.read_gpickle(filename)
    #pdb.set_trace()
    #path_name_to_write = '/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/scope_analysis/single/ubunturepeathighfiber/'
    path_name_to_write = 'C:\\Users\\Aarthi\\Dropbox\\MetQuest_applications\\Fourth_objective\\RABOrganisms\\graph_based_anlayses\\scope_analysis\\single\\windowsminglucose\\'

    seed_mets = set([])
    splitfilenames = graphname.split('_.gpickle')[0] + ' '
    for mets in seed_mets_nonmodel:
        renamed_seedmets_1 = splitfilenames + mets
        seed_mets.add(renamed_seedmets_1)
    lowerboundmet, status_dict, scope = metquest.forward_pass(G, seed_mets)
    graphname_split = graphname.split('_.gpickle')[0]
    metsproducedbyfirst = []
    for mets in scope:
        if mets not in seed_mets:
            if graphname_split in mets:
                metsproducedbyfirst.append(mets)
    scope_fname = graphname + '_scope_single' + '.pickle'
    with open(scope_fname, 'wb') as f:
        pickle.dump(metsproducedbyfirst, f)
#    filename_to_write = path_name_to_write + 'scope_single_orgs_v2_minglucose' + '.txt'
##    print(len(scope), len(seed_mets), len(set(seed_mets_nonmodel)), len(metsproducedbyfirst))
#    filename_to_write_withmetnames = path_name_to_write + 'scope_single_orgs_withmetnames_v2_minglucose' + '.txt'
#
#    with open(filename_to_write_withmetnames,'a') as f:
#        strtowrite2 = graphname.split('_.gpickle')[0] + '\t' + ','.join(metsproducedbyfirst)
#        f.write(strtowrite2)
#        f.write('\n')
#    with open(filename_to_write,'a') as f:
#        strtowrite2 = graphname.split('_.gpickle')[0] + '\t' + str(len(metsproducedbyfirst))
#        f.write(strtowrite2)
#        f.write('\n')
#
#path_name = '/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/single_graphs_agora101/'
#with open('/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/high_fiber_seed.txt', 'r') as f:
path_name = 'C:\\Users\\Aarthi\\Dropbox\\MetQuest_applications\\Fourth_objective\\RABOrganisms\\graph_based_anlayses\\single_graphs_agora101\\'
#with open('/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/high_fiber_seed.txt', 'r') as f:
with open('C:\\Users\\Aarthi\\Dropbox\\MetQuest_applications\\Fourth_objective\\RABOrganisms\\graph_based_anlayses\\' + 'seed_mets_minimalglucosemedium.txt', 'r') as f:
    seed_mets_nonmodel = f.read().splitlines()
single_graph_name=['Bacteroides_intestinalis_341_DSM_17393_.gpickle']
for graphname in single_graph_name: #os.listdir(path_name):
    if graphname.endswith('.gpickle'):
        check_scope(graphname,seed_mets_nonmodel)
