#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Here you could list all of you variables so
   that they are not in your steering file
"""

from variables import variables as vm
import variables.collections as vc
import variables.utils as vu


# list of variable collections
""
vm.addAlias("decayModeID", "extraInfo(decayModeID)")
vm.addAlias("SigProb", "extraInfo(SignalProbability)")


# simple CS variables
simpleCSVariables=[
    'Bsig_d0_R2' , 'Bsig_d0_thrustOm', 'Bsig_d0_cosTBTO',
 'Bsig_d0_cosTBz', 'Bsig_d0_KSFWVariables_hso00',
 'Bsig_d0_KSFWVariables_hso01' ,'Bsig_d0_KSFWVariables_hso02',
 'Bsig_d0_KSFWVariables_hso03', 'Bsig_d0_KSFWVariables_hso04',
 'Bsig_d0_KSFWVariables_hso10', 'Bsig_d0_KSFWVariables_hso12',
 'Bsig_d0_KSFWVariables_hso14', 'Bsig_d0_KSFWVariables_hso20',
 'Bsig_d0_KSFWVariables_hso22', 'Bsig_d0_KSFWVariables_hso24',
 'Bsig_d0_KSFWVariables_hoo0', 'Bsig_d0_KSFWVariables_hoo1',
 'Bsig_d0_KSFWVariables_hoo2', 'Bsig_d0_KSFWVariables_hoo3',
 'Bsig_d0_KSFWVariables_hoo4', 
   "foxWolframR2", "harmonicMomentThrust1","harmonicMomentThrust2","harmonicMomentThrust3", "harmonicMomentThrust4"
]


# Kinematics (the variables Mbc and delta E only make sense for Btag)
kinematics = ["M", "Mbc", "E", "p", "useCMSFrame(p)", "deltaE"]

# MC Matching
mcmatch = ["mcErrors", "mcPDG", "isNotContinuumEvent", "isSignal", "isSignalAcceptMissingNeutrino", "SigProb"]

# PID
precut_PID=["electronID", "pionID", "muonID", "kaonID", "particleID", "decayModeID", "FEIProbRank" ]

# missing momentum and energy
missing = ["isSignalAcceptMissing", "isSignalAcceptMissingGamma", "isSignalAcceptMissingNeutrino",
         "missingMomentumOfEvent", "missingMomentumOfEventCMS",  "pRecoilPhi", "pRecoilTheta",
          "missingEnergyOfEventCMS","missingMomentumOfEvent","missingMomentumOfEventCMS",
          "missingMomentumOfEventCMS_theta","missingMomentumOfEvent_theta", "missingMass2OfEvent"]
#"cosThetaBetweenParticleAndNominalB"

meta_fuctions = ["nParticlesInList(Upsilon(4S):generic)", "nParticlesInList(B+:sig)", "nParticlesInList(B-:tag/FEI)"]



# roe
roe_kinematics = ["roeE()", "roeM()", "roeP()", "roeMbc()", "roeDeltae()", "roeEextra()", "roeNeextra()"]
roe_track_cluster = ["nTracks", "nROE_Tracks()", "nROE_Charged()", "nROE_RemainingTracks", "nROE_ECLClusters()", "nROE_KLMClusters", "clusterE", "clusterPhi"]
#roe_missing = ["weDeltae()", "weMbc()", "weMissE()","weMissP()", "weMissPTheta()"]



standard_vars = vc.kinematics + vc.mc_kinematics + vc.mc_truth


# variable list for different particles
##############################################################################
# generic B reconstructed with FEI
tag_vars = []
tag_vars += vc.deltae_mbc
tag_vars += standard_vars
tag_vars += kinematics
#tag_vars += meta_fuctions 
# tag_vars += roe_kinematics
# tag_vars += roe_track_cluster
# you need to build the rest of event for the generic B otherwise you get the error
# [ERROR] Relation between particle and ROE doesn't exist!  { module: VariablesToNtuple_B-:generic }
# I added the rest of event for your generic B to the steering file
# tag_vars += roe_missing

# applying roemask to tag variables
for roe_variable in roe_kinematics:
   roe_variable_with_mask7 = roe_variable.replace("()", "(cleanMask)")
   tag_vars.append(roe_variable_with_mask7)

for roe_variable in roe_track_cluster:
   roe_variable_with_mask8 = roe_variable.replace("()", "(cleanMask)")
   tag_vars.append(roe_variable_with_mask8)

# for roe_variable in roe_missing:
#    roe_variable_with_mask9 = roe_variable.replace("()", "(cleanMask, 5)")
#    tag_vars.append(roe_variable_with_mask9)

tag_vars += mcmatch
tag_vars += simpleCSVariables
tag_vars += missing
tag_vars += vc.tag_vertex + vc.mc_tag_vertex



tag_vars_ups = vu.create_daughter_aliases(tag_vars,1,prefix='Btag')





# kaon ntuple
kaon_vars = []
kaon_vars += vc.deltae_mbc
kaon_vars += standard_vars
kaon_vars += kinematics
# kaon_vars += roe_kinematics
kaon_vars += mcmatch
# kaon_vars += roe_track_cluster
kaon_vars += simpleCSVariables
#kaon_vars += roe_missing # you don't build a rest of event for kaon so this won't work
kaon_vars += missing
kaon_vars += vc.vertex + vc.mc_vertex
#kaon_vars += meta_fuctions 






# signal B
sig_vars = []

sig_vars += simpleCSVariables
sig_vars += roe_kinematics
sig_vars += roe_track_cluster
#sig_vars += roe_missing

sig_vars += mcmatch
sig_vars += precut_PID
sig_vars += standard_vars
sig_vars += missing

sig_vars += vc.tag_vertex + vc.mc_tag_vertex
#sig_vars += meta_fuctions



for roe_variable in roe_kinematics:
    roe_variable_with_mask = roe_variable.replace("()", "(cleanMask)")
    sig_vars.append(roe_variable_with_mask)

for roe_variable in roe_track_cluster:
    roe_variable_with_mask2 = roe_variable.replace("()", "(cleanMask)")
    sig_vars.append(roe_variable_with_mask2)

sig_vars_ups = vu.create_daughter_aliases(sig_vars,0,prefix='Bsig')


# Upsilon(4S)

# Upsilon_vars = ["Btag_SigProb", "Btag_decayModeID", "Btag_Mbc", "Bsig_isSignal", "nCharged", "m2RecoilSignalSide" ]
Upsilon_vars = []
Upsilon_vars += kinematics
Upsilon_vars += roe_kinematics
Upsilon_vars += mcmatch
Upsilon_vars += roe_track_cluster
Upsilon_vars += simpleCSVariables
Upsilon_vars += standard_vars
Upsilon_vars += roe_kinematics
Upsilon_vars += roe_track_cluster
Upsilon_vars += missing
#Upsilon_vars += meta_fuctions
#Upsilon_vars += roe_missing
# applying roemask to Upsilon variables

for roe_variable in roe_kinematics:
    roe_variable_with_mask4 = roe_variable.replace("()", "(cleanMask)")
    Upsilon_vars.append(roe_variable_with_mask4)

for roe_variable in roe_track_cluster:
    roe_variable_with_mask5 = roe_variable.replace("()", "(cleanMask)")
    Upsilon_vars.append(roe_variable_with_mask5)

# for roe_variable in roe_missing:
#    roe_variable_with_mask6 = roe_variable.replace("()", "(cleanMask)")
#    Upsilon_vars.append(roe_variable_with_mask6)
