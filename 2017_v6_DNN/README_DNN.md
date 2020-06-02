- To import the sample list in the correct json format use:

python unfold_sample.py -i .samples.py -o samples_v1.json -s Wjets DY top VZ VVV VBS_VV_QCD VBS_VV_EW


- To perform the Nunpy extraction (for a single specific signal region):

source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh

python latinoRDF_numpy_exporter.py  --config-dir ./2017_DNN  --cut boos_sig  --outputdir /eos/user/m/mpresill/CMS/VBS/VBS_ZV  --vers v1  --samples WJets DY top VZ VVV VBS_VV_QCD VBS_VV_EW  --debug


