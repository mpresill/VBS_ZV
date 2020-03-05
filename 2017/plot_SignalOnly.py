
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

Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

plot['ZTo2L_ZTo2J']  = {
                  'color': Red+2, # kAzure -3  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ZTo2L_ZTo2J_aQGC']  = {
                  'color': Green+2, # kAzure -3  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ZTo2L_ZTo2J_QCD']  = {
                  'color': Orange+2, # kAzure -3  
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }



# additional options

legend['lumi'] = 'L =41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'





