import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import nltk
from pathlib import Path

datapath = Path.cwd().parent / "databank" / "reviews.csv"
dataset=pd.read_csv(datapath)
dataset=dataset[['sentiment', 'text']]
dataset = dataset.rename(columns={'sentiment': 'class'})

X = dataset['text'].str.lower()
X = X.str.replace(r'[^a-zA-Z\s]', '', regex=True)
X = X.str.replace(r'\s+', ' ', regex=True)

# simplified for speed, just vectorizing
vectorizer = CountVectorizer(min_df=10, max_df=0.995, stop_words='english', max_features=1000)
X = vectorizer.fit_transform(X)

le = LabelEncoder()
y = le.fit_transform(dataset['class'])

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25)

train_y = np.array(train_y).reshape(-1, 1)

def forward_pass(X, W, b):
    Z = X @ W + b
    return 1/(1 + np.exp(-Z))

def gradient_descent(X, W, b, P, y, lr):
    n = X.shape[0]
    dW = 1/n * X.T @ (P - y)
    db = 1/n * np.sum(P - y)
    W = W - lr * dW
    b = b - lr * db
    return W, b

def logistic_regression(X, y, lr, iters, init_type='zeros'):
    d = X.shape[1]
    if init_type == 'zeros':
        W = np.zeros((d, 1))
        b = np.zeros(1)
    else:
        W = np.random.random(size=(d,1))
        b = np.random.random(size=1)
    
    for i in range(iters):
        P = forward_pass(X, W, b)
        W, b = gradient_descent(X, W, b, P, y, lr)
    return W, b

for init in ['random', 'zeros']:
    W, b = logistic_regression(train_X, train_y, lr=1.5, iters=500, init_type=init)
    P_train = 1 * (forward_pass(train_X, W, b) >= 0.5)
    print(f"{init} init accuracy: {(P_train == train_y).mean():.3f}")
