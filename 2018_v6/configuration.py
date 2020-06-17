# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_17June2020'

tag = 'VBS_ZV'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'

# file with list of samples
#samplesFile = 'samples_sig.py'
samplesFile = 'samples.py'


# file with list of samples
#plotFile = 'plot_sig.py'
plotFile = 'plot.py'


# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2018_v6/PlotsVBS_ZV'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
#nuisancesFile ='nuisances_StatOnly.py'
