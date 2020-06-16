cuts["supercut"] = {
    'expr' : ' nLepton == 2. \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>20  \
            && nCleanJetNotFat >= 2 \
            &&  abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && Alt(Take(CleanJet_pt, CleanJetNotFat_jetIdx),0,-9999.)>30. \
            && abs(Alt(Take(CleanJet_eta,CleanJetNotFat_jetIdx),0,-9999.))<5.0 \
            && mll >60. && mll <120.',
            
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
#no mjj/detajj cut since we want to have a look at their distrib with BDT

#cuts['preselection'] = '1.'


##a selection on VBS_jets is still required

#############################
######### BOOSTED SR
#############################
cuts['SR_boosted_minimal'] = {
    'expr': '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 )) \
        && nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200. \
        && abs(Alt(CleanFatJet_eta,0,-9999.))<2.4',
     
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }


