                        Algorithm of the directed taxonomic search of attributes (NTPO).

The main task of this method is to get some informational content of factors.
                  
          
                           Step 1. Solve the problem of clustering n features into m clusters.

![ElbowMethod](https://user-images.githubusercontent.com/47052805/67286960-eac3d680-f4e2-11e9-9d28-27cf8ea62efa.png)

![ScatterPlot](https://user-images.githubusercontent.com/47052805/67286997-fa431f80-f4e2-11e9-9ef1-17509534b929.png)



    Step 2. Select a typical characteristic in each cluster. 
    Such signs will be as independent as possible from one another.
    
![Sorting](https://user-images.githubusercontent.com/47052805/67288140-1778ed80-f4e5-11e9-9746-da4551570f60.png)


    Step 3. Run each factor in each cluster and select the coefficient
    of information content (in my case it is the Gini Index)
    
![GiniIndex](https://user-images.githubusercontent.com/47052805/67288134-1647c080-f4e5-11e9-83d1-257db7fb2820.png)

![PrintImourityIndex](https://user-images.githubusercontent.com/47052805/67288148-19db4780-f4e5-11e9-88c2-5ee93f944ca9.png)
    
    
In this example, I used USA Housing dataset.








