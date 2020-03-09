# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 3
# }

#n.b. for implementing varibles with functions with more than 7 arguments see the case of M_leplepBjet

variables['nJet']  = {   'name': 'nJet',
                         'range' : (6,0,6),
                         'xaxis' : 'njets',
                         'fold' : 3
                         }
variables['nJet_v2']  = {   'name': 'Sum$(CleanJet_pt>30)',
                            'range' : (4,0,4),
                            'xaxis' : 'njets',
                            'fold' : 3
                            }


variables['nLepton'] =  {
    'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',
    'range': (5,0,5),
    'xaxis': '# leptons',
    'fold': 3
}

variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (4, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['mll_v2']  = {   'name': 'mll',            #   variable name
                           'range' : (80, 0. ,800),    #   variable range
                           'xaxis' : 'mll [GeV]',  #   x axis name
                           'fold' : 3
                           }


variables['mjj']  = {  'name': 'mjj',
                       'range': ([500,800,1100,1500,2000],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }
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

variables['M_leplepBjet'] = { 'name': "M_leplepBjet",
                             'range': (300, 0.,3000),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3,
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc

variables['M_leplep'] = { 'name': 'M_leplep(Lepton_pt[0],Lepton_phi[0],Lepton_eta[0],Lepton_pt[1],Lepton_phi[1],Lepton_eta[1])',  #formula defined in aliases.py  
                             'range': (80, 0.,800),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ll} [GeV]',
                             'fold': 3,
                             'linesToAdd' : ['.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/M_leplep.C+']
                        }


variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,500),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }

variables['jetpt1']  = {   'name': 'Alt$(Jet_pt[0],-9999.)',
                           'range' : (15,0.,200),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(Jet_pt[1],-9999.)',
                           'range' : (15,0.,150),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 3
                           }

variables['FatJetpt']  = {   'name': 'Alt$(FatJet_pt[0],-9999.)',
                           'range' : (20,0.,800),
                           'xaxis' : 'p_{T} FatJet',
                           'fold'  : 3
                           }

variables['FatJet_mass'] = {   'name': 'Alt$(FatJet_mass,-9999.)',
	                       'range': (50,0.,350),
                               'xaxis': 'FJ mass',
			       'fold': 3
			       }

variables['FatJet_softdropmass'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (50,0.,350),
                               'xaxis': 'FJ softdrop mass',
                               'fold': 3
                               }

#tau variables, ... to be added


variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (10,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['etaj1'] = {  'name': 'Alt$(Jet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': '\eta j1',
                        'fold': 3
                        }

variables['etaj2'] = {         'name': 'Alt$(Jet_eta[1],-9999.)',
                               'range': (10,-5,5),
                               'xaxis': '\eta j2',
                               'fold': 3
                               }

variables['detajj']  = {  'name': 'detajj',
                          'range': (8,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 3
                          }

variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                          'range': (10,-1.5,1.5),
                          'xaxis': 'Z^{lep}_{1}',
                          'fold': 3
                          }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                          'range': (10,-1.5,1.5),
                          'xaxis': 'Z^{lep}_{2}',
                          'fold': 3
                          }


variables['Zeppll']  = {   'name': 'Zeppll(Lepton_pt[0],Lepton_phi[0],Lepton_eta[0],Lepton_pt[1],Lepton_phi[1],Lepton_eta[1],Jet_eta[0],Jet_eta[1],detajj)',            #   variable name    
                           'range' : (20,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_{ll}',  #   x axis name
                           'fold' :3,
                           'linesToAdd' : ['.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/Zeppll.C+']
                           }

#variables['R']  = {   'name': 'R(ptll,phill(Lepton_pt[0],Lepton_phi[0],Lepton_pt[1],Lepton_phi[1]),metPfType1,metPfType1Phi,Jet_pt[0],Jet_phi[0],Jet_pt[1],Jet_phi[1])',# variable name     
#                        'range' : (20,0.,1.),    #   variable range
#                        'xaxis' : 'R',  #   x axis name
#                        'fold' : 3,
#                       'linesToAdd' : ['.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/R.C+','.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/phill.C+']
#                        }

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
