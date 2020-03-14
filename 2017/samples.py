
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return [sample]
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Fall2017_102X_nAODv5_Full2017v6'
mcProductionSig = 'Fall2017_102X_nAODv5_SigOnly_Full2017v5' #vbs signals

dataReco = 'Run2017_102X_nAODv4_Full2017v5'

mcStepsSig = 'MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5' #vbs signals
mcSteps = 'MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6'

fakeSteps = 'DATAl1loose2017v5__l2loose__fakeW'

dataSteps = 'DATAl1loose2017v5__l2loose__l2tightOR2017v5'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'


#def makeMCDirectory(var=''):
#    if var:
#        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
#        return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Fall17/l2tightOR__{var}'.format(var=var)
#    else:
#        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
#        return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Fall17/l2tightOR'

mcDirectory = os.path.join(treeBaseDir, mcProduction, mcSteps)
mcDirectorySig = os.path.join(treeBaseDir, mcProductionSig, mcStepsSig)
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'
################################################
############### Lepton WP ######################
################################################


################################################

eleWP='mvaFall17V1Iso_WP90'
#eleWP='mvaFall17V2Iso_WP90'
#eleWP='mvaFall17V1Iso_WP90_SS'
muWP='cut_Tight_HWWW'


LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
GenLepMatch   = 'GenLepMatch'+Nlep+'l'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

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

#FIXME b-tagging to be optimized
# Definitions in aliases.py


SFweight += '*btagSF'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-Nano1June2019-v1'] ,
            ['C','Run2017C-Nano1June2019-v1'] ,
            ['D','Run2017D-Nano1June2019-v1'] ,
            ['E','Run2017E-Nano1June2019-v1'] ,
            ['F','Run2017F-Nano1June2019-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' 
}#data trigger to be checked

###########################################
#############  BACKGROUNDS  ###############
###########################################

###########################################
#############   VBS PROCESSES ##################
###########################################

#########################################
############# SIGNALS ###################
########VBS aQGC - SMP-18-006 model: all signals givin aQGC with Z to 2L and V to 2J
# WpTo2J_ZTo2L_aQGC
# WmTo2J_ZTo2L_aQGC
# ZTo2L_ZTo2J_aQGC
########################################

samples['VBS_ZV_aQGC'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(mcDirectorySig, 'WmTo2J_ZTo2L_aQGC'),
    'weight':  XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
    'FilesPerJob': 1
}


#######################################################
#########VBS backgrounds from purely SM processes
##########VBS QCD 
samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WmToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySig, 'WmTo2J_ZTo2L_QCD'),
    'weight':  XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
    'FilesPerJob': 1
}


#######VBS EW 

samples['VBS_VV_EW'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(mcDirectorySig, 'WmToLNu_WmTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WmToLNu_ZTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_WmToLNu')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_WmTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_WpTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_ZTo2L'),
    'weight':  XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
    'FilesPerJob': 1
}


##################################################################################################################
