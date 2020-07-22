import os
import copy
import inspect



configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

# TO BE FIXED: change all CleanJet to CleanJet[CleanJetNotFat_jetIdx] after testing
#    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
#same for the index in the tagging


#aliases = {}

# imported from samples.py:
# samples, signals
mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1, 0)',
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

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'samples': ['top']
}
# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples


#bVeto 
aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) == 0'
    #'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
}

#bReq
aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) >= 1'
    #'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}


# B tag scale factors
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF']),
    'samples': mc
}


aliases['category']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[0]"
    }


aliases['vbs_jet_0']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[1]"
    }

aliases['vbs_jet_1']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[2]"
    }

aliases['V_jet_0']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[3]"
    }

aliases['V_jet_1']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[4]"
    }

aliases['Mjj_max']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[5]"
    }
aliases['detajj_mjjmax']= {
      'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[6]"
}

aliases['V_jet_mass']= {
      'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx)[7]"
}
