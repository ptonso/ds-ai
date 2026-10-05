import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense

vocab_size = 1000
embedding_dim = 32
max_len = 30

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len),
    GRU(32),
    Dense(1, activation='sigmoid')
])
model.summary()
