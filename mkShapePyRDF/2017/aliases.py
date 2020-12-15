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


############b tag
# B tagging
#loose 0.1241
#tight 0.7527

#bVeto 
aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1241) == 0'
    #'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
}

#bReq
aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1241) >= 1'
    #'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}

aliases['bReqTight'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.7527) >= 1'
    #'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
}


# B tag scale factors
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}
#'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))'
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}
#TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))
aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF']),
    'samples': mc
}

aliases['cat']={
    'expr': "jets_cat(nCleanJet, nFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx, FatJet_mass, nLepton, Lepton_eta)",
    }




#jets: problem if -999


aliases['Mjj_max']={
    'expr': "cat[0]"
    }
aliases['detajj_mjjmax']= {
      'expr': "cat[1]"
}
aliases['dphijj_mjjmax']={'expr': 'cat[2]'}

aliases['V_jet_mass']= {
      'expr': "cat[3]"
}
aliases['Zepp_ll']= {
      'expr': "cat[4]"
}
aliases['Zlep_1']= {
      'expr': "cat[5]"
}
aliases['Zlep_2']= {
      'expr': "cat[6]"
}

aliases['vbs_jet_pt1']= {
      'expr': "cat[7]"
}
aliases['vbs_jet_pt2']= {
      'expr': "cat[8]"
}
aliases['vbs_jet_eta1']= {
      'expr': "cat[9]"
}
aliases['vbs_jet_eta2']= {
      'expr': "cat[10]"
}
aliases['V_jet_pt1']= {
      'expr': "cat[11]"
}
aliases['V_jet_pt2']= {
      'expr': "cat[12]"
}
aliases['V_jet_eta1']= {
      'expr': "cat[13]"
}
aliases['V_jet_eta2']= {
      'expr': "cat[14]"
}
aliases['category']={
    'expr': "cat[15]"
    }


aliases['ptllDYW_NLO'] = {
    'expr': '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll*gen_ptll+9.19509e-05*gen_ptll*gen_ptll*gen_ptll-6.0212e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll*gen_ptll-4.29708e-09*gen_ptll*gen_ptll*gen_ptll+3.35791e-11*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
}
aliases['ptllDYW_LO'] = {
    'expr': '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
}
