import sys
from Util.load import loadFromFolder
from Util.debug import showAbstracts, showVectorized
from Util.prep import get_vectorized
from Util.cluster import kmeans, silhouette, davies_bouldin, cal, plot_cluster

def main():
    # Specify the path to your PDF folder
    pdf_folder_path = 'Docs'
    
    try:
        data_from_folder = loadFromFolder(pdf_folder_path)
        # showAbstracts(data_from_folder)

        vec, tokens = get_vectorized(data_from_folder, keep_nums = False, method = 'tfidf')
        # showVectorized(vec)

        label_set = kmeans(vec)
        plot_cluster(label_set[20], vec, data_from_folder)
        #print('Hello World!')

        for i, title in enumerate(data_from_folder):
            print(f'Paper: "{title[0]}" belongs to cluster {label_set[20][i] + 1}')
        
        #reverse the label-cluster relationship
        #print(f'Number of clusters identified as optimal: 21')

        freq_clust = {}
        for i in range(len(label_set[20])):
            #print(f'{label_set[20][i]}')
            if label_set[20][i] + 1 not in freq_clust:
                freq_clust[label_set[20][i] + 1] = 0
            #print('Hello World!')
            freq_clust[label_set[20][i] + 1] += 1
        
        for key, val in freq_clust.items():
            print(f'Cluster {key} had {val} paper/s.')
        
        for key, val in freq_clust.items():
            print(f'Cluster: {key}, with {val} paper/s had the following terms/topics:')
            
            unique_tokens = set()
            for i in range(len(label_set[20])):
                if label_set[20][i] + 1 == key:
                    for token in tokens[i].split():
                        if token not in unique_tokens and ('\\' or '/' not in token):
                            unique_tokens.add(token)

            print(f'    {unique_tokens}')
            #print(tokens)
    except Exception as e:
        print(f"Error loading data from folder: {e}")

if __name__ == "__main__":
    origional_stdout = sys.stdout
    f = open('log.txt', 'w')
    #sys.stdout = f
    main()
    sys.stdout = origional_stdout
