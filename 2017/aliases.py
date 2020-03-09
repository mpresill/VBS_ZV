import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017v6s5
configurations = os.path.dirname(configurations) # VBSjjlnu
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

bAlgo = 'DeepB'
bWP = '0.1522'

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0)'
}
aliases['tauVeto_ww'] = {
    'expr': '(Sum$(Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)<10 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) > 0.4) == 0)'
}
aliases['tauVeto_wz'] = {
    'expr': '(Sum$(Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>20 && Alt$(Lepton_pt[3],0.)<10 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[2],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[2],-9999.))-pi)-pi, 2) ) > 0.4) == 0)'
}

aliases['tauVeto_zz'] = {
    'expr': '(Sum$(Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>10 && Alt$(Lepton_pt[3],0.)>10 && Alt$(Lepton_pt[4],0.)<10 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[2],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[2],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[3],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[3],-9999.))-pi)-pi, 2) ) > 0.4) == 0)'
}

aliases['M_leplepBjet'] = {
             'class': 'InvMass',
             'args': ("M_leplepBjet"),
             'linesToAdd' : [
                 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                 '.L /afs/cern.ch/work/m/mpresill/Latino_workdir/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2017/M_leplepBjet_class.cc+'.format(configurations)
             ]           
 }



