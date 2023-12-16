import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D


def loadData():
    df = pd.read_csv('Analysis.csv', header=0, index_col=0)  # Change the path depending on where you save the files
    df = df[df.columns.difference(['id', 'name', 'isKeyboard', 'rumbleItems', 'index'])]
    y_strings = df['label']
    df['label'] = df['label'].replace(
        {'Silver-Gold': 1, 'Platinum-Diamond': 2, 'Champion-Grand-Champion': 3, 'Supersonic-Legend': 4})
    y = df[
        'label'].to_numpy()  # y contains the labels in the form of 1,2,3,4. y_strings contains the labels in string form
    df.drop('label', axis=1, inplace=True)
    columns = [c.strip("'") for c in df.columns]  # contains the feature names
    X = df.to_numpy()

    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)
    return (X_std, y, y_strings, columns, df)


# 2D


def get2dGraph(X, y_strings, df):
    tsne_results_2d = TSNE(n_components=2, learning_rate='auto', init='random', n_jobs=-1).fit_transform(X)  # reducing to 2-d space

    df['tsne-2d-one'] = tsne_results_2d[:, 0]
    df['tsne-2d-two'] = tsne_results_2d[:, 1]
    plt.figure(figsize=(20, 15))
    scatterplot = sns.scatterplot(
        x="tsne-2d-one", y="tsne-2d-two",
        hue=y_strings,
        palette=('red', 'black', 'green', 'blue'),
        style=y_strings,
        markers=('D', 'o', '^', 'X'),
        data=df,
        legend="full",
        alpha=0.3
    )

    fig = scatterplot.get_figure()
    # fig.savefig("tsne.png", bbox_inches='tight', pad_inches=0) # enable only if you want to save the image
    plt.show()

    return fig


# 3D
def get3dGraph(X, y):
    tsne_results = TSNE(n_components=3, learning_rate='auto', init='random', n_jobs=-1 ).fit_transform(X)

    fig = plt.figure(figsize=(10, 10))

    ax = Axes3D(fig)  # Method 1
    ax.scatter(tsne_results[:, 0], tsne_results[:, 1], tsne_results[:, 2], c=y, marker='o')
    ax.set_xlabel('tsne x')
    ax.set_ylabel('tsne y')
    ax.set_zlabel('tsne z')
    plt.title("Data distribution in 3D")
    # plt.savefig("tsne-3d-plot.png", dpi=100, bbox_inches='tight', pad_inches=0.2) # enable only if you want to save the image
    plt.show() # enable if you want to see the plot
    return fig


"""# Cumulative distribution function of each of the features"""


def load8dData():
    df_8 = pd.read_csv('AnalysisReducedToEight.csv', header=0,
                       index_col=0)  # Change the path depending on where you save the files
    df_8 = df_8[df_8.columns.difference(['id', 'index'])]
    y_strings = df_8['label']
    df_8['label'] = df_8['label'].replace(
        {'Silver-Gold': 1, 'Platinum-Diamond': 2, 'Champion-Grand-Champion': 3, 'Supersonic-Legend': 4})
    df_8['label'].unique()
    y = df_8['label'].to_numpy()
    df_8.drop('label', axis=1, inplace=True)
    columns = [c.strip("'") for c in df_8.columns]
    X = df_8.to_numpy()
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)
    return (X_std, y, y_strings, columns, df_8)


def getCDFgraph(X_std, columns):
    idx = 0
    figure, axis = plt.subplots(4, 2, figsize=(10, 10))
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    # k=0
    for i in range(4):
        for j in range(2):
            x_sorted = np.sort(X_std[:][idx])
            cdf = 1. * np.arange(len(x_sorted)) / (len(x_sorted) - 1)
            axis[i, j].plot(x_sorted, cdf)
            axis[i, j].set_title(columns[idx], fontsize='large')
            idx += 1
    # plt.savefig("cdf.png", bbox_inches='tight', pad_inches=0.2) # enable only if you want to save the image
    plt.show()
    return figure


#X, y, y_strings, columns,  df = loadData()
#graph2d = get2dGraph(X, y_strings, df)
# graph3d = get3dGraph(X, y)
X_8, y_8, y_strings_8, columns_8, df_8 = load8dData() # loading the 8-d reduced dataset
graphCDF = getCDFgraph(X_8, columns_8)