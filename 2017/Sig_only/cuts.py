# -*- coding: utf-8 -*-

# cuts


supercut_vector = [
  'nLepton == 2' ,
  '(Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=40 && Alt$(Lepton_pt[1],0.)>=40  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5) || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>30 && Alt$(Lepton_pt[1],0.)>30  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4)', #ee (µµ) pt >40(30) |eta|>2.5 (2.4)
 

'nFatJet == 1 && FatJet_pt[0] >= 200.',
'Sum$(CleanJet_pt>30.)>=2', #2 jets
'mll>76 && mll<107', #around Z peak

]


supercut = ' && '.join(supercut_vector)


cuts['all'] ='1.'


"""

cuts['Mild_signal'] = 'Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0]<105,0.) && mjj > 200 && detajj > 2.0 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
 

cuts['Top_CR'] = 'Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0]<105,0.) && mjj > 200 && detajj > 2.0 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'


cuts['Wjets_CR'] = 'Alt$(FatJet_mass[0],0.)<65 || Alt$(FatJet_mass[0],0.)>105 && mjj > 200 && detajj > 2.0 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'

"""
"""
cuts['Boosted']  = 'nFatJet == 1 && FatJet_pt[0] >=200. \
    && nJet >=2 && Jet_pt[0] >= 30. && Jet_pt[1]> 30.'
# high invariant mass from initial partons scattering


cuts['Resolved'] = 'nJet >=4 && Jet_pt[0] >= 30. && Jet_pt[1]> 30.&& Jet_pt[2] >= 30. && Jet_pt[3]> 30.'
#pairing 2 resolved hadronic decay of V boson (pair with mass near W/Z)
#pairing 2 tag jets with max inv mass pair

"""




