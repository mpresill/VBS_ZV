supercut = '   mll>300 \
            && Lepton_pt[0]>150 \
            && Lepton_pt[1]>100 \
            && nCleanFatJet >= 1 '

cuts['preselection'] = '1.'


#############################
######### TRIGGER TEST
#############################
cuts['opposite_flavor_plus_trigger']= 'fabs(Lepton_pdgId[0]) == 11  && fabs(Lepton_pdgId[1]) == 13 && (HLT_Photon200==1 || HLT_Ele35_WPTight_Gsf==1)'
cuts['trigger']= '(HLT_Photon200==1 || HLT_Ele35_WPTight_Gsf==1)'
cuts['opposite_flavor']= 'fabs(Lepton_pdgId[0]) == 11  && fabs(Lepton_pdgId[1]) == 13'
