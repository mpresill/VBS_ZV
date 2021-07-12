# cuts

#cuts = {}
cuts["supercut"] = {
    'expr' :'   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >76. && mll <106. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
	    && nCleanJetNotFat >= 2 \
	    && Mjj_max > 200 && detajj_mjjmax > 2.0 ' ,
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet

#cuts['preselection'] = '1.'

#######################################
#
#   BOOSTED CATEGORY
#
#######################################
cuts['Boosted_SR'] = {
    'expr': 'category==0 && nCleanFatJet == 1 &&  (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && V_jet_mass > 65. && V_jet_mass < 105 && bVeto',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
"""
cuts['Boosted_SR'] = {
    'expr': 'category==0 && nCleanFatJet == 1 &&  (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && V_jet_mass >65. && V_jet_mass < 105 && bVeto',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
"""
cuts['Boosted_DYcr']  = {
	'expr' : 'category==0 && nCleanFatJet==1 && bVeto && ( V_jet_mass<65 || V_jet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
	'parent' : 'supercut',
    	'doVars' : True,
    	'doNumpy': True
}

cuts['Boosted_DYcr_bVeto']  = {
	'expr' : 'category==0 && bVeto && nCleanFatJet==1 && ( V_jet_mass<65 || V_jet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
  'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
}

#######################################
#
#   RESOLVED CATEGORY
#
#######################################
cuts['Resolved_SR'] = {
    'expr': 'category==1  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && V_jet_mass >65. && V_jet_mass < 105 && bVeto',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
"""
cuts['Resolved_SR'] = {
    'expr': 'category==1  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && V_jet_mass >65. && V_jet_mass < 105 ',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
"""
cuts['Resolved_DYcr']  = {
	'expr':'category==1 && bVeto && ( V_jet_mass<65 || V_jet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
  'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
}


cuts['Resolved_DYcr_bVeto']  = {
	'expr' : 'category==1 && bVeto && ( V_jet_mass<65 || V_jet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
  'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True

}




