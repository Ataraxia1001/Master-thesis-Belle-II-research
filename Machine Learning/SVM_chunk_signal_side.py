#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import pandas as pd
from root_pandas import read_root

import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn import metrics
from sklearn.metrics import roc_curve, auc

from sklearn.model_selection import train_test_split



from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import roc_auc_score
from sklearn.metrics import plot_roc_curve

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Binarizer

from sklearn.inspection import permutation_importance
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

import seaborn as sns


# In[4]:


print('The scikit-learn version is {}.'.format(sklearn.__version__))


# In[5]:


#sig_nochunk = read_root('merged_1000_sig.root')
#uu = read_root('merged_1000_uu.root')
#dd = read_root('merged_1000_dd.root')
#ss = read_root('merged_1000_ss.root')
#cc = read_root('merged_1000_cc.root')
#charged = read_root('merged_1000_charged.root')
#mixed = read_root('merged_1000_mixed.root')
#print(sig_nochunk.columns.values)


# In[6]:


ML_columns_tag= [
    'Bsig_d0_roeE','Bsig_d0_nROE_ECLClusters_cleanMask',
   'Bsig_d0_R2',
  'Bsig_d0_missingMomentumOfEvent',
    'Bsig_d0_missingEnergyOfEventCMS',
    'missingMass2OfEvent', 'roeEextra__bo__bc', #'roeEextra__bocleanMask__bc',
    'Bsig_d0_roeNeextra_cleanMask',
    'Bsig_d0_nROE_Tracks_cleanMask',
 #'Bsig_d0_nROE_Charged_cleanMask','Bsig_d0_roeP'

    'Bsig_d0_roeM', 'Bsig_d0_roeMbc',  'Bsig_d0_nTracks', #'Bsig_d0_nROE_Tracks' ,'Bsig_d0_nROE_Charged',
 #'Bsig_d0_nROE_RemainingTracks',
    'Bsig_d0_nROE_ECLClusters',
 'Bsig_d0_nROE_KLMClusters', 'Bsig_d0_roeE_cleanMask', 'Bsig_d0_roeM_cleanMask'

]

# In[7]:


sig_chunk = read_root(
    ['merged_1000_final_sig.root'], columns=ML_columns_tag, chunksize=10000
)
uu_chunk = read_root(
    ['merged_1000_final_uu.root'], columns=ML_columns_tag, chunksize=100000
)
dd_chunk = read_root(
    ['merged_1000_final_dd.root'], columns=ML_columns_tag, chunksize=100000
)
ss_chunk = read_root(
    ['merged_1000_final_ss.root'], columns=ML_columns_tag, chunksize=100000
)
cc_chunk = read_root(
    ['merged_1000_final_cc.root'], columns=ML_columns_tag, chunksize=100000
)
charged_chunk = read_root(
    ['merged_1000_final_charged.root'], columns=ML_columns_tag, chunksize=100000
)
mixed_chunk = read_root(
    ['merged_1000_final_mixed.root'], columns=ML_columns_tag, chunksize=100000
)


# In[8]:


sig_list = []
for chunk in sig_chunk:
    sig_list.append(chunk)
sig = pd.concat(sig_list)


uu_list = []
for chunk in uu_chunk:
    uu_list.append(chunk)
uu = pd.concat(uu_list)

dd_list = []
for chunk in dd_chunk:
    dd_list.append(chunk)
dd = pd.concat(dd_list)


ss_list = []
for chunk in ss_chunk:
    ss_list.append(chunk)
ss = pd.concat(ss_list)


cc_list = []
for chunk in cc_chunk:
    cc_list.append(chunk)
cc = pd.concat(cc_list)


charged_list = []
for chunk in charged_chunk:
    charged_list.append(chunk)
charged = pd.concat(charged_list)


mixed_list = []
for chunk in mixed_chunk:
    mixed_list.append(chunk)
mixed = pd.concat(mixed_list)


# In[9]:


sig


# In[10]:


frames = [uu, dd, ss, cc, charged, mixed]
bkg = pd.concat(frames, keys=['uu', 'dd', 'ss', 'cc', 'charged', 'mixed'])


# In[11]:


bkg


# In[12]:


## Use only fraction of data frame
shuffled = sig.sample(frac=1)   # shuffle the rows of dataframe
sig_frac = np.array_split(shuffled, 10)  # split it into n dataframes
sig_frac[0]  # choose first array with 0


# In[13]:



shuffled = bkg.sample(frac=1) # shuffle the rows of dataframe
bkg_frac = np.array_split(shuffled, 10)  # split it into n dataframes
bkg_frac[0] # choose first array with 0


# In[ ]:





# In[14]:


sig_drop = sig_frac[0].dropna()
bkg_drop = bkg_frac[0].dropna()
bkg_drop


# In[15]:


frames_all = [sig, uu, dd, ss, cc, charged, mixed]
all_com = pd.concat(frames_all, keys=['sig', 'uu', 'dd', 'ss', 'cc', 'charged', 'mixed'])


# In[16]:


f = plt.figure(figsize=(30, 30))
plt.matshow(all_com.corr(), fignum=f.number)
plt.xticks(range(all_com.select_dtypes(['number']).shape[1]), all_com.select_dtypes(['number']).columns, fontsize=14, rotation=45)
plt.yticks(range(all_com.select_dtypes(['number']).shape[1]), all_com.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=10)
#plt.title('Correlation Matrix', fontsize=16);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[73]:


sig_drop


# In[74]:


list_values =  sig_drop.values.tolist()
list_values_bkg =  bkg_drop.values.tolist()

#add bkg in sig list_values
list_values.extend(list_values_bkg)


# In[75]:


len(sig_drop)


# In[76]:


sig_can = len(sig_drop)
sig_can

# In[77]:


bkg_can = len(bkg_drop)
bkg_can


# In[78]:



label = []
for i in range(sig_can):
    label.append(1)


for i in range(bkg_can):
    label.append(0)



# In[79]:


len(label)


# In[80]:


len(list_values)


# In[81]:


list_values_train, list_values_test, label_train, label_test = train_test_split(list_values, label, test_size=0.25)


# In[82]:


##########################################################################
# SVM fit
clf_initial = SVC()
clf_initial.fit(list_values_train, label_train)
label_score = clf_initial.fit(list_values_train, label_train).decision_function(list_values_test)


# In[83]:


clf_initial.get_params()
 #{'C': 1.0,
 #'break_ties': False,
 #'cache_size': 200,
 #'class_weight': None,
 #'coef0': 0.0,
 #'decision_function_shape': 'ovr',
 #'degree': 3,
 #'gamma': 'scale',
 #'kernel': 'rbf',
 #'max_iter': -1,
 #'probability': False,
 #'random_state': None,
 #'shrinking': True,
 #'tol': 0.001,
 #'verbose': False}


# In[84]:


##############################################################################################################
# AUC score from prediction score:
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
roc_auc_score(label_train, clf_initial.decision_function(list_values_train))
#0.9961601363447251


# In[85]:


score = clf_initial.score(list_values_train, label_train)
score
#.9995400894931149

# score and AUC score are different!!


# In[86]:


plot_roc_curve(clf_initial, list_values_test, label_test)


# In[87]:


# Combilne multiple ROC curves
plt.figure()
test_roc = plot_roc_curve(clf_initial, list_values_test, label_test)
plot_roc_curve(clf_initial, list_values_train, label_train, ax=test_roc.ax_);
plt.title('ROC curve test and train')
plt.show()


# In[88]:


label_score.shape
#(1328520,)


# In[89]:


label_score
#array([-4.40926997, -6.19161143, -5.31994299, ..., -3.49443269,
    #   -3.94563064, -4.64976888])


# In[90]:


clf_initial.score(list_values_train, label_train)
#0.9995400894931149


# In[91]:


############################################################################################
############################################################################################
# Permutation feature importance
#https://scikit-learn.org/stable/modules/permutation_importance.html


# In[92]:


#r = permutation_importance(clf_initial, list_values_test, label_test,
#                           n_repeats=30,
#                            random_state=0)
#r


# In[93]:


#r.importances_mean


# In[94]:


# https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py
#sorted_idx = r.importances_mean.argsort()
#sorted_idx


# In[ ]:





# In[95]:


#df_list_values_test = pd.DataFrame(list_values_test, columns =ML_columns_tag)
#df_list_values_test

# feature of importance in test set

r_test = permutation_importance(
    clf_initial, list_values_test, label_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx = r_test.importances_mean.argsort()

fig, ax = plt.subplots()
ax.boxplot(
    r_test.importances[sorted_idx].T, vert=False, labels=sig_drop.columns[sorted_idx]
)

ax.set_title("Permutation Importances (test set)")
fig.tight_layout()
plt.show()


# In[96]:



# feature of importance in train set
r_train = permutation_importance(
    clf_initial, list_values_train, label_train, n_repeats=10, random_state=42, n_jobs=2
)

sorted_idx2 = r_train.importances_mean.argsort()

fig, ax = plt.subplots()
ax.boxplot(
    r_train.importances[sorted_idx2].T, vert=False, labels=sig_drop.columns[sorted_idx2]
)

ax.set_title("Permutation Importances (train set)")
fig.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
