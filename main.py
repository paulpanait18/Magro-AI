import cv2

camera = cv2.VideoCapture(0)

print("Starting Magro's eyes... Press 'q' on your keyboard to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read from camera!")
        break

    cv2.imshow("Magro AI - Vision Test", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Closing Magro's vision.")
        break

camera.release()
cv2.destroyAllWindows()