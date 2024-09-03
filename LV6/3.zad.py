from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def generate_data(n_samples, flagc):
    if flagc == 1:
        random_state = 365
        X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)

    elif flagc == 2:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                   centers=4,
                                   cluster_std=[1.0, 2.5, 0.5, 3.0],
                                   random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)

    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)

    else:
        X = []

    return X


n_samples = 500
method = 1
X = generate_data(n_samples, method)


# Funkcija za crtanje dendograma za različite metode
def plot_dendrogram(X, method):
    Z = linkage(X, method=method)
    plt.figure(figsize=(10, 7))
    dendrogram(Z)
    plt.title(f'Dendrogram (method={method})')
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.show()


# Prikaz dendograma za različite metode
methods = ['single', 'complete', 'average', 'ward']

for method in methods:
    plot_dendrogram(X, method)