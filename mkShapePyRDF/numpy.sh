#! /bin/bash

#source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh
#try LCG97?

source /cvmfs/sft.cern.ch/lcg/views/LCG_97python3//x86_64-centos7-gcc8-opt/setup.sh

python latinoRDF_numpy_exporter.py\
  --config-dir ./ZV_2018\
  --cut Resolved_SR\
  --o /eos/home-a/ahakimi/www/ZV_analysis/Numpy\
  --vers v1\
  --s VBS_ZV VBS_VV_QCD DY top WJets WW ggWW Vg VZ VVV VBF-V \
  --debug --functions functions.hh

#done VBS_ZV VBS_VV_QCD DY top WJets WW ggWW Vg VZ VVV VBF-V
#to do VgS 
