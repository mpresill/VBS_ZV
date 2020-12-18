# -*- coding: utf-8 -*-
# cuts
# NB: mjj and detajj cannot be used!!!! (they belong to WW analysis)
supercut_vector = [#2 lepton selection:  pt >30 |eta|<2.5 (2.4) pt>50 GeV
  'nLepton == 2 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50',

#jet selection: 1 FJ, pt>200 GeV, |eta|<2.4  + 2 jets with pt>30 and |eta|<5 and with mjj_vbs>200GeV and detajj_vbs>2.0
'nFatJet == 1 && FatJet_pt[0] >= 200. && fabs(Alt$(FatJet_eta[0],-9999.))<2.4',
'Sum$(CleanJet_pt>30.)>=2 && fabs(Alt$(CleanJet_eta[0],-9999.))<5.0',
 'mjj_vbs > 200 && detajj_vbs > 2.0'
]
#at some point we should add a selectio of FatJet in case of more than one candidate

supercut = ' && '.join(supercut_vector)

#####Signal Regions

cuts['MinimalVBS']='1.'

###check btagging algorithm

cuts['Mild_SR'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50 && Alt$(Lepton_pt[1],0.)>50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) ) &&  Alt$(FatJet_msoftdrop[0],0.)>65 && Alt$(FatJet_msoftdrop[0],0.)<105 && Alt$(FatJet_tau2[0]/FatJet_tau1[0],0.)<0.55 && \
             mll_vbs>76 && mll_vbs<107  &&\
             mjj_vbs > 400 && detajj_vbs > 3.5 &&\
             Sum$(Jet_btagDeepB[CleanJet_jetIdx ] > 0.1522) == 0 '

cuts['Tight_SR'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50 && Alt$(Lepton_pt[1],0.)>50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && Alt$(FatJet_msoftdrop[0],0.)>65 && Alt$(FatJet_msoftdrop[0],0.)<105 && Alt$(FatJet_tau2[0]/FatJet_tau1[0],0.)<0.55 \
             && mll_vbs>76 && mll_vbs<107 \
             && Sum$(Jet_btagDeepB[CleanJet_jetIdx ] > 0.1522) == 0 \
             && mjj_vbs>800 && detajj_vbs>4.0'

#########Control regions

cuts['DY_CR'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50 && Alt$(Lepton_pt[1],0.)>50  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4))  && mll_vbs>76 && mll_vbs<107\
    && (FatJet_msoftdrop[0] < 65 || FatJet_msoftdrop[0] >105)\
    && Sum$(Jet_btagDeepB[CleanJet_jetIdx ] > 0.1522) == 0\
    && mjj_vbs>800 && detajj_vbs>4.0'

cuts['Top_CR'] = '(Alt$(FatJet_msoftdrop[0],0.)>65 && Alt$(FatJet_msoftdrop[0],0.)<105 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13)))' #SR cuts and bveto condition inverted + 2opposite flavour leptons ---CHECK THIS CR!!

cuts['Top_CR_mll'] = '(Alt$(FatJet_msoftdrop[0],0.)>65 && Alt$(FatJet_msoftdrop[0],0.)<105 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13)))\
    && mll_vbs >76 && mll_vbs>105'


#cuts['Wjets_CR'] = '((Alt$(FatJet_msoftdrop[0],0.)>40 && Alt$(FatJet_msoftdrop[0],0.)<65) || (Alt$(FatJet_msoftdrop[0],0.)>105 && Alt$(FatJet_msoftdrop[0],0.)<150)  && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0)'#SR cuts and msoftdrop window inverted

"""
cuts['Boosted']  = 'nFatJet == 1 && FatJet_pt[0] >=200. \
    && nJet >=2 && Jet_pt[0] >= 30. && Jet_pt[1]> 30.'
# high invariant mass from initial partons scattering
cuts['Resolved'] = 'nJet >=4 && Jet_pt[0] >= 30. && Jet_pt[1]> 30.&& Jet_pt[2] >= 30. && Jet_pt[3]> 30.'
#pairing 2 resolved hadronic decay of V boson (pair with mass near W/Z)
#pairing 2 tag jets with max inv mass pair
"""
