#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import wg1template
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


# In[4]:


sig = read_root('merged_1000_final_sig.root')
#uu = read_root('merged_1000_final_uu.root')
#dd = read_root('merged_1000_final_dd.root')
#ss = read_root('merged_1000_final_ss.root')
#cc = read_root('merged_1000_final_cc.root')
#charged = read_root('merged_1000_final_charged.root')
#mixed = read_root('merged_1000_final_mixed.root')


# In[6]:


sig['Bsig_d0_isSignal'].value_counts()


# In[7]:


sig_nokaon['Bsig_d0_isSignal'].value_counts()


# In[14]:


sig['Bsig_d0_isSignalAcceptMissingNeutrino'].value_counts()


# In[15]:


sig['Bsig_d0_isSignalAcceptMissingGamma'].value_counts()


# In[4]:


features = ['isNotContinuumEvent','Bsig_d0_isSignal', 'Btag_d1_isSignal', 'Bsig_d0_missingEnergyOfEventCMS', 'Bsig_d0_roeE',
           'Btag_d1_roeEextra_cleanMask', 'Btag_d1_Mbc',  'roeEextra__bo__bc','nROE_Tracks__bo__bc','roeP__bo__bc', 
           'roeNeextra__bo__bc', 'Bsig_d0_R2' , 'Bsig_d0_thrustOm' ,'Bsig_d0_cosTBTO',
 'Bsig_d0_cosTBz', 'Bsig_d0_KSFWVariables_hso00',
 'Bsig_d0_KSFWVariables_hso01', 'Bsig_d0_KSFWVariables_hso02',
 'Bsig_d0_KSFWVariables_hso03','Bsig_d0_KSFWVariables_hso04',
 'Bsig_d0_KSFWVariables_hso10', 'Bsig_d0_KSFWVariables_hso12',
 'Bsig_d0_KSFWVariables_hso14' ,'Bsig_d0_KSFWVariables_hso20',
 'Bsig_d0_KSFWVariables_hso22', 'Bsig_d0_KSFWVariables_hso24',
 'Bsig_d0_KSFWVariables_hoo0' ,'Bsig_d0_KSFWVariables_hoo1',
 'Bsig_d0_KSFWVariables_hoo2' ,'Bsig_d0_KSFWVariables_hoo3',
 'Bsig_d0_KSFWVariables_hoo4'  ,  'Btag_FEIProbabilityRank'
]


# In[5]:


features


# In[8]:


frames = [uu, dd, ss, cc, charged, mixed]
bkg = pd.concat(frames, keys=['uu', 'dd', 'ss', 'cc', 'charged', 'mixed'])


# In[14]:


av_groupSize_sig=4662/2677  # before cut


# In[15]:


len(sig)


# In[16]:


len(bkg)


# In[17]:


############################################################################
############################################################################
# Figure of merit


# In[18]:


sig_cut = sig.query("Bsig_d0_missingEnergyOfEventCMS > 1.85 & Bsig_d0_roeE< 8.0")
bkg_cut = bkg.query("Bsig_d0_missingEnergyOfEventCMS > 1.85 & Bsig_d0_roeE< 8.0")


# In[19]:


len(sig_cut)


# In[20]:


len(bkg_cut) 


# In[21]:


math.sqrt(len(bkg_cut))


# In[23]:


sig['Bsig_d0_isSignal'].value_counts()


# In[24]:


sig['Btag_d1_isSignal'].value_counts() 


# In[25]:


sig_both_1 = sig.query("Bsig_d0_isSignal > 0.5 & Btag_d1_isSignal > 0.5")
sig_both_1


# In[26]:


len(sig_both_1)


# In[27]:


sig_cut['Bsig_d0_isSignal'].value_counts()


# In[28]:


sig_cut['Btag_d1_isSignal'].value_counts() 


# In[30]:


eff = 7453301 / (189000 * 264) # efficiency only considering signal side
eff                            # need to eff with tag+sig side, expect under 1%
                               # ε = ε_tag(0.5) *ε_sig


# In[31]:


eff_both = len(sig_both_1) / (1000 * 264)
eff_both


# In[32]:


sig_both_cut = sig_cut.query("Bsig_d0_isSignal > 0.5 & Btag_d1_isSignal > 0.5")
eff_cut = len(sig_both_cut) / (1000 * 264)
eff_cut


# In[33]:


len(sig_both_cut)


# In[34]:


a = 3  #sigma


# In[35]:


FoM_nocut = eff_both/( (a/2) + math.sqrt(len(bkg))) 
FoM_nocut


# In[36]:


FoM = eff_cut/( (a/2) + math.sqrt(len(bkg_cut))) 
FoM


# In[40]:


############################################################################
############################################################################
# Purity


# In[41]:


purity_nocut = len(sig) / (len(sig) + len(bkg))
purity_nocut


# In[42]:


purity = len(sig_cut) / (len(sig_cut) + len(bkg_cut))
purity


# In[43]:


# Tag cut
sig_cut2 = sig_cut.query("Btag_d1_roeEextra_cleanMask < 2.5 & Btag_d1_Mbc > 5.265")
bkg_cut2 = bkg_cut.query("Btag_d1_roeEextra_cleanMask < 2.5 & Btag_d1_Mbc > 5.265")


# In[44]:


len(sig_cut2)


# In[45]:


len(bkg_cut2)


# In[46]:


sig_both_cut2 = sig_cut2.query("Bsig_d0_isSignal > 0.5 & Btag_d1_isSignal > 0.5")
eff_cut2 = len(sig_both_cut2) / (1000 * 264)


# In[47]:


FoM = eff_cut2/( (a/2) + math.sqrt(len(bkg_cut2))) 
FoM


# In[48]:


purity = len(sig_cut2) / (len(sig_cut2) + len(bkg_cut2))
purity


# In[49]:


# Upsilon cut
sig_cut3 = sig_cut2.query("roeEextra__bo__bc < 2.0 & nROE_Tracks__bo__bc < 3.0  & roeP__bo__bc < 1.5 & roeNeextra__bo__bc<2.0")  
bkg_cut3 = bkg_cut2.query("roeEextra__bo__bc < 2.0 & nROE_Tracks__bo__bc < 3.0 & roeP__bo__bc < 1.5 & roeNeextra__bo__bc<2.0") 


# In[50]:


len(sig_cut3)   # fitting after cut


# In[51]:


len(bkg_cut3)


# In[52]:


sig_both_cut3 = sig_cut3.query("Bsig_d0_isSignal > 0.5 & Btag_d1_isSignal > 0.5")
eff_cut3 = len(sig_both_cut3) / (1000 * 264)


# In[53]:


sig_cut3


# In[54]:


len(sig_both_cut3)


# In[55]:


FoM = eff_cut3/( (a/2) + math.sqrt(len(bkg_cut3))) 
FoM


# In[56]:


purity = len(sig_cut3) / (len(sig_cut3) + len(bkg_cut3))
purity


# In[59]:


group_sig_cut3 = sig_cut3.groupby(by=["__event__"])
group_bkg_cut3 = bkg_cut3.groupby(by=["__event__"])


# In[60]:


group_sig_cut3.size()


# In[61]:


group_bkg_cut3.size()


# In[62]:


len(bkg)


# In[64]:


idx = sig_cut3.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == sig_cut3['Btag_FEIProbabilityRank']


# In[65]:


sig_cut3[idx]


# In[66]:


idx_bkg = bkg_cut3.groupby(['__event__'])['Btag_FEIProbabilityRank'].transform(min) == bkg_cut3['Btag_FEIProbabilityRank']


# In[67]:


bkg_cut3[idx_bkg]


# In[68]:


purity = len(group_sig_cut3) / (len(group_sig_cut3) + len(group_bkg_cut3))
purity
# 9938/5309416 = 0.001871.  0.187% of initial bkg is left.(99.813% bkg removed)


# In[69]:


av_groupSize_sig=4662/2677 


# In[70]:


var1 = wg1.HistVariable("Btag_FEIProbabilityRank",
                             n_bins=20,
                             scope=(0, 10),
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
hp2.add_component("Signal", sig, weights=sig.__weight__ *50,
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




