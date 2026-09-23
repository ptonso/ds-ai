"""
Helper functions for the XAI labs.

Every group works with slightly different data and settings. Set your group
number once at the top of each notebook and use the functions below.

Lab 1 and Lab 2 only need pandas / numpy / scikit-learn.
Lab 3 also needs torch and torchvision (imported only inside the functions
that use them).
"""
import os

import numpy as np

# ---------------------------------------------------------------------------
# Group setup
# ---------------------------------------------------------------------------
DATA_DIR = "data"
IMAGE_DIR = "images"
MYSTERY_DIR = "mystery_models"
N_MYSTERY_MODELS = 8

FASHION_CLASSES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                   "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Pairs of classes that are easy to confuse
FASHION_PAIRS = [(0, 6), (2, 4), (2, 6), (4, 6), (5, 7), (7, 9), (0, 2), (3, 4)]
DIGIT_PAIRS = [(4, 9), (3, 8), (1, 7), (3, 5), (5, 6), (2, 7), (7, 9), (0, 6)]

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def _check_group(group_number):
    if group_number is None:
        raise ValueError("Set GROUP_NUMBER at the top of the notebook first.")
    group_number = int(group_number)
    if group_number < 1:
        raise ValueError("The group number must be 1 or higher.")
    return group_number


def group_seed(group_number):
    """The seed S of your group. Use it everywhere a random seed is needed."""
    return _check_group(group_number)


def personal_data_path(group_number, data_dir=DATA_DIR):
    """Path to the data file of your group.

    You have to read the file yourself with pandas (Lab 1, Q1).
    """
    g = _check_group(group_number)
    path = os.path.join(data_dir, f"heart_group_{g:02d}.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Ask the TA for your group file.")
    return path


def your_patient_index(group_number, n_test):
    """Index p of 'your patient' in the test set: p = S mod n."""
    return group_seed(group_number) % int(n_test)


def assignment(group_number, image_dir=IMAGE_DIR):
    """Settings of your group for Lab 3."""
    s = group_seed(group_number)
    result = {
        "fashion_pair": FASHION_PAIRS[s % len(FASHION_PAIRS)],
        "fashion_pair_names": tuple(FASHION_CLASSES[c] for c in FASHION_PAIRS[s % len(FASHION_PAIRS)]),
        "digit_pair": DIGIT_PAIRS[s % len(DIGIT_PAIRS)],
        "mystery_id": s % N_MYSTERY_MODELS,
        "image": None,
    }
    if os.path.isdir(image_dir):
        images = sorted(f for f in os.listdir(image_dir) if f.lower().endswith(IMAGE_EXTENSIONS))
        if images:
            result["image"] = os.path.join(image_dir, images[s % len(images)])
    return result


# ---------------------------------------------------------------------------
# Lab 3: small CNN used for MNIST and for the mystery models
# ---------------------------------------------------------------------------
def _torch():
    import torch
    from torch import nn
    return torch, nn


def make_small_cnn():
    """Small CNN for 28x28 grey images with 10 classes.

    Only nn modules are used (no functional calls), so shap.DeepExplainer works.
    Inputs are expected in [0, 1] (no normalisation).
    """
    torch, nn = _torch()

    class SmallCNN(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv_layers = nn.Sequential(
                nn.Conv2d(1, 16, kernel_size=5),
                nn.MaxPool2d(2),
                nn.ReLU(),
                nn.Conv2d(16, 32, kernel_size=5),
                nn.MaxPool2d(2),
                nn.ReLU(),
            )
            self.fc_layers = nn.Sequential(
                nn.Linear(32 * 4 * 4, 64),
                nn.ReLU(),
                nn.Linear(64, 10),
            )

        def forward(self, x):
            x = self.conv_layers(x)
            x = x.view(-1, 32 * 4 * 4)
            return self.fc_layers(x)

    return SmallCNN()


def train_small_cnn(model, train_loader, epochs=2, lr=1e-3, seed=0, verbose=True):
    torch, nn = _torch()
    torch.manual_seed(seed)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for epoch in range(epochs):
        total, correct, running = 0, 0, 0.0
        for x, y in train_loader:
            opt.zero_grad()
            out = model(x)
            loss = loss_fn(out, y)
            loss.backward()
            opt.step()
            running += loss.item() * len(y)
            correct += (out.argmax(1) == y).sum().item()
            total += len(y)
        if verbose:
            print(f"epoch {epoch + 1}: loss {running / total:.3f}, train accuracy {correct / total:.3f}")
    model.eval()
    return model


def accuracy(model, loader):
    torch, _ = _torch()
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for x, y in loader:
            correct += (model(x).argmax(1) == y).sum().item()
            total += len(y)
    return correct / total


def mnist_loaders(root=DATA_DIR, batch_size=128, fashion=False):
    torch, _ = _torch()
    from torchvision import datasets, transforms
    ds = datasets.FashionMNIST if fashion else datasets.MNIST
    tf = transforms.ToTensor()  # values in [0, 1]
    train = ds(root, train=True, download=True, transform=tf)
    test = ds(root, train=False, download=True, transform=tf)
    return (torch.utils.data.DataLoader(train, batch_size=batch_size, shuffle=True),
            torch.utils.data.DataLoader(test, batch_size=batch_size, shuffle=False))


def load_or_train_mnist_cnn(path="mnist_cnn.pt", epochs=1):
    """Load the MNIST CNN, or train it once (about 1-2 minutes on a laptop)."""
    torch, _ = _torch()
    model = make_small_cnn()
    train_loader, test_loader = mnist_loaders()
    if os.path.exists(path):
        model.load_state_dict(torch.load(path, map_location="cpu"))
        model.eval()
    else:
        train_small_cnn(model, train_loader, epochs=epochs)
        torch.save(model.state_dict(), path)
    print(f"MNIST test accuracy: {accuracy(model, test_loader):.3f}")
    return model, train_loader, test_loader


def load_mystery_model(mystery_id, model_dir=MYSTERY_DIR):
    torch, _ = _torch()
    path = os.path.join(model_dir, f"mystery_{int(mystery_id)}.pt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Ask the TA for the mystery models.")
    model = make_small_cnn()
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model
