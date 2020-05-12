supercut_vector = [##2 lepton selection:  pt >30 |eta|<2.5 (2.4) pt>30 GeV
  'nLepton == 2. && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.',
  'mll >60. && mll <120.'
##jet selection: 1 FJ, pt>200 GeV, |eta|<2.4  + 2 jets with pt>30 and |eta|<5 and with mjj_vbs>200GeV and detajj_vbs>2.0
 #'nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. && fabs(Alt$(CleanFatJet_eta[0],-9999.))<2.4',
 'nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0'  ##'Sum$(CleanJet_pt>30.)>=2 && fabs(Alt$(CleanJet_eta[0],-9999.))<5.0',
 #'mjj_vbs_AK4NotFat > 200 && eta1eta2 < 0.' 
 'detajj_vbs_AK4NotFat>2.0'
]
#at some point we should add a selection of FatJet in case of more than one candidate...
#and same for vbs_jets in case of more than two candidates

supercut = ' && '.join(supercut_vector)

cuts['preselection'] = '1.'


#############################
######### BOOSTED SR
#############################
cuts['SR_boosted_minimal']= '2lSF &&\
                    mll >80. && mll <100. &&\
                    Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50.'

cuts['SR_boosted_leptons']= '2lSF &&\
                    mll >80. && mll <100. &&\
                    Alt$(Lepton_pt[0],0.)>=40. && Zlep_1 < 1.0 && Zlep_2 < 1.0  && Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. '

cuts['SR_boosted_j1j2']= '2lSF &&\
                    mll >80. && mll <100. &&\
                    Alt$(Lepton_pt[0],0.)>=40.  && Alt$(CleanJet_pt[0],0.)>=80. && Alt$(CleanJet_pt[1],0.)>=50. &&  mjj_vbs_AK4NotFat >  300.'


#############################
######### BOOSTED CR
#############################
cuts['DYJets_CR_boosted'] = '2lSF && bVeto '

cuts['Top_CR_boosted'] = 'bReq && 2lOF'

#############################
######### RESOLVED SR
#############################



#############################
######### RESOLVED CR
#############################
