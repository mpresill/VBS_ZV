#! /bin/bash
DATE=20June2020 #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files
cd 2018_v6

mkPlot.py --pycfg=2018_v6/configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --plotNormalizedDistributions=True #--fileFormats=png,eps
#--showNormalizedDistributions

cp /eos/user/m/mpresill/www/VBS/2018_v6/index.php /eos/user/m/mpresill/www/VBS/2018_v6/PlotsVBS_ZV_${DATE}/.
rm -rf /eos/user/m/mpresill/www/VBS/2018_v6/PlotsVBS_ZV_${DATE}*root

cd ..
#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root
