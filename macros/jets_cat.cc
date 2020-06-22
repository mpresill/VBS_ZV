/*
This macrol computes the AK4 jets categorization in the VBS event:   
    - mjj as the maximum of all the AK4 jets couples masses
    - their detajj
    - the indices of these VBS-jets
    - in the resolved case (4jets and no FJ), the inv mass of the other two jets (Vjets_mass)
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

class jets_cat : public multidraw::TTreeFunction {
public:
  jets_cat( char const* _type, const char* year);
  jets_cat( unsigned type, const char* year);

  char const* getName() const override { return "jets_cat"; }
  TTreeFunction* clone() const override { return new jets_cat(returnVar_,year_.c_str() ); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
        mjj_max, 
        detajj_mjjmax, 
        VBSjetsId, 
        Vjets_mass, 
        nVarTypes
  };
  
 
  void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
  

  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  
  static UIntValueReader* nFatJet; 
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;

  static IntArrayReader* CleanJet_jetId;
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
FloatArrayReader* jets_cat::Jet_mass{};
UIntValueReader*  jets_cat::nCleanJet; 
FloatArrayReader* jets_cat::CleanJet_pt{};
FloatArrayReader* jets_cat::CleanJet_eta{};
FloatArrayReader* jets_cat::CleanJet_phi{};



std::array<double, jets_cat::nVarTypes> jets_cat::returnValues{};

// --- function Helper
float jets_cat::deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}

// function Helper ---


jets_cat::jets_cat( char const* _type, const char* year):
   TTreeFunction(){
     
    std::string type(_type);
    if (type ==  "VBSjetsId")
      returnVar_ = VBSjetsId;
    else if (type == "Vjets_mass")
      returnVar_ = Vjets_mass;
    else if (type == "mjj_max")
      returnVar_ = mjj_max;
    else if (type == "detajj_mjjmax")
      returnVar_ = detajj_mjjmax;
    else
      throw std::runtime_error("unknown return type " + type);

}

jets_cat::jets_cat( unsigned type, const char* year):
TTreeFunction(), returnVar_(type){}


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

    _library.bindBranch(CleanJet_jetId, "CleanJetNotFat_jetIdx");
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
  float V_jets_mass=0;
  float detajj_tmp=0;
  float detajj_mjj_max=0;
  unsigned int njet{*nCleanJet->Get()};
  unsigned int nFJ{*nFatJet->Get()};
  std::vector<std::pair<int,float>> VBS_jets_Id;
  


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
          //qui in qualche modo bisogna estrarre l'indice dei due VBS-jets
          VBS_jets_Id=push_back(ijet);    //non sono affatto convinto vada bene
          VBS_jets_Id=push_back(jjet);    //non sono affatto convinto vada bene
          }
        else{
          if(njet==4 && nFJ==0 ){ 
          //qui in qualche modo bisogna sputare fuori gli indici per i V-jets
            V_jets_mass = Mjj_tmp;
          }
        }
    
      }
    }
   
  
  }

  returnValues[mjj_max]= Mjj_tmp;
  returnValues[detajj_mjjmax] = detajj_mjj_max;
  
  returnValues[VBSjetsId] = VBS_jets_Id;//indice dei VBS jets //non sono affatto convinto vada bene

  returnValues[Vjets_mass]= V_jets_mass;  //su questa massa si può mettere un qualche requisito per selezionare DY da sr come con la softdropmass


}


