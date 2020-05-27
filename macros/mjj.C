#include "TLorentzVector.h"
#include "TVector2.h"
#include <iostream>

using namespace std;

//this macro computes the invariant mass of the VBS-jets taken as the leading and subleading jets in the event

Float_t mjj(double pt1, double phi1, double eta1, double mass1,
	       double pt2, double phi2, double eta2, double mass2){
  TLorentzVector l1;
  l1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
  TLorentzVector l2;
  l2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);

  TLorentzVector ll;
  ll=l1+l2;


  return ll.M();
}
