#! /bin/bash

source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh

python latinoRDF_numpy_exporter.py\
  --config-dir ./ZV_2018\
  --cut Resolved_SR\
  --o /eos/home-a/ahakimi/www/ZV_analysis/Numpy\
  --vers v1\
  --s VBS_ZV\
  --debug --functions functions.hh
