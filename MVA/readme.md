# MVA training files

ZV_functions contain functions to preprocess the dataframes (should be modified if samples change name)
  - prep_data_multi should be used, prep_data is deprecated. The folders structures should be base_dir + NUmpy + ZV_ + "name of the year" 
  ex: prep_data_multi(['2018_nobtag'], '2018','Boosted_SR', 'test','base_dir') will process files in base_dir/Numpy/ZV_2018_nobtag/Boosted_SR/samples/v1 and write them to base_dir/2018/Boosted_SR/data
  

BDT/DNN training are used to train the models

BDT_opti runs a gridsearch for BDT parameteres

DNN_opti is a bayesian optimization for the DNN

Dump DNN allows to dump a .h5 keras model to tensorflow .pb (needed for integration in latinos, with the tf_metadata and scaler files) (carefull, the dumpin will fail if multiple metrics were used during training)

latinoVsPython_check is used to check the conformity of the inputs and ouputs for latinos and python files (currently configured for Boosted SR DY sample.
