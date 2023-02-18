#!/usr/bin/env python
# coding: utf-8
# %%
#get_ipython().run_line_magic('matplotlib', 'inline')


# Reconstruction of Upsilon(4S) -> B+ B-

# %%
# import libraries
import sys
import basf2 as b2
import fei
import modularAnalysis as ma
import stdV0s
import variables.collections as vc
import variables.utils as vu
from variables import variables as vm  # .py file of variable
import vertex
#from variables.MCGenTopo import mc_gen_topo

import ntuple_variables as nv


# %%
# MC14 signal
# /pnfs/desy.de/belle/local/bdata/MC/release-05-02-00/DB00001330/MC14ri_a/prod00016780/s00/e1003/4S/r00000/1290000002/mdst/sub00/mdst_000050_prod00016780_task10020000050.root
# 189000 events in one sig root file

# MC14 background
# mixed: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018937/e1003/4S/r00000/mixed/11180500/udst/sub00/udst_000059_prod00018937_task10020000059.root
# charged: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018952/e1003/4S/r00000/charged/11180500/udst/sub00/udst_000018_prod00018952_task10020000018.root 
# uubar: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018977/e1003/4S/r00000/uubar/11180500/udst/sub00
# ddbar: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018994/e1003/4S/r00000/ddbar/11180500/udst/sub00%
# ccbar: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018959/e1003/4S/r00000/ccbar/11180500/udst/sub00
# ssbar: /pnfs/desy.de/belle/local/belle/MC/release-05-02-11/DB00001363/SkimM14ri_ax1/prod00018969/e1003/4S/r00000/ssbar/11180500/udst/sub00/

	# %%
# Setup
main = b2.Path()


# %%
# assume first argument is input file
input_file = sys.argv[1]
# assume second argument is name of output file
output_file = sys.argv[2]
print("input file = " + str(input_file))
print("output file = " + str(output_file))

# %%
ma.inputMdstList("default", input_file, path=main)


ma.buildEventKinematics(path = main)
ma.buildEventShape(path=main)

# %%
if "SkimM14ri_ax1" not in input_file:  # it is signal
    from skim.fei import feiHadronicBplus 
    skim = feiHadronicBplus() 
    skim(main)
    afterSkimPath = skim.postskim_path
       
else:   # it is background
    ma.copyLists(
    outputListName="B-:generic",
    inputListNames=["B-:feiHadronic"],  # other way around of input and output makes error.    
    path=main)
    afterSkimPath = main

# %%
print("hello")

# vertex fit
vertex.TagV("B-:generic", fitAlgorithm="Rave", path=afterSkimPath)

print("world")

# rest of event
ma.buildRestOfEvent(target_list_name="B-:generic", path=afterSkimPath)
ma.appendROEMask("B-:generic",
                 "cleanMask",
                 "[nCDCHits > 0] and [thetaInCDCAcceptance == 1] and [pt > 0.1] and [abs(dr) < 1] and [abs(dz) < 3]",
                 "[p >= 0.05] and [useCMSFrame(p)<=3.2]",
                 path=afterSkimPath)

ma.cutAndCopyList(outputListName="B-:aftercut_tag", inputListName= "B-:generic", 
                  cut= "roeEextra() < 2.5 and Mbc>5.265", #"roeEextra() < 2.5 and Mbc>5.265", 
                  path=afterSkimPath 
) 

ma.buildContinuumSuppression(list_name="B-:aftercut_tag", roe_mask="cleanMask", path=afterSkimPath)





ma.applyEventCuts("[nParticlesInList(B-:aftercut_tag) > 0]", path=afterSkimPath)


# %%
vm.addAlias("FEIProbRank", "extraInfo(FEIProbabilityRank)")

ma.matchMCTruth(list_name="B-:aftercut_tag", path=afterSkimPath)

#ma.variablesToNtuple(
#    "B-:generic",
#     variables = nv.tag_vars,
#    filename="B-_sig_MC14_full.root",
#    path=afterSkimPath,
#)


# %%
# reconstruction of signal B (B -> K nunu)
stdV0s.stdKshorts(path=afterSkimPath)
ma.fillParticleList(
      "K+:charged",  
      "kaonID > 0.5",                                      
      path = afterSkimPath)

ma.rankByHighest(
    particleList="K+:charged",
    variable="kaonID",
    outputVariable="Kaon_rank",
    path=main,
)

# vertex fit of K
vertex.kFit("K+:charged", conf_level=-1.0, path=afterSkimPath)


ma.matchMCTruth(list_name="K+:charged", path=afterSkimPath)


#ma.variablesToNtuple(
#    "K+:charged",
#    variables=nv.kaon_vars,
#    filename="K+_sig_MC14_full.root",
#    path=afterSkimPath,
#)


## removed it for skimmed MC14
ma.reconstructDecay(
      "B+:signal -> K+:charged ?nu",
  #      cut = "Bsig_d0_missingEnergyOfEventCMS > 1.85 and roeE()< 8.0", 
         "", 
      path=afterSkimPath)
ma.matchMCTruth(list_name="B+:signal", path=afterSkimPath)


# %%
# ranking
ma.rankByHighest(
    particleList="B+:signal",
    variable="extraInfo(SignalProbability)",
    outputVariable="FEIProbabilityRank",
    path=afterSkimPath,
)


# %%


# rest of event
ma.buildRestOfEvent(target_list_name="B+:signal", path=afterSkimPath)

##  roemask is removed because of error.
ma.appendROEMask("B+:signal",
                 "cleanMask",
                "[nCDCHits > 0] and [thetaInCDCAcceptance == 1] and [pt > 0.1] and [abs(dr) < 1] and [abs(dz) < 3]",
                 "[p >= 0.05] and [useCMSFrame(p)<=3.2]",
                 path=afterSkimPath) 


# %%
#write another cutandcopyList for B+:signal for cut
ma.cutAndCopyList(outputListName="B+:aftercut", inputListName= "B+:signal", 
                  cut= "roeE()< 8.0", #"Bsig_d0_missingEnergyOfEventCMS > 1.85 and roeE()< 8.0", 
                  
           path=afterSkimPath)
 
ma.buildContinuumSuppression(list_name="B+:aftercut", roe_mask="cleanMask", path=afterSkimPath)

# %%


ma.applyEventCuts("[nParticlesInList(B+:aftercut) > 0]", path=afterSkimPath)
#ma.variablesToNtuple(
#    "B+:signal",
#    variables= nv.sig_vars+ mc_gen_topo(200),
#    filename="B+_sig_MC14_full.root",
#    path=afterSkimPath,
#)


# %%


# reconstruction Upsilon(4S)
ma.reconstructDecay(
                      "Upsilon(4S):generic -> B+:aftercut B-:aftercut_tag",
   "",               
  path=afterSkimPath                                             
)




#add ranking of Upsilon(4S). Rank Upsilon by SigProb of B_tag 
ma.rankByHighest(
    particleList="Upsilon(4S):generic",
    variable="daughter(1, extraInfo(SignalProbability))",
    outputVariable="Btag_FEIProbabilityRank",
    path=afterSkimPath,
)

vm.addAlias("Btag_FEIProbabilityRank", "extraInfo(Btag_FEIProbabilityRank)")
vm.addAlias("Btag_candidate", "daughter(1, nParticlesInList(B-:aftercut))")


ma.applyEventCuts("[nParticlesInList(Upsilon(4S):generic) > 0]", path=afterSkimPath)


# %%


# rest of event
ma.buildRestOfEvent("Upsilon(4S):generic", fillWithMostLikely=True, path=afterSkimPath)
ma.appendROEMask("Upsilon(4S):generic",
                 "cleanMask",
                 "[nCDCHits > 0] and [thetaInCDCAcceptance == 1] and [pt > 0.1] and [abs(dr) < 1] and [abs(dz) < 3]",
                 "[p >= 0.05] and [useCMSFrame(p)<=3.2]",
                 path=afterSkimPath)




# %%
# write another cutandcopyList for upsilon cut
ma.cutAndCopyList(outputListName="Upsilon(4S):aftercut", inputListName= "Upsilon(4S):generic", 
                  cut= "roeEextra()<2.0 and nROE_Tracks()<3.0 and roeP()< 1.5 and roeNeextra()<2.0", #"roeEextra()<2.0 and nROE_Tracks()<3.0 and roeP()< 1.5 and roeNeextra()<2.0", 
                  path=afterSkimPath 
)

ma.buildContinuumSuppression(list_name="Upsilon(4S):aftercut", roe_mask="cleanMask", path=afterSkimPath)



# %%




# topoana output to a ntuple
#ma.variablesToNtuple('', mc_gen_topo(200), 'MCGenTopo', 'MCGenTopo_sig_MC14_full.root', path=afterSkimPath)


# %%


ma.variablesToNtuple(
    "Upsilon(4S):aftercut",
    variables = nv.Upsilon_vars+ nv.tag_vars_ups+ nv.sig_vars_ups+["Btag_FEIProbabilityRank", "nParticlesInList(Upsilon(4S):aftercut)"],
    filename=output_file,   
    path=afterSkimPath,
)

print("start processing")

b2.process(main)

print(b2.statistics)

