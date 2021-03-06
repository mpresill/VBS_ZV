# plot configuration

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
groupPlot['VZ_EW_VBS']  = {  
                  'nameHR' : "ZV_EW_VBS",
                  'isSignal' : 1,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['ZZ_EW_VBS', 'ZW_EW_VBS']
              }

groupPlot['VBF-V']  = {  
                  'nameHR' : 'VBF-V',
                  'isSignal' : 0,
                  'color':  810,   # kOrange + 10 
                  'samples'  : ['VBF-V']
              }

groupPlot['VBS_VV_QCD']  = {  
                  'nameHR' : 'VBS_VV_QCD',
                  'isSignal' : 0,
                  'color':  817,   # kOrange + 10 
                  'samples'  : ['VBS_VV_QCD']
              }

groupPlot['VV']  = {  
                  'nameHR' : 'VV',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW','WW_ewk', 'VZ', 'ggWW']
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY']
              }



groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }



groupPlot['WJets']  = {
                  'nameHR' : "WJets",
                  'isSignal' : 0,
                  'color'    :800,   # kGreen - 9
                  'samples'  : ['WJets']
              }



groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }


#plot = {}

# keys here must match keys in samples.py    
#                    


### signal ###
plot['ZZ_EW_VBS']  = {  
                  'color': 400,    # kYellow+2
                  'isSignal' : 1,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }

plot['ZW_EW_VBS'] = {  
                  'color': 405,    # kGreen+2
                  'isSignal' : 1,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


### background###
plot['WW']  = {  
                  'color': 419,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


plot['WW_ewk']  = {  
                  'color': 360,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


plot['VZ']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


plot['ggWW']  = {  
                  'color': 420,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


plot['DY']  = {  
                  'color': 500,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }


plot['VVV']  = {  
                  'color': 600,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }

plot['VBF-V'] = {
                'color': 700,    # kGreen+2
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0
} 
plot['VBS_VV_QCD'] = {
                'color': 703,    # kGreen+2
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0
} 


plot['WJets']  = {  
                  'color': 480,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }



plot['top']  = {  
                  'color': 400,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0
              }

"""
plot['DATA'] = {  
                  'color': 1,    # kblack
                  'isSignal' : 0,
                  'isData'   : 1, 
                  'scale'    : 1.0
              }
"""