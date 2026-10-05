import json

file_path = "/home/tonso/code/ptonso/learn/course/ut/ds-ai/lab-1-dt-adv/notebooks/NLP-Advanced-Classification.ipynb"

with open(file_path, "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell.get("id") == "5fe3e325":
        cell["source"] = [
            "import gensim.downloader as api\n",
            "\n",
            "# We use the gensim downloader to get a pretrained GloVe model (50 dimensions)\n",
            "# This will automatically download and cache it if not already present.\n",
            "print(\"Loading embeddings...\")\n",
            "word_vectors = api.load(\"glove-wiki-gigaword-50\")\n",
            "print(\"Embeddings loaded!\")"
        ]
    elif cell.get("id") == "6e580d5d":
        cell["source"] = [
            "embedding_dim = 50\n",
            "embedding_weights = np.zeros((vocab_size, embedding_dim))\n",
            "\n",
            "for word, i in tokenizer.word_index.items():\n",
            "    if word in word_vectors:\n",
            "        embedding_weights[i] = word_vectors[word]"
        ]
    elif cell.get("id") == "b7bc4329":
        cell["source"] = [
            "print(\"Embedding weights shape:\", embedding_weights.shape)"
        ]

with open(file_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Done updating Exercise 10")
