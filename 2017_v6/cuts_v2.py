supercut_vector = [##2 lepton selection:  pt >30 |eta|<2.5 (2.4) pt>30 GeV
  'nLepton == 2. && Alt$(Lepton_pt[0],0.)>=30. && Alt$(Lepton_pt[1],0.)>=30.',

##jet selection: 1 FJ, pt>200 GeV, |eta|<2.4  + 2 jets with pt>30 and |eta|<5 and with mjj_vbs>200GeV and detajj_vbs>2.0
 'nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. && fabs(Alt$(CleanFatJet_eta[0],-9999.))<2.4',
 'nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0'  ##'Sum$(CleanJet_pt>30.)>=2 && fabs(Alt$(CleanJet_eta[0],-9999.))<5.0',
 #'detajj_AK4NotFat >2.0 &&  mjj_AK4NotFat > 300 ' UPDATE THIS!!!!
]
#at some point we should add a selection of FatJet in case of more than one candidate...
#and same for vbs_jets in case of more than two candidates

supercut = ' && '.join(supercut_vector)

cuts['preselection'] = '1.'

cuts['mjj']= 'mjj_vbs_AK4NotFat > 200 && detajj_AK4NotFat >2.0'

###############################
#####Signal Regions
###############################
"""

cuts['SR_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=35. && Alt$(Lepton_pt[1],0.)>=35.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>30. && Alt$(Lepton_pt[1],0.)>30.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>85. && mll_vbs<99.  &&\
                    detajj_AK4NotFat >2.5 &&  mjj_vbs_AK4NotFat > 300 && fabs(Alt$(CleanJet_pt,-9999.))>50. &&\
                    Sum$(Jet_btagDeepB[ CleanJetNotFat_jetIdx ] > 0.1522) == 0 '


cuts['SR_medium'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=35. && Alt$(Lepton_pt[1],0.)>=35.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>30. && Alt$(Lepton_pt[1],0.)>30.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>85. && mll_vbs<99.  &&\
                    detajj_AK4NotFat >3.0 &&  mjj_vbs_AK4NotFat > 300 && fabs(Alt$(CleanJet_pt,-9999.))>50. &&\
                    Sum$(Jet_btagDeepB[ CleanJetNotFat_jetIdx ] > 0.1522) == 0 &&\
                    fabs((Alt$(CleanFatJet_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj_vbs_AK4NotFat ) < 0.7 ' 


cuts['SR_tight'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=35. && Alt$(Lepton_pt[1],0.)>=35.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>30. && Alt$(Lepton_pt[1],0.)>30.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>85. && mll_vbs<99.  &&\
                    detajj_AK4NotFat >3.5 &&  mjj_vbs_AK4NotFat > 500 && fabs(Alt$(CleanJet_pt,-9999.))>50. &&\
                    Sum$(Jet_btagDeepB[ CleanJetNotFat_jetIdx ] > 0.1522) == 0 &&\
                    fabs((Alt$(CleanFatJet_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj_vbs_AK4NotFat ) < 0.7 &&\
                    Alt$(CleanFatJet_mass,0.)>50. && Alt$(CleanFatJet_mass,0.)<120.' 

###############################
#Control Regions
###############################


cuts['DY_CR'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=35. && Alt$(Lepton_pt[1],0.)>=35.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>30. && Alt$(Lepton_pt[1],0.)>30.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4))  && mll_vbs>60. && mll_vbs<120.\
    && mjj_vbs_AK4NotFat >300. && detajj_vbs_AK4NotFat >3.5'

cuts['Top_CR'] = '(Alt$(CleanFatJet_mass[0],0.)>65. && Alt$(CleanFatJet_mass[0],0.)<105. && Sum$(Jet_btagDeepB[CleanJetNotFat_jetIdx] > 0.1522) >= 1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13)))\
    && mll_vbs>60. && mll_vbs<120.'

cuts['Wjets_CR'] = '((Alt$(CleanFatJet_mass[0],0.)>40. && Alt$(CleanFatJet_mass[0],0.)<50.) || (Alt$(CleanFatJet_mass[0],0.)>105. && Alt$(CleanFatJet_mass[0],0.)<150.)  && Sum$(Jet_btagDeepB[CleanJetNotFat_jetIdx] > 0.1522) == 0)'#SR cuts and msoftdrop window inverted
"""