
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
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
#mcProduction = 'Summer16_102X_nAODv4_Full2016v5'
#mcProduction = 'Summer16_102X_nAODv5_SigOnly_Full2016v5'
mcProduction = 'Summer16_102X_nAODv5_Full2016v6'
mcProduction_v6 = 'Summer16_102X_nAODv6_Full2016v6'

dataReco = 'Run2016_102X_nAODv5_Full2016v6'

#mcSteps = 'MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5{var}'
mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}'

fakeSteps = 'DATAl1loose2016v6__l2loose__fakeW'

dataSteps = 'DATAl1loose2016v6__l2loose__l2tightOR2016v6'

##############################################
###### Tree base directory for the site ######
##############################################
SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

def makeMCDirectory_v6(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_v6, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_v6, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
mcDirectory_v6 = makeMCDirectory_v6()

fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'],
    ['C','Run2016C-Nano1June2019-v1'],
    ['D','Run2016D-Nano1June2019-v1'],
    ['E','Run2016E-Nano1June2019-v1'],
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1']
]
DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}
#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############   SIGNALS  ##################
###########################################
#still not available for 2016 samples
#######VBS EW: only ZV processes
"""
samples['VBS_ZV'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L') 
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}


###########################################
#############  BACKGROUNDS  ###############
###########################################

########## irreducible VBS QCD 

samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J_QCD') 
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J_QCD') 
             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L_QCD'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}
"""
########## DY ####
useDYtt = False

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

if useDYtt:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
        'FilesPerJob': 4,
    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

else:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toinf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-70to100') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-400to600') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-600toinf')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
        'FilesPerJob': 4,
    }
    addSampleWeight(samples, 'DY', 'DYJetsToTT_M-50', '('+ptllDYW_NLO+')*(LHE_HT < 70)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', '('+ptllDYW_LO+')*(LHE_HT < 70)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-70to100', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toinf', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-70to100', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-100to200', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-200to400', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-400to600', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-600toinf', ptllDYW_LO)

###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
    #'EventsPerJob': 100000
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

######WJets#####

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') 


samples['WJets'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 2
}


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight': mcCommonWeight, #+ '*nllW',
    'FilesPerJob': 3
}


samples['ggWW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}
######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'FilesPerJob': 4
}



######## VgS ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


########VBF-V##########

files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################
"""
samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 80
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}
"""
###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 100
}


for _, sd in DataRun:
  for pd in DataSets:
    # only this file is v3
    if ('2016E' in sd and 'MuonEG' in pd):
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd.replace('v1', 'v3'))
      print(files)

    else:
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
      print(files)
    
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
