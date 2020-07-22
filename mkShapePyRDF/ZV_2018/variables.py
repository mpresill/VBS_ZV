##leptons
variables['pt1']  = {   'name': 'Alt(Lepton_pt,0,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt2']  = {   'name': 'Alt(Lepton_pt,1,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }


variables['eta1']  = {   'name': 'Alt(Lepton_eta,0,-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }

variables['eta2']  = {   'name': 'Alt(Lepton_eta,1,-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (30,60,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }


#jet cat

variables['category'] = {'name' : 'category',
                         'range' : (3,-1,1),
                         'xaxis' : 'category',
                         'fold' : 3
                        }

variables['vbs_jet_pt1']  = {   'name': 'Alt(Take(CleanJet_pt,vbs_jet_0),0,-999)',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 1st vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_pt2']  = {   'name': 'Alt(Take(CleanJet_pt,vbs_jet_1),0,-999)',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 2nd vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_eta1']  = {   'name': 'Alt(Take(CleanJet_eta,vbs_jet_0),0,-999)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st vbs jet [GeV]',
                        'fold' :3
                        }

variables['vbs_jet_eta2']  = {   'name': 'Alt(Take(CleanJet_eta,vbs_jet_1),0,-999)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd vbs jet [GeV]',
                        'fold' :3
                        }


variables['V_jet_pt1']  = {   'name': 'Alt(Take(CleanJet_pt,V_jet_0),0,-999)',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 1st V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_pt2']  = {   'name': 'Alt(Take(CleanJet_pt,V_jet_1),0,-999)',
                        'range' : (20,0.,300),
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_eta1']  = {   'name': 'Alt(Take(CleanJet_eta,V_jet_0),0,-999)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st V jet [GeV]',
                        'fold' :3
                        }

variables['V_jet_eta2']  = {   'name': 'Alt(Take(CleanJet_eta,V_jet_1),0,-999)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd V jet [GeV]',
                        'fold' :3
                        }
