#include "TLorentzVector.h"
#include "TVector2.h"
#include <iostream>

using namespace std;

//this macro computes the delta R of the VBS-jets taken as the leading and subleading jets in the event


Float_t dRjj(double phi1, double eta1, 
	       double phi2, double eta2){

return sqrt( pow((eta2-eta1),2) + pow(deltaPhi(phi1,phi2),2) );

}
