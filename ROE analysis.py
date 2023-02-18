#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import wg1template
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

#import wg1template.histogram_plots as wg1
#import wg1template.point_plots as points
#from wg1template.plot_style import TangoColors
#from wg1template.plot_utilities import export
#
import pandas as pd
from root_pandas import read_root


# In[3]:


sig = read_root('merged_1000_final_sig.root')
uu = read_root('merged_1000_final_uu.root')
dd = read_root('merged_1000_final_dd.root')
ss = read_root('merged_1000_final_ss.root')
cc = read_root('merged_1000_final_cc.root')
charged = read_root('merged_1000_final_charged.root')
mixed = read_root('merged_1000_final_mixed.root')


# In[4]:


print(uu.columns.values)


# In[5]:


frames = [uu, dd, ss, cc, charged, mixed]
bkg = pd.concat(frames, keys=['uu', 'dd', 'ss', 'cc', 'charged', 'mixed'])


# In[ ]:





# In[10]:


plt.style.use('belle2')
m_bins = 10
m_range = (0, 8)
fig, ax = plt.subplots(1,2, figsize=(15, 7))
# Left subplot of ROE mass:
ax[0].hist(sig['nROE_Tracks__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].hist(sig['nROE_Tracks__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].set_xlim(m_range)
ax[0].set_xlabel('# of ROE tracks(Signal)')
ax[0].legend()
# Right subplot of number of charged ROE particles:
m_bins = 10
m_range = (-3, 15)
# Left subplot of ROE mass:
ax[1].hist(bkg['nROE_Tracks__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].hist(bkg['nROE_Tracks__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].set_xlim(m_range)
ax[1].set_xlabel('# of ROE tracks(Background)')
ax[1].legend()
fig.tight_layout()
fig.savefig('roe_mask_comparison.svg')


# In[12]:


plt.style.use('belle2')
m_bins = 50
m_range = (0, 4)
fig, ax = plt.subplots(1,2, figsize=(15, 7))
ax[0].hist(sig['roeEextra__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].hist(sig['roeEextra__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].set_xlim(m_range)
ax[0].set_xlabel('roeEextra(Signal) in GeV')
ax[0].legend()
# Right subplot of number of charged ROE particles:
m_bins = 50
m_range = (0, 8)
ax[1].hist(bkg['roeEextra__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].hist(bkg['roeEextra__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].set_xlim(m_range)
ax[1].set_xlabel('roeEextra(Background) in GeV')
ax[1].legend()
fig.tight_layout()
fig.savefig('roe_mask_comparison.svg')


# In[15]:


plt.style.use('belle2')
m_bins = 30
m_range = (0, 5)
fig, ax = plt.subplots(1,2, figsize=(15, 7))
# Left subplot of ROE mass:
ax[0].hist(sig['roeP__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].hist(sig['roeP__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].set_xlim(m_range)
ax[0].set_xlabel('roeP(Signal) in GeV')
ax[0].legend()
# Right subplot of number of charged ROE particles:
m_bins = 30
m_range = (0, 5)
# Left subplot of ROE mass:
ax[1].hist(bkg['roeP__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].hist(bkg['roeP__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].set_xlim(m_range)
ax[1].set_xlabel('roeP(Background) in GeV')
ax[1].legend()
fig.tight_layout()
fig.savefig('roe_mask_comparison.svg')


# In[ ]:





# In[ ]:





# In[14]:


plt.style.use('belle2')
m_bins = 15
m_range = (0,30)
fig, ax = plt.subplots(1,2, figsize=(15, 7))
ax[0].hist(sig['nROE_ECLClusters__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].hist(sig['nROE_ECLClusters__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[0].set_xlim(m_range)
ax[0].set_xlabel('# of ECL clusters in the ROE(Signal)')
ax[0].legend()
# Right subplot of number of charged ROE particles:
m_bins = 15
m_range = (0,40)
ax[1].hist(bkg['nROE_ECLClusters__bo__bc'], label='No mask',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].hist(bkg['nROE_ECLClusters__bocleanMask__bc'], label='"cleanmask" applied',
           bins = m_bins, range=m_range, alpha=0.6)
ax[1].set_xlim(m_range)
ax[1].set_xlabel('# of ECL clusters in the ROE(Background)')
ax[1].legend()
fig.tight_layout()
fig.savefig('roe_mask_comparison.svg')


# In[ ]:





# In[ ]:





# In[ ]:




