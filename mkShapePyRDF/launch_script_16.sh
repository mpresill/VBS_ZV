#!/bin/bash



python latinoRDF_numpy_exporter.py --config Full2016v6s5_v2 \
    --cut res_sig --ver v11 -o /eos/user/d/dvalsecc/www/VBSPlots/DNN_archive \
    -s VVV Wjets DY top  \
    --debug --functions functions.hh


python latinoRDF_numpy_exporter.py --config Full2016v6s5_v2 \
    --cut boost_sig --ver v11 -o /eos/user/d/dvalsecc/www/VBSPlots/DNN_archive \
    -s VVV Wjets DY top  \
    --debug --functions functions.hh