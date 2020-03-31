
# variables: currently used version Apr2020

#variables = {}
variables['nvtx']  = {   'name': 'PV_npvsGood',      
                        'range' : (100,0,100),  
                        'xaxis' : 'nvtx', 
                         'fold' : 3
                      }



variables['nLepton'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 0
                        }

variables['nLepton_fold1'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 1
                        }

variables['nLepton_fold2'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 2
                        }

variables['nLepton_fold3'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 3
                        }

variables['mll_vbs'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }
variables['mll_vbs_fold1'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 1
                        }

variables['mll_vbs_fold2'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 2
                        }

variables['mll_vbs_fold3'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 3
                        }


variables['ptll']  = {   'name': 'ptll',     
                        'range' : (30,0.,500),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }
variables['ptll_fold1']  = {   'name': 'ptll',     
                        'range' : (30,0.,500),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 1
                        }
variables['ptll_fold2']  = {   'name': 'ptll',     
                        'range' : (30,0.,500),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 2
                        }
variables['ptll_fold3']  = {   'name': 'ptll',     
                        'range' : (30,0.,500),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }



variables['pt1']  = {   'name': 'Lepton_pt',
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
variables['eta1_fold1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 1                         
                        }

variables['eta2_fold1']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 1                         
                        }
variables['eta1_fold2']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 2                         
                        }

variables['eta2_fold2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 2                         
                        }
variables['eta1_fold3']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }

variables['eta2_fold3']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3                         
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
variables['eta_jet1_fold1']  = {  'name': 'CleanJet_eta[0]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 1                         
                        }

variables['eta_jet2_fold1']  = {  'name': 'CleanJet_eta[1]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 1                         
                        }
variables['eta_jet1_fold2']  = {  'name': 'CleanJet_eta[0]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 2                         
                        }

variables['eta_jet2_fold2']  = {  'name': 'CleanJet_eta[1]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 2                         
                        }
variables['eta_jet1_fold3']  = {  'name': 'CleanJet_eta[0]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 3                         
                        }

variables['eta_jet2_fold3']  = {  'name': 'CleanJet_eta[1]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 3                         
                        }



variables['mjj_vbs'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['mjj_vbs_fold1'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 1
                        }

variables['mjj_vbs_fold2'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 2
                        }


variables['mjj_vbs_fold3'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 3
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

variables['btag'] = {   'name': 'Jet_btagDeepB',            #   variable name
                           'range' : (80,0.,1.),    #   variable range
                           'xaxis' : 'btag',  #   x axis name
                           'fold' : 0
                        }


variables['nFatJet']  = {
                        'name': 'Sum$(FatJet_pt>200)',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['FatJet_pt']  = {
                        'name': 'FatJet_pt[0]',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 0   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJeteta'] = {'name': 'FatJet_eta[0]',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 0
                           }
"""
variables['FatJet_mass'] = {   'name': 'FatJet_mass',
	                       'range': (35,0,220),
                               'xaxis': 'FJ mass',
			       'fold': 3
			       }
"""			       
variables['FatJet_softdropmass'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (35,0.,350),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 0
                               }


variables['FatJet_softdropmass_fold1'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (35,0.,350),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 1
                               }

variables['FatJet_softdropmass_fold2'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (35,0.,350),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 2
                               }

variables['FatJet_softdropmass_fold3'] = {   'name': 'Alt$(FatJet_msoftdrop[0],0.)',
                               'range': (35,0.,350),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 3
                               }                               
                                                              
                                  
                               

variables['fatjet_tau21'] = {   'name': 'FatJet_tau2[0]/FatJet_tau1[0]',
                        'range' : (35,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 0
                        }

variables['fatjet_tau32'] = {   'name': 'FatJet_tau3[0] / FatJet_tau2[0] ',
                        'range' : (40,0,1),
                        'xaxis' : '#tau_{32}',
                        'fold' : 0
                        }

variables['nCleanJet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 0   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJet_fold1']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 1   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJet_fold2']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJet_fold3']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['detajj_vbs']  = {  'name': 'detajj_vbs',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 0
                          }
                                
variables['detajj_vbs_fold1']  = {  'name': 'detajj_vbs',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 1
                          }

variables['detajj_vbs_fold2']  = {  'name': 'detajj_vbs',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 2
                          }

variables['detajj_vbs_fold3']  = {  'name': 'detajj_vbs',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 3
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

variables['M_Zv'] = { 'name': "M_ZV",
                             'range': ([0,250,500,750,1000,1200,1500,2000,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 0
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc

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

