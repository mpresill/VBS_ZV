#! /bin/bash

source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh

python3 mkShapePyRDF/latinoRDF_numpy_exporter.py\
  --config-dir ./2017_v6\
  --cut SR_boosted_minimal\
  --outputdir /eos/user/m/mpresill/www/VBS/DNN/2017_v6/\
  --vers v1\
  --samples top\
  --debug


#NB: no cmsenv is needed for this step
