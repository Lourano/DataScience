                        Algorithm of the directed taxonomic search of attributes (NTPO).

                  The main task of this method is to get some informational content of factors.



                           Step 1. Solve the problem of clustering n features into m clusters.

![ElbowMethod](https://user-images.githubusercontent.com/47052805/67286960-eac3d680-f4e2-11e9-9d28-27cf8ea62efa.png)

![ScatterPlot](https://user-images.githubusercontent.com/47052805/67286997-fa431f80-f4e2-11e9-9ef1-17509534b929.png)



    Step 2. Select a typical characteristic in each cluster. Such signs will be as independent as possible from one another.







Step 3. Determine the number m ' m. Performing enumeration of factors from m to m '(total Cm' times), identifying
m
the corresponding sample and checking their accuracy on the control sample, we conclude on the composition of the set of informative features.

In this example, I will use USA Housing dataset.


