# variables

#variables = {}


variables['mll'] = {   'name': 'mll',            #   variable name
                           'range' : (80,80,100),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
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
                           'xaxis' : 'VBS jets mass [GeV]',  #   x axis name
                           'fold' : 0
                        }

#variables['mjj_NotFat'] = {   'name': 'mjj_vbs_AK4NotFat',            #   variable name
 #                          'range' : (50,0,1500),    #   variable range
  #                         'xaxis' : 'VBS jets mass cleaned of FatJet [GeV]',  #   x axis name
   #                        'fold' : 0
    #                    }
 

variables['jetpt1'] = { 'name': 'Alt(CleanJet_pt,0,-9999.)',
                        'range': (30,0.,500),
                        'xaxis': 'p_{T} 1st jet',
                        'fold':0
}
variables['jetpt2'] = { 'name': 'Alt(CleanJet_pt,1,-9999.)',
                        'range': (30,0.,300),
                        'xaxis': 'p_{T} 2nd jet',
                        'fold':0
}

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
variables['nCleanJet']  = {
                        'name': 'nCleanJet',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets w/ p_{T}>30 GeV (cleaned)',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


#variables['btag_cleanjet'] = {   'name': 'Take(Jet_btagDeepB, CleanJet_jetIdx)',            #   variable name
 #                          'range' : (80,0.,1.),    #   variable range
  #                         'xaxis' : 'btag of cleaned jets',  #   x axis name
   #                        'fold' : 0
    #                    }



variables['FatJet_pt']  = {
                        'name': 'CleanFatJet_pt[0]',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 0   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJeteta'] = {'name': 'CleanFatJet_eta[0]',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 0
                           }


variables['FatJet_mass'] = {   'name': 'CleanFatJet_mass[0]',
	                       'range': (35,0,220),
                               'xaxis': 'FJ softdrop mass',
			       'fold': 3
			       }

variables['detajj']  = {  'name': 'detajj',
                          'range': (32,0.0,8.0),
                         'xaxis': '\Delta \eta (jj)',
                          'fold': 3
                          }


#variables['detajj']  = {  'name': 'detajj_vbs_AK4NotFat',
 #                         'range': (32,0.0,8.0),
  #                        'xaxis': '\Delta \eta (jj) not Fat',
   #                       'fold': 3
    #                      }

#
# MET
#

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,500),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }


#variables['M_ZV'] = { 'name': "M_ZV",
 #                            'range': ([0,250,500,750,1000,1200,1500,2000,2500],),  #for 0  < mVV < 3000
  #                           'xaxis': 'M_{ZV} [GeV]',
   #                          'fold': 3,
    #                        }#function implemented in aliases.py and in M_leplepBjets_class.cc



