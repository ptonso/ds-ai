import pandas as pd
from pathlib import Path
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, LSTM

data_path = Path.cwd() / "lab-1-dt-adv" / "databank" / "spam.csv"
dataset = pd.read_csv(data_path, encoding='ISO-8859-1')
X=dataset.v2
y=dataset.v1

def to_lower(X): 
    X = X.str.lower()
    return X

def clean_text(X):
    X = X.str.replace(r'[^a-zA-Z\s]', ' ', regex=True)
    X = X.str.replace(r'\s+', ' ', regex=True)
    X = X.str.strip()
    return X

X=to_lower(X)
X=clean_text(X)

y = (y=='spam').astype(int)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
X_encoded = tokenizer.texts_to_sequences(X)
vocab_size = len(tokenizer.word_index) + 1

max_len = 30
X_padded = pad_sequences(X_encoded, maxlen=max_len, padding='post', truncating='post')

TEST_SIZE = 0.25
X_train, X_test, y_train, y_test = train_test_split(X_padded, y, test_size=TEST_SIZE, random_state=100)

embedding_dim = 32

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=2, batch_size=32, validation_data=(X_test, y_test), verbose=1)
print(history.history)
