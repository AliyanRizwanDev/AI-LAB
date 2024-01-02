import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b)**2))

def kmeans(data, k, max_iters=100):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(point)
        
        new_centroids = [np.mean(cluster, axis=0) if cluster else centroids[i] for i, cluster in enumerate(clusters)]
        
        if np.allclose(new_centroids, centroids):
            break
        
        centroids = new_centroids
    
    return clusters, centroids
