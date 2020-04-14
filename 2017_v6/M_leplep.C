#include "TLorentzVector.h"
#include "TVector2.h"
#include <iostream>

using namespace std;


Float_t M_leplep(double pt1, double phi1, double eta1,
               double pt2, double phi2, double eta2){
  //if(pt1<0. || pt2<0.|| FJ_pt<0. ) return -1.;
  TLorentzVector l1;
  l1.SetPtEtaPhiM(pt1,eta1,phi1,0);
  TLorentzVector l2;
  l2.SetPtEtaPhiM(pt2,eta2,phi2,0);
  //TLorentzVector FJ;
  //FJ.SetPtEtaPhiM(FJ_pt,FJ_eta,FJ_phi,FJ_mass);

  //TLorentzVector MllJ;
  //MllJ=l1+l2+FJ;

  return (l1+l2).M();
}
