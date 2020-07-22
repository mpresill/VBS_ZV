import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

samples={}

# Steps
mcSteps   = 'MCl1loose2017v6__MCCorr2017v6__VBSjjlnuSkim2017v5' 
dataSteps = 'DATAl1loose2017v6__VBSjjlnuSkim2017v5_data'
fakeSteps = 'DATAl1loose2017v6__VBSjjlnuSkim2017v5_data'

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

directory_bkg    = treeBaseDir + 'Fall2017_102X_nAODv5_Full2017v6/' + mcSteps
directory_signal = treeBaseDir + 'Fall2017_102X_nAODv5_Full2017v6/' + mcSteps
directory_fakes  = treeBaseDir + 'Run2017_102X_nAODv5_Full2017v6/'  + fakeSteps
directory_data   = treeBaseDir + 'Run2017_102X_nAODv5_Full2017v6/'  + dataSteps

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

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

XSWeight   = 'XSWeight'
SFweight1l =       'puWeight*\
                   TriggerEffWeight_1l*\
                   Lepton_RecoSF[0]*\
                   EMTFbug_veto'
SFweight   = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l
SFweight += '*PrefireWeight*btagSF'

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
}
###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useEmbeddedDY = False
DY_photon_filter = '(Sum(GenPart_pdgId == 22 && OddVec(GenPart_statusFlags) && GenPart_pt > 20.) == 0)'

samples['DY'] = {    'name'   :   
    nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-100to200_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-200to400_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-400to600_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-600toInf_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50-LO')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext1')
  # + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-70to100') # to be added
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600_ext1')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
                                ,
        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + DY_photon_filter, # ewknloW ADD ME, admin
        'FilesPerJob' : 3,
                  }

addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200_ext1', ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400_ext1', ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600_ext1', ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf_ext1', ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50-LO',               ptllDYW_LO  + '*(LHE_HT<100)') # ewknloW not yet processed
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext1',                ptllDYW_NLO + '*(LHE_HT<100)') # "*ewknloW" not yet processed
addSampleWeight(samples,'DY','DYJetsToLL_M-50',                     ptllDYW_NLO +'*(LHE_HT<100)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',         ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',    ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1',    ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',         ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',        ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',       ptllDYW_LO  )
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',        ptllDYW_LO  )



############ Top ############
samples['top'] = {    
            'name'   :  nanoGetSampleFiles(directory_bkg,'ST_s-channel') 
                      + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
                      + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
                      + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop') 
                      + nanoGetSampleFiles(directory_bkg,'ST_tW_top')
                      + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic')
                      + nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu')
                      + nanoGetSampleFiles(directory_bkg,'TTWjets_ext1')
                      + nanoGetSampleFiles(directory_bkg,'TTZjets_ext1'),  
                      'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + "* Top_pTrw",
}


samples['Wjets'] = { 'name' :   
          # nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO')
          nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO_ext1')
          # + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100') # BROKEN
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf'),
				'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
				'FilesPerJob' : 2,
		   }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets', 'WJetsToLNu-LO_ext1', 'LHE_HT < 100') # no ewknloW here!
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT100_200',   'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT200_400',   'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT400_600',   'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT600_800',   'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT800_1200',  'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT1200_2500', 'ewknloW')
addSampleWeight(samples,'Wjets', 'WJetsToLNu_HT2500_inf',  'ewknloW')


samples['VV']  = { 'name' :  
               nanoGetSampleFiles(directory_bkg,'WmTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_bkg,'WmToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_bkg,'WmToLNu_ZTo2J_QCD',) +
               nanoGetSampleFiles(directory_bkg,'WpTo2J_WmToLNu_QCD') +
               nanoGetSampleFiles(directory_bkg,'WpTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_bkg,'WpToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_bkg,'WpToLNu_WpTo2J_QCD') +
               nanoGetSampleFiles(directory_bkg,'WpToLNu_ZTo2J_QCD',) ,
              #  nanoGetSampleFiles(directory_bkg,'ZTo2L_ZTo2J_QCD',  ) , #admin, ADD ME
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + "* ewknloW",
        'FilesPerJob' : 3,
}

############ VVV ############

samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch  ,
                    'FilesPerJob' : 5,
                  }

############## VBF-V ########


###
samples['VBF-V']  = {  'name'   : nanoGetSampleFiles(directory_bkg,'WLNuJJ_EWK')
                                  + nanoGetSampleFiles(directory_bkg,'EWKZ2Jets_ZToLL_M-50'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 6
                  }


##########################################
################ SIGNALS #################
##########################################

#
samples['VBS']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J'),
               #nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J' ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
       'FilesPerJob' : 4,
}

##########################################
################# DATA ###################
##########################################

# #fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP + '_mu10_ele35'
# # from alias
# fakeW = 'fake_weight_corrected'

# #### Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob': 14
# }

# for _, sd in DataRun:
#   for pd in DataSets:
#     files = nanoGetSampleFiles(directory_fakes, pd + '_' + sd)
#     samples['Fake']['name'].extend(files)
#     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))



samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 15,
                  }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])

