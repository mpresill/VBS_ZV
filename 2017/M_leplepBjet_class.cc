#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

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

//see https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/VBSjjlnu/Configurations/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc for another example

using namespace std;

class InvMass : public multidraw::TTreeFunction {
public: 
  InvMass(char const* type);
  InvMass(unsigned type);

  char const* getName() const override { return "InvMass"; }
  TTreeFunction* clone() const override { return new InvMass(returnVar_); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
                   M_leplepBjet,
                   nVarTypes
  };
  

void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
 
  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  static UIntValueReader* nJets; 
  static FloatArrayReader* Jet_pt;
  static FloatArrayReader* Jet_eta;
  static FloatArrayReader* Jet_phi;
  static IntArrayReader* Jet_idx;
  static FloatArrayReader* Jet_mass;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;
 //static IntArrayReader* vbs_jets;
 //static IntArrayReader* v_jets;

  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};


std::tuple<UInt_t, UInt_t, ULong64_t> InvMass::currentEvent{};
UIntValueReader* InvMass::nJets; 
FloatArrayReader* InvMass::Jet_pt{};
FloatArrayReader* InvMass::Jet_eta{};
FloatArrayReader* InvMass::Jet_phi{};
IntArrayReader* InvMass::Jet_idx{};
FloatArrayReader* InvMass::Jet_mass{};
FloatArrayReader* InvMass::Lepton_pt{};
FloatArrayReader* InvMass::Lepton_eta{};
FloatArrayReader* InvMass::Lepton_phi{};
FloatArrayReader* InvMass::FatJet_pt{};
FloatArrayReader* InvMass::FatJet_eta{};
FloatArrayReader* InvMass::FatJet_phi{};
FloatArrayReader* InvMass::FatJet_mass{};
//IntArrayReader* InvMass::vbs_jets{};
//IntArrayReader* InvMass::v_jets{};

std::array<double, InvMass::nVarTypes> InvMass::returnValues{};


InvMass::InvMass(char const* _type) :
  TTreeFunction()
{
  std::string type(_type);
  if (type == "M_leplepBjet")
    returnVar_ = M_leplepBjet;
  else
    throw std::runtime_error("unknown return type " + type);
  
}

InvMass::InvMass(unsigned type) :
  TTreeFunction(),
  returnVar_(type) {}


double
InvMass::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
InvMass::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nJets, "nJet");
    _library.bindBranch(Jet_pt, "CleanJet_pt");
    _library.bindBranch(Jet_eta, "CleanJet_eta");
    _library.bindBranch(Jet_phi, "CleanJet_phi");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(Jet_idx, "CleanJet_jetIdx");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(FatJet_pt, "FatJet_pt");
    _library.bindBranch(FatJet_eta, "FatJet_eta");
    _library.bindBranch(FatJet_phi, "FatJet_phi");
    _library.bindBranch(FatJet_mass, "FatJet_mass");
    //_library.bindBranch(vbs_jets, "VBS_jets_maxmjj_massWZ");
    //_library.bindBranch(v_jets, "V_jets_maxmjj_massWZ");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
                                     nJets = nullptr;
                                     Jet_pt = nullptr;
                                     Jet_eta = nullptr;
                                     Jet_phi = nullptr;
                                     Jet_mass = nullptr;
                                     Jet_idx = nullptr;
                                     Lepton_pt = nullptr;
                                     Lepton_eta = nullptr;
                                     Lepton_phi = nullptr;
                                     FatJet_pt = nullptr;
                                     FatJet_eta = nullptr;
                                     FatJet_phi = nullptr;
                                     FatJet_mass = nullptr;
                                   });
}

/*static*/
void
InvMass::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

 currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

/* TLorentzVector ;
  for (auto ij : *vbs_jets){
    TLorentzVector v;
    float pt = Jet_pt->At(ij);
    float eta = Jet_eta->At(ij);
    float phi = Jet_phi->At(ij);
    float mass = Jet_mass->At(Jet_idx->At(ij));
    v.SetPtEtaPhiM(pt,eta,phi, mass);
    vbsjets += v;
  }

  TLorentzVector whad;
  for (auto ij : *v_jets){
    TLorentzVector v;
    float pt = Jet_pt->At(ij);
    float eta = Jet_eta->At(ij);
    float phi = Jet_phi->At(ij);
    float mass = Jet_mass->At(Jet_idx->At(ij));
    v.SetPtEtaPhiM(pt,eta,phi, mass);
    whad += v;
  }
*/

  TLorentzVector lep1; 
  lep1.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0.);

  TLorentzVector lep2;
  lep2.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0.);

 // TLorentzVector jet0;
 // jet0.SetPtEtaPhiM(Jet_pt->At(0), Jet_eta->At(0),Jet_phi->At(0),Jet_mass->At(Jet_idx->At(0)));   

  TLorentzVector BJet;
  BJet.SetPtEtaPhiM(FatJet_pt->At(0), FatJet_eta->At(0),FatJet_phi->At(0),FatJet_mass->At(0));
	

  returnValues[M_leplepBjet] = (lep1+lep2+BJet).M();

}


