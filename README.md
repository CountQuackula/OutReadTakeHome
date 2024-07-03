# OutReadTakeHome
Take home assessment for the Outread AI startup final round of interview/s involving the usage of unsupervised AI techniques to identify clusters of research.

To run:
Use requirements.txt to install all dependencies in a venv ideally. Next run 'python main.py' and 5 graphs will be generated
as well as relevent infromation printed to CLI.

Due to a bit of difficulty getting papers from the links in the .xslx loaded them into a Docs/ dir in local machine
and ran clustering from there. Sadly due to some file name lenght limits couldn't upload this to the repo. Also faced challenges with identifying and extracting the abstracts in cases where it was not clearly defined by an 'Abstract:'
and 'Introduction:' title, so in edge cases took the text of the whole first page to guarantee the abstract was present in the data but at the cost of having muddied the data with introduction and title.

used the following links to understand some stuff:
    atlas - https://m.youtube.com/watch?v=UZDiGooFs54
    vectorisation options - https://dev.to/admantium/nlp-text-vectorization-methods-with-scikit-learn-1lgl
    clustering options - https://scikit-learn.org/stable/modules/clustering.html

design reasoning:
    chose the tfidf vectorisation as it accounts for the importance of each key word/feature
    in an abstract using its frequency rather than the sheer count like count vectorization
    which imparts the information of relative-to-paper importance of each keyword rather than
    possibly having seperated similar papers due to large differences in frequency/count of keywords

    used kmeans for clustering as it was the most familiar algorithm and then tried elbow and silhouette
    for optimal cluster number and user Davies-Bouldin and Calsinki as eval metrics cause they were present
    and understandable from the documentation