supercut = ' nLepton == 2. && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20. \
            && mll >60. && mll <120. \
            && nCleanJet >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 '
#in the preselection we require at least two Ak4 jets (not necessarily cleaned from  AK8) and two leptons

cuts['preselection'] = '1.'


##a selection on VBS_jets is still required

#############################
######### BOOSTED SR
#############################
cuts['SR_boosted_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 &&  fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 &&\
                    nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. && fabs(Alt$(CleanFatJet_eta[0],-9999.))<2.4'


"""
cuts['SR_boosted_minimal']= '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50.'

cuts['SR_boosted_leptons']= '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&   mll >80. && mll <100. &&\
                    Alt$(Lepton_pt[0],0.)>=40. && Zlep_1 < 1.0 && Zlep_2 < 1.0  && Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. '

cuts['SR_boosted_j1j2']= '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    Alt$(Lepton_pt[0],0.)>=40.  && Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. &&  mjj_vbs_AK4NotFat >  300.'
"""
#############################
######### BOOSTED CR
#############################
"""
cuts['DYJets_CR_boosted'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) && bVeto '

cuts['Top_CR_boosted'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) && bReq'
"""
#############################
######### RESOLVED SR
#############################
#add selection on the V-jet

cuts['SR_resolved_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 &&  fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    nCleanJet >= 4 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 && nCleanFatJet == 0'


#############################
######### RESOLVED CR
#############################
