import os

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

#
# function to simplify the life later ...
#

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()


#######################
### Skims and trees ###
#######################

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

mcReco = 'Fall2017_102X_nAODv5_Full2017v6/'
#mcSteps = 'MCl1loose2017v6__MCCorr2017v6__VBSjjlnuSkim2017v5'
#mcDirectory = os.path.join(treeBaseDir, mcReco, mcSteps)  

#try matteo's directories
mcSteps='MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6{var}'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcReco, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcReco, mcSteps.format(var=''))
mcDirectory= makeMCDirectory()
#dataReco  = 'Run2017_102X_nAODv4_Full2017v5'
#dataSteps = 'DATAl1loose2017v5__l2loose__l2tightOR2017v5'

#fakeSteps = 'DATAl1loose2017v5__l2loose__fakeW'

       # --> treeBaseDir/mcReco/mcSteps
#dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)   # --> treeBaseDir/dataReco/dataSteps
#fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)   # --> treeBaseDir/dataReco/fakeSteps





################################################################
### Definition of common cuts (on lepton id/iso) and weights ###
################################################################
Nlep='2'

eleWP='mvaFall17V1Iso_WP90'
#eleWP='mvaFall17V2Iso_WP90'
#eleWP='mvaFall17V1Iso_WP90_SS'
muWP='cut_Tight_HWWW'


LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
#LepWPCut        = 'LepCut2l__ele_'+eleWP+'__mu_'+muWP
#LepWPweight     = 'LepSF2l__ele_'+eleWP+'__mu_'+muWP

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
#SFweight      = 'SFweight2l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
#GenLepMatch   = 'GenLepMatch'+Nlep+'l'

GenLepMatch   = 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1, 0)'

#GenLepMatch   = 'Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]'
################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'
################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py
SFweight += '*btagSF'

# Also updated jet PUid SF
#SFweight += '*PUJetIdSF' #FIX: add this


#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = XSWeight+'*'+SFweight+'*'+METFilter_MC
mcCommonWeight = XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC

###########################################
#############  SIGNAL  ###############
###########################################

############ ZZTo2L2Q ############

files = nanoGetSampleFiles(mcDirectory ,'ZTo2L_ZTo2J' )

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}

############ ZWTo2L2J ############

files = nanoGetSampleFiles(mcDirectory ,'WpTo2J_ZTo2L' ) + \
    nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L')

samples['ZW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


###########################################
#############  BACKGROUNDS  ###############
###########################################
useDYtt = False
############ DY ############
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


files= nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_ext1') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf')

samples['DY'] = {    'name'   :   files,
                         'weight' : mcCommonWeight, #'*1.21/1.158', #updating k-factor=1.158 in Latino
                         'FilesPerJob' : 5,
}

###### Top #######

#Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'


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
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

#addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)


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
    'name' : nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight' : mcCommonWeight + '*nllW',
    'FilesPerJob' : 1,
}            


samples['WW_ewk'] = {
    'name' : nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight' : mcCommonWeight + '*(Sum(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',  #filter tops and Higgs
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
    'weight' : mcCommonWeightNoMatch + '*1.53/1.4', #updating k-factor
    'FilesPerJob' : 10


}

###VZ####
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') +\
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ']= {
    'name': files,
    'weight' : mcCommonWeight + '*1.11', #updating k-factor
    'FilesPerJob' : 10

}


########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight
}



########VBF-V##########
files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['VBF-V'] = {
    'name': files,
    'weight':mcCommonWeight
}


####QCD background####
samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J_QCD') 
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J_QCD')
             #+nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J_QCD') MISSING
             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L_QCD'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}

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

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }







######DATA#######
samples['DATA']  = {   'name': [ ] ,
                       'weight' :'METFilter_DATA * LepWPCut' ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 40,
                  }

for Run in DataRun :
        directory = treeBaseDir+'Run2017_102X_nAODv5_Full2017v6/DATAl1loose2017v6__l2loose__l2tightOR2017v6'
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(directory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
#                        print(iFile)
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
