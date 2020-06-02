import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]',
    'samples': mc
} 


# B tagging

aliases['bVeto'] = {
    'expr': '(Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1241) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1241) >= 1)'
}


aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}


## BAD NOT TO INCLUDE THIS
## THIS WILL BE ADDED IN NEXT SKIM
# # PU jet Id SF

# puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')

# aliases['PUJetIdSF'] = {
#     'linesToAdd': [
#         'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#         '.L %s/patches/pujetidsf_event.cc+' % configurations
#     ],
#     'class': 'PUJetIdEventSF',
#     'args': (puidSFSource, '2018', 'loose'),
#     'samples': mc
# }

# aliases['nvtx_reweighting'] = {
#     'class': 'NvtxReweight',
#     # Using Z->mm factors for both electron and muon regions
#     'args':("%s/VBSjjlnu/Full2018v6/corrections/zmmnorm_reweighting_Zmm_fit.txt" % configurations),
#     'linesToAdd' : [
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         '.L %s/patches/nvtx_reweight.cc+' % configurations
#    ],
#     'samples' : mc      
# }