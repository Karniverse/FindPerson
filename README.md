# FindPerson
 # Project Title: Object Detection - Person Detection in Images

## Description

This project consists of two parts, one implemented in Python using OpenCV library, and the other in C# using TensorFlow.NET. Both parts aim to detect if an input image contains a person or not.

## Python Implementation (using OpenCV)

Python implementation utilizes OpenCV library for object detection. It reads an input image, performs preprocessing, loads the Haar Cascade classifier model, and applies it to detect objects in the image.

### Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [OpenCV 4.x](https://opencv.org/releases/)

### Usage

1. Save the provided Python script (`person_detection.py`) in a new project folder.
2. Install OpenCV by following the instructions on the official website.
3. Run the Python script using your preferred IDE or terminal: `python person_detection.py <path_to_image>`

## C# Implementation (using TensorFlow.NET)

C# implementation utilizes TensorFlow.NET library to run a pre-trained model (MobileNet V2) for object detection. It reads an input image, preprocesses it and passes through the model to predict if a person is present in the image or not.

### Requirements

- [.NET 5 SDK](https://dotnet.microsoft.com/download/dotnet/5.0)
- [TensorFlow.NET](https://github.com/tensorflow/tensorflow.net#installation)

### Usage

1. Save the provided C# script (`PersonDetection.cs`) in a new project folder.
2. Install TensorFlow.NET by following the instructions on GitHub.
3. Run the C# script using your preferred IDE or terminal: `dotnet run --project PersonDetection.cs <path_to_image>`

## Testing

For testing, prepare a set of images with and without people to evaluate both Python and C# implementations. Place them in the project folder and ensure that the paths are set accordingly. Both scripts will output the detection result (whether a person is present or not) for each input image.