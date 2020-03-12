#! /bin/bash
rm -r /eos/home-a/ahakimi/www/ZV_analysis/Sig_only
mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_Signal.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

cd ..
cp -a Sig_only/ /eos/home-a/ahakimi/www/ZV_analysis

cp /afs/cern.ch/user/a/ahakimi/index.php /eos/home-a/ahakimi/www/ZV_analysis/Sig_only
cp /afs/cern.ch/user/a/ahakimi/index.php  /eos/home-a/ahakimi/www/ZV_analysis/Sig_only/plot
