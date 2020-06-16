# cuts


#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>20 \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>30. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0 \
            && mjj > 300 \
            && detajj > 2.0 \
           '
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet

#
#   BOOSTED CATEGORY
#

## Top control regions
cuts['BR_top']  = { 
   'expr' : 'topcr',
   'categories' : {
#      '0j' : 'zeroJet',
#      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
#       '' : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
       '2j_btag' : 'nCleaFatJet==1 && Alt$(FatJet_msoftdrop[0],0.)>65 && Alt$(FatJet_msoftdrop[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
   }
}


## DYtt control regions
cuts['BR_DY']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
#        '0j'     : 'zeroJet',
#        '1j'     : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
        '2j_btag'     : 'nCleaFatJet==1 && (Alt$(FatJet_msoftdrop[0],0.)<65 || Alt$(FatJet_msoftdrop[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)', 
#        '2j_ee'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
#        '2j_mm'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    }
}



#######################################
#
#   RESOLVED CATEGORY
#
