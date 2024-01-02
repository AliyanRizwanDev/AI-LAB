from sklearn.neighbors import KNeighborsClassifier

def knn_sklearn(train_X, train_y, test_X, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_X, train_y)
    return knn.predict(test_X)
