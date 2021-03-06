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

class VBSvar_AK4 : public multidraw::TTreeFunction {
public: 
  VBSvar_AK4(char const* type);
  VBSvar_AK4(unsigned type);

  char const* getName() const override { return "VBSvar_AK4"; }
  TTreeFunction* clone() const override { return new VBSvar_AK4(returnVar_); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
	                 mjj_vbs,
                   detajj_vbs,
                   mll_vbs,
                   M_ZV,
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
  static IntArrayReader* Jet_jetId;
  static FloatArrayReader* Jet_mass;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_msoftdrop;
 //static IntArrayReader* vbs_jets;
 //static IntArrayReader* v_jets;

  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};


std::tuple<UInt_t, UInt_t, ULong64_t> VBSvar_AK4::currentEvent{};
UIntValueReader* VBSvar_AK4::nJets; 
FloatArrayReader* VBSvar_AK4::Jet_pt{};
FloatArrayReader* VBSvar_AK4::Jet_eta{};
FloatArrayReader* VBSvar_AK4::Jet_phi{};
IntArrayReader* VBSvar_AK4::Jet_jetId{};
FloatArrayReader* VBSvar_AK4::Jet_mass{};
FloatArrayReader* VBSvar_AK4::Lepton_pt{};
FloatArrayReader* VBSvar_AK4::Lepton_eta{};
FloatArrayReader* VBSvar_AK4::Lepton_phi{};
FloatArrayReader* VBSvar_AK4::FatJet_pt{};
FloatArrayReader* VBSvar_AK4::FatJet_eta{};
FloatArrayReader* VBSvar_AK4::FatJet_phi{};
FloatArrayReader* VBSvar_AK4::FatJet_msoftdrop{};
//IntArrayReader* VBSvar_AK4::vbs_jets{};
//IntArrayReader* VBSvar_AK4::v_jets{};

std::array<double, VBSvar_AK4::nVarTypes> VBSvar_AK4::returnValues{};


VBSvar_AK4::VBSvar_AK4(char const* _type) :
  TTreeFunction()
{
  std::string type(_type);
 if (type == "mjj_vbs")
   returnVar_ = mjj_vbs;
 else if ( type == "detajj_vbs")
   returnVar_ = detajj_vbs;
 else if (type == "mll_vbs")
   returnVar_ = mll_vbs;
 else if (type == "M_ZV")
    returnVar_ = M_ZV;
  else
    throw std::runtime_error("unknown return type " + type);
  
}

VBSvar_AK4::VBSvar_AK4(unsigned type) :
  TTreeFunction(),
  returnVar_(type) {}


double
VBSvar_AK4::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
VBSvar_AK4::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nJets, "nCleanJet");
    _library.bindBranch(Jet_pt, "CleanJet_pt");
    _library.bindBranch(Jet_eta, "CleanJet_eta");
    _library.bindBranch(Jet_phi, "CleanJet_phi");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(Jet_jetId, "CleanJet_jetIdx");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(FatJet_pt, "CleanFatJet_pt");
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_msoftdrop, "CleanFatJet_mass");
    //_library.bindBranch(vbs_jets, "VBS_jets_maxmjj_massWZ");
    //_library.bindBranch(v_jets, "V_jets_maxmjj_massWZ");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
                                     nJets = nullptr;
                                     Jet_pt = nullptr;
                                     Jet_eta = nullptr;
                                     Jet_phi = nullptr;
                                     Jet_mass = nullptr;
                                     Jet_jetId = nullptr;
                                     Lepton_pt = nullptr;
                                     Lepton_eta = nullptr;
                                     Lepton_phi = nullptr;
                                     FatJet_pt = nullptr;
                                     FatJet_eta = nullptr;
                                     FatJet_phi = nullptr;
                                     FatJet_msoftdrop = nullptr;
                                   });
}

/*static*/
void
VBSvar_AK4::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

 currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

/*
 TLorentzVector ;
  for (auto ij : *vbs_jets){
    TLorentzVector v;
    float pt = Jet_pt->At(ij);
    float eta = Jet_eta->At(ij);
    float phi = Jet_phi->At(ij);
    float mass = Jet_mass->At(Jet_jetId->At(ij));
    v.SetPtEtaPhiM(pt,eta,phi, mass);
    vbsjets += v;
  }

  TLorentzVector vbs_jets2;
  for (auto ij : *vbs_jets2){
    TLorentzVector v;
    float pt = Jet_pt->At(ij);
    float eta = Jet_eta->At(ij);
    float phi = Jet_phi->At(ij);
    float mass = Jet_mass->At(Jet_jetId->At(ij));
    v.SetPtEtaPhiM(pt,eta,phi, mass);
    vbs_jets2 += v;
  }

  TLorentzVector FJ;
  for (auto ij : *FJ){
    TLorentzVector v;
    float pt = FatJet_pt->At(ij);
    float eta = FatJet_eta->At(ij);
    float phi = FatJet_phi->At(ij);
    float mass = FatJet_msoftdrop->At(Jet_jetId->At(ij));
    v.SetPtEtaPhiM(pt,eta,phi, mass);
    FJ += v;
  }
*/


  TLorentzVector lep1; 
  lep1.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0.);

  TLorentzVector lep2;
  lep2.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0.);

  TLorentzVector jet0;
  jet0.SetPtEtaPhiM(Jet_pt->At(0), Jet_eta->At(0),Jet_phi->At(0),Jet_mass->At(Jet_jetId->At(0)));   

  TLorentzVector jet1;
  jet1.SetPtEtaPhiM(Jet_pt->At(1), Jet_eta->At(1),Jet_phi->At(1),Jet_mass->At(Jet_jetId->At(1))); 

  TLorentzVector FJet;
  FJet.SetPtEtaPhiM(FatJet_pt->At(0), FatJet_eta->At(0),FatJet_phi->At(0),FatJet_msoftdrop->At(0));
	
  returnValues[mjj_vbs] = (jet0+jet1).M();
  returnValues[detajj_vbs] = abs(jet0.Eta() - jet1.Eta());
  returnValues[mll_vbs] = (lep1+lep2).M();
  returnValues[M_ZV] = (lep1+lep2+FJet).M();
}


