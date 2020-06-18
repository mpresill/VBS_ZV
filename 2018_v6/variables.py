# variables

#variables = {}
'''
variables['VARIABLE']  = {  
          'name': 'expression',        # variable expression as one would use in TTree::Draw. Also 2D expression works e.g. var1:var2    
          'range' : range:             # anything that a TH1 can digest van be put here: 
                                       # a 3-valued tuple is interpreted as (nbins, xmin, xmax).
                                       # a 6-valued tuple is interpreted as (nbinsx, xmin, xmax, nbinsy, ymin, ymax)
                                       # a ([list]) is interpreted as a vector of bin edges
                                       # a ([list],[list],) is interpreted as a 2D vector of bin edges (mind the comma before the closing ")")
          'xaxis' : 'DR_{ll}',         # x axis name, human readable name, what goes into h->GetXaxis()->SetTitle()
          'fold' : NUMBER,             # 0 -> no underflow/overflow folding. 1 -> fold underflow in the first bin. 2-> fold overflow in the last bin. 3 -> fold both underflow and overflow.
          'divideByBinWidth': VALUE,   #OPTIONAL, whether to divide (1) or not (0) the bin content by the bin width (for variable bin size histograms). Default is 0
} 
'''
#  
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }      
#
# leptons
#

variables['ptlep']  = {   'name': 'Alt$(Lepton_pt,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} lep [GeV]',
                        'fold' :3
                        }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }


variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }

variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }

variables['ptll']  = {   'name': 'ptll',            #   variable name    
                        'range' : (20,30,400),    #   variable range
                        'xaxis' : 'pT_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (20,50,400),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }
variables['mll-peak']  = {   'name': 'mll',            #   variable name    
                        'range' : (10,40,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }


#
# jets AK8
#

variables['nFatJet']  = {
                        'name': 'nCleanFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['FatJet_pt']  = {
                        'name': 'CleanFatJet_pt[0]',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJeteta'] = {'name': 'CleanFatJet_eta[0]',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 3
                           }

variables['FatJet_softdropmass'] = {   'name': 'Alt$(CleanFatJet_mass[0],0.)',
                               'range': (50,0.,200),
                               'xaxis': 'AK8 jet softdrop mass',
                               'fold': 3
                               }
##this is the softdrop mass

                                                                                                                        
variables['FatJet_tau21'] = {   'name': 'CleanFatJet_tau21[0]',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 3
                        }


#
# jet AK4
#

variables['nCleanJet']  = {   'name': 'Sum$(CleanJet_pt >= 30)',            #   variable name    
                        'range' : (10,0,10),    #   variable range
                        'xaxis' : 'Number of jets',  #   x axis name
                        'fold' : 3
                        }

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets (cleaned)',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st VBS jet',
                        'fold' : 3
                        }
variables['jeteta2'] = {  'name': 'Alt$(CleanJet_eta[1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd VBS jet',
                        'fold' : 3
                        }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',            #   variable name    
                        'range' : (20,0,300),    #   variable range
                        'xaxis' : 'p_{T} 1st VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',            #   variable name    
                        'range' : (20,0,300),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['Zepp1']  = {   'name': 'Lepton_eta[0]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (10,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_1',  #   x axis name
                           'fold' :0
                           }

variables['Zepp2']  = {   'name': 'Lepton_eta[1]-0.5*(CleanJet_eta[0]+CleanJet_eta[1])',            #   variable name    
                           'range' : (10,-5,5),    #   variable range
                           'xaxis' : 'Zeppenfeld_2',  #   x axis name
                           'fold' :0
                           }       


#AK4 variables with Latino variables

variables['mjj']  = {   'name': 'mjj',            #   variable name    
                        'range' : (50,200,2500),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['detajj']  = {   'name': 'detajj',            #   variable name    
                           'range' : (10,2.0,8.5),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }

#AK4 variables with class definition


variables['mjj_vbs_AK4NotFat'] = {   'name': 'mjj_vbs_AK4NotFat',            #   variable name
                           'range' : (50,200,2500),    #   variable range
                           'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                          'fold' : 3
                       }


variables['detajj_vbs_AK4NotFat']  = {  'name': 'detajj_vbs_AK4NotFat',
                          'range': (32,2.0,8.5),
                          'xaxis': '#Delta #eta jj',
                          'fold': 3
                          }



#
# MET
#

variables['puppiMET_pt']  = {   'name': 'PuppiMET_pt',  
                        'range' : (25,0,250),    #   variable range
                        'xaxis' : 'MET p_{T} [GeV]',  #   x axis name
                        'fold' : 3          
                        }
variables['puppiMET_phi']  = {   'name': 'PuppiMET_phi',  
                        'range' : (20,-3.14,3.14),    #   variable range
                        'xaxis' : 'MET #phi',  #   x axis name
                        'fold' : 3          
                        }


###

variables['M_ZV'] = { 'name': "M_ZV",
                             'range': ([0,250,500,750,1000,1200,1500,2000,2500,3000],),  #for 0  < mVV < 3000
                             'xaxis': 'M_{ZV} [GeV]',
                             'fold': 3
                            }#function implemented in aliases.py and in M_leplepBjets_class.cc




#--- 2D variables --


#variables['MjjVSmTi']  = {   'name': 'mjj:mTi',            #   variable name    
#                        'range' : ([100,250,400,600,1000],[500,700,1000,1300,1600,2000],),    #   variable range
#                        'xaxis' : 'mjj:mTi',  #   x axis name
#                        'fold' : 3
#                        }