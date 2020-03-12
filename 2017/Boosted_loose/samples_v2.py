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
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP





################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
GenLepMatch   = 'GenLepMatch'+Nlep+'l'

METFilter_MC = 'METFilter_MC'
"""
################################################
############### B-Tag  WP ######################
################################################

bAlgo = 'DeepB'
btagSF = 'btagWeight'
bWP = '0.1522'

bVeto = '( Alt$(CleanJet_pt[0],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[0]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[1],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[1]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[2],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[2]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[3],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[3]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[4],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[4]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[5],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[5]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[6],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[6]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[7],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[7]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[8],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[8]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[9],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[9]],0)<'+bWP+' )\
      && ( Alt$(CleanJet_pt[10],0)<20 || Alt$(Jet_btag'+bAlgo+'[CleanJet_jetIdx[10]],0)<'+bWP+' )\
      '

SFweight += '*'+btagSF

"""
#########################################
############ MC COMMON ##################
#########################################

#
# SFweight does not include btag weights
#
# -> genmatching is not required for Vg sample
#

mcCommonWeightNoMatch = 'XSWeight*' + SFweight + '*METFilter_MC'
mcCommonWeight        = 'XSWeight*' + SFweight + '*' + GenLepMatch +'*METFilter_MC'


###########################################
#############  SIGNAL  ###############
###########################################

############ ZZTo2L2Q ############

files = nanoGetSampleFiles(mcDirectory ,'ZTo2L_ZTo2J' )

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2
}

############ ZWTo2L2J ############

files = nanoGetSampleFiles(mcDirectory ,'WpTo2J_ZTo2L' ) + \
    nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L')

samples['ZW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2
}


###########################################
#############  BACKGROUNDS  ###############
###########################################
useDYtt = False
############ DY ############
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

"""files= nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_ext1') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200') + \
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500') +\
                                     nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf')
"""
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
    'weight': mcCommonWeight,
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
    'weight' : mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',  #filter tops and Higgs
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
    'weight' : mcCommonWeight + '*1.53/1.4', #updating k-factor
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
    'weight': mcCommonWeight
}







