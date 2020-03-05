# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg

'''
structure['ChMisId']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ttbar'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
'''
structure['Vg']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['WZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['DPS']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['VVV']  = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'removeFromCuts' : ['hww2l2v_13TeV_dytt_of2j_vbf'],
                  }
##Irreducible Bkg

structure['WW_strong']  = {
                      'isSignal' : 0,
                      'isData'   : 0
                      }

##Signal

structure['WpWp_EWK']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
#Fake
structure['Fake_lep']  = {
                  'isSignal' : 0,
                  'isData'   : 0,
              }

'''
structure['Vg_promptSubtr']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['WZ_promptSubtr']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }
'''
# data


structure['DATA']  = {
                  'isSignal' : 0,
                  'isData'   : 1
              }









#structure['Wjets']  = {
#                  'isSignal' : 0,
#                  'isData'   : 0
#              }

#structure['Fake']  = {
#                  'isSignal' : 0,
#                  'isData'   : 0
#              }

#structure['ttbar'] = {
#                  'isSignal' : 0,
#                  'isData'   : 0
#                  }


#structure['singletop'] = {
#                  'isSignal' : 0,
#                  'isData'   : 0
#                  }

#structure['WW']  = {
#                  'isSignal' : 0,
#                  'isData'   : 0
#                  }

# structure['ggWW']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['ggWW_Int']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['Wg']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['VgS'] = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['WZgS_L'] = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['WZgS_H'] = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['Zg']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['VZ']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['WZ']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }

# structure['ZZ']  = {
#                   'isSignal' : 0,
#                   'isData'   : 0
#                   }


# structure['ggH'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['ggH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['qqH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['qqH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['WH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['ZH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['ggZH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['H_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['bbH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['ttH_hww'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }

# structure['ggH_htt'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   }

# structure['qqH_htt'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   }

# structure['WH_htt'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   }

# structure['ZH_htt'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0,
#                   }

# structure['H_htt'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0
#                   }
