cuts["supercut"] = {
    'expr' : ' nLepton == 2. \
            && mll >60. && mll <120.',
    'parent' : None,
    'doVars' : False,
    'doNumpy': False
}



cuts['SR_boosted_minimal'] = {
    'expr': 'nCleanFatJet == 1 && CleanFatJet_pt[0] >= 200.',
    'parent' : 'supercut',
    'doVars' : True,
    'doNumpy': True
    }
