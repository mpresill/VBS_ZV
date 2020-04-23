//
//https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/VBSjjlnu/Configurations/VBSjjlnu/Full2017v6s5/macros/deltaphivars_class.cc for another example
//https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/macros/whss_wlep_v3.cc
//https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/WH_SS/STXS_nanoAOD/v5/Full2016nano_STXS_1p1/aliases.py#L16-L22

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <string>
#include <unordered_map>
#include <stdexcept>
#include <tuple>


using namespace std;

class VBSvar_AK4NotFat : public multidraw::TTreeFunction {
public: 
  VBSvar_AK4NotFat(char const* type);
  VBSvar_AK4NotFat(unsigned type);

  char const* getName() const override { return "VBSvar_AK4NotFat"; }
  TTreeFunction* clone() const override { return new VBSvar_AK4NotFat(returnVar_); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
	                 mjj_vbs_AK4NotFat,
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

  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};


std::tuple<UInt_t, UInt_t, ULong64_t> VBSvar_AK4NotFat::currentEvent{};
UIntValueReader* VBSvar_AK4NotFat::nJets; 
FloatArrayReader* VBSvar_AK4NotFat::Jet_pt{};
FloatArrayReader* VBSvar_AK4NotFat::Jet_eta{};
FloatArrayReader* VBSvar_AK4NotFat::Jet_phi{};
IntArrayReader* VBSvar_AK4NotFat::Jet_jetId{};
FloatArrayReader* VBSvar_AK4NotFat::Jet_mass{};
FloatArrayReader* VBSvar_AK4NotFat::Lepton_pt{};
FloatArrayReader* VBSvar_AK4NotFat::Lepton_eta{};
FloatArrayReader* VBSvar_AK4NotFat::Lepton_phi{};
FloatArrayReader* VBSvar_AK4NotFat::FatJet_pt{};
FloatArrayReader* VBSvar_AK4NotFat::FatJet_eta{};
FloatArrayReader* VBSvar_AK4NotFat::FatJet_phi{};
FloatArrayReader* VBSvar_AK4NotFat::FatJet_msoftdrop{};

std::array<double, VBSvar_AK4NotFat::nVarTypes> VBSvar_AK4NotFat::returnValues{};


VBSvar_AK4NotFat::VBSvar_AK4NotFat(char const* _type) :
  TTreeFunction()
{
  std::string type(_type);
 if (type == "mjj_vbs_AK4NotFat")
   returnVar_ = mjj_vbs_AK4NotFat;
 else if (type == "mll_vbs")
   returnVar_ = mll_vbs;
 else if (type == "M_ZV")
    returnVar_ = M_ZV;
  else
    throw std::runtime_error("unknown return type " + type);
  
}

VBSvar_AK4NotFat::VBSvar_AK4NotFat(unsigned type) :
  TTreeFunction(),
  returnVar_(type) {}


double
VBSvar_AK4NotFat::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
VBSvar_AK4NotFat::bindTree_(multidraw::FunctionLibrary& _library)
{   
  std::cout << "Loading vbs_variables_class_AK4NotFat" << std::endl;
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nJets, "nCleanJetNotFat");   //AK4 after cleaning
    _library.bindBranch(Jet_pt, "CleanJet_pt");
    _library.bindBranch(Jet_eta, "CleanJet_eta");
    _library.bindBranch(Jet_phi, "CleanJet_phi");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(Jet_jetId, "CleanJetNotFat_jetIdx");   //AK4 after cleaning through cross-references
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(FatJet_pt, "CleanFatJet_pt");
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_msoftdrop, "CleanFatJet_mass");  //CleanFatJet_mass == softdrop
  

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
VBSvar_AK4NotFat::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

 currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

  unsigned int njets{*nJets->Get()};
  double Mjj_temp=0;
  double Mjj_max=0;  
  if(njets>=2){
    for(unsigned int i=0; i<= njets; i++ ){
      for(unsigned int j=i+1; j<= njets; j++){
        TLorentzVector jet0; jet0.SetPtEtaPhiM(Jet_pt->At(Jet_jetId->At(i)), Jet_eta->At(Jet_jetId->At(i)),Jet_phi->At(Jet_jetId->At(i)),Jet_mass->At(Jet_jetId->At(i)));   
        TLorentzVector jet1; jet1.SetPtEtaPhiM(Jet_pt->At(Jet_jetId->At(j)), Jet_eta->At(Jet_jetId->At(j)),Jet_phi->At(Jet_jetId->At(j)),Jet_mass->At(Jet_jetId->At(j))); 
        Mjj_temp=(jet0+jet1).M();
       if(Mjj_temp >= Mjj_max){
          Mjj_max=Mjj_temp;
        }      
      }
    }
  }
  returnValues[mjj_vbs_AK4NotFat] = Mjj_max;    // (jet0+jet1).M();

  TLorentzVector lep1; lep1.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0.);
  TLorentzVector lep2; lep2.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0.);
  TLorentzVector FJet; FJet.SetPtEtaPhiM(FatJet_pt->At(0), FatJet_eta->At(0),FatJet_phi->At(0),FatJet_msoftdrop->At(0));
	 
  returnValues[mll_vbs] = (lep1+lep2).M();   
  returnValues[M_ZV] = (lep1+lep2+FJet).M();  //the invariant mass is computed with the leading (and only) Fat Jet 
}