# cuts

#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>50. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0 \
           '
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet

#cuts['preselection'] = '1.'

#######################################
#
#   BOOSTED CATEGORY
#
#######################################
cuts['Boosted_topcr']  = 'mjj > 200 && detajj > 2.0 && nCleanFatJet==1 && Alt$(CleanFatJet_mass[0],0.)>65 && Alt$(CleanFatJet_mass[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Boosted_DYcr']  = 'mjj > 200 && detajj > 2.0 && nCleanFatJet==1 && (Alt$(CleanFatJet_mass[0],0.)<65 || Alt$(CleanFatJet_mass[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Boosted_SR']  = 'mll>80. && mll<105. && mjj > 200. && detajj > 2.0 && nCleanFatJet==1 && Alt$(CleanFatJet_mass[0],0.)>65 && Alt$(CleanFatJet_mass[0],0.)<105 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#######################################
#
#   RESOLVED CATEGORY
#
#######################################
cuts['Resolved_topcr']  = 'nCleanJet == 4 && mjj > 200 && detajj > 2.0 && nCleanFatJet==0 &&  bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Resolved_DYcr']  = 'nCleanJet == 4 && mjj > 200 && detajj > 2.0 && nCleanFatJet==0 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Resolved_SR']  = 'nCleanJet == 4 && mll>80. && mll<105. && mjj > 200. && detajj > 2.0 && nCleanFatJet==0 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'


