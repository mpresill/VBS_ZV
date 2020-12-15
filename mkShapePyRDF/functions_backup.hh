#ifndef FUNCTIONS_HH
#define FUNCTIONS_HH

using namespace ROOT::VecOps;
//#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
//#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TH1.h"

#include <cmath>
#include <string>
#include <vector>
#include <array>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

float deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}
float deltaphi(float phi1, float phi2){
    float PHI = std::abs(phi1-phi2);
  if (PHI<=3.14159265)
    return PHI;
  else
    return 2*3.14159265-PHI;
}



RVec<float> jets_cat(int nCleanJet,int  nFatJet,RVec<float> & CleanJet_pt, RVec<int> & CleanJetNotFat_jetId, RVec<float> & CleanJet_phi, RVec<float> & CleanJet_eta, RVec<float> & Jet_mass, RVec<int> &CleanJet_jetId, RVec<float> &FatJet_mass, int nLepton, RVec<float> & Lepton_eta){



//first part: compute the mjj_max of all the AK4 (CleanedNotFat)
float Mjj_tmp=0;
float Mjj_max=0;
float deltamass_Vjet=1e5;
float detajj_tmp=0;
float detajj_mjj_max=0;
float dphijj_mjj_max=0;
float Vjet_mass_tmp = 0.;
float mean_eta_vbs=0;
float sum_eta_lep=0;
unsigned int njet=nCleanJet;
unsigned int nFJ=nFatJet;
unsigned int njetNotFat=CleanJetNotFat_jetId.size();
unsigned int nlep=nLepton;

// Index in the collection of CleanJetNotFat
int VBS_jets[2] = {999,999};
int V_jets[2]   = {999,999};
float category = 999;  // 0 fatjet, 1 resolved, -1 none

// Load all the quadrivectors for performance reason

float pt_cut=30. ;//define pt cut on jets
std::vector<TLorentzVector> vectors; 
for (unsigned int ijet=0 ; ijet<njetNotFat ; ijet++){
TLorentzVector jet0; 
//if ijet < len(CleanJetNotFat_jet_id)
jet0.SetPtEtaPhiM(CleanJet_pt.at(CleanJetNotFat_jetId.at(ijet)), CleanJet_eta.at(CleanJetNotFat_jetId.at(ijet)),CleanJet_phi.at(CleanJetNotFat_jetId.at(ijet)),Jet_mass.at(CleanJet_jetId.at(CleanJetNotFat_jetId.at(ijet)))); 
if (jet0.Pt()>pt_cut){vectors.push_back(jet0);}
}

njet=vectors.size();
njetNotFat=njet; //does it makes sense to keep both?

if (njet>=2 && nlep==2){
    sum_eta_lep=Lepton_eta[0]+Lepton_eta[1];
// Calculate max mjj invariant pair on CleanJetNotFat to exclude the correct jets
for (unsigned int ijet=0 ; ijet<njetNotFat ; ijet++){
    for (unsigned int jjet= ijet+1 ; jjet<njetNotFat ; jjet++){
    if (ijet==jjet) continue;
    TLorentzVector jet0 = vectors.at(ijet);
    TLorentzVector jet1 = vectors.at(jjet); 

    Mjj_tmp = (jet0 + jet1).M();
    detajj_tmp = deltaEta(CleanJet_eta.at(CleanJetNotFat_jetId.at(ijet)),CleanJet_eta.at(CleanJetNotFat_jetId.at(jjet)));
    
    if( Mjj_tmp >= Mjj_max ){
        Mjj_max=Mjj_tmp;
        detajj_mjj_max=detajj_tmp;
        dphijj_mjj_max=deltaphi(CleanJet_phi.at(CleanJetNotFat_jetId.at(ijet)),CleanJet_phi.at(CleanJetNotFat_jetId.at(jjet)));
        mean_eta_vbs=std::abs(CleanJet_eta.at(CleanJetNotFat_jetId.at(ijet))+CleanJet_eta.at(CleanJetNotFat_jetId.at(jjet)))*0.5;
        // Index in the collection of CleanJetNotFat
        VBS_jets[0]= ijet;
        VBS_jets[1]= jjet;
    }
    }
}

// Now we have the njets
// Check if boosted
if (nFJ >= 1){
    category = 0;
    Vjet_mass_tmp = FatJet_mass[0];

}else if (njet>=4)
{ 
    category = 1;
    for (unsigned int ijet=0 ; ijet<njetNotFat ; ijet++){
    for (unsigned int jjet= ijet+1 ; jjet<njetNotFat ; jjet++){
        if (VBS_jets[0] == ijet || VBS_jets[1] == ijet || VBS_jets[0] == jjet || VBS_jets[1] == jjet) continue;
        else{
        TLorentzVector jet0 = vectors.at(ijet);
        TLorentzVector jet1 = vectors.at(jjet); 
        float mvjet = (jet0+jet1).M();
        float dmass = abs( mvjet - 85.7863 );
        if (dmass < deltamass_Vjet){
            // Index in the collection of CleanJetNotFat
            V_jets[0] = ijet;
            V_jets[1] = jjet;
            deltamass_Vjet = dmass;
            Vjet_mass_tmp = mvjet;
        }
        }
    }
    }
}else{
    category = -1;
}

}else{
category = -1;
}

int vbs_jet_0=999;
int vbs_jet_1=999;
int v_jet_0=999;
int v_jet_1=999;


if (VBS_jets[0] != 999) vbs_jet_0 = CleanJetNotFat_jetId.at(VBS_jets[0]);
if (VBS_jets[1] != 999) vbs_jet_1 = CleanJetNotFat_jetId.at(VBS_jets[1]);

if (V_jets[0] != 999) v_jet_0 = CleanJetNotFat_jetId.at(V_jets[0]);

if (V_jets[1] != 999) v_jet_1= CleanJetNotFat_jetId.at(V_jets[1]);





//create vec [Mjj_max, detajj_mjjmax, dphijj_mjjmax, V_jet_mass, Zepp_ll, Zlep_1, Zlep_2, vbs_jet_pt1, vbs_jet_pt2, vbs_jet_eta1, vbs_jet_eta2, v_jet_pt1, v_jet_pt2, v_jet_eta1, v_jet_eta2, category]
float Zepp_ll=std::abs(sum_eta_lep-mean_eta_vbs)/detajj_mjj_max;
float Zlep_1=(Lepton_eta[0]-mean_eta_vbs)/detajj_mjj_max;
float Zlep_2=(Lepton_eta[1]-mean_eta_vbs)/detajj_mjj_max;


RVec<float> cat{Mjj_max,detajj_mjj_max,dphijj_mjj_max,Vjet_mass_tmp, Zepp_ll, Zlep_1, Zlep_2, 999,999,999,999,999,999,999,999, category };

if (vbs_jet_0 != 999){
     cat[7]= CleanJet_pt.at(vbs_jet_0);
     cat[9]= CleanJet_eta.at(vbs_jet_0);
}
if (vbs_jet_1 != 999){
     cat[8]= CleanJet_pt.at(vbs_jet_1);
     cat[10]= CleanJet_eta.at(vbs_jet_1);
}

if (category==1){
    if (v_jet_0 != 999){
        cat[11]=CleanJet_pt.at(v_jet_0);
        cat[13]=CleanJet_eta.at(v_jet_0);
    }
    if (v_jet_1 != 999){
    cat[12]=CleanJet_pt.at(v_jet_1);
    cat[14]=CleanJet_eta.at(v_jet_1);
    }
}


return cat;
}

//My version=========================================================================================


float PUJetIdEventSF(string filename, string yr, string wp, int nJet, int nLepton, RVec<float> & Lepton_eta, RVec<float> & Lepton_phi, RVec<float> & Jet_pt, RVec<float> & Jet_eta, RVec<float> & Jet_phi, RVec<int> & Jet_jetId, RVec<int> & Jet_genJetIdx, RVec<int> & Jet_puId){
    //unsigned nWPs = 1;
//def types
    typedef std::array<std::unique_ptr<TH1>, 2> MapSet;
    typedef std::array<MapSet, 2> MapSets;
    //MapSets sfMapSets;
    //MapSets effMapSets;
    float scalefactor = 1.;
    std::string wpStr_{};
    MapSets effMapSets;
    MapSets sfMapSets;
    std::string year;
    wpStr_=wp;
    year = yr;
    std::string wp_;

//assign wp_
    if (wpStr_ == "loose") {
        wp_ = "L";
    }else if (wpStr_ == "medium"){
        wp_ = "M";
    }else if (wpStr_ == "tight"){
        wp_ = "T";
    }else{
        throw std::runtime_error("unknown working point " + wpStr_);
    }
//read sf file
//TDirectory::TContext context;

    TFile *f = TFile::Open(filename.c_str());
    // Same order of bit to check the Jetid 
    effMapSets[0][1].reset(static_cast<TH1*>(f->Get(("h2_eff_mc"+year +"_" + wp_).c_str())));
    effMapSets[1][1].reset(static_cast<TH1*>(f->Get(("h2_mistag_mc"+year +"_" + wp_).c_str())));
    effMapSets[0][1]->SetDirectory(nullptr);
    effMapSets[1][1]->SetDirectory(nullptr);
    sfMapSets[0][1].reset(static_cast<TH1*>(f->Get(("h2_eff_sf"+year +"_" + wp_).c_str())));
    sfMapSets[1][1].reset(static_cast<TH1*>(f->Get(("h2_mistag_sf"+year +"_" + wp_).c_str())));
    sfMapSets[0][1]->SetDirectory(nullptr);
    sfMapSets[1][1]->SetDirectory(nullptr);
    
    delete f;



//calculate SF
 unsigned nJ = nJet;

  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    double pt= Jet_pt.at(iJ);
    double eta=Jet_eta.at(iJ);


//not  sure about following line
    if (pt < 30. || pt > 50.|| std::abs(eta) > 4.7 || Jet_jetId.at(iJ)<2)
    // excluding also the jets with jetId < 2 since we are considering only these jets in the selection before PUid selection.
      continue;

    bool isLeptonMatched = false;
    for (int ilep = 0; ilep < nLepton; ilep++){
      float lepEta = Lepton_eta.at(ilep);
      float lepPhi = Lepton_phi.at(ilep);
      float jetEta = Jet_eta.at(iJ);
      float jetPhi = Jet_phi.at(iJ);
      float dPhi = abs(lepPhi - jetPhi);
      if (dPhi > TMath::Pi())  
        dPhi = 2*TMath::Pi() - dPhi;

      float dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi;
      
      if (dR2 < 0.3*0.3)  isLeptonMatched =true;
    }
    if (isLeptonMatched) continue;

    unsigned mapType{};
    if (Jet_genJetIdx.at(iJ) != -1)
      mapType = 0;
    else
      mapType = 1;
    
      // if mapTap = 0 efficiency h2 are used, if mapType = 1 mistag h2 are used
      
      auto& sf_map{sfMapSets[mapType][1]};
      auto& eff_map{effMapSets[mapType][1]};

      int iX{eff_map->GetXaxis()->FindFixBin(pt)};
      if (iX == 0)
        iX = 1;
      else if (iX > eff_map->GetNbinsX())
        iX = eff_map->GetNbinsX();

      int iY{eff_map->GetYaxis()->FindFixBin(eta)};
      if (iY == 0)
        iY = 1;
      else if (iY > eff_map->GetNbinsY())
        iY = eff_map->GetNbinsY();

      // iWP = 0 Tight, 1 Medium, 2 Loose 
      unsigned iWP = 2;
      bool passId = (Jet_puId.at(iJ)) & (1 << iWP);
      if (passId)  scalefactor *= (sf_map->GetBinContent(iX, iY));
      else         
            scalefactor *= (1- sf_map->GetBinContent(iX, iY)*eff_map->GetBinContent(iX,iY)) / (1-eff_map->GetBinContent(iX,iY));
            
    }
	//cout << "test PU SF" << endl;
    return scalefactor;
}

float getGenZpt(int nGenPart, RVec <float> & GenPart_pt, RVec<int> & GenPart_pdgId, RVec<int> & GenPart_genPartIdxMother, RVec<int> & GenPart_statusFlags, float gen_ptll){
 	cout << "test 1 getGenZpt" <<endl;   
    unsigned nGen = nGenPart;
    std::vector<int> LepCands{};
    std::vector<int> MotherIdx{};
    std::vector<int> MotherPdgId{};
    int pdgId, sFlag, MIdx;
    bool hasZ = false;


    for (unsigned iGen{0}; iGen != nGen; ++iGen){
    pdgId = std::abs(GenPart_pdgId.at(iGen));
    sFlag = GenPart_statusFlags.at(iGen);
    //std::cout << pdgId << " ; " << sFlag << " ; " << GenPart_pt->At(iGen) << " ; " << GenPart_genPartIdxMother->At(iGen) << std::endl;
    if (((pdgId == 11) || (pdgId == 13) || (pdgId == 15)) && ((sFlag >> 0 & 1) || (sFlag >> 2 & 1) || (sFlag >> 3 & 1) || (sFlag >> 4 & 1))){
      LepCands.push_back(iGen);
      MIdx = GenPart_genPartIdxMother.at(iGen);
      MotherIdx.push_back(MIdx);
      if (MIdx > -1){
        MotherPdgId.push_back(GenPart_pdgId.at(MIdx));
        if (GenPart_pdgId.at(MIdx)==23) hasZ = true;
      }else{
        MotherPdgId.push_back(0);
      }
    }
  }

  //std::cout << "Check:" << std::endl;
  for (unsigned iGen{0}; iGen != LepCands.size(); ++iGen){
    for (unsigned jGen{0}; jGen != LepCands.size(); ++jGen){
      if (jGen <= iGen) continue;
      //std::cout << iGen << " ; " << MotherIdx[iGen] << " ; " << jGen << " ; " << MotherIdx[jGen] << " ; " << MotherPdgId[iGen] << " ; " << hasZ << std::endl;
      // Some DY samples generate the Z; others have the two leptons produced directly -> motherId is 0 for those events
      if (hasZ){
        if (MotherIdx[iGen] == MotherIdx[jGen] && MotherPdgId[iGen] == 23) return GenPart_pt.at(MotherIdx[iGen]);
      }else{
        if (MotherIdx[iGen] == MotherIdx[jGen] && MotherIdx[iGen] == 0) return GenPart_pt.at(MotherIdx[iGen]);
      }
    }
  }
  //std::cout << "Falling back!" << std::endl;
  cout << "test 2 getGenZpt" <<endl;
  return gen_ptll; // Fallback value
}

int CountGenJet(int nLeptonGen, RVec<bool> & LeptonGen_isPrompt, RVec<int> & LeptonGen_pdgId, RVec<float> & LeptonGen_pt, RVec<float> & LeptonGen_eta, RVec<float> &  LeptonGen_phi, RVec<float> & LeptonGen_mass, int nPhotonGen, RVec<float> &  PhotonGen_pt, RVec<float> & PhotonGen_eta, RVec<float> & PhotonGen_phi, RVec<float> & PhotonGen_mass, int nGenJet, RVec<float> & GenJet_pt, RVec<float> & GenJet_eta, RVec<float> & GenJet_phi){
	 cout << "test 1 CountGenJet" <<endl;
    unsigned nJ = nGenJet;

    unsigned nL = nLeptonGen;

    std::vector<unsigned> iPromptL{};
    iPromptL.reserve(nL);

    for (unsigned iL{0}; iL != nL; ++iL) {
    if (!LeptonGen_isPrompt.at(iL))
        continue;

    unsigned absId{static_cast<unsigned>(std::abs(LeptonGen_pdgId.at(iL)))};
    if (absId != 11 && absId != 13)
        continue;

    iPromptL.push_back(iL);
    }

    if (iPromptL.size() == 0) {
    unsigned n{0};
    for (unsigned iJ{0}; iJ != nJ; ++iJ) {
        if (GenJet_pt.at(iJ) > 30.)
        ++n;
    }
    return n;
    }

    std::vector<ROOT::Math::PtEtaPhiMVector> dressedLeptons{};
    for (unsigned iL : iPromptL) {
    dressedLeptons.emplace_back(
        LeptonGen_pt.at(iL),
        LeptonGen_eta.at(iL),
        LeptonGen_phi.at(iL),
        LeptonGen_mass.at(iL));
    }

    unsigned nP = nPhotonGen;

    for (unsigned iP{0}; iP != nP; ++iP) {
    double minDR2{1000.};
    int iDMin{-1};
    for (unsigned iD{0}; iD != iPromptL.size(); ++iD) {
        unsigned iL{iPromptL[iD]};
        double dEta{LeptonGen_eta.at(iL) - PhotonGen_eta.at(iP)};
        double dPhi{TVector2::Phi_mpi_pi(LeptonGen_phi.at(iL) - PhotonGen_phi.at(iP))};
        double dR2{dEta * dEta + dPhi * dPhi};
        if (dR2 < minDR2) {
        minDR2 = dR2;
        iDMin = iD;
        }
    }

    if (minDR2 < 0.09)
        dressedLeptons[iDMin] += ROOT::Math::PtEtaPhiMVector(
        PhotonGen_pt.at(iP),
        PhotonGen_eta.at(iP),
        PhotonGen_phi.at(iP),
        PhotonGen_mass.at(iP));
    }

    unsigned n{0};
    for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    if (GenJet_pt.at(iJ) < 30.)
        continue;

    bool overlap{false};
    for (auto& p4 : dressedLeptons) {
        if (p4.pt() < 10.)
        continue;

        double dEta{p4.eta() - GenJet_eta.at(iJ)};
        double dPhi{TVector2::Phi_mpi_pi(p4.phi() - GenJet_phi.at(iJ))};
        if (dEta * dEta + dPhi * dPhi < 0.016) {
        overlap = true;
        break;
        }
    }
    if (!overlap)
        ++n;
    }
    cout << "test 2 CountGenJet" <<endl;
    return n;  



}












#endif


