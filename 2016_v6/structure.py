
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
"""

structure['ggWW']  = {
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

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VBF-V']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VBS_VV_QCD'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['VBS_ZV'] = {
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



