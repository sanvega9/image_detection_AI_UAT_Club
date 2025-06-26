# 🍅 Tomato Leaf Disease Classification with TensorFlow and Image Augmentation

This project uses deep learning and image preprocessing techniques to classify tomato leaf diseases, specifically targeting bacterial spot disease, using TensorFlow and Keras.

---

## 🧩 Overview

The model is trained on a dataset of tomato leaf images, augmented with various image transformations to improve generalization and accuracy. The goal is to automatically detect bacterial spot disease on tomato leaves.

---

## ⚙️ Features

- Image preprocessing and augmentation using `ImageDataGenerator`
- Rescaling, zooming, rotation, and flips for robust training
- Binary classification for bacterial spot disease
- Visualizing sample images using Matplotlib
- Uses TensorFlow/Keras for model training (model code can be added separately)

---

## 📂 Dataset Structure

```plaintext
tomato/
├── train/
│   ├── Tomato___Bacterial_spot/
│   └── Tomato___Other_classes/
├── val/
│   ├── Tomato___Bacterial_spot/
│   └── Tomato___Other_classes/
