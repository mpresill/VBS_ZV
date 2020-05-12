supercut_vector = [##2 lepton selection:  pt >30 |eta|<2.5 (2.4) pt>30 GeV
  'nLepton == 2. && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.',
   'mll >60. && mll <120.',
##jet selection: 1 FJ, pt>200 GeV, |eta|<2.4  + 2 jets with pt>30 and |eta|<5 and with mjj_vbs>200GeV and detajj_vbs>2.0
 'nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. && fabs(Alt$(CleanFatJet_eta[0],-9999.))<2.4',
 'nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0',  ##'Sum$(CleanJet_pt>30.)>=2 && fabs(Alt$(CleanJet_eta[0],-9999.))<5.0',
 'mjj_vbs_AK4NotFat > 200 && detajj_vbs_AK4NotFat>2.0'
 #'mjj_vbs_AK4NotFat > 200 && eta1eta2 < 0.' 
]
#at some point we should add a selection of FatJet in case of more than one candidate...
#and same for vbs_jets in case of more than two candidates

supercut = ' && '.join(supercut_vector)

cuts['preselection'] = '1.'

#cuts['mjj']= 'mjj_vbs_AK4NotFat > 200'# && detajj_vbs_AK4NotFat >2.0'

#cuts['detajj'] ='detajj_vbs_AK4NotFat >2.0'

#cuts['mjj_etaregions'] = 'eta1eta2 < 0.'  #il taglio in eta region butta meno segnale di quello in detajj

###############################
#####Signal Regions 5
###############################

cuts['SR_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=20. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll>80. && mll<100.  &&\
                    mjj_vbs_AK4NotFat > 200 &&\
                    Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. '#detajj_vbs_AK4NotFat >2.5 &&  

cuts['SR_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=20. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll>80. && mll<100.  &&\
                    mjj_vbs_AK4NotFat > 200 &&\
                    bVeto &&\
                    Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. '#detajj_vbs_AK4NotFat >2.5 &&  


cuts['SR_tight'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=20. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll>80. && mll<100.  &&\
                    mjj_vbs_AK4NotFat > 200 &&\
                    bVeto &&\
                    Alt$(Lepton_pt[0],0.)>=40. && Zlep_1 < 1.0 && Zlep_2 < 1.0  && Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. ' 
                    #detajj_vbs_AK4NotFat >3.5 &&  
###############################
#Control Regions
###############################


cuts['DYJets_CR'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=20. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4))  && mll>60. && mll<120.\
    && bVeto'#&& detajj_vbs_AK4NotFat >3.5


cuts['Top_CR'] = 'bReq && ((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13) || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13))'


"""
cuts['Wjets_CR'] = '((Alt$(CleanFatJet_mass[0],0.)>40. && Alt$(CleanFatJet_mass[0],0.)<50.) || (Alt$(CleanFatJet_mass[0],0.)>105. && Alt$(CleanFatJet_mass[0],0.)<150.)  && bVeto'#SR cuts and msoftdrop window inverted
"""