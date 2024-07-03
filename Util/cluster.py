import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.manifold import TSNE

def kmeans(vec):
    #run kmeans for elbow, silhouette, davies-bouldwin and calinski
    vec_dense = vec.toarray()
    inertia = []
    silhouette_scores = []
    label_set = []
    clusts = 30

    davies_bouldin_scores = []
    calinski_harabasz_scores = []
    for k in range(1, clusts):
        kmeans = KMeans(n_clusters=k, random_state=42)

        labels = kmeans.fit_predict(vec_dense)
        label_set.append(labels)

        inertia.append(kmeans.inertia_)
        if k >= 2:
            silhouette_scores.append(silhouette_score(vec_dense, labels))
            davies_bouldin_scores.append(davies_bouldin_score(vec_dense, labels))
            calinski_harabasz_scores.append(calinski_harabasz_score(vec_dense, labels))
    
    plt.plot(range(1, clusts), inertia, marker='x')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.title('K-Means Clustering - Elbow Method - stationary point is better')
    plt.show()
    
    plt.plot(range(2, clusts), silhouette_scores, marker='x')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('K-Means Clustering - Silhouette Score - higher is better')
    plt.show()

    plt.plot(range(2, clusts), davies_bouldin_scores, marker='x')
    plt.xlabel('Number of clusters')
    plt.ylabel('Davies-Bouldin Index')
    plt.title('K-Means Clustering - Davies-Bouldin Index - lower is better')
    plt.show()

    plt.plot(range(2, clusts), calinski_harabasz_scores, marker='x')
    plt.xlabel('Number of clusters')
    plt.ylabel('Calinski-Harabasz Index')
    plt.title('K-Means Clustering - Calinski-Harabasz - higher is better')
    plt.show()

    return label_set

def plot_cluster(label_set, vec, data_from_folder):
    vec_dense = vec.toarray()
    # Reduce dimensionality to 2D using t-SNE
    tsne_2d = TSNE(n_components=2, random_state=42)
    vec_2d = tsne_2d.fit_transform(vec_dense)

    # Plot the 2D t-SNE visualization with titles
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(vec_2d[:, 0], vec_2d[:, 1], c=label_set, cmap='viridis')

    #print('About to start labellign all points in 2D plot')
    # Add titles as annotations
    #for i, title in enumerate(data_from_folder):
    #    plt.annotate(title[0], (vec_2d[i, 0], vec_2d[i, 1]), fontsize=8, alpha=0.75)

    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('2D t-SNE Visualization of Clusters with Titles')
    plt.colorbar(scatter)
    plt.show()

def silhouette(vec):
    #higher better
    scores = []
    clusts = 60
    for k in range(2, clusts):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(vec)
        score = silhouette_score(vec, labels)
        scores.append(score)
    plt.plot(range(2, clusts), scores, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette Score')
    plt.show()

def davies_bouldin(vec):
    #lower is better
    scores = []
    vec_dense = vec.toarray()
    cluts = 30
    for k in range(2, cluts):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(vec_dense)
        score = davies_bouldin_score(vec_dense, labels)
        scores.append(score)
    plt.plot(range(2, cluts), scores, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Davies-Bouldin Index')
    plt.show()

def cal(vec):
    scores = []
    cluts = 30
    vec_dense = vec.toarray()
    for k in range(2, cluts):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(vec_dense)
        score = calinski_harabasz_score(vec_dense, labels)
        scores.append(score)
    plt.plot(range(2, cluts), scores, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Calinski-Harabasz Index')
    plt.show()