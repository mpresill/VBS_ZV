#! /bin/bash
rm -r rootFile PlotsVBS_ZV
mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_SR.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000000 --maxLogCratio=10000000  --showIntegralLegend=1 --onlyPlot=cratio
