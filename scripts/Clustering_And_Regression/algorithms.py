from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def optimal_k(X,range_n_clusters):
    def silhouette(n_clusters):
        clusterer = KMeans(n_clusters=n_clusters)
        cluster_labels = clusterer.fit_predict(X)
        return silhouette_score(X, cluster_labels)
    return max(range_n_clusters,key=silhouette)

def k_means_classify(X):
    clusterer = KMeans(n_clusters=optimal_k(X,range(2,len(X))))
    cluster_labels = clusterer.fit_predict(X)

    clusters = [[] for _ in range(max(cluster_labels)+1)]
    [clusters[cluster_labels[i]].append([X[i][0],X[i][1]]) for i in range(len(cluster_labels))]
    return clusters

def linear_r_squared_of_points(coords):
    x = np.array([[coord[0]] for coord in coords])
    y = np.array([[coord[1]] for coord in coords])
    reg = LinearRegression().fit(x, y)
    return reg.score(x,y)

def poly_r_squared_of_points(coords):
    X = np.array([[coord[0]] for coord in coords])
    y = np.array([[coord[1]] for coord in coords])
    poly_reg = PolynomialFeatures(degree=3)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)
    return pol_reg.score(X_poly,y)

def get_centroid_and_radius(coords):
    x = np.array([coord[0] for coord in coords])
    y = np.array([coord[1] for coord in coords])
    return (int(sum(x) / len(coords)), int(sum(y) / len(coords))), int((((max(x)+min(x))/2) + ((max(y)+min(y))/2))/2)
