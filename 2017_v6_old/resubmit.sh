
#!/bin/bash

set -e 

DIR=$PWD
JOB="/afs/cern.ch/work/s/shoh/analysis/WH-Study/my-latino/nanov6/jobs"
#QUEUE="longlunch" #
#QUEUE="workday" 
QUEUE="testmatch"

for year in Full2017nano_STXS_1p1 Full2018nano_STXS_1p1 #Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
do
    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
    echo " --> $year"
    cd $DIR; cd $year

    for i in ${JOB}/mkShapes__WHSS_${YEAR}_v6_STXS/*jid
    do 
	CHECK=`echo "$i" | awk -F "/" '{print $NF}'`
        if [ ${CHECK} == "*jid" ]
        then
            echo "CONGRATULATION ALL JOB FINISH FOR $year"
        else    
	    echo "sed -i \"s/${QUEUE}/tomorrow/g\" ${i/jid/jds}"
	    #sed -i "s/${QUEUE}/tomorrow/g" ${i/jid/jds}
	    #condor_submit ${i/jid/jds}
	fi
    done
done

condor_q