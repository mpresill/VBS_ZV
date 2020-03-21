#! /bin/bash
DATE=21Mar2020 #change date 
mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files

mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_aQGC_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

cp -r PlotsVBS_ZV_${DATE} /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/. 

