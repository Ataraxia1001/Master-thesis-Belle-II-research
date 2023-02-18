#!/usr/bin/env python
# coding: utf-8

# In[24]:


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

from sklearn.neural_network import MLPClassifier


# In[2]:

# In[4]:


print('The scikit-learn version is {}.'.format(sklearn.__version__))


# In[5]:


sig_nochunk = read_root('merged_1000_sig.root')
#uu = read_root('merged_1000_uu.root')
#dd = read_root('merged_1000_dd.root')
#ss = read_root('merged_1000_ss.root')
#cc = read_root('merged_1000_cc.root')
#charged = read_root('merged_1000_charged.root')
#mixed = read_root('merged_1000_mixed.root')
print(sig_nochunk.columns.values)


# In[6]:


ML_columns_tag= [
   'Bsig_d0_R2', #'Bsig_d0_thrustBm',
  'Bsig_d0_missingMomentumOfEvent',
    'Bsig_d0_missingEnergyOfEventCMS',
    'missingMomentumOfEvent',
    'missingMass2OfEvent', 'roeEextra__bo__bc', 'roeEextra__bocleanMask__bc','Bsig_d0_roeNeextra_cleanMask',
    'Bsig_d0_nROE_Tracks_cleanMask',
 'Bsig_d0_nROE_Charged_cleanMask', 'Bsig_d0_nROE_ECLClusters_cleanMask',
    'Bsig_d0_roeE', 'Bsig_d0_roeM', 'Bsig_d0_roeP', 'Bsig_d0_roeMbc',  'Bsig_d0_nTracks', 'Bsig_d0_nROE_Tracks' ,'Bsig_d0_nROE_Charged',
 'Bsig_d0_nROE_RemainingTracks', 'Bsig_d0_nROE_ECLClusters',
 'Bsig_d0_nROE_KLMClusters', 'Bsig_d0_roeE_cleanMask', 'Bsig_d0_roeM_cleanMask'

]


# In[ ]:





# In[7]:


sig_chunk = read_root(
    ['merged_1000_sig.root'], columns=ML_columns_tag, chunksize=100000
)
uu_chunk = read_root(
    ['merged_1000_uu.root'], columns=ML_columns_tag, chunksize=100000
)
dd_chunk = read_root(
    ['merged_1000_dd.root'], columns=ML_columns_tag, chunksize=100000
)
ss_chunk = read_root(
    ['merged_1000_ss.root'], columns=ML_columns_tag, chunksize=100000
)
cc_chunk = read_root(
    ['merged_1000_cc.root'], columns=ML_columns_tag, chunksize=100000
)
charged_chunk = read_root(
    ['merged_1000_charged.root'], columns=ML_columns_tag, chunksize=100000
)
mixed_chunk = read_root(
    ['merged_1000_mixed.root'], columns=ML_columns_tag, chunksize=100000
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
# https://stackoverflow.com/questions/54730276/how-to-randomly-split-a-dataframe-into-several-smaller-dataframes

shuffled = sig.sample(frac=1)   # shuffle the rows of dataframe
sig_frac = np.array_split(shuffled, 100)  # split it into n dataframes
sig_frac[0]  # choose first array with 0


# In[13]:


## Use only fraction of data frame
shuffled = bkg.sample(frac=1) # shuffle the rows of dataframe
bkg_frac = np.array_split(shuffled, 100)  # split it into n dataframes
bkg_frac[0] # choose first array with 0


# In[14]:


sig_drop = sig_frac[0].dropna()
bkg_drop = bkg_frac[0].dropna()
bkg_drop


# In[15]:


sig_drop


# In[16]:


list_values =  sig_drop.values.tolist()
list_values_bkg =  bkg_drop.values.tolist()

#add bkg in sig list_values
list_values.extend(list_values_bkg)


# In[17]:


sig_can = len(sig_drop)
sig_can


# In[18]:


bkg_can = len(bkg_drop)
bkg_can


# In[19]:



label = []
#label signal: 49696
for i in range(sig_can):
    label.append(1)


for i in range(bkg_can):
    label.append(0)



# In[20]:


len(label)


# In[21]:


len(list_values)


# In[22]:


list_values_train, list_values_test, label_train, label_test = train_test_split(list_values, label, test_size=0.25)


# In[26]:


##########################################################################
# MLP fit
clf_initial = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(15,), random_state=1, alpha=1)
clf_initial.fit(list_values_train, label_train)
#label_score = clf_initial.fit(list_values_train, label_train).decision_function(list_values_test)


# In[27]:


clf_initial.get_params()
#{'activation': 'relu',
#'alpha': 1,
#'batch_size': 'auto',
#'beta_1': 0.9,
#'beta_2': 0.999,
#'early_stopping': False,
#'epsilon': 1e-08,
#'hidden_layer_sizes': (15,),
#'learning_rate': 'constant',
#'learning_rate_init': 0.001,
#'max_fun': 15000,
#'max_iter': 200,
#'momentum': 0.9,
#'n_iter_no_change': 10,
#'nesterovs_momentum': True,
#'power_t': 0.5,
#'random_state': 1,
#'shuffle': True,
#'solver': 'lbfgs',
#'tol': 0.0001,
#'validation_fraction': 0.1,
#'verbose': False,
#'warm_start': False}


# In[28]:


##############################################################################################################
# AUC score from prediction scpre:
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
roc_auc_score(label_train, clf_initial.decision_function(list_values_train))


# In[29]:


score = clf_initial.score(list_values_train, label_train)
score
#0.9976852428006073
# score and AUC score are different.

# In[30]:


plot_roc_curve(clf_initial, list_values_test, label_test)


# In[31]:


label_score.shape


# In[32]:


label_score


# In[33]:


clf_initial.score(list_values_train, label_train)
#0.9976852428006073


# In[34]:


############################################################################################
############################################################################################
# Permutation feature importance
#https://scikit-learn.org/stable/modules/permutation_importance.html


# In[35]:


#r = permutation_importance(clf_initial, list_values_test, label_test,
#                           n_repeats=30,
#                            random_state=0)
#r


# In[36]:


#r.importances_mean


# In[37]:


# https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py
#sorted_idx = r.importances_mean.argsort()
#sorted_idx


# In[ ]:





# In[38]:


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


# In[39]:



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


C_range = [1e-2, 1e-1, 1, 3, 5, 10, 100,200, 300]
gamma_range = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2,1e-1,1]

classifiers = []
C_data=[]
gamma_data=[]
score_data=[]
for C in C_range:
    for gamma in gamma_range:
        clf = SVC(C=C, gamma=gamma)
        clf.fit(list_values_train, label_train)
        score = clf.score(list_values_train, label_train)
        classifiers.append((C, gamma, score))
        C_data.append(C)
        gamma_data.append(gamma)
        score_data.append(score)


# In[ ]:


print(gamma_data)


# In[ ]:


df = pd.DataFrame(list(zip(C_data, gamma_data, score_data)),
               columns =['C', 'gamma', 'score'])


# In[ ]:


df


# In[ ]:


result = df.pivot(index='C', columns='gamma', values='score')
result


# In[ ]:


# parameter optimization
sns.heatmap(result, annot=True)


# In[ ]:


#svc_disp = RocCurveDisplay.from_estimator(classifier, Upsilon_list_test, label_test)
#plt.show()
