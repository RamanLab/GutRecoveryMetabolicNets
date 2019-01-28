#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:25:49 2018

@author: aarthi
"""

import pickle
import os
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# single_org_file_name = "/home/aarthi/agora_analysis/results/scope_single_orgs.txt"
#single_org_file_name = "/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/Rest/rab_organisms_in_agora_subspeciesID.txt"
single_org_file_name = "C:\\Users\\Aarthi\\Dropbox\\MetQuest_applications\\Fourth_objective\\RABOrganisms\\Rest\\rab_organisms_in_agora_subspeciesID_phylagrouped_fullname.txt" #rab_organisms_in_agora_subspeciesID.txt" #graph_based_anlayses\\scope_analysis\\single\\"
#pair_org_folder_name = "/home/aarthi/Desktop/scope_pair/"
# pair_org_folder_name = "/data/Aarthi/Agora/scope_pair_results/" #"/data/Aarthi/Agora/scope_pair_results/"
#  Since they are single files with values for a particular combination only

with open(single_org_file_name, 'r') as f:
    all_data = f.read().splitlines()

org_names = []
for entries in all_data:
    org_names.append(entries.split(' ')[0])

org_names_without_sp = []
for org in org_names:
    org_names_without_sp.append(org.split('_')[0] + ' ' + org.split('_')[1])
row_names_wosp = pd.Index(org_names_without_sp, name='organism')
column_names_wosp = pd.Index(org_names_without_sp, name='in the presence of')

row_names = pd.Index(org_names, name='organism')
column_names = pd.Index(org_names, name='in the presence of')

df = pd.DataFrame(index=row_names, columns=column_names)
df_diagval = pd.DataFrame(index=row_names, columns=column_names)
#With numbers of scope metabolites
#path_name_to_read = '/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/scope_analysis/single/'
path_name_to_read = 'C:\\Users\\Aarthi\\Dropbox\\MetQuest_applications\\Fourth_objective\\RABOrganisms\\graph_based_anlayses\\scope_analysis\\single\\windowsminglucose\\'
filename_to_read_combined = path_name_to_read + 'scope_combined_orgs_minglucose.txt' #scope_combined_orgs_highfiberdiet
with open(filename_to_read_combined, 'r') as f:
    scope_data = f.read().splitlines()
for entries in scope_data:
    if 'twopple' in entries:
        splitentries = entries.split('\t')
        orgnames = splitentries[0].split('-twopple-')
        df.at[orgnames[0],orgnames[1]] = int(splitentries[1])
        df.at[orgnames[1],orgnames[0]] = int(splitentries[2])
filename_to_read_single = path_name_to_read + 'scope_single_orgs_v2_minglucose.txt'

with open(filename_to_read_single, 'r') as f:
    scope_data_single = f.read().splitlines()
diagvalues = []
for entries in scope_data_single:
    currentent = entries.split('\t')
    df.at[currentent[0], currentent[0]] = int(currentent[1])
    diagvalues.append(int(currentent[1]))
df.to_csv('rabscope_minglucose_windows.csv')
diff_only_num = df - df.T
diff_only_num.to_csv('increase_in_scope_minglucose_windows.csv')

for entries in scope_data:
    if 'twopple' in entries:
        splitentries = entries.split('\t')
        orgnames = splitentries[0].split('-twopple-')
        df_diagval.at[orgnames[0], orgnames[0]] = df.at[orgnames[0], orgnames[0]]
        df_diagval.at[orgnames[0], orgnames[1]] = df.at[orgnames[0], orgnames[0]]
        df_diagval.at[orgnames[1], orgnames[0]] = df.at[orgnames[1], orgnames[1]]
        #df_diagval.at[orgnames[1], orgnames[0]] = df.at[orgnames[1], orgnames[1]]


#With metabolites in scope
df4_metmap = pd.DataFrame(index=row_names, columns=column_names)
df4_metmap= df4_metmap.astype('object')

#path_name_to_read = '/home/aarthi/Dropbox/metquest_applications/Fourth_objective/RABOrganisms/graph_based_anlayses/scope_analysis/single/'
filename_to_read_combined = path_name_to_read + 'scope_combined_orgs_withmetas_minglucose.txt'
with open(filename_to_read_combined, 'r') as f:
    scope_data_withmetnames = f.read().splitlines()

for entries in scope_data_withmetnames:
    if 'twopple' in entries:
        splitentries = entries.split('\t')
        orgnames = splitentries[0].split('-twopple-')
        df4_metmap.at[orgnames[0],orgnames[1]] = set(splitentries[1].split())
        df4_metmap.at[orgnames[1],orgnames[0]] = set(splitentries[2].split())

filename_to_read_single = path_name_to_read + 'scope_single_orgs_withmetnames_v2_minglucose.txt'
with open(filename_to_read_single, 'r') as f:
    scope_data_single_withmetnames = f.read().splitlines()

for entries in scope_data_single_withmetnames:
    currentent = entries.split('\t')
    df4_metmap.at[currentent[0], currentent[0]] = set(currentent[1])

#diff_mat_met = df4_metmap - df4_metmap.T
#diff_mat_met = df - df.T
diff_mat_num = df - df_diagval
diff_mat_num.to_csv('difference_in_scope_internal_mets_windows_minglucose.csv')
#entries_in_df = list(df.index)
diff_mat_without_sp_name = pd.DataFrame(index=row_names_wosp, columns=column_names_wosp)
diff_mat_num_without_sp_name = pd.DataFrame(index=row_names_wosp, columns=column_names_wosp)

for ele in diff_mat_num:
    for keys in diff_mat_num[ele].keys():
        if ele!= keys:
            #print(ele)
            keys1 = keys.split('_')[0] + ' ' + keys.split('_')[1]
            ele1 = ele.split('_')[0] + ' ' + ele.split('_')[1]
            diff_mat_without_sp_name[ele1][keys1] = diff_mat_num[ele][keys]
            diff_mat_num_without_sp_name[ele1][keys1] = diff_mat_num[ele][keys]

        elif ele == keys:
            print(ele)
            ele1 = ele.split('_')[0] + ' ' + ele.split('_')[1]
            keys1 = keys.split('_')[0] + ' ' + keys.split('_')[1]
            diff_mat_without_sp_name[ele1][keys1] = '-'
            diff_mat_num_without_sp_name[ele1][keys1]= 0


plt.figure(figsize=(50,50))
plt.subplots_adjust(bottom=0.43)
#plt.xticks(style='italic',size='large')
#plt.yticks(style='italic',size='large')
#
#diff_mat_without_sp_name = diff_mat_without_sp_name.fillna(0)
#diff_mat_num = diff_mat_num.fillna(0)
#diff_mat_num_without_sp_name = diff_mat_num_without_sp_name.fillna(0)
#j = sns.heatmap(diff_mat_num_without_sp_name, fmt = '', annot = diff_mat_without_sp_name, cmap="Blues", square=True,annot_kws={"size": 15}) #,PiYG ) #, metric="correlation", standard_scale=1) #,vmin=0,annot= True, linewidths = 20.0) #, square = True, cbar = False)
#plt.title('Increase in the metabolic capabilites of the organism in minimal glucose medium')
#for x, idx in enumerate(entries_in_df):
plt.xticks(style='italic', weight= 'bold',size='medium')
plt.yticks(style='italic', weight='bold',size='medium')
#colors =['r','r','b','b','b','b','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta','magenta']
sns.set(font_scale=1)
diff_mat_without_sp_name = diff_mat_without_sp_name.fillna(0)
diff_mat_num = diff_mat_num.fillna(0)
diff_mat_num_without_sp_name = diff_mat_num_without_sp_name.fillna(0)
j = sns.heatmap(diff_mat_num_without_sp_name, fmt = '', annot = diff_mat_without_sp_name, cmap="Blues", square=True,annot_kws={"size": 18}) #,PiYG ) #, metric="correlation", standard_scale=1) #,vmin=0,annot= True, linewidths = 20.0) #, square = True, cbar = False)
plt.title('Increase in the metabolic capabilites of the organism in minimal glucose medium', weight= 'bold',size='x-large')
#plt.title('Heatmap of the Metabolic Support Index (MSI) on minimal glucose medium',
colors = ['magenta','magenta','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','indigo','teal','teal','teal','teal','teal','teal','teal','teal']
ax = plt.subplot()
for xtick,colortech in zip(ax.get_xticklabels(),colors):
    plt.setp(xtick, color=colortech)
for ytick,colortech in zip(ax.get_yticklabels(),colors):
    plt.setp(ytick, color=colortech)
plt.ylabel('(organism)', weight= 'bold',size='x-large')
plt.xlabel('(in the presence of)', weight= 'bold',size='x-large')
plt.savefig('ScopeIncreaseinminimalglucose_Phylagrouped.pdf')
