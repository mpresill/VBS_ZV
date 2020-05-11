import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) 
configurations = os.path.dirname(configurations)
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]


# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}


#b-tagging 
bAlgo = 'DeepB'
bWP = '0.1522'

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1)'
}


#b-tag scale factors OLD
"""
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}


systs = ['jes']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
"""

############################################################
#############additional variables
############################################################
aliases['M_ZV'] = {
             'class': 'VBSvar_AK4',
             'args': ("M_ZV"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]           
 }

aliases['mll_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("mll_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['mjj_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("mjj_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['detajj_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("detajj_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['mjj_vbs_AK4NotFat'] = {
    'class': 'WHSS_wpt_v3',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/mjj_max_vbs.cc+'.format(configurations)
    ]
}

aliases['detajj_vbs_AK4NotFat'] = {
    'class': 'detajj',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/detajj_mjj_max_vbs.cc+'.format(configurations)
    ]
}

aliases['eta1eta2'] = {
    'class': 'eta12',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/eta12_mjj_max_vbs.cc+'.format(configurations)
    ]
}
