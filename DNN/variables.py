# variabeadines

#variables = {}
    

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }



#leptons

variables['mll'] = {   'name': 'mll',            #   variable name
                           'range' : (60,300,1000),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 3
                        }

variables['mllpeak'] = {   'name': 'mll',            #   variable name
                           'range' : (80,80,100),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 3
                        }

variables['ptll']  = {   'name': 'ptll',     
                        'range' : (20, 0,200),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }

variables['pt_lep']  = {   'name': 'Lepton_pt',
                        'range' : (30,0.,400),
                        'xaxis' : 'p_{T} lep',
                        'fold'  : 3
                        }

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (30,0.,400),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3                         
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',     
                        'range' : (30,0.,200),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3                         
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3                         
                        }




#
# jets AK4
#
variables['eta_jet1']  = {  'name': 'CleanJet_eta[0]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 3                         
                        }

variables['eta_jet2']  = {  'name': 'CleanJet_eta[1]',     
                        'range' : (40,-5,5),   
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 3                         
                        }

variables['jetpt1'] = { 'name': 'CleanJet_pt[0]',
                        'range': (30,0.,500),
                        'xaxis': 'p_{T} 1st jet',
                        'fold':3
}

variables['jetpt2'] = { 'name': 'CleanJet_pt[1]',
                        'range': (30,0.,300),
                        'xaxis': 'p_{T} 2nd jet',
                        'fold':3
}

variables['nCleanJet']  = {
                        'name': 'nCleanJet',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets (cleaned from AK8)',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['mjj'] = {   'name': 'mjj',            #   variable name
                           'range' : (40,200,4000),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 3
                        }


variables['detajj'] = {   'name': 'detajj',            #   variable name
                           'range' : (16,2,8),    #   variable range
                           'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                           'fold' : 3
                        }


#
# jets AK8
#

variables['nFatJet']  = {
                        'name': 'nCleanFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['FatJet_pt']  = {
                        'name': 'CleanFatJet_pt',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJeteta'] = {'name': 'CleanFatJet_eta',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '#eta FatJet',
                           'fold'  : 3
                           }

variables['FatJet_softdropmass'] = {   'name': 'CleanFatJet_mass',
                               'range': (50,0.,200),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 3
                               }
##this is the softdrop mass

                                                                                                                        
variables['FatJet_tau21'] = {   'name': 'CleanFatJet_tau21',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 3
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
