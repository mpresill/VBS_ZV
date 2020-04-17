supercut_vector = [##2 lepton selection:  pt >30 |eta|<2.5 (2.4) pt>50 GeV
  'nLepton == 2. && Alt$(Lepton_pt[0],0.)>=50. && Alt$(Lepton_pt[1],0.)>=50.',

##jet selection: 1 FJ, pt>200 GeV, |eta|<2.4  + 2 jets with pt>30 and |eta|<5 and with mjj_vbs>200GeV and detajj_vbs>2.0
 'nCleanFatJet >= 1 && CleanFatJet_pt >= 200. && fabs(Alt$(CleanFatJet_eta,-9999.))<2.4',
 'nCleanJet >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0',  ##'Sum$(CleanJet_pt>30.)>=2 && fabs(Alt$(CleanJet_eta[0],-9999.))<5.0',
]
#at some point we should add a selection of FatJet in case of more than one candidate...
#and same for vbs_jets in case of more than two candidates

supercut = ' && '.join(supercut_vector)

#####Signal Regions
####effect of differenct cuts
cuts['preselection'] = '1.'

#cuts on the AK4 jets

cuts['SR_mjj'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                    mjj_vbs > 400.'
cuts['SR_detajj'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                    detajj>3.0'
cuts['SR_etaPlane'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                    (Alt$(CleanJet_eta[0],-9999.)*Alt$(CleanJet_eta[1],-9999.)) < 0'
cuts['SR_btag'] =  '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                    Sum$(Jet_btagDeepB[CleanJet_jetIdx ] > 0.1522) == 0'

#cuts on AK8 jets
cuts['SR_FJ'] =  '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                  nCleanFatJet == 1 '
cuts['SR_FJmass'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                  Alt$(CleanFatJet_mass,0.)>65. && Alt$(CleanFatJet_mass,0.)<105.'
cuts['SR_nFJ_mjj'] =  '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                  nCleanFatJet == 1 &&\
                  mjj_vbs > 400. && detajj>3.0 '
cuts['SR_FJmass_mjj'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=50 && Alt$(Lepton_pt[1],0.)>=50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>50. && Alt$(Lepton_pt[1],0.)>50.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4) )  && mll_vbs>83. && mll_vbs<99.  &&\
                  Alt$(CleanFatJet_mass,0.)>65. && Alt$(CleanFatJet_mass,0.)<105. &&\
                   mjj_vbs > 400. && detajj>3.0 '




