from sklearn import cluster, datasets, metrics, model_selection
import numpy as np
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Week 9 HW")
print(ascii_banner)

# load data
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

# Option 1: k-means on all data
print("Option 1: k-means on all data")

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

print("Accuracy Score: %s" % metrics.accuracy_score(y_iris, k_means.labels_))
print("Adjusted Rand Score: %s" % metrics.adjusted_rand_score(y_iris, k_means.labels_))
print("Homogeneity Score: %s" % metrics.homogeneity_score(y_iris, k_means.labels_))
print("\n")


# Option 2: k-means on data split in half
print("Option 2: k-means on data split in half")

X_train, X_test, y_train, y_test = model_selection.train_test_split(X_iris, y_iris, test_size=0.5)

k_means_1 = cluster.KMeans(n_clusters=3, n_init=10)
k_means_1.fit(X_train)

k_means_2 = cluster.KMeans(n_clusters=3, n_init=10)
k_means_2.fit(X_test)

print("Score of first half")
print("Accuracy Score: %s" % metrics.accuracy_score(y_train, k_means_1.labels_))
print("Adjusted Rand Score: %s" % metrics.adjusted_rand_score(y_train, k_means_1.labels_))
print("Homogeneity Score: %s" % metrics.homogeneity_score(y_train, k_means_1.labels_))
print("\n")

print("Score of second half")
print("Accuracy Score: %s" % metrics.accuracy_score(y_test, k_means_2.labels_))
print("Adjusted Rand Score: %s" % metrics.adjusted_rand_score(y_test, k_means_2.labels_))
print("Homogeneity Score: %s" % metrics.homogeneity_score(y_test, k_means_2.labels_))
print("\n")

print("Combined Score of both halves")
combined_y_train = np.concatenate((y_train, y_test))
new_combined_y_train = np.concatenate((k_means_1.labels_, k_means_2.labels_))
print("Accuracy Score: %s" % metrics.accuracy_score(combined_y_train, new_combined_y_train))
print("Adjusted Rand Score: %s" % metrics.adjusted_rand_score(combined_y_train, new_combined_y_train))
print("Homogeneity Score: %s" % metrics.homogeneity_score(combined_y_train, new_combined_y_train))

