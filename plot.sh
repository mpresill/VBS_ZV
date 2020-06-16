#! /bin/bash
DATE=16June2020 #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files

mkPlot.py --pycfg=2018_v6/configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1 #--fileFormats=png,eps
#--showNormalizedDistributions

rm -rf /eos/user/m/mpresill/www/VBS/2018_v6/plots/PlotsVBS_ZV_${DATE}
mkdir /eos/user/m/mpresill/www/VBS/2018_v6/plots/PlotsVBS_ZV_${DATE}
cp -r PlotsVBS_ZV_${DATE}/* /eos/user/m/mpresill/www/VBS/2018_v6/plots/PlotsVBS_ZV_${DATE}/. 

#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root
