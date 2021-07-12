import os
import copy
import inspect



configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # current year
#configurations = os.path.dirname(configurations) # mkSHapePyRDF
#configurations = os.path.dirname(configurations) # Configurations
#configurations = os.path.dirname(configurations) # Configurations

# TO BE FIXED: change all CleanJet to CleanJet[CleanJetNotFat_jetIdx] after testing
#    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
#same for the index in the tagging


#aliases = {}

# imported from samples.py:
# samples, signals
mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mvaFall17V1Iso_WP90'  #should change to 2018?
muWP='cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1, 0)',
    'samples': mc
}
##additional variables for VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

###########################################################
################fakes
###########################################################
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
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
#added 20.11
aliases['antitopGenPtOTF'] = {
    'expr': 'Sum((GenPart_pdgId == -6 && OddVec(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}


aliases['Top_pTrw'] = {
            # New Top PAG added 20.11
    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPtOTF - 8.90557e-08*topGenPtOTF*topGenPtOTF) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPtOTF - 8.90557e-08*antitopGenPtOTF*antitopGenPtOTF))) + (topGenPtOTF * antitopGenPtOTF <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5
 #'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'samples': ['top']
}



# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples


############b tag
# B tagging
#loose 0.1241
#tight 0.7527

#bVeto 
aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) == 0'

}

#bReq
aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) >= 1'
 
}

aliases['bReqTight'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.8001) >= 1'
   
}


# B tag scale factors
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=20 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape,CleanJet_jetIdx)+1*(CleanJet_pt<=30 || AbsVec(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto*bVetoSF + bReq*bReqSF)',
    'samples': mc
}


for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

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

"""
# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF']),
    'samples': mc
}
"""
aliases['cat']={
    'expr': "jets_cat(nCleanJetNotFat, nCleanFatJet, CleanJet_pt, CleanJetNotFat_jetIdx, CleanJet_phi, CleanJet_eta, Jet_mass, CleanJet_jetIdx, CleanFatJet_mass,nLepton, Lepton_eta,  CleanFatJet_eta, Jet_qgl, CleanFatJet_jetIdx, Jet_btagDeepB, 2017)",
    }



aliases['Mjj_max']={
    'expr': "cat[0]"
    }
aliases['detajj_mjjmax']= {
      'expr': "cat[1]"
}
aliases['dphijj_mjjmax']={'expr': 'cat[2]'}

aliases['V_jet_mass']= {
      'expr': "cat[3]"
}
aliases['Zepp_ll']= {
      'expr': "cat[4]"
}
aliases['Zlep_1']= {
      'expr': "cat[5]"
}
aliases['Zlep_2']= {
      'expr': "cat[6]"
}

aliases['vbs_jet_pt1']= {
      'expr': "cat[7]"
}
aliases['vbs_jet_pt2']= {
      'expr': "cat[8]"
}
aliases['vbs_jet_eta1']= {
      'expr': "cat[9]"
}
aliases['vbs_jet_eta2']= {
      'expr': "cat[10]"
}
aliases['V_jet_pt1']= {
      'expr': "cat[11]"
}
aliases['V_jet_pt2']= {
      'expr': "cat[12]"
}
aliases['V_jet_eta1']= {
      'expr': "cat[13]"
}
aliases['V_jet_eta2']= {
      'expr': "cat[14]"
}
aliases['category']={
    'expr': "cat[15]"
    }
aliases['nCleanJet30'] = { 'expr': "cat[16]"}
aliases['Zvjet'] = { 'expr': "cat[17]"}
aliases['vbs_jet_qgl1']={'expr': "cat[18]"}
aliases['vbs_jet_qgl2']={'expr': "cat[19]"}
aliases['V_jet_qgl1']= {'expr': "cat[20]"}
aliases['V_jet_qgl2']={'expr': "cat[21]"}
aliases['FatJet_qgl']={'expr': "cat[22]"}
aliases['nbtag'] = {
         'expr': 'cat[23]'
}
"""
aliases['ptllDYW_NLO'] = {
    'expr': '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
}
aliases['ptllDYW_LO'] = {
    'expr': '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

}
"""

# variations
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
#new matteo aliases

aliases['nCleanGenJet'] = {
    'expr' : 'CountGenJet(nLeptonGen, LeptonGen_isPrompt, LeptonGen_pdgId, LeptonGen_pt, LeptonGen_eta, LeptonGen_phi, LeptonGen_mass, nPhotonGen, PhotonGen_pt, PhotonGen_eta, PhotonGen_phi, PhotonGen_mass, nGenJet, GenJet_pt, GenJet_eta, GenJet_phi)',
    'samples': mc
}

##### DY Z pT reweighting

aliases['getGenZpt_OTF'] = {
    'expr' : 'getGenZpt(nGenPart, GenPart_pt, GenPart_pdgId, GenPart_genPartIdxMother, GenPart_statusFlags, gen_ptll)',
    'samples': ['DY']
}


DYrew={
    '2016': {
        'NLO': "1.062955818914*((-0.0775395733886*TMath::Erf((x-14.4141170861)/7.10247643949)-0.00091236718546*x-(-0.0775395733886*TMath::Erf((40.0-14.4141170861)/7.10247643949)-0.00091236718546*40.0)+0.853848155607)*(x<40.0)+0.853848155607*(x>=40.0))",
        'LO': "1.063362210877*((-0.0553940992672*TMath::Erf((x-11.2183081709)/3.87755429192)+0.000493004133573*x-(-0.0553940992672*TMath::Erf((40.0-11.2183081709)/3.87755429192)+0.000493004133573*40.0)+0.908504652392)*(x<40.0)+0.908504652392*(x>=40.0))",
    },
    '2017': {
        'NLO': "1.072564805233*((0.212607076578*TMath::Erf((x-5.71348276564)/4.53536003061)-0.00482524130124*x+5.19057756733e-05*x*x-(0.212607076578*TMath::Erf((40.0-5.71348276564)/4.53536003061)-0.00482524130124*40.0+5.19057756733e-05*40.0*40.0)+0.989989173037)*(x<40.0)+0.989989173037*(x>=40.0))",
        'LO': "1.070357717802*((0.0904901258328*TMath::Erf((x-5.50288489736)/2.28426506238)+0.00938804955833*x-3.13579209847e-05*x*x-(0.0904901258328*TMath::Erf((40.0-5.50288489736)/2.28426506238)+0.00938804955833*40.0-3.13579209847e-05*40.0*40.0)+1.15868093233)*(x<40.0)+1.15868093233*(x>=40.0))",
    },
    '2018': {
        'NLO': "1.037822324341*((0.232707489797*TMath::Erf((x-5.49247649598)/5.14236049539)-0.00453696373368*x+7.45078183646e-05*x*x-(0.232707489797*TMath::Erf((40.0-5.49247649598)/5.14236049539)-0.00453696373368*40.0+7.45078183646e-05*40.0*40.0)+1.06118030177)*(x<40.0)+1.06118030177*(x>=40.0))",
        'LO': "1.038916491841*((0.0948703608054*TMath::Erf((x-5.47228332651)/2.2133221824)+0.00959307355966*x-1.67661013599e-06*x*x-(0.0948703608054*TMath::Erf((40.0-5.47228332651)/2.2133221824)+0.00959307355966*40.0-1.67661013599e-06*40.0*40.0)+1.22775815139)*(x<40.0)+1.22775815139*(x>=40.0))",
    },
}
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2017']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2017']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

###########################################################################################
# PU jet Id SF

# PU jet Id SF
#puidSFSource = '{}/patches/PUID_81XTraining_EffSFandUncties.root'.format(configurations)

aliases['PUJetIdSF'] = {
    'expr' : 'PUJetIdEventSF("/afs/cern.ch/user/a/ahakimi/ZV_analysis/mkShapePyRDF/patches/PUID_81XTraining_EffSFandUncties.root", "2017", "loose", nJet, nLepton, Lepton_eta, Lepton_phi, Jet_pt, Jet_eta, Jet_phi, Jet_jetId, Jet_genJetIdx, Jet_puId)',
    'samples': mc
}

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','PUJetIdSF', 'btagSF']),
    'samples': mc
}
# variations
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
