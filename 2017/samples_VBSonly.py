import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

# samples

samples = {}

skim=''

directory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/'
directorySignals = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_SigOnly_Full2017v5/MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5/'
chargeFlipDir = '/eos/cms/store/cmst3/group/hww/HWWNano/Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__ChargeFlip/'
PromptSubtr = '/eos/cms/store/cmst3/group/hww/HWWNano/Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__fakeWMC/'
MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/'


################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17Iso_WP90_SS'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
GenLepMatch   = 'GenLepMatch'+Nlep+'l'


################################################
############## FAKE WEIGHTS ####################
################################################

if Nlep == '2' :
    fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
    fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py

# SFweight += '*btagSF'
############### VBS SAMPLES ##############
##########################################

#samples['DPS'] = {    'name':getSampleFiles(MCDir,'WWTo2L2Nu_DoubleScattering',False,'nanoLatino_')
 #                           ,
  #                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
   #                   'FilesPerJob' : 1,
    #              }





###aQGC####
#samples['ZTo2L_ZTo2J_aQGC'] = {  	'name'  :getSampleFiles(directorySignals,'ZTo2L_ZTo2J_aQGC',False,'nanoLatino_')
#								,
#						'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*1.067466' ,
#						'FilesPerJob' : 1 ,
#				}

###VBS EW###(bkg)
samples['ZTo2L_ZTo2J'] = {         'name'  :getSampleFiles(directorySignals,'ZTo2L_ZTo2J',False,'nanoLatino_')
                                                                ,
                                                'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*1.067466' ,
                                                'FilesPerJob' : 1 ,
                                }       
###VBS QCD###(bkg)
#samples['ZTo2L_ZTo2J_QCD'] = {         'name'  :getSampleFiles(directorySignals,'ZTo2L_ZTo2J_QCD',False,'nanoLatino_')
#                                                                ,
#                                                'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*1.067466' ,
#                                                'FilesPerJob' : 1 ,
#				}
