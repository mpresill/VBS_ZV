# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 3
# }

#n.b. for implementing varibles with functions with more than 7 arguments see the case of M_leplepBjet

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

###############################   lepton variables

variables['nLepton'] =  {
    'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',
    'range': (5,0,5),
    'xaxis': '# leptons',
    'fold': 3
}

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (80, 0. ,400),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }
"""
variables['mll_v2']  = {   'name': 'mll',            #   variable name
                           'range' : (80, 0. ,800),    #   variable range
                           'xaxis' : 'mll [GeV]',  #   x axis name
                           'fold' : 3
                           }

variables['M_leplep'] = { 'name': 'M_leplep(Lepton_pt[0],Lepton_phi[0],Lepton_eta[0],Lepton_pt[1],Lepton_phi[1],Lepton_eta[1])',  #formula defined in aliases.py  
                             'range': (40, 0.,200),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ll} [GeV]',
                             'fold': 3,
                             'linesToAdd' : ['.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/M_leplep.C+']
                        }

"""
variables['ptl'] = { 'name': 'Alt$(Lepton_pt,-9999.)',
                        'range' : (25,0.,300),
                        'xaxis' : 'Lepton p_{T}',
                        'fold'  : 3
                        }

variables['ptl1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (35,0.,400),
                        'xaxis' : 'p_{T} Lep1',
                        'fold'  : 3
                        }

variables['ptl2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (25,0.,300),
                        'xaxis' : 'p_{T} Lep2',
                        'fold'  : 3
                        }
##############################  jet variables

#variables['nJet']  = {   'name': 'nJet',
#                         'range' : (6,0,6),
#                         'xaxis' : '# jets',
 #                        'fold' : 3
  #                       }
variables['nJet_v2']  = {   'name': 'Sum$(CleanJet_pt>30)',
                            'range' : (4,0,4),
                            'xaxis' : 'njets',
                            'fold' : 3
                            }

variables['mjj']  = {  'name': 'mjj',
                       'range': ([500,800,1100,1500,2000],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }
"""
variables['mjj_v2']  = {  'name': 'mjj',
                          'range': ([500,800,1200,1800,2000],),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                          }

variables['mjj_v3']  = {  'name': 'mjj',
                          'range': (15, 500. ,2000),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 3
                          }
"""
variables['jetpt1']  = {   'name': 'Alt$(Jet_pt[0],-9999.)',
                           'range' : (26,0.,650),
                           'xaxis' : 'p_{T} jet1',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(Jet_pt[1],-9999.)',
                           'range' : (25,0.,350),
                           'xaxis' : 'p_{T} jet2',
                           'fold'  : 3
                           }

variables['etaj1'] = {  'name': 'Alt$(Jet_eta[0],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': ' \eta jet1',
                        'fold': 3
                        }

variables['etaj2'] = {         'name': 'Alt$(Jet_eta[1],-9999.)',
                               'range': (20,-5,5),
                               'xaxis': ' \eta jet2',
                               'fold': 3
                               }

variables['detajj']  = {  'name': 'detajj',
                          'range': (8,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 3
                          }
##################################  Fat Jet variables

variables['M_ZV'] = { 'name': "M_ZV",
                             'range': ([0,250,500,750,1000,1200,1500,2000,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3,
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc

variables['M_ZV_v2'] = { 'name': "M_ZV",
                             'range': ([500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3,
                          }

variables['FatJetpt']  = {   'name': 'Alt$(FatJet_pt[0],-9999.)',
                           'range' : (24,0.,1200),
                           'xaxis' : 'AK8 jet p_{T}',
                           'fold'  : 3
                           }

variables['FatJeteta'] = {'name': 'Alt$(FatJet_eta[0],-9999.)',
                           'range' : (25,0.,2.5),
                           'xaxis' : 'AK8 jet p_{T}',
                           'fold'  : 3
                           }


#variables['FatJet_mass'] = {   'name': 'Alt$(FatJet_mass[0],-9999.)',
#	                       'range': (35,0.,350),
#                               'xaxis': 'FJ mass',
#			       'fold': 3
#			       }

variables['FatJet_softdropmass'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (35,0.,350),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 3
                               }

variables['fatjet_tau21'] = {   'name': 'FatJet_tau2[0]/FatJet_tau1[0]',      
                        'range' : (35,0,1),  
                        'xaxis' : '#tau_{21}', 
                        'fold' : 3
                        }

variables['fatjet_tau32'] = {   'name': 'FatJet_tau3[0] / FatJet_tau2[0] ',      
                        'range' : (40,0,1),  
                        'xaxis' : '#tau_{32}', 
                        'fold' : 3
                        }


############################# other variables
#variables['met']  = {   'name': 'MET_pt',            #   variable name
#                        'range' : (10,0,200),    #   variable range
#                        'xaxis' : 'pfmet [GeV]',  #   x axis name
#                        'fold' : 3
#                        }


variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                          'range': (10,-1.5,1.5),
                          'xaxis': 'Z^{lep}_{l1}',
                          'fold': 3
                          }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                          'range': (10,-1.5,1.5),
                          'xaxis': 'Z^{lep}_{l2}',
                          'fold': 3
                          }


variables['Zeppll']  = {   'name': 'Zeppll(Lepton_pt[0],Lepton_phi[0],Lepton_eta[0],Lepton_pt[1],Lepton_phi[1],Lepton_eta[1],Jet_eta[0],Jet_eta[1],detajj)',            #   variable name    
                           'range' : (20,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_{ll}',  #   x axis name
                           'fold' :3,
                           'linesToAdd' : ['.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/Zeppll.C+']
                           }
"""
variables['csvv2ivf_1']  = {
    'name': 'Alt$(Jet_btagCSVV2[0],0.)',
    'range' : (10,0,1),
    'xaxis' : 'csvv2ivf 1st jet ',
    'fold'  : 3
}

variables['csvv2ivf_2']  = {
    'name': 'Alt$(Jet_btagCSVV2[1],0.)',
    'range' : (10,0,1),
    'xaxis' : 'csvv2ivf 2nd jet ',
    'fold'  : 3
}
"""
