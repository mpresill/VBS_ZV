# cuts

#cuts = {}
cuts["supercut"] = {
    'expr' :'   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2' ,
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
    'expr': 'category==0 ',
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
    'expr': 'category==1',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
