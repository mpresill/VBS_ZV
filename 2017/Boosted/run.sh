#! /bin/bash
rm -r /eos/home-a/ahakimi/www/ZV_analysis/Boosted
rm -r plot rootFile
mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_Boosted.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --logOnly

cd ..
cp -a Boosted/ /eos/home-a/ahakimi/www/ZV_analysis

cp /afs/cern.ch/user/a/ahakimi/index.php /eos/home-a/ahakimi/www/ZV_analysis/Boosted
cp /afs/cern.ch/user/a/ahakimi/index.php  /eos/home-a/ahakimi/www/ZV_analysis/Boosted/plot
