#include "TLorentzVector.h"
#include "TVector2.h"
#include <iostream>

using namespace std;
const double PI  =3.141592653589793238463;


Float_t dR(double eta1, double phi1,double eta2, double phi2){
  double deta = eta1 - eta2;
  double dphi = phi1 - phi2;
  if(dphi > PI){
    dphi -= 2*PI;
  }
  if(dphi < PI ){
      dphi += 2*PI;
  }
  dR = sqrt((deta*deta)+(dphi*dphi));
  return dR;
}
