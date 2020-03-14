#! /bin/bash
DATE=13Mar2020 #change date 
mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_aQGC_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

cp -r PlotsVBS_ZV_${DATE} /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/. 

