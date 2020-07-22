#!/bin/bash

# python latinoRDF_numpy_exporter.py --config Full2018v6s5_v2 \
#     --cut boost_sig --ver v11 -o /eos/user/d/dvalsecc/www/VBSPlots/DNN_archive \
#     -s VVV Wjets VBS DY VBF-V top VV \
#     --debug --functions functions.hh



python latinoRDF_numpy_exporter.py --config Full2017v6s5_v2 \
    --cut res_sig --ver v11 -o /eos/user/d/dvalsecc/www/VBSPlots/DNN_archive \
    -s VVV Wjets VBS DY VBF-V top VV \
    --debug --functions functions.hh


python latinoRDF_numpy_exporter.py --config Full2017v6s5_v2 \
    --cut boost_sig --ver v11 -o /eos/user/d/dvalsecc/www/VBSPlots/DNN_archive \
    -s VVV Wjets VBS DY VBF-V top VV \
    --debug --functions functions.hh