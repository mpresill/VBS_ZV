
#!/bin/bash

set -e 
DATE=_20June2020
DIR=$PWD
JOB="/afs/cern.ch/work/m/mpresill/Latino/jobs"
QUEUE="longlunch" #
#QUEUE="workday" 
#QUEUE="testmatch"

#for year in Full2017nano_STXS_1p1 Full2018nano_STXS_1p1 #Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
#do
#    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
#    echo " --> $year"
#    cd $DIR; cd $year
    cd $JOB 

    for i in ${JOB}/mkShapes__VBS_ZV${DATE}/*jid
    do 
	CHECK=`echo "$i" | awk -F "/" '{print $NF}'`
        if [ ${CHECK} == "*jid" ]
        then
            echo "CONGRATULATION ALL JOB FINISH FOR $year"
        else    
	    #echo "sed -i \"s/${QUEUE}/tomorrow/g\" ${i/jid/jds}"
	    sed -i "s/${QUEUE}/tomorrow/g" ${i/jid/jds}
	    condor_submit ${i/jid/jds}
	fi
    done
#done

        cd $DIR
        
condor_q


#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done
