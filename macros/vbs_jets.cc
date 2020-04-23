/*
Building invariant mass of the VBS jets and their delta R:
1) if the event 2 or more jets compute the maximum invariant mass
2) returns also the delta R (and eta1*eta2) of the two jets making the highet mjj
*/

//see https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/macros/whss_wlep_v3.cc

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TSystem.h"

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iterator>

#include "TLorentzVector.h"
#include "TVector2.h"
#include "TMath.h"

class VBS_ak4 : public multidraw::TTreeFunction {
public:
  VBS_ak4();

  char const* getName() const override { return "VBS_ak4"; }
  TTreeFunction* clone() const override { return new VBS_ak4(); }
  //TTreeFunction* clone() const override;
  unsigned getNdata() override { return 1; }

//  float deltaPhi(float, float);
// float deltaR(float, float, float, float);
//float deltaEta(float, float);
  double evaluate(unsigned) override;
  


protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader* nLepton;
  UIntValueReader* nCleanFatJet;
  UIntValueReader* nCleanJet;
  FloatArrayReader* CleanJet_pt;
  FloatArrayReader* CleanJet_eta;
  FloatArrayReader* CleanJet_phi;
  IntArrayReader* CleanJet_jetId;
  FloatArrayReader* CleanJet_mass;
  
};

VBS_ak4::VBS_ak4() :
  TTreeFunction()
{}

// --- Helper
/*float VBS_ak4::deltaPhi(float phi1, float phi2)
{
  float PHI = std::abs(phi1-phi2);
if (PHI<=3.14159265)
  return PHI;
else
  return 2*3.14159265-PHI;
}

float VBS_ak4::deltaR(float phi1, float eta1, float phi2, float eta2) {
  //return sqrt((eta2-eta1)**2+deltaPhi(phi1,phi2)**2);
  return sqrt( pow((eta2-eta1),2) + pow(deltaPhi(phi1,phi2),2) );
}

float VBS_ak4::deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}*/
// Helper ---

double
VBS_ak4::evaluate(unsigned)
{
    
  unsigned int njet{*nCleanJet->Get()}; 
  unsigned int nlep{*nLepton->Get()};
  unsigned int nfatjet{*nCleanFatJet->Get()};

  double Mjj_temp=0;
  double Mjj_max=0;  

  if (nlep<2)
    return -9999.;
  if (nfatjet!=1 )
    return -9999.;

  // build dijet system
  if (njet>=2){
    for (unsigned int ijet=0 ; ijet<=njet ; ijet++){
      for (unsigned int jjet=ijet+1 ; jjet<=njet ; jjet++){
        TLorentzVector jet0; jet0.SetPtEtaPhiM(Jet_pt->At(Jet_jetId->At(ijet)), Jet_eta->At(Jet_jetId->At(ijet)),Jet_phi->At(Jet_jetId->At(ijet)),Jet_mass->At(Jet_jetId->At(ijet)));   
        TLorentzVector jet1; jet1.SetPtEtaPhiM(Jet_pt->At(Jet_jetId->At(jjet)), Jet_eta->At(Jet_jetId->At(jjet)),Jet_phi->At(Jet_jetId->At(jjet)),Jet_mass->At(Jet_jetId->At(jjet))); 
        Mjj_temp=(jet0+jet1).M();
        if(Mjj_temp >= Mjj_max){
          Mjj_max=Mjj_temp;
        }
      } // inner jet loop
    } // outer jet loop
  }

  return Mjj_max;

}

void
VBS_ak4::bindTree_(multidraw::FunctionLibrary& _library)
{
  std::cout << "Loading VBS_ak4" << std::endl;
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(nCleanFatJet, "nCleanFatJet");
  _library.bindBranch(nCleanJet, "nCleanJetNotFat");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(CleanJet_jetId, "CleanJet_jetIdx");
  _library.bindBranch(CleanJet_mass, "Jet_mass");

}