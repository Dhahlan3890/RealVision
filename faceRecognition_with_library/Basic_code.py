import cv2
import face_recognition
import os
import time

# Open the default camera (usually the built-in webcam)


ImageList = os.listdir('Images')
Images = []


for photo in ImageList:
    Images.append(photo)

Peoples = []

for i in Images:
    imgPeople = face_recognition.load_image_file(f'./Images/{i}')
    imgPeople = cv2.cvtColor(imgPeople,cv2.COLOR_BGR2RGB)
    #imgTest = face_recognition.load_image_file('tasee.jpg')
    #imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

    faceLoc = face_recognition.face_locations(imgPeople)[0]
    encodeImage = face_recognition.face_encodings(imgPeople)[0]
    cv2.rectangle(imgPeople,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
    Peoples.append(encodeImage)

present_list =[]
# Loop to capture frames from the camera

def open_camera_for_duration(duration_seconds):

    cap = cv2.VideoCapture(0)
    
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    start_time = time.time()

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break
        results = 0
        
        while len(face_recognition.face_locations(frame)) != 0:
            faceLocTest = face_recognition.face_locations(frame)[0]
            #print(face_recognition.face_locations(frame))
            encodeTest = face_recognition.face_encodings(frame)[0]
            cv2.rectangle(frame,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

            file_names = [""]* len(Peoples)
            for i in range(len(Peoples)):
                results = face_recognition.compare_faces([Peoples[i]],encodeTest)
                faceDis = face_recognition.face_distance([Peoples[i]],encodeTest)
                file_names[i] = os.path.splitext(os.path.basename(Images[i]))[0]

            if results == [True]:
                results = file_names[i]
                while results not in present_list:
                    present_list.append(results)
                
                return results, faceDis
            

            #print(results,faceDis)
            cv2.putText(frame,f'{results}: {faceDis}',(faceLocTest[3]+6,faceLocTest[2]-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        

        # Display the frame in a window
        #cv2.imshow('Camera', frame)

        # Break the loop if the specified duration has passed
        if time.time() - start_time > duration_seconds:
            break

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Set the duration in seconds (e.g., 10 seconds)
    duration_seconds = 10

    # Open the camera for the specified duration
    print(open_camera_for_duration(duration_seconds))
