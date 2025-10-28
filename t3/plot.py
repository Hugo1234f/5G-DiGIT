import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def show_forest():
    forest_f0 = pd.read_csv('./data/results/IsolationForest_f0.csv')
    forest_f1 = pd.read_csv('./data/results/IsolationForest_f1.csv')

    fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
    fig.suptitle('Isolation Forest')

    sc1 = ax1.scatter(forest_f0['PCA1'], forest_f0['PCA2'], c=forest_f0['Label'], cmap="coolwarm_r", s=20)
    ax1.set_title("Frequency 3649.44MHz")
    ax1.set_xlabel("PCA 1")
    ax1.set_ylabel("PCA 2")

    ax2.scatter(forest_f1['PCA1'], forest_f1['PCA2'], c=forest_f1['Label'], cmap="coolwarm_r", s=20)
    ax2.set_title("Frequency 3725.76MHz")
    ax2.set_xlabel("PCA 1")
    ax2.set_ylabel("PCA 2")
    
    cbar = fig.colorbar(sc1, ax=[ax1,ax2], orientation='vertical')
    cbar.set_label("Anomaly Score")
    plt.show()



show_forest()



