
import cv2
import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Magro: {text}")
    engine.say(text)
    engine.runAndWait()

camera = cv2.VideoCapture(0)

speak("Magro vision systems online.")

while True:
    success, frame = camera.read()

    if not success:
        speak("Camera error detected.")
        break

    cv2.imshow("Magro AI - Vision Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        speak("Powering down.")
        break
    elif key == ord('s'):
        filename = f"snapshot_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        speak("Snapshot captured.")

camera.release()
cv2.destroyAllWindows()