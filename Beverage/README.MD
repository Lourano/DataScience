This Data Set contains data from a social survey. "What kind of sweet beverages people have been drinking for two weeks". 
[34 rows x 8 columns].

Formulation of the problem: Do a cluster analysis, split the Data Set into possible classes. For analyzing will be used Dendrogram and ulnar diagram(Elbow Method).

Firstly, let's build an automatic dendrogram used in Python. The Ward method and the Euclidean metric will be considered as parameters and for finding distance.

![Dendrogram](https://user-images.githubusercontent.com/47052805/56167257-6139c600-5fe0-11e9-813d-61f38a7a7846.png)

Looking at this diagram we can conclude that we have two classes.

Let's do another observation using "KMeans" algorithm and Elbow Method.(For this observation You need to trust your Dendrogram that number of classes must be in PyFunction. For example: model = KMeans(n_clusters = 2, random_state = 42)).

![Plot](https://user-images.githubusercontent.com/47052805/56168175-0786cb00-5fe3-11e9-8864-39026338e9f3.png)

Looking at this plot we also can conclude that we have two classes.



