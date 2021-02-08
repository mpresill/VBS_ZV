import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate, GridSearchCV
from xgboost.sklearn import XGBClassifier 
from sklearn import metrics
from sklearn.utils.class_weight import compute_class_weight
import pickle


def normalize(data):
    #to balance the sample: SoW for signal = SoW bkg
    data['w']=0
    N_sig=len(data[data['signal']==1])
    SoW_sig=sum(data['weight_'][data['signal']==1])
    SoW_bkg=sum(data['weight_'][data['signal']==0])
    coef_sig=N_sig/SoW_sig
    coef_bkg=N_sig/SoW_bkg
    data['w'][data['signal']==0]=coef_bkg
    data['w'][data['signal']==1]=coef_sig
    data['w'] = data['w'] * data['weight_']
    return data


def prep_data(year, cut, vers,  dir):
    #set up directories

    data_dir=dir+year+'\\'+cut+'\\data'+vers
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    fig_dir=dir+year+'\\'+cut+'\\data_figs'
    if not os.path.exists(fig_dir):
        os.makedirs(fig_dir)

    #features=[cut+'_'+i for i in feat]

    samples_dir=dir+'Numpy\\ZV_'+year+'\\'+cut+'\\samples\\v1'
    files=os.listdir(samples_dir)
    samples_name=[file[:-10] for file in files]

    features=pd.read_pickle(samples_dir+'\\'+files[0]).keys().drop('weight_')

    samples_group=[]
    #group samples by 'class'
    for sample in samples_name:
        if 'DY' in sample: samples_group.append('DY')
        elif 'top' in sample: samples_group.append('top')
        elif 'VBS_ZV' in sample: samples_group.append('signal')
        #elif 'Fake' in sample: samples_group.append('fake')
        else : samples_group.append('other')

    samples_df=[]

    df=pd.DataFrame()

    # preparing the sfigamples for later
    for i,name in enumerate(files):
        samples_df.append(pd.read_pickle(samples_dir+'\\'+files[i]))
        samples_df[i]['sample']= samples_name[i]
        samples_df[i]['group'] = samples_group[i]
        samples_df[i]['year'] = year
        df=df.append(samples_df[i], sort=False)
    df['signal'] = df['group'] == 'signal'
    df.replace(999,-999,inplace=True)
    df.replace(np.inf, -999,inplace=True)
    df.replace(-np.inf, -999, inplace=True)
    df.dropna(inplace=True)
    df.to_pickle(dir+year+'\\'+cut+'{}_{}_df.pkl')
    #save full dataframe to pkl in base_dir
    
    
    #data preparation for BDT
    BDT_dir=dir+year+'\\'+cut+'\\BDT_res'+vers
    if not os.path.exists(BDT_dir):
        os.makedirs(BDT_dir)  
    

    x = df[features]
    for key in features:
        print(key, x[key].mean(), x[key].std())
    # Normalize features to optimize performance (min max scaler)
    scaler = preprocessing.StandardScaler()
    X = scaler.fit_transform(x)
    X=pd.DataFrame(X, columns=features)
    #dump scaler
    pickle.dump(scaler, open(f"{BDT_dir}/scaler_model.pkl", "wb"))


    y=df[['signal','sample','group','weight_']]
    y['signal']=y['signal'].astype('int32')
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
    

    
    """if vers == '_wotop':
        #create sample wo tops for tests
        X_top_train=X_train[y_train['sample']!='top']
        y_top_train=y_train[y_train['sample']!='top']
        normalize(y_top_train)
        normalize(y_test)
        np.save(data_dir+'\\X_train_{}_{}{}'.format(year,cut,vers),X_top_train)
        np.save(data_dir+'\\X_test_{}_{}{}'.format(year,cut,vers),X_test)
        np.save(data_dir+'\\y_train_{}_{}{}'.format(year,cut,vers),y_top_train)
        np.save(data_dir+'\\y_test_{}_{}{}'.format(year,cut,vers),y_test)
    if vers == '_DYonly':
        cond= (y_train['sample']=='DY') | (y_train['group']=='signal')
        X_DY_train=X_train[cond]
        y_DY_train=y_train[cond]
        normalize(y_DY_train)
        normalize(y_test)
        np.save(data_dir+'\\X_train_{}_{}{}'.format(year,cut,vers),X_DY_train)
        np.save(data_dir+'\\X_test_{}_{}{}'.format(year,cut,vers),X_test)
        np.save(data_dir+'\\y_train_{}_{}{}'.format(year,cut,vers),y_DY_train)
        np.save(data_dir+'\\y_test_{}_{}{}'.format(year,cut,vers),y_test)"""

    normalize(y)
    print('saving files')
    np.save(data_dir+'\\X_{}_{}{}'.format(year,cut,vers),X)
    np.save(data_dir+'\\y_{}_{}{}'.format(year,cut,vers),y)
    print('Data prepared, X and y saved to {}.'.format(data_dir))
    return X, y, features


def groupplot_var(dir,df,var,xmin=0, xmax=1000,nbins=50, weight='std'):
    #plot hist for every variables for signal vs DY vs top vs others
    plt.figure(figsize=(8,5))
    groups=['DY','top','other','signal']
    color=['green', 'orange','blue','red']
    bins=np.linspace(xmin, xmax,nbins)
    for j,group in enumerate(groups):
        if weight=='std':
            w=df['weight_'][df['group']==group]
        else:
            w=weight
        plt.hist(df[var][df['group']==group],bins=bins,histtype='step',color=color[j],label=group, density=True, weights=w);
    plt.xlabel(var,fontsize=12);
    plt.ylabel('Events',fontsize=12);
    plt.legend(frameon=True);
    plt.savefig(dir + '/{}.png'.format(var))
    


def plot_distrib(var_list, xlims, base_dir, year, cut):
    df = pd.read_pickle(base_dir + year + '\\'+cut+'_df.pkl ')
    
    fig_dir=base_dir+year+'\\'+cut+'\\data_figs'
    
    var=[i for i in var_list]

    for i,var in enumerate(var):
        if 'weight' in var:
            var='weight_'
            groupplot_var(fig_dir,df,var,xmin=xlims[i][0],xmax=xlims[i][1],weight=None)
        else :
            groupplot_var(fig_dir, df,var,xmin=xlims[i][0],xmax=xlims[i][1])
    print('plots saved to {}'.format(fig_dir))


#for fusing mutliple years
def prep_data_multi(years, version,cut, vers,  dir):
    #set up directories
    
    df=pd.DataFrame()
    for year in years:
        print(year)
        
        data_dir=dir+version+'\\'+cut+'\\data'+vers
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        fig_dir=dir+version+'\\'+cut+'\\data_figs'
        if not os.path.exists(fig_dir):
            os.makedirs(fig_dir)

        samples_dir=dir+'Numpy\\ZV_'+year+'\\'+cut+'\\samples\\v1'
        files=os.listdir(samples_dir)
        samples_name=[file[:-10] for file in files]

        features=pd.read_pickle(samples_dir+'\\'+files[0]).keys().drop('weight_')

        samples_group=[]
        #group samples by 'class'
        for sample in samples_name:
            if 'DY' in sample: samples_group.append('DY')
            elif 'top' in sample: samples_group.append('top')
            elif 'VBS_ZV' in sample: samples_group.append('signal')
            #elif 'Fake' in sample: samples_group.append('fake')
            else : samples_group.append('other')

        samples_df=[]



        # preparing the sfigamples for later
        for i,name in enumerate(files):
            samples_df.append(pd.read_pickle(samples_dir+'\\'+files[i]))
            samples_df[i]['sample']= samples_name[i]
            samples_df[i]['group']=samples_group[i]
            samples_df[i]['year'] = year
            #multiply weights by lumi
            if '2018' in year:
                samples_df[i]['weight_'] *= 59.74
            elif '2017' in year:
                samples_df[i]['weight_'] *= 41.53
            elif '2016' in year:
                samples_df[i]['weight_'] *= 35.867

            df=df.append(samples_df[i], sort=False)
            
    df['signal'] = df['group'] == 'signal'
    df.replace(999,-999,inplace=True)
    df.replace(np.inf, -999,inplace=True)
    df.replace(-np.inf, -999, inplace=True)
    df.dropna(inplace=True)

    df.to_pickle(dir+version+'\\'+cut+'_df.pkl')
        #save full dataframe to pkl in base_dir

    
    #data preparation for BDT
    BDT_dir=dir+version+'\\'+cut+'\\BDT_res'+vers
    if not os.path.exists(BDT_dir):
        os.makedirs(BDT_dir)  
    

    x = df[features]
    for key in features:
        print(key, x[key].mean(), x[key].std())
    # Normalize features to optimize performance (min max scaler)
    scaler = preprocessing.StandardScaler()
    X = scaler.fit_transform(x)
    X=pd.DataFrame(X, columns=features)
    #dump scaler
    pickle.dump(scaler, open(f"{data_dir}/scaler_model.pkl", "wb"))


    y=df[['year','signal','sample','group','weight_']]
    y['signal']=y['signal'].astype('int32')
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
    

    normalize(y)
    print('saving files')
    np.save(data_dir+'\\X_{}_{}{}'.format(version,cut,vers),X)
    np.save(data_dir+'\\y_{}_{}{}'.format(version,cut,vers),y)
    print('Data prepared, X and y saved to {}.'.format(data_dir))
    return X, y, features



def plot_scatter(var_list, base_dir, year, cut):
    df = pd.read_pickle(base_dir + year + '\\'+cut+'{} _{} _df.pkl ')
    fig_dir=base_dir + year + '\\'+cut+'\\data_figs'
    
    groups=['DY','top','other','signal']
    #groups=['DY']
    color=['green', 'orange','blue','red']
    plt.figure(figsize=(15,10))
    if cut=='Boosted_SR':
        jetcats=['vbs_jet', 'FatJet']
    if cut=='Resolved_SR':
        jetcats=['vbs_jet', 'V_jet']

    for jetcat in jetcats:
        for jet in [1,2]:
            plt.figure(figsize=(15,10))
            for j,group in enumerate(groups):
                if jetcat != 'FatJet':
                    x=cut+'_'+jetcat+'_pt'+str(jet)
                    y=cut+'_'+jetcat+'_eta'+str(jet)
                    title=year+cut+'_'+jetcat+str(jet)
                else: 
                    x=cut+'_'+jetcat+'_pt'
                    y=cut+'_'+jetcat+'eta'
                    title=year+cut+'_'+jetcat
                plt.scatter(df[x][df['group']==group],df[y][df['group']==group],color=color[j],label=group, s=1);
                plt.xlabel('pt',fontsize=12);
                plt.ylabel('eta',fontsize=12);
                plt.title(title)
                if cut=='Resolved_SR':
                    plt.xlim(0,600)
                if cut=='Boosted_SR':
                    plt.xlim(0,2200)
                plt.legend(frameon=True);
                plt.savefig(fig_dir + '/{}.png'.format(title))
    print('Scatter plots saved to {}'.format(fig_dir))
                
                

def test_BDT(base_dir, training_year, training_vers, testing_year, testing_vers, cut, variables_list, inputs, compare=False):
    #check if traning model exist
    if not os.path.exists(base_dir+'\\'+training_year+'\\'+cut+'\\BDT_res'):
        print('Model trained on {}_{}_{} doesnt exist'.format(training_year, cut,training_vers))
        return
    training_model=base_dir+'\\'+training_year+'\\'+cut+training_vers+'\\BDT_res\\{}{}_{}.model'.format(training_year,training_vers,cut)
    print('loaded {}{}_{}.model'.format(training_year,training_vers,cut))
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model(training_model)
    #
    data_dir=base_dir+'\\'+testing_year+'\\'+cut+'\\data'+testing_vers
    if not os.path.exists(data_dir):
        print('prepping testing data')
        prep_data(testing_year,cut,testing_vers, base_dir)
    
    Res_dir=base_dir+'\\'+testing_year+'\\'+cut+'\\BDT_res'
    if not os.path.exists(Res_dir):
        os.makedirs(Res_dir)

    X= pd.DataFrame(np.load(data_dir+'\\X_{}_{}{}.npy'.format(testing_year,cut,testing_vers), allow_pickle=True), columns=variables_list)
    X=X[inputs]
    y= pd.DataFrame(np.load(data_dir+'\\y_{}_{}{}.npy'.format(testing_year,cut,testing_vers), allow_pickle=True), columns= ['signal','sample','group','weight_', 'w'])
    test=xgb.DMatrix(data=X,label=y['signal'], feature_names=inputs, weight=y['w'])
    pred=bst.predict(test)
    
    #plot AUC
    plt.figure(figsize=(5,5))
    fpr, tpr, threshold = metrics.roc_curve(y['signal'].astype('int32'),pred, pos_label=1, sample_weight=y['w'])
    tpr.sort()
    fpr.sort()
    roc_auc = metrics.auc(fpr, tpr)
    print ("AUC Score (Test): {:4%}".format(roc_auc))
    plt.plot(tpr,(1-fpr), label =' AUC = %0.4f' %(roc_auc))
    #plt.ylim(0.6,1.05)
    plt.xlabel('Signal efficiency')
    plt.ylabel('Background reduction')
    plt.title('BDT ROC curve')
    plt.grid()
    plt.legend()
    plt.savefig(Res_dir+'\\{}{}_trainedOn{}{}_{}_ROC.png'.format(testing_year,testing_vers,training_year,training_vers,cut))

    #plot BDT ouput by sample
    plt.figure(figsize=(15,8))
    groups=['DY','top','other','signal']
    color=['green', 'orange','blue','red']
    x=[]
    for i,group in enumerate(groups):    
        plt.hist(pred[y['group']==group],bins=np.linspace(0,1,50), label=group, density=True, histtype='step', color=color[i])
    plt.xlabel('BDT output',fontsize=12)
    plt.ylabel('events',fontsize=12)
    plt.title('BDT output')
    plt.legend()
    plt.savefig(Res_dir+'\\{}{}_trainedOn{}{}_{}_BDToutput.png'.format(testing_year,testing_vers,training_year,training_vers,cut))
"""
    if compare = True:
        comp_dir=base_dir+'\\'+training_year+'\\'+cut+'\\data'+training_vers
        X_comp= pd.DataFrame(np.load(data_dir+'\\X_{}_{}{}.npy'.format(training_year,cut,training_vers), allow_pickle=True), columns=variables_list)
        X_comp=X_comp[inputs]
        y_comp= pd.DataFrame(np.load(data_dir+'\\y_{}_{}{}.npy'.format(training_year,cut,training_vers), allow_pickle=True), columns= ['signal','sample','group','weight_', 'w'])
        test_compt=xgb.DMatrix(data=X_comp,label=y_comp['signal'], feature_names=features_Resolved, weight=y_comp['w'])
        pred=bst.predict(test_comp)"""