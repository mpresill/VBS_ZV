# cuts

#cuts = {}
cuts["supercut"] = {
    'expr' :' 1' ,
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
cuts['event1'] = {
    'expr': 'run == 276810',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
#######################################
#
#   RESOLVED CATEGORY
#
#######################################
cuts['event2'] = {
    'expr': ' event == 3403508960',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }





