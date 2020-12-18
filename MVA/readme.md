# MVA training files

ZV_functions contain functions to preprocess the dataframes

BDT/DNN training are used to train the models

BDT_opti runs a gridsearch for BDT parameteres

DNN_opti is a bayesian optimization for the DNN

Dump DNN allows to dump a .h5 keras model to tensorflow .pb (needed for integration in latinos, with the tf_metadata and scaler files)

latinoVsPython_check is used to check the conformity of the inputs and ouputs for latinos and python files (currently configured for Boosted SR DY sample.
