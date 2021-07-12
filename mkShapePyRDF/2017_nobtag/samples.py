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

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'
dataReco = 'Run2017_102X_nAODv7_Full2017v7'

mcSteps = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

fakeReco = 'Run2017_102X_nAODv7_Full2017v7'
fakeSteps = 'DATAl1loose2017v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2017v7__l2loose__l2tightOR2017v7'

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

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7'
################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['B','Run2017B-02Apr2020-v1'] ,
            ['C','Run2017C-02Apr2020-v1'] ,
            ['D','Run2017D-02Apr2020-v1'] ,
            ['E','Run2017E-02Apr2020-v1'] ,
            ['F','Run2017F-02Apr2020-v1']
          ]


DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
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
ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'



files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext1') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200_newpmx') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600_newpmx') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-100to200_newpmx') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400_newpmx') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf')

samples['DY'] = {    'name'   :   files,
                         'weight' : mcCommonWeight + "*( !(Sum(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && AbsVec(PhotonGen_eta)<2.6) > 0 && Sum(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2))", #'*1.21/1.158', #updating k-factor=1.158 in Latino
                         'FilesPerJob': 4,
                         'EventsPerJob': 70000,
}

addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', 'DY_NLO_pTllrw * (LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', 'DY_LO_pTllrw * (LHE_HT < 100)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-70to100',  'DY_LO_pTllrw * 1.000')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200',  'DY_LO_pTllrw * 1.000')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400',  'DY_LO_pTllrw * 0.999')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600',  'DY_LO_pTllrw * 0.990')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800',  'DY_LO_pTllrw * 0.975')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500',  'DY_LO_pTllrw * 0.833')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-100to200',  'DY_LO_pTllrw')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-200to400',  'DY_LO_pTllrw')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-400to600',  'DY_LO_pTllrw')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-600toInf',  'DY_LO_pTllrw')


###### Top #######

#Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'


files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
	nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
	nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    	nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    	nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') + \
	nanoGetSampleFiles(mcDirectory,'TTZjets_ext1') + \
    	nanoGetSampleFiles(mcDirectory,'TTWjets_ext1')
    
 
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

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100') + \
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
addSampleWeight(samples,'WJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT100_200', '0.993') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT200_400', '1.002') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT400_600', '1.009') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT600_800', '1.120') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT800_1200', '1.202') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT1200_2500', '1.332') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT2500_inf', '4.200') 

###### WW ########

samples['WW'] = {
    'name' : nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight' : mcCommonWeight,# + '*nllW',
    'FilesPerJob' : 3,
}            



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
######## Vg ########

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    'weight' : mcCommonWeightNoMatch +'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }
#the following baseW correction is needed in v5 and should be removed in v6
#addSampleWeight(samples,'Vg','ZGToLLG','0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG')
                                 + nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
                      'weight' : mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 6,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
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

files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50_newpmx')
samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob':4,
}


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
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L') 
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}
addSampleWeight(samples,'VBS_ZV','WmTo2J_ZTo2L', 'Sum(AbsVec(GenPart_pdgId) == 6)==0') 
addSampleWeight(samples,'VBS_ZV','WpTo2J_ZTo2L', 'Sum(AbsVec(GenPart_pdgId) == 6)==0')

samples['VBS_ZV_dipoleRecoil'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_dipoleRecoil')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}
addSampleWeight(samples,'VBS_ZV_dipoleRecoil','WmTo2J_ZTo2L_dipoleRecoil', 'Sum(AbsVec(GenPart_pdgId) == 6)==0')
addSampleWeight(samples,'VBS_ZV_dipoleRecoil','WpTo2J_ZTo2L_dipoleRecoil', 'Sum(AbsVec(GenPart_pdgId) == 6)==0')




"""samples['tZq'] = {
    'name': nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight + '*(Sum(AbsVec(GenPart_pdgId) == 6) >= 1)' ,
    'FilesPerJob': 1
}
"""
samples['tZq'] = {
        'name' : nanoGetSampleFiles(mcDirectory, 'tZq_ll'),
        'weight' : mcCommonWeight,
        'FilesPerJob': 7,
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
