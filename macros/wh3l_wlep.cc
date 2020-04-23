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

class WHSS_wpt_v3 : public multidraw::TTreeFunction {
public:
  WHSS_wpt_v3();

  char const* getName() const override { return "WHSS_wpt_v3"; }
  TTreeFunction* clone() const override { return new WHSS_wpt_v3(); }
  //TTreeFunction* clone() const override;
  unsigned getNdata() override { return 1; }

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

WHSS_wpt_v3::WHSS_wpt_v3() :
  TTreeFunction()
{}



double
WHSS_wpt_v3::evaluate(unsigned)
{

  float Mjj_tmp=0;
  float Mjj_max=0;
  unsigned int njet{*nCleanJet->Get()};
  unsigned int nlep{*nLepton->Get()};
 
  if (nlep<2){
    return -9999.;
  }
  if (njet>=2){
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
      for (unsigned int jjet=0 ; jjet<njet ; jjet++){
        if (ijet==jjet) continue;
        TLorentzVector jet0; jet0.SetPtEtaPhiM(CleanJet_pt->At(ijet), CleanJet_eta->At(ijet),CleanJet_phi->At(ijet),Jet_mass->At(CleanJet_jetId->At(ijet)));   
        TLorentzVector jet1; jet1.SetPtEtaPhiM(CleanJet_pt->At(jjet), CleanJet_eta->At(jjet),CleanJet_phi->At(jjet),Jet_mass->At(CleanJet_jetId->At(jjet))); 
        Mjj_tmp = (jet0 + jet1).M();
        if(Mjj_max >= Mjj_tmp){
          Mjj_max=Mjj_tmp;
        }
      }
    }
    return Mjj_max;

  }
  // CASE 2: assume lepton2 colinear with neutrino1
  else{
    return -9999.;
  }
}

void
WHSS_wpt_v3::bindTree_(multidraw::FunctionLibrary& _library)
{
  std::cout << "Loading WHSS_wpt_v3" << std::endl;
  _library.bindBranch(CleanJet_jetId, "CleanJetNotFat_jetIdx");
  _library.bindBranch(Jet_mass, "Jet_mass");
  _library.bindBranch(nCleanJet, "nCleanJetNotFat");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(nLepton, "nLepton");

}
