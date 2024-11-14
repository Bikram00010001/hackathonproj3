import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.regularizers import l2

# Dataset directory
data_dir = 'C:/Users/DELL/OneDrive/Desktop/code/dataset/Dataset/Train'
categories = ['Alluvial soil', 'Black Soil', 'Clay soil', 'Red soil']
IMG_SIZE = 128

# Prepare dataset
images = []
labels = []

for idx, category in enumerate(categories):
    category_path = os.path.join(data_dir, category)
    if not os.path.exists(category_path):
        print(f"Error: The directory {category_path} does not exist.")
        continue
    for img_name in os.listdir(category_path):
        img_path = os.path.join(category_path, img_name)
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        img = cv2.imread(img_path)
        if img is None:
            print(f"Warning: Unable to load image {img_path}")
            continue
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = img / 255.0  # Normalize pixel values to [0, 1]
        images.append(img)
        labels.append(idx)  # Use the index as the label

# Convert images and labels to numpy arrays
images = np.array(images)
labels = np.array(labels)

# One-hot encode the labels
labels = to_categorical(labels, num_classes=len(categories))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Define the model
model = Sequential()

# Convolutional layers with regularization
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3), kernel_regularizer=l2(0.01)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu', kernel_regularizer=l2(0.01)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu', kernel_regularizer=l2(0.01)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the convolutional layers
model.add(Flatten())

# Fully connected layers with dropout regularization
model.add(Dense(512, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dropout(0.5))

# Output layer
model.add(Dense(len(categories), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=15, batch_size=256, validation_data=(X_test, y_test))

# Save the trained model
model.save('soil_classifier_model.h5')

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

