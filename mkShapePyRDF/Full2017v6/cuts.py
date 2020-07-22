# cuts


cuts["supercut"] ={
    'expr': '( \
                     ( (abs(Lepton_pdgId[0])==11) && (Lepton_pt[0]>40) ) || \
                     ( (abs(Lepton_pdgId[0])==13) && (Lepton_pt[0]>30) )    \
                   )',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}

cuts["lowen_looseVBS"] = {
    'expr': 'VBS_category==1 \
            && vbs_0_pt > 30 && vbs_1_pt > 30  \
            && vjet_0_pt > 30 && vjet_1_pt > 30 \
            && mjj_vbs >=300    \
            && deltaeta_vbs >= 2  \
            && PuppiMET_pt > 30 \
            && bVeto \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}

cuts["boost_looseVBS"] = {
    'expr': 'VBS_category==0 \
            && vbs_0_pt > 30 && vbs_1_pt > 30  \
            && vjet_0_pt > 200 \
            && mjj_vbs >=300    \
            && deltaeta_vbs >= 2  \
            && PuppiMET_pt > 30 \
            && bVeto \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}

# # Second lepton veto already done in post-processing 
# #and Lepton WP setup in samples.py
# supercut = 'Lepton_pt[0]>30'


# #########################################################################
# ###############|----------------------------------|######################
# ###############|          Lowenergy category      |######################
# ###############|----------------------------------|######################
# #########################################################################

# cuts["lowen_incl_ele"] = 'VBS_category==1 \
#                         && abs(Lepton_pdgId[0])==11 \
#                         && Lepton_pt[0] >= 40 \
#                         && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                         && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                         '

# cuts["lowen_incl_mu"] =  'VBS_category==1 \
#                         && abs(Lepton_pdgId[0])==13 \
#                         && Lepton_pt[0] >= 30 \
#                         && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                         && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                         '


# cuts["lowen_CR_looseVBS_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["lowen_CR_looseVBS_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["lowen_CR_top_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["lowen_CR_top_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["lowen_CR_wjets_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 '

# cuts["lowen_CR_wjets_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 '

# ########## --> Signal region
# # Increased cut on mjj_vbs and deltaeta VBS
# # Keeping top and W+jets control regions

# cuts["lowen_SR_tightVBS_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["lowen_SR_tightVBS_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["lowen_SR_top_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["lowen_SR_top_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '
# cuts["lowen_SR_wjets_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["lowen_SR_wjets_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# #########################################################################
# ###############|----------------------------------|######################
# ###############|          Boosted category        |######################
# ###############|----------------------------------|######################
# #########################################################################

# cuts["boost_incl_ele"] = 'VBS_category==0 \
#                         && abs(Lepton_pdgId[0])==11 \
#                         && Lepton_pt[0] >= 40 \
#                         && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                         && vjet_0_pt > 200 \
#                         '

# cuts["boost_incl_mu"] =  'VBS_category==0  \
#                         && abs(Lepton_pdgId[0])==13 \
#                         && Lepton_pt[0] >= 30 \
#                         && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                         && vjet_0_pt > 200 \
#                         '

# cuts["boost_CR_looseVBS_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["boost_CR_looseVBS_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["boost_CR_top_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["boost_CR_top_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 '

# cuts["boost_CR_wjets_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 '

# cuts["boost_CR_wjets_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && mjj_vbs >=300    \
#                                 && deltaeta_vbs >= 2  \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 '

# ########## --> Signal region
# # Increased cut on mjj_vbs and deltaeta VBS
# # Keeping top and W+jets control regions

# cuts["boost_SR_tightVBS_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["boost_SR_tightVBS_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["boost_SR_top_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["boost_SR_top_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bReq \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '
# cuts["boost_SR_wjets_ele"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && Lepton_pt[0] >= 40 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '

# cuts["boost_SR_wjets_mu"] = 'VBS_category==0 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && Lepton_pt[0] >= 30 \
#                                 && vbs_0_pt > 30 && vbs_1_pt > 30  \
#                                 && vjet_0_pt > 200 \
#                                 && PuppiMET_pt > 30 \
#                                 && bVeto \
#                                 && (mjj_vjet < 65 || mjj_vjet > 105) \
#                                 && mjj_vbs >=600    \
#                                 && deltaeta_vbs >= 3.5  \
#                                 '