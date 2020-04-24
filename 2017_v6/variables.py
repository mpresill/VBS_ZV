
# variables: currently used version Apr2020

#variables = {}
#variables['nvtx']  = {   'name': 'PV_npvsGood',      
#                        'range' : (100,0,100),  
#                        'xaxis' : 'nvtx', 
#                         'fold' : 3
#                      }



variables['nLepton'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 0
                        }

variables['mll_vbs'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }


variables['pt_lep']  = {   'name': 'Lepton_pt',
                        'range' : (30,0.,400),
                        'xaxis' : 'p_{T} lep',
                        'fold'  : 0
                        }

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (30,0.,400),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0                         
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',     
                        'range' : (30,0.,200),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0                         
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 0                         
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 0                         
                        }


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

#
# jets
#
variables['eta_jet1']  = {  'name': 'CleanJet_eta[0]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0                         
                        }

variables['eta_jet2']  = {  'name': 'CleanJet_eta[1]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 0                         
                        }


variables['mjj_vbs'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,300,2500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['mjj_vbs_AK4NotFat'] = {   'name': 'mjj_vbs_AK4NotFat',            #   variable name
                           'range' : (50,300,2500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV] (cleaned)',  #   x axis name
                          'fold' : 0
                       }

variables['jetpt1'] = { 'name': 'Alt$(CleanJet_pt[0],-9999.)',
                        'range': (30,0.,500),
                        'xaxis': 'p_{T} 1st jet',
                        'fold':0
}

variables['jetpt2'] = { 'name': 'Alt$(CleanJet_pt[1],-9999.)',
                        'range': (30,0.,300),
                        'xaxis': 'p_{T} 2nd jet',
                        'fold':0
}

variables['nFatJet']  = {
                        'name': 'nCleanFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['FatJet_pt']  = {
                        'name': 'CleanFatJet_pt',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 0   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJeteta'] = {'name': 'CleanFatJet_eta',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 0
                           }

variables['FatJet_softdropmass'] = {   'name': 'Alt$(CleanFatJet_mass,0.)',
                               'range': (50,0.,200),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 0
                               }
                                                                                                                        
variables['FatJet_tau21'] = {   'name': 'CleanFatJet_tau21',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 0
                        }


variables['nCleanJet']  = {
                        'name': 'nCleanJet',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV (cleaned)',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['detajj_vbs']  = {  'name': 'detajj_vbs',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 0
                          }

variables['detajj_vbs_AK4NotFat']  = {  'name': 'detajj_vbs_AK4NotFat',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj) (cleaned)',
                          'fold': 0
                          }



#
# MET
#

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,500),
                        'xaxis' : 'puppimet [Gev]',
                        'fold'  : 3
                        }

variables['M_ZV'] = { 'name': "M_ZV",
                             'range': ([0,250,500,750,1000,1200,1500,2000,2500,3000],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 0
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc

"""
variables['M_ZV_v0'] = { 'name': "M_ZV",
                             'range': ([500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 0
                          }

variables['M_ZV_fold1'] = { 'name': "M_ZV",
                             'range': ([500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 1
                        }
variables['M_ZV_fold2'] = { 'name': "M_ZV",
                             'range': ([500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 2
                          }

variables['M_ZV_fold3'] = { 'name': "M_ZV",
                             'range': ([500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3
                          }

"""                          


variables['ZlepV']  = {  'name': '(Alt$(CleanFatJet_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj_vbs',
                          'range': (15,-1.5,1.5),
                          'xaxis': 'z_{V}',
                          'fold': 3
                          }

"""
variables['WH2l_pTW'] = { 'name': 'WH2l_pTW',
                               'range' : (60,0,1200),
                             'xaxis' : 'WH2l_pTW [GeV]',
                             'fold' : 1
                         }
"""