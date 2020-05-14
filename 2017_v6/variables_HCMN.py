
# variables: currently used version Apr2020

#variables = {}

variables['events']  = {   'name': '1',
                           'range' : (1,0,2),
                           'xaxis' : 'events',
                           'fold' : 3
                     }


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

variables['mll'] = {   'name': 'mll',            #   variable name
                           'range' : (60,300,1000),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['mllpeak'] = {   'name': 'mll',            #   variable name
                           'range' : (80,80,100),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['ptll']  = {   'name': 'ptll',     
                        'range' : (20, 0,200),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
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
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV (cleaned)',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
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
