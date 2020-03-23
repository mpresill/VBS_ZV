# variables

#variables = {}
"""variables['nvtx']  = {   'name': 'PV_npvsGood',      
                        'range' : (100,0,100),  
                        'xaxis' : 'nvtx', 
                         'fold' : 3
                      }


"""

"""variables['nLepton'] = {   'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',            #   variable name
                           'range' : (5,0,5),    #   variable range
                           'xaxis' : 'number of lepton',  #   x axis name
                           'fold' : 3
                        }
"""
variables['mll'] = {   'name': 'mll',            #   variable name
                           'range' : (80,50,120),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['mll_custom'] = {   'name': 'mll_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0,
                           
                        }


variables['ptll']  = {   'name': 'ptll',     
                        'range' : (30,0.,500),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
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

variables['mjj'] = {   'name': 'mjj',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 0
                        }

variables['mjj_custom'] = {   'name': 'mjj_vbs',            #   variable name
                           'range' : (50,0,1500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                           'fold' : 0,
                                                
                        }
 

variables['jetpt1'] = { 'name': 'Alt$(Jet_pt[0],-9999.)',
                        'range': (30,0.,500),
                        'xaxis': 'p_{T} 1st jet',
                        'fold':0
}
variables['jetpt2'] = { 'name': 'Alt$(Jet_pt[1],-9999.)',
                        'range': (30,0.,300),
                        'xaxis': 'p_{T} 2nd jet',
                        'fold':0
}

variables['btag'] = {   'name': 'Jet_btagDeepB',            #   variable name
                           'range' : (80,0.,1.),    #   variable range
                           'xaxis' : 'btag',  #   x axis name
                           'fold' : 0
                        }


"""variables['nFatJet']  = {
                        'name': 'Sum$(FatJet_pt>200)',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
"""

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


variables['FatJet_msoftdrop'] = {   'name': 'FatJet_mass',
	                       'range': (35,0,220),
                               'xaxis': 'FJ softdrop mass',
			       'fold': 3
			       }

variables['nCleanJet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (8,0,8),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['detajj']  = {  'name': 'detajj',
                          'range': (32,0.0,8.0),
                          'xaxis': '\Delta \eta (jj)',
                          'fold': 3
                          }

variables['detajj_custom']  = {  'name': 'detajj_vbs',
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
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }


variables['M_ZV'] = { 'name': "M_ZV",
                             'range': ([0,250,500,750,1000,1200,1500,2000,2500],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3,
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc

