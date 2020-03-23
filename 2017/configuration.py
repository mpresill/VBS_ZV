# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_23Mar2020'

tag = 'VBS_ZV_aQGC'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables_v2.py'

# file with list of cuts
cutsFile = 'cuts_v3.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_sig.py'

# file with list of samples
plotFile = 'plot_sig.py'

# luminosity to normalize to (in 1/fb)
lumi = 41.5

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_StatOnly.py'
