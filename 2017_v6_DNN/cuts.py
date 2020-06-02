# cuts

cuts["supercut"] ={
    'expr': '( \
                  ( nLepton == 2. \
                    && ( (  (Lepton_pdgId[0]*Lepton_pdgId[1]== - 11*11) && (Lepton_pt[0]>25) && (Lepton_pt[1]>20)  ) || \
                    (  (Lepton_pdgId[0]*Lepton_pdgId[1]== - 13*13) && (Lepton_pt[0]>25) && (Lepton_pt[0]>20) )  )  \
                    && mll >60. && mll <120. \
                    && nCleanJet >= 2 && AbsVec(CleanJet_pt)>30. && AbsVec(CleanJet_eta)<5.0  \
                    && mjj > 250. && detajj > 2.0 \
                   )',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}
#########################################################################
###############|----------------------------------|######################
###############|          Boosted category        |######################
###############|----------------------------------|######################
#########################################################################

# only 1 FJ in the event (is it a good request?!? maybe we should ask for at least one and then apply some algorithm in the slection)
# at least 2 cleaned jets (from both leptons and FJ)
# + bVetoed 
# + tighter selection on mass window

cuts["boos_sig"] = {
    'expr': ' nCleanFatJet == 1 && AbsVec(CleanFatJet_eta[0])<2.4\
            && nCleanJetNotFat >= 2 \
            && mll >80. && mll <100. \
            && bVeto \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}



#########################################################################
###############|----------------------------------|######################
###############|          Resolved category       |######################
###############|----------------------------------|######################
#########################################################################


# no FJ in the event
# at least 4 cleaned jets
# 2 of them are required to be central
# + bVetoed
# + tighter selection on mass window


cuts["res_sig"] = {
    'expr': ' nCleanFatJet == 0 \
            && nCleanJet >= 4 \
            && Sum(AbsVec(CleanJet_eta)<5.0)==2 \
            && mll >80. && mll <100. \
            && bVeto \
                ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}
