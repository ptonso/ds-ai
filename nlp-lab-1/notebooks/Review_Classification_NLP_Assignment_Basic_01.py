#!/usr/bin/env python
# coding: utf-8

# # NLP - Text Classification Lab
# 
# Note that this lab has three levels: basic, regular and advanced.
# 
# 
# Completing the **basic** part earns you a grade of 5.5-6.0.
# 
# Completing the **regular** part earns you a max grade of 8.0.
# 
# Completing the **advanced** part earns you a max grade of 10.0.
# 
# Please return a Jupyter notebook as a submission in Canvas, to make the grading easier for us.
# 
# 
# 

# ## Basic Level

# ## Necessary Imports

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score
import re
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
from nltk.corpus import stopwords
from tqdm import tqdm

import nltk
nltk.download('stopwords')


# ### Reading the Dataset

# In[ ]:


datapath = Path.cwd().parent / "databank" / "reviews.csv"
dataset=pd.read_csv(datapath)

dataset=dataset[['sentiment', 'text']]
dataset = dataset.rename(columns={'sentiment': 'class'})
dataset


# ### Exercise 1
# Split the dataset into two data structures (pandas frames), one for the reviews (our documents) (X) and one for the class (y).
# Check that the lengths of both dataframes are equal

# In[ ]:


#Your answer goes here

X = dataset['text']
y = dataset['class']
assert len(X) == len(y), "X and y must have the same length"
print(f"Size of X is : {X.shape}, Size of y is : {y.shape}")


# ### Preprocessing
# We now begin our preprocessing task, by lowercasing all of the documents, removing special characters and numerical values. Then we tokenize and stem our documents. 
# ### Exercise 2
# Write a function to_lower(X) that takes a dataframe and returns its content in lower case.

# In[ ]:


def to_lower(X): 
    X = X.str.lower()
    return X


# In[ ]:


X=to_lower(X)
X.head()


# ### Exercise 3 
# Write a function clean_text(X), that takes the dataset as an input and removes all special characters and numerical values from it.

# In[ ]:


def clean_text(X):

    X = X.str.replace(r'[^a-zA-Z\s]', '', regex=True)
    X = X.str.replace(r'\s+', ' ', regex=True)
    return X


# In[ ]:


X=clean_text(X)


# In[ ]:


X


# ### Exercise 4
# Write a function tokenize(X) that takes a dataframe and returns the tokens in each row (document).

# In[ ]:


def tokenize(X):
    '''
    TODO: implement this function
    '''
    X = X.apply(lambda x: x.split())
    return X


# In[ ]:


X=tokenize(X)
print(X)


# ### Exercise 5
# Write a function remove_stop_words(X, stop_words), that takes a dataset X and the set of stop words you want removed from it. Your function should return the dataset, free of any common words.

# In[ ]:


def remove_stop_words(X, stop_words):
    stop_set = set(stop_words)
    return X.apply(lambda x: [word for word in x if word not in stop_set])


# In[ ]:


X = remove_stop_words(X, stopwords.words('english'))


# In[ ]:


X


# ### Exercise 6
# Write a function stem(X), that takes a dataframe X and returns the stems of all the words in it.
# 
# You're free to choose any stemmer you want.
# 
# It's also possible to use a lemmatizer (lemmatization will be a lot slower!).

# In[ ]:


def stem(X):
    stemmer = PorterStemmer()
    return X.apply(lambda x: [stemmer.stem(word) for word in x])    



# In[ ]:


X=stem(X)


# In[ ]:


X


# ### Exercise 7
# Having called a tokenizer and a stemmer on our dataset, the resulting rows are now of type list.
# We need to convert them back to str, as our CountVectorizer expects a dataset where every document is a string. 
# Define a function to_String(X), that takes your dataset and stitches back its rows back to the str format.

# In[ ]:


def to_String(X): 
    X = X.apply(lambda x: ' '.join(x))
    return X


# In[ ]:


X=to_String(X)
X


# ### Vector Space Model
# Now that we preprocessed our corpus, we can proceed to vectorize it.
# ### Exercise 8
# We can now use the [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) from sklearn to create our document-term-matrix.
# 
# a. Create a document-term matrix from your dataset X, use min_df and max_df parameters to exclude words that appear in less than 10 documents, and words that appear in more than 99.5% of the documents. We want to keep only words of medium frequency, as stated in the lecture.

# In[ ]:


vectorizer = CountVectorizer(min_df=10, max_df=0.995)
X = vectorizer.fit_transform(X)


# b. Print the size and the contents of your vocab (feature space)

# In[ ]:


vocab = vectorizer.get_feature_names_out()
print(f"The size of the vocabulary is: {len(vocab)}")
print("The first 10 items in the vocab are:\n", vocab[:10])


# ### Training our Logistic Regressor
# 
# ### Exercise 9:
# Before we dive into training our model, let's get our vector of true labels **y** into the right format.
# Notice that by printing the contents of **y** below, what we get are the labels **neg** and **pos**. 
# The model works only with **1 and 0**.
# Let's convert the labels accordingly.

# In[ ]:


y[:10]


# a. Use the [label_ encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) from Sklearn, to transform the labels in the vector **y** accordingly.

# In[ ]:


le = LabelEncoder()
y = le.fit_transform(y)


# In[ ]:


y[:10]


# We also create a test and train set from our DTM and our vector y.

# In[ ]:


train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25)


# ### Exercise 10
# Use the [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) classifier from Sklearn to train your model, and check its accuracy on the test set

# In[ ]:


model = LogisticRegression(max_iter=1000)
model.fit(train_X, train_y)


# In[ ]:


print("Accuracy on train set", accuracy_score(train_y, model.predict(train_X)) * 100)
print("Accuracy on test set", accuracy_score(test_y, model.predict(test_X)) * 100)


# **Our results show a clear sign of overfitting**

# ## Regular 
# 
# Our main goal in the regular exercises is to provide a basic implementation for the logistic regression model.
# 
# 
# We'll first define a function **initialize(X)** to get the initial vector of weights W and bias b.
# 
# We will then do our **forward_pass(X, W, b)** to get a vector of predictions.
# 
# We then write a function **gradient_descent(X, W, b, y, lr)** to get the updated vector of weights W and bias b.
# 
# 
# We conclude this part by writing the model function, which calls all of the functions we defined, and proceed with the learning.

# ### Exercise 11
# Write a function **initialize(X)**, which takes a DTM as an input and returns a vector of weights W and a scalar b for the bias. Both are initialized with some random values.

# In[ ]:


train_X=train_X.toarray()
train_y=np.array(train_y)
train_y=train_y.reshape(train_y.shape[0],1)


# In[ ]:


def initialize(X):
    d = X.shape[1]
    W = np.random.random(size=(d,1))
    b = np.random.random(size=1)

    return (W, b)


# In[ ]:


W,b=initialize(train_X)
print("Shape of the vector W is:",W.shape)


# ### Exercise 12
# Write a function **forward_pass(X, W, b)** which takes the DTM X, the vector W and the bias b as inputs and returns a vector of predictions P.
# 
# Your function should implement the following equations
# 
# $$Z=X.W + b$$
# $$P=\sigma{(Z)}=\frac{1}{1+e^{-Z}}$$
# 
# You can also implement the sigmoid as a separate function, 

# In[ ]:


def forward_pass(X, W, b):
    Z = X @ W + b
    return 1/(1 + np.exp(-Z))


# In[ ]:


P=forward_pass(train_X, W, b)
print("The vector of predictions shape is:",P.shape)


# ### Exercise 13
# Calculating the loss/cost function
# You can use the [implementation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html) by Sklearn, but feel free to also implement your own.
# <!-- #endregion -->i
# 
# ```python id="36N1AVywgUy6"
# def log_loss(y_true, p_pred):
#     loss = -(y_true * np.log(p_pred) + (1-y_true) * np.log(1-p_pred))
#     return np.mean(loss)
# 
# ```
# 
# <!-- #region id="vonvu9_UGM6x" -->
# ### Exercise 14
# Write a function **gradient_descent(X, W, b , P, y, lr)** and returns the updated weight vector W, and bias b.
# Your function needs to implement the following equations:
# 
# $$dW=\frac{1}{ne}X^T . (P-y)$$
# 
# $$db=\frac{1}{ne} \sum(P-y)$$
# 
# $$W=W-\alpha dW$$
# 
# $$b=b-\alpha db$$

# In[ ]:


def gradient_descent(X, W, b, P, y, lr):
    n = X.shape[0]
    dW = 1/n * X.T @ (P - y)
    db = 1/n * np.sum(P - y)
    W = W - lr * dW
    b = b - lr * db
    return W, b


# In[ ]:


W, b=gradient_descent(train_X, W, b, P, train_y, lr=0.2)
print("shape of the updated W is:", W.shape)


# ### Exercise 15
# Now we can implement our logistic regression model in 3 simple steps
# 1. initialize the vector W and the bias b
# 
# 2. repeat until number of iterations is reached   
#     2.1. get a vector of predictions P  
#     2.2. update the weights W and bias b using gradient descent  
#     
# 3. return the final vector W and bias b
# 
# **logistic_regression(X, y, lr, iters)**, takes the matrix X as an input, the vector of true labels y, a learning rate, and the number of iterations iters. The function returns the learned parameters of the model, namely W and b.

# In[ ]:


def logistic_regression(X, y, lr, iters):

    W, b = initialize(X)


    for i in tqdm(range(iters)):
        P = forward_pass(X, W, b)
        W, b = gradient_descent(X, W, b, P, y, lr)

    return W, b



# In[ ]:


W, b= logistic_regression(train_X, train_y, lr=1.5, iters=5)


# ### Testing our model
# We have been able to implement the model and run it on our training set. It's time to see how well it does. 
# We'll first make a function **predict(X, W, b)**, that takes the dataset and the learned parameters and returns an array of predictions. Our threshold is 0.5, any prediction below that is returned as 0, and any above it are returned as 1.

# In[ ]:


def predict(X, W, b):
    P = forward_pass(X, W, b)
    P=1*(P >= 0.5)
    return P


# In[ ]:


P_train=predict(train_X, W, b)


# In[ ]:


print("Accuracy on our train set is, ",accuracy_score( train_y, P_train)*100, "%")


# In[ ]:


P_test=predict(test_X, W, b)


# In[ ]:


print("Accuracy on our test set is", accuracy_score(test_y, P_test)*100, "%")


# ## Advanced
# 
# In this part, we set to understand what did the model actually learn.
# 
# ### Exercise 16
# Using the CountVectorizer of Sklearn, recreate a pandas frame where the rows contain the documents and the columns contain the features. 
# 
# 

# In[ ]:


#Your code goes here
DTM = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())


# In[ ]:


DTM


# ### Exercise 17
# Knowing that our logistic regressor learns a weight for each feature (word in the vocab),  return the words with the highest weights (5 highest), and the words with lowest weights (5 lowest).

# In[ ]:


weights = model.coef_[0]
vocab = vectorizer.get_feature_names_out()
weights_df = pd.DataFrame({'word': vocab, 'weight': weights})
sorted_weights = weights_df.sort_values(by='weight')

print('5 words with the lowest weights')
for index, row in sorted_weights.head(5).iterrows():
    print(f"the word `{row['word']}` has weight {row['weight']:.2f}")

print('__________________')
print('5 words with the highest weights')
for index, row in sorted_weights.tail(5).iterrows():
    print(f"the word `{row['word']}` has weight {row['weight']:.2f}")


# ### Exercise 18
# Print the weights of the words "good" and "bad"

# In[ ]:


#Your code goes here
bad_weight = weights_df.loc[weights_df['word'] == 'bad', 'weight'].values[0]
good_weight = weights_df.loc[weights_df['word'] == 'good', 'weight'].values[0]

print(f"weight of word bad [{bad_weight}]")
print(f"weight of word good [{good_weight}]")


# ##### Hope you enjoyed learning about logistic regression!
