#! /bin/bash
#DATE=3May2020 #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files
cd 2018_v6
mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday #--dry-run #espresso #longlunch #--dry-run

cd ..
##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files

#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1

#rm -rf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#mkdir /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}
#cp -r PlotsVBS_ZV_${DATE}/*.png /eos/user/m/mpresill/CMS/VBS/VBS_ZV/plots/PlotsVBS_ZV_${DATE}/. 

#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root
