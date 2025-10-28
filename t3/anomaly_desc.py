import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

forest_f0 = pd.read_csv('./data/results/IsolationForest_f0-long.csv')
forest_f1 = pd.read_csv('./data/results/IsolationForest_f1-long.csv')

abnum = 0
nornum = 0

def norms(data):

    f0_ab = forest_f0[forest_f0['Label'] == -1]
    f0_norm = forest_f0[forest_f0['Label'] == 1]

    abnum = len(f0_ab)
    nornum = len(f0_norm)

    features = forest_f0.columns
    features = features.drop("Label")
    means = []
    sums = 0

    for feature in features:
        mean = abs(f0_ab[feature].mean() - f0_norm[feature].mean())
        means.append(mean)
        sums += mean
    
    norm_difs = []
    norm_sum = 0.0
    for mean in means:
        norm_difs.append(mean / sums)
        norm_sum += mean / sums
    

    for i in range(len(features)):
        print(f"\t{features[i]}: {round(norm_difs[i],3)}")
    print('\t--------------------')
    print(f"\tmean contribution: {round(norm_sum/len(means),3)}")
    print(f"Fraction of abnormalities: {round(abnum/(abnum+nornum),4)}")
    

print("\tAnomaly contribution 3649.44MHz:")
norms(forest_f0)

print("\n\tAnomaly contribution 3725.76MHz:")
norms(forest_f1)

