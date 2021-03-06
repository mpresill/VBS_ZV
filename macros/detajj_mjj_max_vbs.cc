/*
  Building W pt proxy assuming second neutrino is collinear wrt to second lepton.
  1.) If event consist of 2 jets or more, the colinear neutrino2 is scaled with kfactor with invariant mass constrain from higgs boson.
  2.) The neutrino1 is recovered by subtracting MET with coliear neutrino2, and accounted with recovered pz by using invariant mass of W mass.
*/

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

class detajj : public multidraw::TTreeFunction {
public:
  detajj();

  char const* getName() const override { return "detajj"; }
  TTreeFunction* clone() const override { return new detajj(); }
  //TTreeFunction* clone() const override;
  unsigned getNdata() override { return 1; }

  float deltaEta(float, float);
  double evaluate(unsigned) override;


protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  IntArrayReader* CleanJet_jetId;
  FloatArrayReader* Jet_mass;
  UIntValueReader* nCleanJet;
  FloatArrayReader* CleanJet_pt;
  FloatArrayReader* CleanJet_eta;
  FloatArrayReader* CleanJet_phi;
  UIntValueReader* nLepton;  
};

detajj::detajj() :
  TTreeFunction()
{}


// --- Helper
float detajj::deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}
// Helper ---

double
detajj::evaluate(unsigned)
{

  float Mjj_tmp=0;
  float Mjj_max=0;
  float detajj_tmp=0;
  float detajj_mjj_max=0;
  unsigned int njet{*nCleanJet->Get()};
  unsigned int nlep{*nLepton->Get()};
 

  if (njet>=2){
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
      for (unsigned int jjet=0 ; jjet<njet ; jjet++){
        if (ijet==jjet) continue;
        TLorentzVector jet0; jet0.SetPtEtaPhiM(CleanJet_pt->At(ijet), CleanJet_eta->At(ijet),CleanJet_phi->At(ijet),Jet_mass->At(CleanJet_jetId->At(ijet)));   
        TLorentzVector jet1; jet1.SetPtEtaPhiM(CleanJet_pt->At(ijet), CleanJet_eta->At(ijet),CleanJet_phi->At(ijet),Jet_mass->At(CleanJet_jetId->At(jjet))); 
        Mjj_tmp = (jet0 + jet1).M();
        detajj_tmp = deltaEta(CleanJet_eta->At(ijet),CleanJet_eta->At(jjet));
        if(Mjj_tmp>=Mjj_max){
          Mjj_max=Mjj_tmp;
          detajj_mjj_max=detajj_tmp;
        }
      }
    }

 ///test 1: salvare elemento di un vettore per ogni mjj 
 // calcolare max con helper

    return detajj_mjj_max;

  }
  // CASE 2: assume lepton2 colinear with neutrino1
  else{
    return -9999.;
  }
}

void
detajj::bindTree_(multidraw::FunctionLibrary& _library)
{
  std::cout << "Loading detajj" << std::endl;
  _library.bindBranch(CleanJet_jetId, "CleanJetNotFat_jetIdx");
  _library.bindBranch(Jet_mass, "Jet_mass");
  _library.bindBranch(nCleanJet, "nCleanJetNotFat");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(nLepton, "nLepton");

}
