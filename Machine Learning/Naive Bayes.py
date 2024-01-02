class NaiveBayesClassifier:
    def __init__(self):
        self.class_prob = {}
        self.mean = {}
        self.std = {}
    
    def fit(self, X, y):
        self.class_prob = {label: len(y[y == label]) / len(y) for label in set(y)}
        
        for label in set(y):
            label_data = X[y == label]
            self.mean[label] = np.mean(label_data, axis=0)
            self.std[label] = np.std(label_data, axis=0)
    
    def predict(self, X):
        predictions = []
        for point in X:
            probabilities = {}
            for label in self.class_prob:
                probabilities[label] = np.prod(
                    (1 / (np.sqrt(2 * np.pi) * self.std[label])) *
                    np.exp(-(point - self.mean[label])**2 / (2 * self.std[label]**2))
                )
            predictions.append(max(probabilities, key=probabilities.get))
        return predictions
