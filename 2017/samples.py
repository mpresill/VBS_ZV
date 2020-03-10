
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
############### Lepton WP ######################
################################################

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight1l =       'puWeight*\
                   TriggerEffWeight_1l*\
                   Lepton_RecoSF[0]*\
                   EMTFbug_veto'
SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'* PrefireWeight * btagSF'
     
GenLepMatch   = 'Lepton_genmatched[0]'


####
# NVTX reweighting
#SFweight += '*nvtx_reweighting'
################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

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
#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
#mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
#mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight_test = '1.'
###########################################
#############  BACKGROUNDS  ###############
###########################################

###########################################
#############   SIGNALS  ##################
###########################################

signals = []

#######VBS EW 

samples['ZTo2L_ZTo2J'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J'),
    'weight':  XSWeight+'*'+SFweight,+'*'+METFilter_MC+'*'+GenLepMatch,
    'FilesPerJob': 1
}

signals.append('ZTo2L_ZTo2J')

########VBS aQGC - SMP-18-006 model
samples['ZTo2L_ZTo2J_aQGC'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J_aQGC'),
    'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
    'FilesPerJob': 1
}

signals.append('ZTo2L_ZTo2J_aQGC')





#do I have to consider all the WV processes as backgrounds??? I am expecting them not to be relevant with the cut on invariant mass ... is that so????



##########VBS QCD 
samples['ZTo2L_ZTo2J_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J_QCD'),
    'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
    'FilesPerJob': 1
}

signals.append('ZTo2L_ZTo2J_QCD')




