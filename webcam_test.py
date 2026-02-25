import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("best.pt")

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Webcam not detected")
    exit()

print("✅ Webcam started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO inference
    results = model(frame, conf=0.4)

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Webcam Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()