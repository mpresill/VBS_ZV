# cuts

cuts["supercut"] ={
    'expr': '( \
                  ( ( (abs(Lepton_pdgId[0])==11) && (Lepton_pt[0]>35) ) || \
                    ( (abs(Lepton_pdgId[0])==13) && (Lepton_pt[0]>30) ) )   \
                    && vbs_0_pt > 30 && vbs_1_pt > 30 \
                    && deltaeta_vbs >= 2  \
                    && PuppiMET_pt > 30 \
                    && mjj_vbs >=250 \
                   )',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}
#########################################################################
###############|----------------------------------|######################
###############|          Resolved category       |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["res_sig_mjjincl"] = {
    'expr': 'VBS_category==1 \
            && vjet_0_pt > 30 && vjet_1_pt > 30 \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            && bVeto \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}

cuts["res_wjetcr_mjjincl"] = {
    'expr': 'VBS_category==1 \
                && abs(Lepton_pdgId[0])==11 \
                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                && bVeto \
                ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True    
}

#########################################################################
###############|----------------------------------|######################
###############|          Boosted category        |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["boos_sig_mjjincl"] = {
    'expr': 'VBS_category==0 \
            && vjet_0_pt > 200 \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            && bVeto \
            && mjj_vbs >=250 \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}