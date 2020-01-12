# K-Nearest Neighbors (KNN)

K- Nearest Neighbors is a

- **Supervised machine learning algorithm** as target variable is known [1].
- **Non parametric**. Non-parametric means there is no assumption for underlying data distribution. In other words, the model structure determined from the dataset. This will be very helpful in practice where most of the real world datasets do not follow mathematical theoretical assumptions [2].
- **Lazy algorithm** as KNN does not have a training step. All data points will be used only at the time of prediction. With no training step, prediction step is costly. An eager learner algorithm eagerly learns during the training step [1].
- Used for both **Classification and Regression** [1].
- Uses **feature similarity** to predict the cluster that the new point will fall into [1].

K in KNN :

- K is a **number used to identify similar neighbors for the new data point** [1].
- Choice of K has a drastic impact on the results we obtain from KNN [1].
- K value is odd , ex: 1, 3, 5, etc.

How does KNN Work ?

We have age and experience in an organization along with the salaries. We want to predict the salary of a new candidate whose age and experience is available [1].

Step 1: **Choose a value for K**. K should be an odd number.

Step2: **Find the distance of the new point to each of the training data**.

Step 3: **Find the K nearest neighbors to the new data point**.

Step 4: For classification, count the number of data points in each category among the k neighbors. **New data point will belong to class that has the most neighbors**.

For regression, value for the **new data point will be the average of the k neighbors**.

Distance in KNN can be calculated using :

- **Euclidean distance**

- **Manhattan distance**

- **Hamming Distance**

- **Minkowski Distance**

  

Pros of using KNN :

- The training phase of K-nearest neighbor classification is **much faster** compared to other classification algorithms [2].
- There is **no need to train a model for generalization**, That is why KNN is known as the **simple and instance-based learning algorithm** [2].
- KNN can be **useful in case of nonlinear data** [2].
- Can be used with the regression problem [2].
- Output value for the object is computed by the average of k closest neighbors value [2].

Cons of using KNN :

- The testing phase of K-nearest neighbor classification is **slower and costlier in terms of time and memory** [2]. 
- It requires **large memory for storing the entire training dataset for prediction** [2].
-  KNN **requires scaling of data** because KNN uses the Euclidean distance between two data points to find nearest neighbors [2].
- KNN also **not suitable for large dimensional data** [2].

References

[1] <https://medium.com/datadriveninvestor/k-nearest-neighbors-knn-7b4bd0128da7>

[2] <https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn>



