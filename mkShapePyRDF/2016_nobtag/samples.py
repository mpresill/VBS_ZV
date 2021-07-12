import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
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

mcProduction = 'Summer16_102X_nAODv7_Full2016v7'
dataReco = 'Run2016_102X_nAODv7_Full2016v7'

fakeReco = 'Run2016_102X_nAODv7_Full2016v7'
fakeSteps = 'DATAl1loose2016v7__l2loose__fakeW'

mcSteps = 'MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7{var}'


dataSteps = 'DATAl1loose2016v7__l2loose__l2tightOR2016v7'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirSMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
def makeMCDirectorySMPeos(var=''):
    if var:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
mcDirectorySMPeos = makeMCDirectorySMPeos() #this was added just for signals 
################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-02Apr2020_ver1-v1'],
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1']
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
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

useDYtt = False
############ DY ############ consider using HT binned samples for stat reasons

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'


files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \
	nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
	    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-70to100') + \
	    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-200to400_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-400to600_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-600toinf') + \
	    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
	    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')
	 ##nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \ 
samples['DY'] = {    'name'   :   files,
                         'weight' : mcCommonWeight + "*( !(Sum(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && AbsVec(PhotonGen_eta)<2.6) > 0 && Sum(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2))", #'*1.21/1.158', #updating k-factor=1.158 in Latino
                         'FilesPerJob': 4,
                         'EventsPerJob': 70000,
}
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', '('+ptllDYW_NLO+')*(LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', '('+ptllDYW_LO+')*(LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-70to100', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500', ptllDYW_LO)
    #addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-70to100', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-100to200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-200to400_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-400to600_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-600toinf', ptllDYW_LO)

###### Top #######

#Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'


files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
	nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
	nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    	nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic')
	#nanoGetSampleFiles(mcDirectory,'TTZjets') + \
    	#nanoGetSampleFiles(mcDirectory,'TTWjets')
    
 
samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples, 'top', 'TTTo2L2Nu', 'Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

######WJets#####

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
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
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT100_200', '0.993') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT200_400', '1.002') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT400_600', '1.009') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT600_800', '1.120') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT800_1200', '1.202') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT1200_2500', '1.332') 
#addSampleWeight(samples,'WJets', 'WJetsToLNu-HT2500_inf', '4.200') 

###### WW ########

samples['WW'] = {
    'name' : nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight' : mcCommonWeight,# + '*nllW',
    'FilesPerJob' : 3,
}            

"""
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN') 

samples['ggWW'] = {
    'name': files,
    'weight' : mcCommonWeight +'*1.53/1.4', #updating k-factor
    'FilesPerJob' : 2


}
"""



samples['ggWW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}
######## Vg ########

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(mcDirectory,'Zg'),
                    'weight' : mcCommonWeightNoMatch +'*!(Gen_ZGstar_mass > 0)',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }
#the following baseW correction is needed in v5 and should be removed in v6
#addSampleWeight(samples,'Vg','ZGToLLG','0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'Zg')
                                 + nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
                      'weight' : mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 6,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','Zg', '(Gen_ZGstar_mass > 0)') #*0.448
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


###VZ####
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') +\
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') +\
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ']= {
    'name': files,
    'weight' : mcCommonWeight + '*1.11', #updating k-factor
    'FilesPerJob' : 2

}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob':4,
}


########VBF-V##########
"""
files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')
samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob':4,
}
"""

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


#######VBS EW: only ZV processes

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



addSampleWeight(samples,'VBS_ZV','WmTo2J_ZTo2L', '(Sum(AbsVec(GenPart_pdgId) == 6) ==0)')
addSampleWeight(samples,'VBS_ZV','WpTo2J_ZTo2L', '(Sum(AbsVec(GenPart_pdgId) == 6) ==0)')

samples['tZq'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight +'*(Sum(AbsVec(GenPart_pdgId) == 6) >=1)',
    'FilesPerJob': 7
}
###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


###########################################
################## DATA ###################
###########################################
samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA * LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 120
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
