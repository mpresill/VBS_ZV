# nuisances
# name of samples here must match keys in samples.py 
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

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()

# name of samples here must match keys in samples.py

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
# luminosity uncertainty is 2.3%
#for data driven background should not be included(?)
nuisances['lumi']  = {
    'name'  : 'lumi_13TeV_2017',
    'samples'  : {
        'DY'       : '1.023',  
        'top'      : '1.023',  
        'VBS_VV_QCD'       : '1.023',   
        'VBS_VV_EW'       : '1.023',
        'WW'       : '1.023',
        'VZ'   : '1.023',
        'ggWW'       : '1.023',
        'VVV'      : '1.023',
        'WJets'  : '1.023',
        'VBF-V'  : '1.023',
        'WW_ewk'   : '1.023',
    },
    'type'  : 'lnN',
}

#### FAKES
"""
if Nlep == '2' :
    # already divided by central values in formulas !
    fakeW_EleUp       = fakeW+'_EleUp'
    fakeW_EleDown     = fakeW+'_EleDown'
    fakeW_MuUp        = fakeW+'_MuUp'
    fakeW_MuDown      = fakeW+'_MuDown'
    fakeW_statEleUp   = fakeW+'_statEleUp'
    fakeW_statEleDown = fakeW+'_statEleDown'
    fakeW_statMuUp    = fakeW+'_statMuUp'
    fakeW_statMuDown  = fakeW+'_statMuDown'

else:
    fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
    fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

## FIXME: check the 30% lnN
nuisances['fake_syst']  = {
    'name'  : 'CMS_fake_syst',
    'type'  : 'lnN',
    'samples'  : {
        'Fake_lep' : '1.30',
    },
}

nuisances['fake_ele']  = {
    'name'  : 'fake_ele',
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
        'Fake_lep'     : [ fakeW_EleUp , fakeW_EleDown ],
    },
}
nuisances['fake_ele_stat']  = {
    'name'  : 'fake_ele_stat',
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
        'Fake_lep'      : [ fakeW_statEleUp , fakeW_statEleDown ],
    },
}

nuisances['fake_mu']  = {
    'name'  : 'fake_mu',
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
        'Fake_lep'     : [ fakeW_MuUp , fakeW_MuDown ],
    },
}


nuisances['fake_mu_stat']  = {
    'name'  : 'hww_fake_mu_stat',
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
        'Fake_lep'     : [ fakeW_statMuUp , fakeW_statMuDown ],
    },
}

"""

################################ THEORY UNCERTAINTIES  #################################
nuisances['QCDscale']  = {
    'name'  : 'QCDscale',
    'type'  : 'lnN',
    'samples'  : {
        #'ChMisId'  : '1.10',
	    'ttbar'   : '1.10',
        'WZ'   : '1.10',
        'ZZ'   : '1.10',
        'VVV'  : '1.10',
       # 'DPS'   : '1.10',
       # 'Vg'    : '1.10' ,
       # 'WpWp_EWK': '1.10' ,
       # 'WW_strong': '1.10' ,
    },
}

nuisances['QCDscale_gg_accept']  = {
    'name'  : 'QCDscale_gg_accept',
    'type'  : 'lnN',
    'samples'  : {
         'DY': '0.976/1.012' ,
       #  'WpWp_EWK': '0.994/0.981' ,
    },
 }


# pdf uncertainty

nuisances['pdf']  = {
    'name'  : 'pdf',
    'type'  : 'lnN',
    'samples'  : {
        #'ChMisId'  : '1.005',
	   'top'   : '1.01',
        'WZ'   : '1.04',
        'ZZ'   : '1.04',
        'VVV'  : '1.01',
        #'DPS'   : '1.01',
        #'Vg'    : '1.01' ,
        #'WpWp_EWK': '1.01' ,
        #'WW_strong': '1.01' ,
    },
}

#FIXME: check this 3%
nuisances['QCDscale_VZ']  = {
    'name'  : 'QCDscale_VZ',
    'samples'  : {
        'WZ' : '1.03',
        'ZZ' : '1.03',
    },
    'type'  : 'lnN'
}


################################ BKG ESTIMATION UNCERTAINTIES  #################################
"""
nuisances['WZ_norm']  = {
               'name'  : 'WZ_norm',
               'samples'  : {
                   'WZ'   : '1.3',
		},
               'type'  : 'lnN',
}

#7% of uncertainty due to systematic uncertainties on simulations
nuisances['charge_flip']  = {
               'name'  : 'charge_flip',
               'samples'  : {
                   'ChMisId'   : '1.07',
				   'ttbar'   : '1.01',
                   },
               'type'  : 'lnN',
              }
"""
###### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }



##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc)
}
##### Electron Efficiency and energy scale

#nuisances['eff_e'] = {
#    'name': 'CMS_eff_e_2017',
#    'kind': 'weight',
#    'type': 'shape',
##    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
#   'samples': dict((skey, ['ttHMVA_2l_ele_SF_Up', 'ttHMVA_2l_ele_SF_Down']) for skey in mc)
#}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

#nuisances['eff_m'] = {
#    'name': 'CMS_eff_m_2017',
#    'kind': 'weight',
#    'type': 'shape',
##    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
#    'samples': dict((skey, ['ttHMVA_2l_mu_SF_Up', 'ttHMVA_2l_mu_SF_Down']) for skey in mc)
#}
#
nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']

for js in jes_systs:
  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': makeMCDirectory('JESup_suffix'),
      'folderDown': makeMCDirectory('JESdo_suffix'),
      'AsLnN': '1'
  }

  ##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        #'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        #'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Zg': variations,
        'Wg': variations,
        'ZZ': variations,
        'WZ': variations
        #'WgS': variations,
        #'ZgS': variations
    }
}


# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
# Use the following if you want to apply the automatic combine MC stat nuisances->Faster than bin-by-bin
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              'samples' : {}
             }




# Differnt type of uncentainties: type->ln N: (modify only event yeld) use a lognorm distributions with sigma = uncertainty. For normalization rateParam
                                        # can be used--> use a uniform distribution;
                                      # Shape: modify not only the events yelds but the event selection too (the shape) will run the varied shapes
                                             # according to the following two possible kinds
                                # kind-> weight: Use the specified weight to reweight events;
                                       # tree: uses the provided alternative trees;
# The MC statistics is a particular uncertainty: is caused by our finite statistics used to elaborate the template fits. Two approach: unfied and bin-by-bin (bbb)
