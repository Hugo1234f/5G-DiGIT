import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print('Reading data...')
data = pd.read_csv('./data/scaled.csv')

scalar = StandardScaler()

def isolation_forest():
    print('Running IsolationForest...')
    data_f0 = data[data['Frequency'] == 0]
    data_f1 = data[data['Frequency'] == 1]

    model_f0 = IsolationForest(max_samples=len(data_f0), random_state=0)
    model_f1 = IsolationForest(max_samples=len(data_f1), random_state=0)

    print('\tFitting the model...')
    forest_f0 = model_f0.fit(data_f0)
    forest_f1 = model_f1.fit(data_f1)
    
    print('\tPredicting labels...')
    labels_f0 = forest_f0.predict(data_f0)
    labels_f1 = forest_f1.predict(data_f1)

    print('\tCalculating mean anomaly score...')
    scores_f0 = forest_f0.decision_function(data_f0)
    scores_f1 = forest_f1.decision_function(data_f1)


    print('\tCreating PCA Projection...')
    pca_f0 = PCA(n_components=2)
    pca_f1 = PCA(n_components=2)

    fitted_cpa_f0 = pca_f0.fit_transform(data_f0)
    fitted_cpa_f1 = pca_f1.fit_transform(data_f1)

    print('\tWriting...')
    df0 = pd.DataFrame({
        "PCA1": fitted_cpa_f0[:,0],
        "PCA2": fitted_cpa_f0[:,1],
        "Label": labels_f0,
        "Scores": scores_f0
    })
    df0_long = data_f0
    df0_long.loc[:, 'Frequency'] = labels_f0
    df0_long.rename(columns={'Frequency':'Label'}, inplace=True)

    df1 = pd.DataFrame({
        "PCA1": fitted_cpa_f1[:,0],
        "PCA2": fitted_cpa_f1[:,1],
        "Label": labels_f1,
        "Scores": scores_f1
    })
    df1_long = data_f1
    df1_long['Frequency'] = labels_f1
    df1_long.rename(columns={'Frequency':'Label'}, inplace=True)

    df0.to_csv('./data/results/IsolationForest_f0.csv', index=False)
    df1.to_csv('./data/results/IsolationForest_f1.csv', index=False)

    df0_long.to_csv('./data/results/IsolationForest_f0-long.csv', index=False)
    df1_long.to_csv('./data/results/IsolationForest_f1-long.csv', index=False)


isolation_forest()