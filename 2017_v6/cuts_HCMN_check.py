supercut_vector = [
  'nLepton == 2. && Alt$(Lepton_pt[0],0.)>=150. && Alt$(Lepton_pt[1],0.)>=100.',
  'mll >300.',
  '(Lepton_pdgId[0]*Lepton_pdgId[0] == - 11*11)  && (Lepton_pdgId[0]*Lepton_pdgId[0] == - 13*13)',
 'nCleanFatJet >= 1 && CleanFatJet_pt[0] >= 190. && fabs(Alt$(CleanFatJet_eta[0],-9999.))<2.4'
]

supercut = ' && '.join(supercut_vector)

cuts['preselection'] = '1.'


#############################
######### TRIGGER TEST
#############################
cuts['SR_plus_trigger']= 'HLT_Photon200==1 || HLT_Ele35_WPTight_Gsf==1'
