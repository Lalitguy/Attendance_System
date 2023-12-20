# Attendance System

This Simple Python project demonstrates the usage of the `face_recognition` library to create a basic attendance system. The program utilizes face detection with the Haarcascade classifier and face recognition to identify known faces from input photos.

## Features:
- **Face Detection:** Utilizes Haarcascade classifier for detecting faces in a live video.
- **Face Recognition:** Matches detected faces with known_faces using the `face_recognition` library.
- **Attendance Logging:** Records the names and time of recognized individuals in a CSV file.

## Usage:
1. Add photos of known individuals to the `photos` directory.
2. Run the code file to start the attendance system.
3. Detected faces matching the input photos will be logged in a CSV file with the date.

## Requirements:
- Python
- OpenCV (`cv2`)
- Numpy
- Face_recognition library
- Haarcascade Frontalface classifier

**Note:** This project is a simple demonstration of face recognition and attendance logging. Further enhancements can be made for scalability and additional features for eg. instead of loading image files one by one, can use the loop for iterating, through all the images and for productive usage instead of giving images for evry time the program is run, it would be efficient to load and save the face encodings of all the face images in a separate file.
