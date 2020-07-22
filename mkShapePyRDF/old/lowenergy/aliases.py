#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake_em', 'Fake_me', 'DATA')]

bAlgo = 'DeepB'
bTaggingWPs = {
    "deepCSV" : {  # DeepB
        "L" : 0.1522,
        "M" : 0.4941,
        "T" : 0.8001
    }
}


aliases['bVeto'] = {
'expr': '( Sum( (CleanJet_pt > 20.) && (abs(CleanJet_eta)<2.5) && ( Take(Jet_btagDeepB,CleanJet_jetIdx)> 0.1522) ) == 0 )'
}

aliases['btag0'] = {
'expr': '( Alt(CleanJet_pt,0,0)<30 && Sum( (CleanJet_pt > 20.) && (abs(CleanJet_eta)<2.5) && (Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.1522) )>0 \
         )'
}

aliases['btag1'] = {
'expr': '(    Alt(CleanJet_pt,0,0)>30 && abs(Alt(CleanJet_eta,0,99))<2.5\
           && Alt(CleanJet_pt,1,0)<30 \
           && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],0) > 0.1522 )'
}

aliases['btag2'] = {
'expr': '(    Alt(CleanJet_pt,0,0)>30 \
           && Alt(CleanJet_pt,1,0)>30 \
           && ( ( abs(Alt(CleanJet_eta,0,99))<2.5 && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],0) > 0.1522 ) \
             || ( abs(Alt(CleanJet_eta,1,99))<2.5 && Alt(Jet_btagDeepB,CleanJet_jetIdx[1],0) > 0.1522 ) ) \
         )' 
}

# # NB These scale factors depend on the selections defined above, if different selections are used also the following expressions need to be changed!
aliases['bVetoSF'] = {
'expr': '( TMath::Exp(Sum( LogVec( (CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}
aliases['btag0SF'] = {
'expr': '( TMath::Exp(Sum( LogVec( (CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_shape,CleanJet_jetIdx)+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}

aliases['btag1SF'] = {
'expr': '( ( Alt(CleanJet_pt,0, 0)>30 && abs(Alt(CleanJet_eta,0,99))<2.5 )*( Alt(Jet_btagSF_shape,CleanJet_jetIdx[0], 1) ) + ( Alt(CleanJet_pt,0, 0)<30 || abs(Alt(CleanJet_eta,0,99))>2.5 ) )',
'samples': mc
}

aliases['btag2SF'] = {
'expr': '( ( ( Alt(CleanJet_pt,0, 0)>30 && abs(Alt(CleanJet_eta,0,99))<2.5 )*( Alt(Jet_btagSF_shape,CleanJet_jetIdx[0], 1) ) + ( Alt(CleanJet_pt,0, 0)<30 || abs(Alt(CleanJet_eta,0,99))>2.5 ) )* \
           ( ( Alt(CleanJet_pt,1, 0)>30 && abs(Alt(CleanJet_eta,1,99))<2.5 )*( Alt(Jet_btagSF_shape,CleanJet_jetIdx[1], 1) ) + ( Alt(CleanJet_pt,1, 0)<30 || abs(Alt(CleanJet_eta,1,99))>2.5 ) ) )\
        ',
'samples': mc
}

aliases['btagSF'] = {
'expr': '( bVetoSF*bVeto + btag0SF*btag0 + btag1SF*btag1 + btag2SF*btag2 + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )',
'samples': mc
}


systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shape','shape_up_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shape','shape_up_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shape','shape_up_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shape','shape_down_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shape','shape_down_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shape','shape_down_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }


