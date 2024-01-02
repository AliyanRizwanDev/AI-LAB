from collections import Counter

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b)**2))

def knn_predict(train_X, train_y, test_point, k):
    distances = [euclidean_distance(test_point, x) for x in train_X]
    sorted_indices = np.argsort(distances)
    k_nearest_indices = sorted_indices[:k]
    k_nearest_labels = train_y[k_nearest_indices]
    return Counter(k_nearest_labels).most_common(1)[0][0]
