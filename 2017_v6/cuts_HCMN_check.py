supercut = '   mll>300 \
            && Lepton_pt[0]>150 \
            && Lepton_pt[1]>100 \
            && nCleanFatJet >= 1 '

cuts['preselection'] = '1.'


#############################
######### TRIGGER TEST
#############################
cuts['SR_plus_trigger']= '(Lepton_pdgId[0]*Lepton_pdgId[0] == - 11*11)  && (Lepton_pdgId[1]*Lepton_pdgId[1] == - 13*13) && (HLT_Photon200==1 || HLT_Ele35_WPTight_Gsf==1)'
