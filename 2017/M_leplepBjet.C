#include <TMath.h>
#include <algorithm>
#include "TLorentzVector.h"
#include "TVector2.h"
#include <iostream>

using namespace std;


Float_t M_leplepBJet(double pt1, double phi1, double eta1,
               double pt2, double phi2, double eta2, 
               double FJ_pt, double FJ_phi, double FJ_eta){
  //if(pt1<0. || pt2<0.|| FJ_pt<0. ) return -1.;
  TLorentzVector l1;
  l1.SetPtEtaPhiM(pt1,eta1,phi1,0);
  TLorentzVector l2;
  l2.SetPtEtaPhiM(pt2,eta2,phi2,0);
  TLorentzVector BJ;
  BJ.SetPtEtaPhiM(FJ_pt,FJ_eta,FJ_phi,0);
 

  return (l1+l2+BJ).M();
}
