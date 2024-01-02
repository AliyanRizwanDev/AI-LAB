from sklearn.cluster import KMeans

def kmeans_sklearn(data, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    return kmeans.labels_, kmeans.cluster_centers_
