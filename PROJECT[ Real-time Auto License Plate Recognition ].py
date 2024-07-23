
import cv2
import numpy as np
import tensorflow as tf
import pytesseract
from PIL import Image
model = tf.keras.models.load_model('license_plate_recognition_model.h5')
cap = cv2.VideoCapture(0)
cv2.namedWindow('License Plate Recognition', cv2.WINDOW_NORMAL)
cv2.resizeWindow('License Plate Recognition', 640, 480)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    outputs = model.predict(blur)
    plates = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:
                x, y, w, h = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                roi = gray[int(y):int(y+h), int(x):int(x+w)]
                plates.append(roi)
    for plate in plates:
        plate = cv2.resize(plate, (300, 100))
        plate = cv2.threshold(plate, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        img = Image.fromarray(plate)
        text = pytesseract.image_to_string(img, config='--psm 11')
        print(text)
        cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 255, 0), 2)
        cv2.putText(frame, text, (int(x), int(y-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Display the output
    cv2.imshow('License Plate Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
cv2.destroyAllWindows()
