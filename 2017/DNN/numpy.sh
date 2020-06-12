#! /bin/bash

source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh

python3 latinoRDF_numpy_exporter.py\
  --config-dir ./ZV_v1\
  --cut SR_boosted_minimal\
  --outputdir /eos/home-a/ahakimi/www/ZV_analysis/Numpy\
  --vers v1\
  --samples ZZ ZW DY WJets WW WW_ewk ggWW VZ VVV VBF-V VBS_VV_QCD top\
  --debug 
