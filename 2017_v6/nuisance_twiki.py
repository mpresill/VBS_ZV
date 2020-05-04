# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 
#directly taken from: https://github.com/lenzip/CMSDataAnalysisSchoolPisa2019ScalarToWW/blob/master/Example2/nuisances.py
################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

xrootdPath  = 'root://eoscms.cern.ch/'

nuisances['lumi']  = {
               'name'  : 'lumi_13TeV',
               'samples'  : {
                   'DY'          : '1.025',  
                   'top'         : '1.025',  
                   'WW'          : '1.025',  
                   'VZ'           : '1.025',
                   'VVV'          : '1.025',
                   'WJets'        : '1.025',
                   'VBS_VV_QCD'   : '1.025',
                   'VBS_VV_EW'    : '1.025',
                   },
               'type'  : 'lnN',
              }

"""
massesFile = "masses.py"

if os.path.exists(massesFile) :
  handle = open(massesFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesFile, " does not exist."

for m in masses:
  nuisances['lumi']['samples']['ggH_hww_'+m] = '1.025'
  nuisances['lumi']['samples']['qqH_hww_'+m] = '1.025'

#### FAKES

# already divided by central values in formulas !
fakeW_EleUp       = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp'
fakeW_EleDown     = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown'
fakeW_MuUp        = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp'
fakeW_MuDown      = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown'
fakeW_statEleUp   = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp'
fakeW_statEleDown = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown'
fakeW_statMuUp    = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp'
fakeW_statMuDown  = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown'

nuisances['fake_syst_em']  = {
               'name'  : 'CMS_hwwem_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_em' : '1.30',
                             },
               }

nuisances['fake_syst_me']  = {
               'name'  : 'CMS_hwwme_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_me' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'hww_fake_ele',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_me'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'hww_fake_ele_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_me'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'hww_fake_mu',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_me'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'hww_fake_mu_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_me'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}
"""
##### B-tagger

btagbc_syst = ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')']

nuisances['btagbc']  = {
                'name'  : 'btag_heavy',
                'kind'  : 'weight',
               'type'  : 'shape',
                'samples'  : { 
                   'DY'          : btagbc_syst,  
                   'top'         : btagbc_syst,  
                   'WW'          : btagbc_syst,  
                   'VZ'          : btagbc_syst,
                   'VVV'         : btagbc_syst,
                   'WJets'       : btagbc_syst,
                   'VBS_VV_QCD'  : btagbc_syst,
                   'VBS_VV_EW'   : btagbc_syst,
                }
}

#for m in masses:
#  nuisances['btagbc']['samples']['ggH_hww_'+m] = btagbc_syst
#  nuisances['btagbc']['samples']['qqH_hww_'+m] = btagbc_syst


btagudsg_syst = ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')']

nuisances['btagudsg']  = {
                'name'  : 'btag_light',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    'DY'          : btagudsg_syst,
                    'top'         : btagudsg_syst,
                    'WW'          : btagudsg_syst,
                    'VZ'          : btagudsg_syst,
                    'VVV'         : btagudsg_syst,
                    'WJets'       : btagudsg_syst,
                    'VBS_VV_QCD'  : btagudsg_syst,
                    'VBS_VV_EW'   : btagudsg_syst,
                }
}
#for m in masses:
#  nuisances['btagudsg']['samples']['ggH_hww_'+m] = btagudsg_syst
#  nuisances['btagudsg']['samples']['qqH_hww_'+m] = btagudsg_syst


##### Trigger Efficiency

trig_syst = ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)']

nuisances['trigg']  = {
                'name'  : 'hww_trigger',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                  'DY'          : trig_syst,
                  'top'         : trig_syst,
                  'WW'          : trig_syst,
                  'VZ'          : trig_syst,
                  'VVV'         : trig_syst,
                  'WJets'       : trig_syst,
                  'VBS_VV_QCD'  : trig_syst,
                  'VBS_VV_EW'   : trig_syst, 
                },
}
#for m in masses:
#  nuisances['trigg']['samples']['ggH_hww_'+m] = trig_syst
#  nuisances['trigg']['samples']['qqH_hww_'+m] = trig_syst

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF2l__ele_'+eleWP+'__Up' , 'LepSF2l__ele_'+eleWP+'__Do' ]

nuisances['eff_e']  = {
                'name'  : 'eff_e',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                  'DY'          : id_syst_ele,
                  'top'         : id_syst_ele,
                  'WW'          : id_syst_ele,
                  'VZ'          : id_syst_ele,
                  'VVV'         : id_syst_ele,
                  'WJets'       : id_syst_ele,
                  'VBS_VV_QCD'  : id_syst_ele,
                  'VBS_VV_EW'   : id_syst_ele, 
                },
}
#for m in masses:
#  nuisances['eff_e']['samples']['ggH_hww_'+m] = id_syst_ele
#  nuisances['eff_e']['samples']['qqH_hww_'+m] = id_syst_ele


##### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF2l__mu_'+muWP+'__Up' , 'LepSF2l__mu_'+muWP+'__Do' ]

nuisances['eff_m']  = {
                'name'  : 'eff_m',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                  'DY'          : id_syst_mu,
                  'top'         : id_syst_mu,
                  'WW'          : id_syst_mu,
                  'VZ'          : id_syst_mu,
                  'VVV'         : id_syst_mu,
                  'WJets'       : id_syst_mu,
                  'VBS_VV_QCD'  : id_syst_mu,
                  'VBS_VV_EW'   : id_syst_mu, 
                },
}

#for m in masses:
#  nuisances['eff_m']['samples']['ggH_hww_'+m] = id_syst_mu
#  nuisances['eff_m']['samples']['qqH_hww_'+m] = id_syst_mu


##### Jet energy scale

nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                    'DY'          : ['1', '1'],
                    'top'         : ['1', '1'],
                    'WW'          : ['1', '1'],
                    'VZ'          : ['1', '1'],
                    'VVV'         : ['1', '1'],
                    'WJets'       : ['1', '1'],
                    'VBS_VV_QCD'  : ['1', '1'],
                    'VBS_VV_EW'   : ['1', '1'], 
                },
                'folderUp'   : treeBaseDir+mcProduction+mcSteps'JESup_suffix',
                'folderDown' : treeBaseDir+mcProduction+mcSteps'JESdo_suffix',
}

#for m in masses:
#  nuisances['jes']['samples']['ggH_hww_'+m] = ['1', '1']
#  nuisances['jes']['samples']['qqH_hww_'+m] = ['1', '1']

"""
##### MET energy scale

nuisances['met']  = {
                'name'  : 'scale_met',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'          : ['1', '1'],
                    'top'         : ['1', '1'],
                    'WW'          : ['1', '1'],
                    'VZ'          : ['1', '1'],
                    'VVV'         : ['1', '1'],
                    'WJets'       : ['1', '1'],
                    'VBS_VV_QCD'  : ['1', '1'],
                    'VBS_VV_EW'   : ['1', '1'], 
                    },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METdo'+skim,
}
"""
#for m in masses:
#  nuisances['met']['samples']['ggH_hww_'+m] = ['1', '1']
#  nuisances['met']['samples']['qqH_hww_'+m] = ['1', '1']


## Shape nuisance due to QCD scale variations for DY
nuisances['DYQCDscale']  = {
                'name'  : 'QCDscale_V',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

nuisances['TopQCDscale']  = {
                'name'  : 'QCDscale_top',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'top'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

nuisances['WWQCDscale']  = {
                'name'  : 'QCDscale_WW',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                   #'ggWW'    : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

#  - WW shaping
nuisances['WWresum']  = {
                'name'  : 'WWresum',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
                }


nuisances['DYttnorm']  = {
               'name'  : 'CMS_hww_DYttnorm', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
              }

nuisances['WWnorm']  = {
               'name'  : 'CMS_hww_WWnorm', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
              }

nuisances['Topnorm']  = {
               'name'  : 'CMS_hww_Topnorm', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
              }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              'samples' : {}
             }