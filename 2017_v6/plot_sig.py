
# plot configuration



#groupPlot['ZTo2L_ZTo2J'] = {
#                  'nameHR' : 'VBS EW',
#                 'isSignal' : 0,
#                  'color': 400,   # kYellow
#                  'samples'  : ['ZTo2L_ZTo2J']
#		  }
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

palette = {
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372   
    "Cardinal" : (194, 35, 38),  #C22326
    "RedOrange" : ( 243, 115, 56),
    "YellowOrange" : ( 253, 182, 50),
    "PineGreen" : (2, 120, 120),
    "ClaretRed" : (128, 22, 56)
}


Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

##########################################
####group plots
#########################################

"""
groupPlot['VZ']  = {  
                  'nameHR' : "ZV",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['VZ']
              }
"""

                  
groupPlot['VBS']  = {
                  'nameHR' : "VBS VV",
                  'color': palette["Cardinal"], # kAzure -3  
                  'isSignal' : 0,
                  'samples'  : ['VBS_VV_EW','VBS_VV_QCD']
                  #'fill': 1001
                  }
"""                  
groupPlot['VBF-V']  = {  
                  'nameHR' : 'VBF-V',
                  'isSignal' : 0,
                  'color':  palette["RedOrange"],   # kOrange + 10 
                  'samples'  : ['VBF-V']
              }

groupPlot['VV']  = {  
                  'nameHR' : 'VV',
                  'isSignal' : 0,
                  'color': palette["YellowOrange"], # kAzure -9 
                  'samples'  : ['WW','WW_ewk', 'VZ', 'ggWW']
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': palette["LightBlue"],    # kGreen+2
                  'samples'  : ['DY']
              }



groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': palette["PineGreen"], # kAzure -3  
                  'samples'  : ['VVV']
              }



groupPlot['WJets']  = {
                  'nameHR' : "WJets",
                  'isSignal' : 0,
                  'color'    : palette["MediumBlue"],   # kGreen - 9
                  'samples'  : ['WJets']
              }



groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': palette["ClaretRed"],   # kYellow
                  'samples'  : ['top']
              }



"""
groupPlot['VBS_ZV_aQGC']  = {
                  'nameHR' : "VBS aQGC",
                  'color': palette["DarkBlue"], # kAzure -3  
                  'isSignal' : 2,
                  'samples'  : ['VBS_ZV_aQGC'],
                  'fill': 0
                  }

#groupPlot['VBS_VV_QCD']  = {
 #                 'nameHR' : "VBS VV QCD",
  #                'color': Azure+2, # kAzure -3  
   #               'isSignal' : 0,
    #              'samples'  : ['VBS_VV_QCD'],
     #             'fill': 1001
      #            }


#plot = {}

# keys here must match keys in samples.py    
#                    

### background###
"""
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
plot['VBS_ZV_aQGC']  = {
                  'nameHR' : "ZV aQGC",
                  'color': 1, # kAzure -3  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VBS_VV_EW']  = {
                  'nameHR' : "VBS VV",
                  'color': Azure, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VBS_VV_QCD']  = {
                  'nameHR' : "VBS VV QCD",
                  'color': Azure+2, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


"""
############# FAKES
plot['Fakes']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['Fakes_em']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

plot['Fakes_ee']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['Fakes_mm']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

############## DATA
plot['DATA']  = {
                  'nameHR' : 'Data',
                  'color': 1 ,
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1 ,
                  'scale'    : 1.0
              }
"""

# additional options

legend['lumi'] = 'L =41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'





