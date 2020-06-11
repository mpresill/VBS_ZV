cuts["supercut"] = {
    'expr' : ' nLepton == 2. && Alt(Lepton_pt[0],0.)>=25. && Alt(Lepton_pt[1],0.)>=20. \
            && mll >60. && mll <120. \
            && SumVec(CleanJet_pt>30.)>=2 \
            && fabs(Alt(CleanJet_eta,-9999.))<5.0 ',
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
#in the preselection we require at least two Ak4 jets (not necessarily cleaned from  AK8) and two leptons

#cuts['preselection'] = '1.'


##a selection on VBS_jets is still required

#############################
######### BOOSTED SR
#############################
cuts['SR_boosted_minimal'] = {
    'expr': '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 &&  fabs(Alt(Lepton_eta[0],-9999.))<2.5 && fabs(Alt(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && fabs(Alt(Lepton_eta[0],-9999.))<2.4 && fabs(Alt(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    nCleanJetNotFat >= 2 && fabs(Alt(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 &&\
                    nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. && fabs(Alt(CleanFatJet_eta[0],-9999.))<2.4',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }


#############################
######### BOOSTED CR
#############################
"""vim 
cuts['DY_old'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25 && Alt$(Lepton_pt[1],0.)>=25  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>20 && Alt$(Lepton_pt[1],0.)>20  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4)) \
    && mll>80 && mll<100\
    && ((CleanFatJet_mass[0] > 50 && CleanFatJet_mass[0] < 65) || (CleanFatJet_mass[0] >100 && CleanFatJet_mass[0] < 120))\
    && Sum$(Jet_btagDeepB[CleanJet_jetIdx ] > 0.1522) == 0\
    && mjj_vbs_AK4NotFat>200 && detajj_vbs_AK4NotFat>4.0'
cuts['DY_CR_Matteo'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) && bVeto '
cuts['Top_CR_Matteo'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) && bReq'
cuts['Top_CR_old'] = '(Alt$(CleanFatJet_mass[0],0.)>65 && Alt$(CleanFatJet_mass[0],0.)<105 && Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13)))\
    && mll >80 && mll>120'
"""
#############################
######### RESOLVED SR
#############################
#add selection on the V-jet

"""cuts['SR_resolved_minimal'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 &&  fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) ) &&  mll >80. && mll <100. &&\
                    nCleanJet >= 4 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 && nCleanFatJet == 0'
"""