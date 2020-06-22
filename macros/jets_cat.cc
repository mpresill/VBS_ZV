/*
This macrol computes the AK4 jets categorization in the VBS event:   
    - the category of the event (1FJ, 0FJ or more than 1FJ)
    - mjj as the maximum of all the AK4 jets couples masses
    - their detajj
    - the indices of these VBS-jets
    - in the resolved case (4jets and no FJ), the inv mass of the other two jets (Vjets_mass)

Note that according to the definition in ll. 147, 149 we use the CleanJetNotFat indecing 

*/


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

// --- function Helper
float deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}


class jets_cat : public multidraw::TTreeFunction {
public:
  jets_cat( char const* _type);
  jets_cat( unsigned type);

  char const* getName() const override { return "jets_cat"; }
  TTreeFunction* clone() const override { return new jets_cat(returnVar_,year_.c_str() ); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
    vbs_category, 
    vbs_jet_0,
    vbs_jet_1, 
    v_jet_0,
    v_jet_1,

    mjj_max, 
    detajj_mjjmax, 
    Vjet_mass, 
    nVarTypes
  };
  
 
  void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
  

  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static string year_;

  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  
  static UIntValueReader* nFatJet; 
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;

  static IntArrayReader* CleanJet_jetId;
  static IntArrayReader* CleanJetNotFat_jetId;
  static FloatArrayReader* Jet_mass;
  static UIntValueReader* nCleanJet;
  static FloatArrayReader* CleanJet_pt;
  static FloatArrayReader* CleanJet_eta;
  static FloatArrayReader* CleanJet_phi;

  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};

std::tuple<UInt_t, UInt_t, ULong64_t> jets_cat::currentEvent{};

UIntValueReader* jets_cat::nFatJet{}; 
FloatArrayReader* jets_cat::FatJet_pt{};
FloatArrayReader* jets_cat::FatJet_eta{};
FloatArrayReader* jets_cat::FatJet_phi{};
FloatArrayReader* jets_cat::FatJet_mass{};


IntArrayReader*   jets_cat::CleanJet_jetId{};
IntArrayReader*   jets_cat::CleanJetNotFat_jetId{};
FloatArrayReader* jets_cat::Jet_mass{};
UIntValueReader*  jets_cat::nCleanJet; 
FloatArrayReader* jets_cat::CleanJet_pt{};
FloatArrayReader* jets_cat::CleanJet_eta{};
FloatArrayReader* jets_cat::CleanJet_phi{};

string jets_cat::year_{};

std::array<double, jets_cat::nVarTypes> jets_cat::returnValues{};


// function Helper ---


jets_cat::jets_cat( char const* _type):
   TTreeFunction(){
     
    std::string type(_type);
    if (type ==  "vbs_category")
      returnVar_ = vbs_category;
    else if (type ==  "vbs_jet_0")
      returnVar_ = vbs_jet_0;
    else if (type == "vbs_jet_1")
      returnVar_ = vbs_jet_1;
    else if (type ==  "v_jet_0")
      returnVar_ = v_jet_0;
    else if (type == "v_jet_1")
      returnVar_ = v_jet_1;
    else if (type == "Vjet_mass")
      returnVar_ = Vjet_mass;
    else if (type == "mjj_max")
      returnVar_ = mjj_max;
    else if (type == "detajj_mjjmax")
      returnVar_ = detajj_mjjmax;
    else
      throw std::runtime_error("unknown return type " + type);

    jets_cat::year_ = year;

}

jets_cat::jets_cat( unsigned type):
TTreeFunction(), returnVar_(type){
  jets_cat::year_ = year;
}


double
jets_cat::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
jets_cat::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nFatJet, "nCleanFatJet");
    _library.bindBranch(FatJet_pt, "CleanFatJet_pt");
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_mass, "CleanFatJet_mass");

    _library.bindBranch(CleanJetNotFat_jetId, "CleanJetNotFat_jetIdx");
    _library.bindBranch(CleanJet_jetId, "CleanJet_jetIdx");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(nCleanJet, "nCleanJetNotFat");
    _library.bindBranch(CleanJet_pt, "CleanJet_pt");
    _library.bindBranch(CleanJet_eta, "CleanJet_eta");
    _library.bindBranch(CleanJet_phi, "CleanJet_phi");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {

                                     nFatJet = nullptr;
                                     FatJet_pt = nullptr;
                                     FatJet_eta = nullptr;
                                     FatJet_phi = nullptr;
                                     FatJet_mass = nullptr;
                                     nCleanJet = nullptr;
                                     CleanJet_pt = nullptr;
                                     CleanJet_eta = nullptr;
                                     CleanJet_phi = nullptr;
                                     Jet_mass = nullptr;
                                     CleanJet_jetId = nullptr;
                                     CleanJetNotFat_jetId = nullptr;
                                   });
}

/*static*/
void
jets_cat::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

  currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

  //first part: compute the mjj_max of all the AK4 (CleanedNotFat)
  float Mjj_tmp=0;
  float Mjj_max=0;
  float deltamass_Vjet=1e5;
  float detajj_tmp=0;
  float detajj_mjj_max=0;
  float Vjet_mass_tmp = 0.;
  unsigned int njet{*nCleanJet->Get()};
  unsigned int nFJ{*nFatJet->Get()};
  // Index in the collection of CleanJetNotFat
  int VBS_jets[2] = {-999,-999};
  int V_jets[2]   = {-999,-999};
  int category = -999;  // 0 fatjet, 1 resolved, -1 none

  // Load all the quadrivectors for performance reason
  std::vector<TLorentzVector> vectors; 
  for (unsigned int ijet=0 ; ijet<njet ; ijet++){
    TLorentzVector jet0; 
    jet0.SetPtEtaPhiM(CleanJet_pt->At(CleanJetNotFat_jetId->At(ijet)), CleanJet_eta->At(CleanJetNotFat_jetId->At(ijet)),
                      CleanJet_phi->At(CleanJetNotFat_jetId->At(ijet)),Jet_mass->At(CleanJet_jetId->At(CleanJetNotFat_jetId->At(ijet)))); 
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
        detajj_tmp = deltaEta(CleanJet_eta->At(CleanJetNotFat_jetId->At(ijet)),CleanJet_eta->At(CleanJetNotFat_jetId->At(jjet)));
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
      Vjet_mass_tmp = FatJet_mass->At(0);

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

  // Now go back to CleanJet indexes for easy use of the collection
  if (VBS_jets[0] != -999) returnValues[vbs_jet_0] = CleanJetNotFat_jetId->At(VBS_jets[0]);
  else                     returnValues[vbs_jet_0] = -999;

  if (VBS_jets[1] != -999) returnValues[vbs_jet_1] = CleanJetNotFat_jetId->At(VBS_jets[1]);
  else                     returnValues[vbs_jet_1] = -999;
 
  if (V_jets[0] != -999) returnValues[v_jet_0] = CleanJetNotFat_jetId->At(V_jets[0]);
  else                     returnValues[v_jet_0] = -999;

  if (V_jets[1] != -999) returnValues[v_jet_1] = CleanJetNotFat_jetId->At(V_jets[1]);
  else                     returnValues[v_jet_1] = -999;


  returnValues[mjj_max]= Mjj_tmp;
  returnValues[detajj_mjjmax] = detajj_mjj_max;
  returnValues[Vjet_mass] = Vjet_mass_tmp;
  returnValues[vbs_category] = category;

}


