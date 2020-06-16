# cuts


#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>20 \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJet >= 2 && fabs(Alt$(CleanJet_pt,-9999.))>30. && fabs(Alt$(CleanJet_eta,-9999.))<5.0 \
            && mjj > 200 \
            && detajj > 2.0 \
           '

#
#   BOOSTED CATEGORY
#

## Top control regions
cuts['top']  = { 
   'expr' : 'topcr',
   'categories' : {
#      '0j' : 'zeroJet',
#      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j_em_me' : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
      '2j_ee_mm' : 'mll>120 && PuppiMET_pt>60 && multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
   }
}


## DYtt control regions
cuts['DY']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
#        '0j'     : 'zeroJet',
#        '1j'     : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
        '2j'     : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)', 
#        '2j_ee'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
#        '2j_mm'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    }
}



#######################################
#
#   RESOLVED CATEGORY
#
