import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017v6s5
configurations = os.path.dirname(configurations) # VBSjjlnu
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

############################################
# DNN reader

# mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2017v6s5/mva/'
# models_path = '/eos/home-d/dmapelli/public/latino/Full2017v6/lowen_looseVBS/models'

# aliases['DNNoutput_boosted'] = {
#     'class': 'MVAReader',
#     'args': ( models_path +'/v8/boosted', False, 0),
#     'linesToAdd':[
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         'gSystem->Load("libDNNEvaluator.so")',
#         '.L ' + mva_reader_path + 'mva_reader.cc+', 
#     ],
# }

# aliases['DNNoutput_resolved'] = {
#     'class': 'MVAReader',
#     'args': ( models_path+ '/v8/resolved', False, 1),
#     'linesToAdd':[
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         'gSystem->Load("libDNNEvaluator.so")',
#         '.L ' + mva_reader_path + 'mva_reader.cc+', 
#     ],
# }


############################################
# BTag

bAlgo = 'DeepB'
bWP = '0.1522'

aliases['bVeto'] = {
    'expr': '(Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) >= 1)'
}


aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF + ( (!bVeto) && (!bReq) ))',
    'samples': mc
}


# #systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']
# systs = ['jes']

# for s in systs:
#   aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
#   aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }

################################################################################################


# LastProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 1' % lastcopy,
     'samples': ['top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum((GenPart_pdgId == 6 && OddVec(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
     'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum((GenPart_pdgId == -6 && OddVec(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
     'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
     'samples': ['top']
}



# aliases['fake_weight_corrected'] = {
#     'class': 'FakeWeightCorrector',
#     'args': ("%s/VBSjjlnu/Full2017v6/corrections/fakeweight_correction.root" % configurations, 
#                 "mvaFall17V1Iso_WP90", "fakeW_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_mu10_ele35", 
#                 os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90/EleFR_jet35.root",
#                 os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90/ElePR.root"),
#     'linesToAdd' : [
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         '.L %s/patches/fakeweight_corrector.cc+' % configurations
#      ],
#     'samples': "Fake"           
# }


# aliases['nvtx_reweighting'] = {
#     'class': 'NvtxReweight',
#     # Using Z->mm factors for both electron and muon regions
#     'args':("%s/VBSjjlnu/Full2017v6/corrections/zmmnorm_reweighting_Zmm_fit_2017.txt" % configurations),
#     'linesToAdd' : [
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         '.L %s/patches/nvtx_reweight.cc+' % configurations
#    ],
#     'samples' : mc      
# }

# ##############################################################
# #### Additional variables

# aliases['deltaphi_lep_whad'] = {
#             'class': 'DeltaPhiVars',
#             'args': ("deltaphi_lep_whad"),
#             'linesToAdd' : [
#                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#                 '.L {}/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc+'.format(configurations)
#             ]           
# }

# aliases['deltaphi_lep_jet0'] = {
#             'class': 'DeltaPhiVars',
#             'args': ("deltaphi_lep_jet0"),
#             'linesToAdd' : [
#                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#                 '.L {}/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc+'.format(configurations)
#                 ]  
# }

# aliases['deltaphi_lep_vbsjets'] = {
#             'class': 'DeltaPhiVars',
#             'args': ("deltaphi_lep_vbsjets"),
#             'linesToAdd' : [
#                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#                 '.L {}/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc+'.format(configurations)
#             ]  
# }

# aliases['deltaphi_lep_ww'] = {
#             'class': 'DeltaPhiVars',
#             'args': ("deltaphi_lep_ww"),
#             'linesToAdd' : [
#                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#                 '.L {}/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc+'.format(configurations)
#             ]  
# }
