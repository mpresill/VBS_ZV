# cuts

#cuts = {}
"""
cuts["preselection"] = {
    'expr' :'   nLepton == 2 \
            && Lepton_pt[0]>25. \
            && Lepton_pt[1]>20. \
            && mll >75 && mll <105. \
            && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
	    && nCleanJetNotFat >= 2 \
	    && Mjj_max > 500 && detajj_mjjmax > 2.5 \
            && ((V_jet_mass>40 && V_jet_mass < 65.) || ( V_jet_mass > 105 && V_jet_mass <= 150))' ,
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}
"""
cuts["supercut"] = {
	'expr': 'nLepton >= 0',
	'parent': None,
	'doVars' : True,
	'doNumpy': True
}

#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet

#cuts['preselection'] = '1.'

#######################################
#
#   BOOSTED CATEGORY
#
#######################################

"""
cuts['Boosted_DYcr'] = {
    'expr': 'category==0 && nCleanFatJet==1  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)',
    'parent' : 'preselection',
    'doVars' : True,
    'doNumpy': True
    }
#######################################
#
#   RESOLVED CATEGORY
#
#######################################
cuts['Resolved_DYcr'] = {
    'expr': 'category==1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) ',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }

"""




