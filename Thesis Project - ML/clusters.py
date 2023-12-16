import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

clustersDF = pd.read_csv('clusters.csv', header=0, index_col=0) #change the directory accordingly
clusterLabels = clustersDF['predictions']
clustersDF.drop(columns=['predictions'])
data = clustersDF.to_numpy()
labels = clusterLabels.to_numpy()
plt.figure(figsize=(10,10))
u_labels = np.unique(labels)

#plotting the results:

for i in u_labels:
    plt.scatter(data[labels == i ,0] , data[labels == i , 1] , label = i, s=7) #change the '1' to any other number between 1-75"
plt.legend()
#plt.savefig("clustersafterPCA-wellformed-4clusters.png", dpi=200, bbox_inches='tight', pad_inches=0.2)
plt.show()