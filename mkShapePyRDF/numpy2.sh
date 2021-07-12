#! /bin/bash

#source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh
#try LCG97?

source /cvmfs/sft.cern.ch/lcg/views/LCG_97python3//x86_64-centos7-gcc8-opt/setup.sh



#python latinoRDF_numpy_exporter.py\
#  --config-dir ./2018_SR\
#  --cut Boosted_SR\
#  --o /eos/home-a/ahakimi/www/ZV_analysis/Numpy\
#  --vers v1\
#  --s VBS_ZV VBS_VV_QCD DY top WJets WW Vg VgS ggWW VZ VVV VBF-V Fake \
#  --debug --functions functions.hh 

python latinoRDF_numpy_exporter.py\
  --config-dir ./2016_nobtag\
  --cut Resolved_DYcr_bVeto\
  --o /eos/home-a/ahakimi/www/ZV_analysis/Numpy\
  --vers v1\
  --s VBS_ZV VBS_VV_QCD DY top WJets WW Vg VgS ggWW VZ VVV Fake tZq DATA\
  --debug --functions functions.hh 
#to do  VBS_ZV VBS_VV_QCD DY top WJets WW Vg VgS ggWW VZ VVV VBF-V Fake

