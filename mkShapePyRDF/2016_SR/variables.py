
##leptons
variables['Lep_pt1']  = {   'name': 'Alt(Lepton_pt,0,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['Lep_pt2']  = {   'name': 'Alt(Lepton_pt,1,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }


variables['Lep_eta1']  = {   'name': 'Alt(Lepton_eta,0,-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }

variables['Lep_eta2']  = {   'name': 'Alt(Lepton_eta,1,-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (30,60,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['Zepp_ll']= {   'name': 'Zepp_ll',            #   variable name    
                        'range' : (40,-1.5,1.5),    #   variable range
                        'xaxis' : 'Zepp_{ll} ',  #   x axis name
                        'fold' :3
                        }



#
# jets AK8
#

variables['nFatJet']  = {
                        'name': 'nFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['FatJet_pt']  = {
                        'name': 'Alt(CleanFatJet_pt,0,-999)',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['FatJeteta'] = {'name': 'Alt(CleanFatJet_eta,0,-999)',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 3
                           }
variables['FatJet_softdropmass'] = {   'name': 'Alt(CleanFatJet_mass,0,0.)',
                               'range': (50,0.,200),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 3
                               }
##this is the softdrop mass
                                                                                                                     
variables['FatJet_tau21'] = {   'name': 'Alt(CleanFatJet_tau21,0,-999)',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 3
                        }



#Zeppenfeld variables

variables['Zlep_1'] = {   'name': 'Zlep_1',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l1}', 
                        'fold' : 3
                        }

variables['Zlep_2'] = {   'name': 'Zlep_2',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l2}', 
                        'fold' : 3
                        }


#jet cat
variables['category'] = {'name' : 'category',
                         'range' : (3,-1,1),
                         'xaxis' : 'category',
                         'fold' : 3
                        }

variables['vbs_jet_pt1']  = {   'name': 'vbs_jet_pt1',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 1st vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_pt2']  = {   'name': 'vbs_jet_pt2',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 2nd vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_eta1']  = {   'name': 'vbs_jet_eta1',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_eta2']  = {   'name': 'vbs_jet_eta2',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd vbs jet [GeV]',
                        'fold' :3
                        }


variables['V_jet_pt1']  = {   'name': 'V_jet_pt1',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 1st V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_pt2']  = {   'name': 'V_jet_pt2',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_eta1']  = {   'name': 'V_jet_eta1',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_eta2']  = {   'name': 'V_jet_eta2',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd V jet [GeV]',
                        'fold' :3
                        }

variables['mjj_max']  = {   'name': 'Mjj_max',            #   variable name    
                        'range' : (20,200,4000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['detajj_mjjmax']  = {   'name': 'detajj_mjjmax',            #   variable name    
                           'range' : (12,2.0,8.0),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }
variables['dphijj_mjjmax']  = {   'name': 'dphijj_mjjmax',            #   variable name    
                           'range' : (12,0,),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }

variables['V_jet_mass']  = {   'name': 'V_jet_mass',            #   variable name    
                           'range' : (35,0,220),    #   variable range
                           'xaxis' : 'V_jet_mass',  #   x axis name
                           'fold' :3
                        }   
variables['njet'] = {	'name': 'nCleanJet30',
			'range' : (10,0,9),
			}

variables['Zvjet'] = {   'name': 'Zvjet',
                        'range' : (40,-1.5,1.5),
                        }

variables['vbs_jet_qgl1'] = {   'name': 'vbs_jet_qgl1',
                        'range' : (40,-1.5,1.5),
                        }
variables['vbs_jet_qgl2'] = {   'name': 'vbs_jet_qgl2',
                        'range' : (40,-1.5,1.5),
                        }
variables['V_jet_qgl1'] = {   'name': 'V_jet_qgl1',
                        'range' : (40,-1.5,1.5),
                        }
variables['V_jet_qgl2'] = {   'name': 'V_jet_qgl2',
                        'range' : (40,-1.5,1.5),
                        }
variables['FatJet_qgl'] = {   'name': 'FatJet_qgl',
                        'range' : (40,-1.5,1.5),
                        }
variables['nbtag'] = {        'name' : 'nbtag',
			'range' : (10, 0, 9)
}
variables['lepton_id'] = {'name' : 'Alt(AbsVec(Lepton_pdgId), 0, -999)',
			'range': (2, 11, 13),
}
