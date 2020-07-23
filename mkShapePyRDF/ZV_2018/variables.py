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

#jets_cat variables
variables['mjj_max']  = {   'name': 'jets_cat[5]',            #   variable name    
                        'range' : (20,200,4000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['detajj_mjjmax']  = {   'name': 'jets_cat[6]',            #   variable name    
                           'range' : (12,2.0,8.0),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }

variables['V_jet_mass']  = {   'name': 'jets_cat[7]',            #   variable name    
                           'range' : (35,0,220),    #   variable range
                           'xaxis' : 'V_jet_mass',  #   x axis name
                           'fold' :3
                           }

