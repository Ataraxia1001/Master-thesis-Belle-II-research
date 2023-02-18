#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wg1template
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

import wg1template.histogram_plots as wg1
import wg1template.point_plots as points
from wg1template.plot_style import TangoColors
from wg1template.plot_utilities import export

import pandas as pd
from root_pandas import read_root
import math


# In[2]:


#sig = read_root('sig_best.root')
#bkg = read_root('bkg_best.root')


# In[2]:


sig = read_root('merged_precut_final_sig.root')
uu = read_root('merged_precut_final_uu.root')
dd = read_root('merged_precut_final_dd.root')
ss = read_root('merged_precut_final_ss.root')
cc = read_root('merged_precut_final_cc.root')
charged = read_root('merged_precut_final_charged.root')
mixed = read_root('merged_precut_final_mixed.root')


# In[3]:


frames = [uu, dd, ss, cc, charged, mixed]
bkg = pd.concat(frames, keys=['uu', 'dd', 'ss', 'cc', 'charged', 'mixed'])


# In[4]:


print(uu.columns.values)


# In[7]:


sig['isNotContinuumEvent']


# In[31]:


sig['isSignal']


# In[8]:


sig['isNotContinuumEvent'].value_counts() 


# In[13]:


mixed['isNotContinuumEvent'].value_counts() 


# In[9]:


sig['isSignal'].value_counts() 


# In[11]:


sig['Btag_d1_isSignal'].value_counts() 


# In[12]:


sig['Bsig_d0_isSignal'].value_counts() 


# In[ ]:





# In[10]:


sig_1 = sig.query("Bsig_d0_isSignal > 0.5") #& Btag_d1_isSignal > 0.5
len(sig_1)


# In[6]:


print(uu.columns.values)


# In[22]:


var1 = wg1.HistVariable("Bsig_d0_roeEextra_cleanMask",
                             n_bins=50,
                             scope=(0, 8),
                             var_name="Bsig_d0_roeEextra_cleanMask")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[14]:



var1 = wg1.HistVariable("Bsig_d0_roeMbc",
                             n_bins=30,
                             scope=(5, 5.3),
                             var_name="Bsig_d0_roeMbc")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[27]:



var1 = wg1.HistVariable("Btag_d1_harmonicMomentThrust1",
                             n_bins=30,
                             scope=(-1, 1),
                             var_name="Btag_d1_harmonicMomentThrust1")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[30]:


var1 = wg1.HistVariable("Btag_d1_harmonicMomentThrust",
                             n_bins=30,
                             scope=(-1, 1),
                             var_name="Btag_d1_harmonicMomentThrust4")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[8]:


var1 = wg1.HistVariable("Bsig_d0_R2",
                             n_bins=30,
                             scope=(-3, 1),
                             var_name="Bsig_d0_R2")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[9]:


var1 = wg1.HistVariable("Btag_d1_KSFWVariables_hso00",
                             n_bins=30,
                             scope=(-3, 1),
                             var_name="Btag_d1_KSFWVariables_hso00")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[ ]:





# In[10]:


sig


# In[38]:


test = read_root('test-ltmva.root')
test['isNotContinuumEvent'].value.counts()


# In[45]:


test['isNotContinuumEvent'].value_counts()


# In[46]:


test['Btag_d1_isSignal'].value_counts()


# In[47]:


sig['Btag_d1_isSignal'].value_counts()


# In[48]:


bkg['Btag_d1_isSignal'].value_counts()


# In[42]:


test['Btag_d1_isSignal'].value.counts()
#test_cut = sig.query("Btag_d1_isSignal > 0.5")


# In[49]:


test


# In[32]:


expert = read_root('expert_tag.root')


# In[33]:


expert


# In[51]:


test_fbdt= pd.concat([test, expert.reindex(test.index)], axis=1)
test_fbdt


# In[ ]:


test_fbdt = sig.query("Btag_d1_isSignal > 0.5 & ")


# In[35]:


sig['isNotContinuumEvent']


# In[36]:


bkg['isNotContinuumEvent']


# In[12]:


purity = len(sig) / (len(sig) + len(bkg))
purity


# In[ ]:





# In[13]:


var1 = wg1.HistVariable("Btag_FEIProbabilityRank",
                             n_bins=15,
                             scope=(0, 8),
                             var_name="Btag_FEIProbabilityRank")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[14]:


var1 = wg1.HistVariable("nParticlesInList__boUpsilon__bo4S__bc__claftercut__bc",
                             n_bins=20,
                             scope=(0, 9),
                             var_name="nParticlesInList(Upsilon(4S))")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[15]:


var1 = wg1.HistVariable("__ncandidates__",
                             n_bins=20,
                             scope=(0, 9),
                             var_name="__ncandidates__")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu, weights=uu.__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd, weights=dd.__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss, weights=ss.__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc, weights=cc.__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed, weights=mixed.__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged, weights=charged.__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig, weights=sig.__weight__ ,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[16]:


idx = sig.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == sig['Btag_FEIProbabilityRank']


# In[17]:


sig_best= sig[idx]
sig_best


# In[18]:


idx_bkg = bkg.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == bkg['Btag_FEIProbabilityRank']


# In[19]:


bkg_best = bkg[idx_bkg]
bkg_best


# In[20]:


purity = len(sig_best) / (len(sig_best) + len(bkg_best))
purity


# In[ ]:





# In[21]:


#from root_pandas import readwrite
#sig_best.to_root("sig_best.root") # These are input file in fBDT.
#bkg_best.to_root("bkg_best.root")


# In[22]:


#'Btag_d1_R2' 'Btag_d1_thrustBm' 'Btag_d1_thrustOm'
# 'Btag_d1_cosTBTO' 'Btag_d1_cosTBz' 'Btag_d1_KSFWVariables_hso00'
# 'Btag_d1_KSFWVariables_hso01' 'Btag_d1_KSFWVariables_hso02'
# 'Btag_d1_KSFWVariables_hso03' 'Btag_d1_KSFWVariables_hso04'
# 'Btag_d1_KSFWVariables_hso10' 'Btag_d1_KSFWVariables_hso12'
# 'Btag_d1_KSFWVariables_hso14' 'Btag_d1_KSFWVariables_hso20'
# 'Btag_d1_KSFWVariables_hso22' 'Btag_d1_KSFWVariables_hso24'
# 'Btag_d1_KSFWVariables_hoo0' 'Btag_d1_KSFWVariables_hoo1'
# 'Btag_d1_KSFWVariables_hoo2' 'Btag_d1_KSFWVariables_hoo3'
# 'Btag_d1_KSFWVariables_hoo4' 


# In[23]:


idx_uu = uu.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == uu['Btag_FEIProbabilityRank']
idx_dd = dd.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == dd['Btag_FEIProbabilityRank']
idx_ss = ss.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == ss['Btag_FEIProbabilityRank']
idx_cc = cc.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == cc['Btag_FEIProbabilityRank']
idx_mixed = mixed.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == mixed['Btag_FEIProbabilityRank']
idx_charged = charged.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == charged['Btag_FEIProbabilityRank']


# In[35]:


var1 = wg1.HistVariable("Btag_d1_KSFWVariables_hso00",
                             n_bins=50,
                             scope=(0, 1.75),
                             var_name="Btag_d1_KSFWVariables_hso00")


hp1 = wg1.StackedHistogramPlot(var1)
hp1.add_component("uubar", uu[idx_uu], weights=uu[idx_uu].__weight__, color=TangoColors.slate,
                  comp_type='stacked')
hp1.add_component("ddbar", dd[idx_dd], weights=dd[idx_dd].__weight__, color=TangoColors.sky_blue,
                  comp_type='stacked')
hp1.add_component("ssbar", ss[idx_ss], weights=ss[idx_ss].__weight__, color=TangoColors.orange,
                  comp_type='stacked')
hp1.add_component("ccbar", cc[idx_cc], weights=cc[idx_cc].__weight__, color=TangoColors.chameleon,
                  comp_type='stacked')
#hp1.add_component("taupair", tau, weights=tau.__weight__, color=TangoColors.aluminium,
#                  comp_type='stacked')
hp1.add_component("mixed", mixed[idx_mixed], weights=mixed[idx_mixed].__weight__, color=TangoColors.butter,
                  comp_type='stacked')
hp1.add_component("charged", charged[idx_charged], weights=charged[idx_charged].__weight__, color=TangoColors.plum,
                  comp_type='stacked')

hp2 = wg1.SimpleHistogramPlot(var1)
hp2.add_component("Signal", sig[idx], weights=sig[idx].__weight__,
                  color=TangoColors.scarlet_red, ls='-.')

fig, ax = wg1.create_solo_figure()
hp1.plot_on(ax, ylabel="Candidates")
hp2.plot_on(ax, hide_labels=True)  # Hide labels to prevent overrides)

plt.show()
export(fig, 'combo', 'examples')
plt.close()


# In[ ]:





# In[ ]:





# In[ ]:




