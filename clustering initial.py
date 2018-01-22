import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
x=([
    [1,2],
    [2,3],
    [5,7],
    [1,0.6],
    [8,9],
    [3,2]
])

# plt.scatter(x[:,0],x[:,1], s=150)
# plt.show()


clf = KMeans(n_clusters=2)
clf.fit(x)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.", "r.", "c.", "b", "k.", "o."]
for i in range(len(x)):
    plt.plot(x[i][0], x[i][1], colors[labels[i]], markersize = 15)
plt.scatter(centroids[:,0], centroids[:,1], marker='X' )
plt.show()

