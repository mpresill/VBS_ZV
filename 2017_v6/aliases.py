import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) 
configurations = os.path.dirname(configurations)
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mvaFall17V1Iso_WP90'
muWP = 'cut_Tight_HWWW'

newEleWP = 'mvaFall17V1Iso_WP90_tthmva_70'
newMuWP = 'cut_Tight_HWWW_tthmva_80'

aliases['LepWPCut'] = {
    #'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP+'*( ( (abs(Lepton_pdgId[0])==11) ||  Muon_mvaTTH[Lepton_muonIdx[0]]>0.8)  && ( ( abs(Lepton_pdgId[1])==11) || Muon_mvaTTH[Lepton_muonIdx[1]]>0.8) )',
    'samples': mc + ['DATA']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

# B tagging

aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
}

# B tag scale factors

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    #'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}

for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/patches/pujetidsf_event.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, '2017', 'loose'),
    'samples': mc
}
######################################################
####################### data/MC scale factors
######################################################
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight','PUJetIdSF']),
    'samples': mc
}
######################################################
################# variations
######################################################
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

############################################################
#############additional variables
############################################################
aliases['M_ZV'] = {
             'class': 'VBSvar_AK4',
             'args': ("M_ZV"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]           
 }

aliases['mll_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("mll_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['mjj_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("mjj_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['detajj_vbs'] = {
             'class': 'VBSvar_AK4',
             'args': ("detajj_vbs"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/vbs_variables_class_AK4.cc+'.format(configurations)
             ]
 }

aliases['mjj_vbs_AK4NotFat'] = {
    'class': 'WHSS_wpt_v3',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/mjj_max_vbs.cc+'.format(configurations)
    ]
}

aliases['detajj_vbs_AK4NotFat'] = {
    'class': 'detajj',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/detajj_mjj_max_vbs.cc+'.format(configurations)
    ]
}

aliases['eta1eta2'] = {
    'class': 'eta12',
    'args': (),
    'linesToAdd': [
        '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/macros/eta12_mjj_max_vbs.cc+'.format(configurations)
    ]
}


############################
###### SR e CR var
############################

aliases['2lSF'] = {
    'expr': '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) )'
}


aliases['2lOF'] = {
    'expr': '((Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=25.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5)  || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 && Alt$(Lepton_pt[0],0.)>=25. && Alt$(Lepton_pt[1],0.)>=20.  && fabs(Alt$(Lepton_eta[0],-9999.))<2.4 && fabs(Alt$(Lepton_eta[1],-9999.))<2.4 ) )'
}


aliases['Zlep_1'] = {
    'expr': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj_vbs_AK4NotFat'
}

aliases['Zlep_2'] = {
    'expr': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[1],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj_vbs_AK4NotFat'
}

