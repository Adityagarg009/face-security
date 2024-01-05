import cv2 as cv
import threading
from deepface import DeepFace
import pyttsx3 
cap= cv.VideoCapture(0,cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv.CAP_PROP_FRAME_WIDTH,480)
counter = 0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
face_match = False
image = cv.imread("content\mera.jpg")
def faceface(frame):
    global face_match
    try:
        if DeepFace.verify(frame, image.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False
while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 ==0:
            try:
                threading.Thread(target=faceface,args=(frame.copy(),)).start()
            except ValueError:
                pass 
        counter +=1
        if face_match:
            cv. putText(frame, "MATCH!", (20,450), cv.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
            engine.say("Match")
            engine.runAndWait()
        else:
            cv.putText(frame, "kon hai be!", (20,450), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)
        cv.imshow("video", frame)    
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
