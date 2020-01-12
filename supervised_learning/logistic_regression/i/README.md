# Logistic Regression

**Logistic regression** is a statistical machine learning algorithm that **classifies the data by considering outcome variables on extreme ends and tries makes a logarithmic line that distinguishes between them** [1].

**Logistic Regression** is a Machine Learning classification algorithm that is **used to predict the probability of a categorical dependent variable** [2]. 

In logistic regression, the **dependent variable is a binary variable** that contains data coded as 1 (yes, success, etc.) or 0 (no, failure, etc.) [2] .

Example of using logistic regression :

- Predict whether an email is spam or not
- Predict whether it rains or not
- Predict whether diabetes or not

Sigmoid function [3] :

![img](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1534281880/image2_kwxquj.png)

Apply Sigmoid function on linear regression [3] :

![img](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1534281880/image3_qldafx.png)

Advantages [3]

- Doesn't require high computation power
- Easy to implement
- Easily interpretable
- Used widely by data analyst and scientist.

Disadvantages [3]

- Not able to handle a large number of categorical features/variables
- Vulnerable to overfitting
- Can't solve the non-linear problem with the logistic regression that is why it requires a transformation of non-linear features.
- Will not perform well with independent variables that are not correlated to the target variable and are very similar or correlated to each other

References

[1] <https://towardsdatascience.com/logistic-regression-b0af09cdb8ad>

[2] <https://medium.com/greyatom/logistic-regression-89e496433063>

[3] <https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python>