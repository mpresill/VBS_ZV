

# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    

structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }


structure['WJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }
"""
structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }
structure['Fake_em']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'removeFromCuts' : [ k for k in cuts if 'me' in k],
              }
structure['Fake_me']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'removeFromCuts' : [ k for k in cuts if 'em' in k],
              }
structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
structure['singletop'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
"""
structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }
"""
structure['WWewk']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }
structure['ggWW_Int']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }
structure['Wg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
structure['VgS_L'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VgS_H'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['Zg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }
"""
structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VBS_VV_QCD'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['VBS_VV_EW'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }


# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

"""
print "INSTRUCTURE"
print cuts
print nuisances['']
print "OK"
for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)
    print nuis
"""

