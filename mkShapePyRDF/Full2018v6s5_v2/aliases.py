import os
import copy
import inspect

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

aliases['detavbs_jetpt_bin'] = {
    'expr': '1* ((deltaeta_vbs < 3.5)  && vbs_1_pt < 75) + \
             2* ((deltaeta_vbs >= 3.5 && deltaeta_vbs < 5.5)  && vbs_1_pt < 75) + \
             3* ((deltaeta_vbs >= 5.5)  && vbs_1_pt < 75) + \
            \
             4* ((deltaeta_vbs < 3)                        &&  ( vbs_1_pt >= 75 && vbs_1_pt <150)  ) + \
             5* ((deltaeta_vbs >= 3  && deltaeta_vbs < 4)  &&  ( vbs_1_pt >= 75 && vbs_1_pt <150) ) + \
             6* ((deltaeta_vbs >= 4)                       &&  ( vbs_1_pt >= 75 && vbs_1_pt <150) ) + \
            \
             7* ((deltaeta_vbs < 3.5)  &&  ( vbs_1_pt >= 150)  ) + \
             8* ((deltaeta_vbs >= 3.5 )  &&  ( vbs_1_pt >= 150) )'
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


# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['whad_pt'] = {
    'expr': "Whad_pt( VBS_category, V_jets_maxmjj_massWZ, CleanJet_pt, CleanJet_eta, CleanJet_phi, Jet_mass,CleanJet_jetIdx )"
}

