# Credits

This project builds on the open-source work below. Each part is used under its author's terms, and the original authors keep all rights to their work.

## Face mask detection

`src/Face_mask_detection/detect_mask_video.py` is adapted from Adrian Rosebrock's tutorial [COVID-19: Face Mask Detector with OpenCV, Keras/TensorFlow, and Deep Learning](https://pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/) (PyImageSearch, 2020). The tutorial fine-tunes MobileNetV2 on a two-class mask dataset created by Prajna Bhandary. We changed the script to run for a fixed 10 seconds and return a mask or no-mask result to the main program instead of streaming indefinitely.

## Face detector model

`src/Face_mask_detection/face_detector/` holds OpenCV's ResNet-10 SSD face detector (`deploy.prototxt` and `res10_300x300_ssd_iter_140000.caffemodel`), distributed with the [OpenCV](https://github.com/opencv/opencv) project's deep learning face detection sample.

## Pulse oximeter driver

`src/MAX30100/max30100.py` is Martin Fitzpatrick's [max30100](https://github.com/mfitzp/max30100) Python library, itself a re-implementation of the Arduino C library by [Connor Huffine/Kontakt](https://github.com/kontakt/MAX30100). The library's own README notes that it returns raw sensor values and does not convert them into heart rate or SpO2.

## Sensor and hardware libraries

- [mfrc522](https://pypi.org/project/mfrc522/) for the RC522 RFID reader
- [Adafruit CircuitPython MLX90614](https://github.com/adafruit/Adafruit_CircuitPython_MLX90614) for the infrared thermometer
- [gpiozero](https://gpiozero.readthedocs.io/) for the LEDs
- [Pyrebase4](https://pypi.org/project/Pyrebase4/) for the Firebase upload
