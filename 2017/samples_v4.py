
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
mcProductionSig = 'Fall2017_102X_nAODv5_SigOnly_Full2017v5'

dataReco = 'Run2017_102X_nAODv4_Full2017v5'

mcStepsSig = 'MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5'
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
############ DATA DECLARATION ##################
################################################
#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
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
    'weight': mcCommonWeight_test,
    'FilesPerJob': 1
}

signals.append('ZTo2L_ZTo2J')


