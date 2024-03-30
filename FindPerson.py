def check_installation(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", package])

# Check for and install required packages
required_packages = ['opencv-python', 'tensorflow', 'numpy']
for package in required_packages:
    check_installation(package)

import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import tensorflow as tf

# Load pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def detect_person(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    predictions = model.predict(img)
    predicted_class = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0]

    if predicted_class[1] == 'person':
        result_label.config(text="Person detected in the image.")
    else:
        result_label.config(text="No person detected in the image.")

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_person(file_path)

# Create GUI window
root = tk.Tk()
root.title("FindPerson")

# Create select image button
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=20)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
