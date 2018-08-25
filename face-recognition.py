import cv2
import os
import numpy as np

"""
    identify the people in the training data folders
    leave first space blank, fill with all of the names in the training directory
    ex: if p1 folder has photos of Emma Watson, i will label the first (1) spot "Emma Watson"
    continue to add more instances of people based on the folder number
    ex: if p2 folder has photos of Cardi B i will label the second (2) spot "Cardi B", and so on
"""
PEOPLE = ["", "Emma Watson", "Cardi B"]

"""
    confidence is the DISTANCE between the item and what it is being matched (lower is better)
    things that may affect this & cause false positives are:
    1. training data photo quality
    2. webcam feed quality
    3. amount of images in training data. higher is usually better
"""
CONFIDENCE_THRESHOLD = 100;

def detect_faces(img):
    print(type(img))
    print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('data/haarcascade.xml')

    #result is a list of faces in image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5);

    if (len(faces) == 0):
        return None, None

    #init array to hold the grayscale'd image maps of faces
    gray_faces = []

    #using the locations of faces, add image maps of grayscaled faces to array
    for i in range(len(faces)):
        (x, y, w, h) = faces[i]
        gray_faces.append(gray[y:y+w, x:x+h])

    return gray_faces, faces

"""
    this function will read all persons' training images, detect face from each image
    also trains the face recognizer
"""
def train_data(data_folder_path):
    print("Preparing data...")
    #get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []

    for dir_name in dirs:
        #ignore directories that dont start with s
        if not dir_name.startswith("s"):
            continue;
        #removing letter 's' from dir_name will give us label (int)
        label = int(dir_name.replace("p", ""))
        subject_path = data_folder_path + "/" + dir_name
        #get the images that are inside the given subject directory
        subject_images = os.listdir(subject_path)

        for image_name in subject_images:
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;

            image_path = subject_path + "/" + image_name
            image = cv2.imread(image_path)

            #detect the faces in image
            #for subject image samples, make sure there is only one face!
            face, rect = detect_faces(image)

            #ignore faces that are not detected, add found faces to list
            #because detect returns an array of faces, we want the first element
            #even if there is only one element in the array we dont want to put an array in an array if we dont need to!
            if face is not None:
                faces.append(face[0])
                labels.append(label)

    #print total faces and labels
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    #train our face recognizer! with our faces + their labels
    #train() expects the labels to be a numpy array, so do a quick conversion
    face_recognizer.train(faces, np.array(labels))

    return face_recognizer

"""
    detirmines the label of predicted person
"""
def predict(img, face_recognizer):
    predicted_faces = []
    img_copy = img.copy()
    #detect face from the image
    faces, rect = detect_faces(img_copy)

    if faces is None:
        return img_copy

    #predict the image using trained face recognizer
    #send face for prediction, but save area of face (rect) for drawing
    for i in range(len(faces)):
        label_index, confidence = face_recognizer.predict(faces[i])
        if confidence > CONFIDENCE_THRESHOLD:
            #confidence isnt strong enough, make label blank
            label_text = PEOPLE[0]
        else:
            label_text = PEOPLE[label_index]

        predicted_faces.append([confidence, label_text, rect[i]])
    #sorting faces by lowest confidence value, get rid of duplicates
    predicted_faces.sort()
    #draw a rectangle around faces detected
    draw_rectangle(img_copy, predicted_faces)

    return img_copy

"""
    draws the rectangle and label
    params: image to draw rectangles on, a list of (confidence, labels, face location)
"""
def draw_rectangle(img, face_list):
    for face in face_list:
        if len(face[2]) == 4:
            (x, y, w, h) = face[2]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, face[1], (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        else:
            return
