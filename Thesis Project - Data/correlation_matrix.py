import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df_8 = pd.read_csv('AnalysisReducedToEight.csv', header=0,
                       index_col=0)  # Change the path depending on where you save the files
df_8 = df_8[df_8.columns.difference(['id', 'index'])]
y_strings = df_8['label']
df_8['label'] = df_8['label'].replace(
    {'Silver-Gold': 1, 'Platinum-Diamond': 2, 'Champion-Grand-Champion': 3, 'Supersonic-Legend': 4})
df_8['label'].unique()
y = df_8['label'].to_numpy()
df_8.drop('label', axis=1, inplace=True)
columns_8 = [c.strip("'") for c in df_8.columns]
X = df_8.to_numpy()
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
f = plt.figure(figsize=(19, 15))
plt.matshow(df_8.corr(), fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.xticks(range(len(columns_8)), columns_8, fontsize=10, rotation=30)
plt.yticks(range(len(columns_8)), columns_8, fontsize=10)
#plt.title('Correlation Matrix', fontsize=16)
plt.savefig("corr_heat_map.png", bbox_inches='tight', pad_inches=0.2) # enable only if you want to save the image
plt.show()