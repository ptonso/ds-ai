import json

file_path = "/home/tonso/code/ptonso/learn/course/ut/ds-ai/lab-1-dt-adv/notebooks/NLP-Advanced-Classification.ipynb"

with open(file_path, "r") as f:
    nb = json.load(f)

cells = nb["cells"]
for i, cell in enumerate(cells):
    if cell["cell_type"] == "markdown":
        source = "".join(cell["source"])
        
        # Block 1
        if "Use the Gensim library to load your embeddings" in source:
            # Find the next code cell
            for j in range(i+1, min(i+5, len(cells))):
                if cells[j]["cell_type"] == "code":
                    cells[j]["source"] = [
                        "import gensim.downloader as api\n",
                        "\n",
                        "print(\"Loading embeddings...\")\n",
                        "word_vectors = api.load(\"glove-wiki-gigaword-50\")\n",
                        "print(\"Embeddings loaded!\")"
                    ]
                    break

        # Block 2
        elif "create a matrix **embeddings**" in source:
            for j in range(i+1, min(i+5, len(cells))):
                if cells[j]["cell_type"] == "code":
                    cells[j]["source"] = [
                        "import numpy as np\n",
                        "embedding_dim = 50\n",
                        "embedding_weights = np.zeros((vocab_size, embedding_dim))\n",
                        "\n",
                        "for word, idx in tokenizer.word_index.items():\n",
                        "    if word in word_vectors:\n",
                        "        embedding_weights[idx] = word_vectors[word]"
                    ]
                    break
        
        # Block 3
        elif "Print the embedding_weights shape" in source:
            for j in range(i+1, min(i+5, len(cells))):
                if cells[j]["cell_type"] == "code":
                    cells[j]["source"] = [
                        "print(\"Embedding weights shape:\", embedding_weights.shape)"
                    ]
                    break

with open(file_path, "w") as f:
    json.dump(nb, f, indent=1)

print("Forced Exercise 10 update")
