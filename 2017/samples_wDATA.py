
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
            ['B','Run2017B-Nano14Dec2018-v1'] ,
            ['C','Run2017C-Nano14Dec2018-v1'] ,
            ['D','Run2017D-Nano14Dec2018-v1'] ,
            ['E','Run2017E-Nano14Dec2018-v1'] ,
            ['F','Run2017F-Nano14Dec2018-v1']
          ]


DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }

###########################################
#############  BACKGROUNDS  ###############
###########################################

useDYtt = False
############ DY ############ consider using HT binned samples for stat reasons
"""
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

if useDYtt :
    samples['DY'] = {    'name'   :   getSampleFiles(mcDirectory,'DYJetsToTT_MuEle_M-50',False,'nanoLatino_')
                                    + getSampleFiles(mcDirectory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'FilesPerJob' : 5,
                    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)
    
    ## Remove OF from inclusive sample (is it needed?)
    #cutSF = '(abs(Lepton_pdgId[0]*Lepton_pdgId[1]) == 11*11)||(Lepton_pdgId[0]*Lepton_pdgId[1]) == 13*13)'
    #addSampleWeight(samples,'DY','DYJetsToLL_M-50',cutSF)

else:
    samples['DY'] = {    'name'   :   getSampleFiles(mcDirectory,'DYJetsToLL_M-50',False,'nanoLatino_')
                                    + getSampleFiles(mcDirectory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'FilesPerJob' : 5,
                     }
    addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)
"""

files= nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_ext1') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf')

samples['DY'] = {    'name'   :   files,
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                         'FilesPerJob' : 5,
}



###### Top #######

Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'


files = nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    nanoGetSampleFiles(mcDirectory, 'TTToSemiLeptonic') + \
    nanoGetSampleFiles(mcDirectory, 'TTWjets') + \
    nanoGetSampleFiles(mcDirectory, 'TTZjets') + \
    nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') 

samples['top'] = {
    'name': files,
    'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)


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
    'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC, 
    'FilesPerJob': 2
}


###### WW ########

samples['WW'] = {
    'name' : nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*nllW',
    'FilesPerJob' : 1,
}            


samples['WW_ewk'] = {
    'name' : nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',  #filter tops and Higgs
    'FilesPerJob' : 2,
}            


files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN') 

samples['ggWW'] = {
    'name': files,
    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*1.53/1.4', #updating k-factor
    'FilesPerJob' : 10


}

###VZ####
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') +\
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ']= {
    'name': files,
    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*1.11', #updating k-factor
    'FilesPerJob' : 10

}


########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC
}



########VBF-V##########
files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['VBF-V'] = {
    'name': files,
    'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC
}

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


###########################################
################## DATA ###################
###########################################
"""
samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
                  }

for Run in DataRun :
  directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__l2loose__l2tightOR2017v5/'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])
"""
