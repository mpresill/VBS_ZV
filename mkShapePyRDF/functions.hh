#ifndef FUNCTIONS_HH
#define FUNCTIONS_HH

using namespace ROOT::VecOps;
//#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
//#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

float deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}




RVec<float> jets_cat(int nCleanJet,int  nFatJet,RVec<float> & CleanJet_pt, RVec<int> & CleanJetNotFat_jetId, RVec<float> & CleanJet_phi, RVec<float> & CleanJet_eta, RVec<float> & Jet_mass, RVec<int> &CleanJet_jetId, RVec<float> &FatJet_mass){



//first part: compute the mjj_max of all the AK4 (CleanedNotFat)
float Mjj_tmp=0;
float Mjj_max=0;
float deltamass_Vjet=1e5;
float detajj_tmp=0;
float detajj_mjj_max=0;
float Vjet_mass_tmp = 0.;
unsigned int njet=nCleanJet;
unsigned int nFJ=nFatJet;

// Index in the collection of CleanJetNotFat
int VBS_jets[2] = {-999,-999};
int V_jets[2]   = {-999,-999};
float category = -999;  // 0 fatjet, 1 resolved, -1 none

// Load all the quadrivectors for performance reason
std::vector<TLorentzVector> vectors; 
for (unsigned int ijet=0 ; ijet<njet ; ijet++){
TLorentzVector jet0; 
jet0.SetPtEtaPhiM(CleanJet_pt[CleanJetNotFat_jetId[ijet]], CleanJet_eta[CleanJetNotFat_jetId[ijet]],CleanJet_phi[CleanJetNotFat_jetId[ijet]],Jet_mass[CleanJet_jetId][CleanJetNotFat_jetId[ijet]]); 
vectors.push_back(jet0);
}

if (njet>=2){
// Calculate max mjj invariant pair on CleanJetNotFat to exclude the correct jets
for (unsigned int ijet=0 ; ijet<njet ; ijet++){
    for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
    if (ijet==jjet) continue;
    TLorentzVector jet0 = vectors.at(ijet);
    TLorentzVector jet1 = vectors.at(jjet); 

    Mjj_tmp = (jet0 + jet1).M();
    detajj_tmp = deltaEta(CleanJet_eta[CleanJetNotFat_jetId[ijet]],CleanJet_eta[CleanJetNotFat_jetId[jjet]]);
    if( Mjj_tmp >= Mjj_max ){
        Mjj_max=Mjj_tmp;
        detajj_mjj_max=detajj_tmp;
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
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
    for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
        if (VBS_jets[0] == ijet || VBS_jets[1] == ijet || VBS_jets[0] == jjet || VBS_jets[1] == jjet){
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


//create vec [category, vbsjet1, vbsjet2, vjet1, vjet2, mjjmax,detajjmjjmax,vjetmass]

RVec<float> cat{category, -999,-999,-999,-999, Mjj_tmp,detajj_mjj_max,Vjet_mass_tmp };

cat[0]=category;
if (VBS_jets[0] != -999) cat[1]= CleanJetNotFat_jetId[VBS_jets[0]];
if (VBS_jets[1] != -999) cat[2]= CleanJetNotFat_jetId[VBS_jets[1]];
if (V_jets[0] != -999)   cat[3]= CleanJetNotFat_jetId[V_jets[0]];
if (V_jets[1] != -999)   cat[4]= CleanJetNotFat_jetId[V_jets[1]];

return cat;
}


#endif

//example
/*
float Whad_pt(int category, RVec<int> & V_jets, RVec<float> & CleanJet_pt,RVec<float> & CleanJet_eta, 
                RVec<float> & CleanJet_phi, RVec<float> & Jet_mass, RVec<int> & CleanJet_jetIdx)
{
    if (category != 1) return -999.;
    
    TLorentzVector vjet1; 
    vjet1.SetPtEtaPhiM(CleanJet_pt.at(V_jets.at(0)),
                    CleanJet_eta.at(V_jets.at(0)),
                    CleanJet_phi.at(V_jets.at(0)),
                    Jet_mass.at(CleanJet_jetIdx.at(V_jets.at(0))));

    TLorentzVector vjet2; 
    vjet2.SetPtEtaPhiM(CleanJet_pt.at(V_jets.at(1)),
                    CleanJet_eta.at(V_jets.at(1)),
                    CleanJet_phi.at(V_jets.at(1)),
                    Jet_mass.at(CleanJet_jetIdx.at(V_jets.at(1))));

    return (vjet1+vjet2).Pt();

    
}

*/

