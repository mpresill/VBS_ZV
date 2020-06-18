# cuts


#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>20 \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>50. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0 \
           '
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet

#
#   BOOSTED CATEGORY
#
cuts['BR_top']  = 'mjj > 200 && detajj > 3.5 && nCleanFatJet==1 && Alt$(CleanFatJet_mass[0],0.)>65 && Alt$(CleanFatJet_mass[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'
#cuts['BR_top_mjjmax']  = 'mjj_vbs_AK4NotFat > 200 && detajj_vbs_AK4NotFat > 2.0 && nCleanFatJet==1 && Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['BR_DY']  = 'mjj > 200 && detajj > 3.5 && nCleanFatJet==1 && (Alt$(CleanFatJet_mass[0],0.)<65 || Alt$(CleanFatJet_mass[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['BR_DY_mjjmax']  = 'mjj_vbs_AK4NotFat > 200 && detajj_vbs_AK4NotFat > 2.0 && nCleanFatJet==1 && (Alt$(FatJet_mass[0],0.)<65 || Alt$(FatJet_mass[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'


"""
## Top control regions
cuts['BR_top']  = { 
   'expr' : 'topcr',
   'categories' : {
#      '0j' : 'zeroJet',
#      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
#       '' : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
       '2j_btag' : 'mjj > 200 && detajj > 2.0 && nCleanFatJet==1 && Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
       '2j_btag_mjjmax' : 'mjj_vbs_AK4NotFat > 200 && detajj_vbs_AK4NotFat > 2.0 && nCleanFatJet==1 && Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0],0.)<105 && bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
   }
}


## DYtt control regions
cuts['BR_DY']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
#        '0j'     : 'zeroJet',
#        '1j'     : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
        '2j_bveto'     : 'mjj > 200 && detajj > 2.0 && nCleanFatJet==1 && (Alt$(FatJet_mass[0],0.)<65 || Alt$(FatJet_mass[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)', 
        '2j_bveto_mjjmax'     : 'mjj_vbs_AK4NotFat > 200 && detajj_vbs_AK4NotFat > 2.0 && nCleanFatJet==1 && (Alt$(FatJet_mass[0],0.)<65 || Alt$(FatJet_mass[0],0.)>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)', 
#        '2j_ee'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
#        '2j_mm'  : 'multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    }
}
"""


#######################################
#
#   RESOLVED CATEGORY
#
