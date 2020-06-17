#! /bin/bash
cd 2018_v6
mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files