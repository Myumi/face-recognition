from facerecognition import *

def main():
    #un-comment these next two lines if you are running this program
    #with new faces in the training data
    face_recognizer = train_data('data/people')
    face_recognizer.save('recognizer/training-data.xml')

    #un-comment next two lines if recognizer was already trained
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    #face_recognizer.load('recognizer/training-data.xml')

    #this is for the first webcam on the system
    #increase value if you have more than one webcam attached
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = predict(frame, face_recognizer)
        cv2.imshow('frame', frame)

        #break loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #turns off camera
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
