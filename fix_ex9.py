import json

file_path = "/home/tonso/code/ptonso/learn/course/ut/ds-ai/lab-1-dt-adv/notebooks/NLP-Advanced-Classification.ipynb"

with open(file_path, "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell.get("id") == "a0b0822f":
        cell["source"] = [
            "model = Sequential([\n",
            "    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len),\n",
            "    GRU(32),\n",
            "    Dense(1, activation='sigmoid')\n",
            "])\n",
            "model.summary()"
        ]
    elif cell.get("id") == "8ddb891e":
        cell["source"] = [
            "model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])"
        ]
    elif cell.get("id") == "c8d539f4":
        cell["source"] = [
            "m_history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test), verbose=2)"
        ]
    elif cell.get("id") == "c22b0fa8":
        cell["source"] = [
            "# visualise training history\n",
            "plt.plot(m_history.history['acc'])\n",
            "plt.plot(m_history.history['val_acc'])\n",
            "plt.title('model accuracy')\n",
            "plt.ylabel('accuracy')\n",
            "plt.xlabel('epoch')\n",
            "plt.legend(['train', 'test'], loc=\"lower right\")\n",
            "plt.show()"
        ]

with open(file_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Done updating Exercise 9")
