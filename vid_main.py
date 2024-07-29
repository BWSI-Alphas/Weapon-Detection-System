# import cv2
# from ultralytics import YOLO  # Import YOLO from the ultralytics package

# # Load YOLOv8 model
# model = YOLO(r'c:\Users\Jack\Documents\GitHub\Home Security System Project\Weapon-Detection-System\train_model\new_trained_model.pt')  # Use the path to your YOLOv8 model file

# # Open video capture
# cap = cv2.VideoCapture(0)  # Use 0 for the default camera or replace with video file path

# while True:
#     # Read frame from video
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform object detection
#     results = model(frame)

#     # Render results on the frame
#     frame_with_boxes = results.render()[0]

#     # Display the frame
#     cv2.imshow('YOLOv8 Object Detection', frame_with_boxes)

#     # Exit if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
import cv2
import torch
from ultralytics import YOLO

# Load the pre-trained YOLO model
model = YOLO(r'c:\Users\Jack\Documents\GitHub\Home Security System Project\Weapon-Detection-System\train_model\new_trained_model.pt')  # Replace with your specific model file if needed

# Initialize the webcam video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (YOLO models expect RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform object detection
    results = model(rgb_frame)

    # Process results
    for result in results:
        # Extract bounding boxes and labels
        boxes = result.boxes.xyxy.tolist()
        scores = result.boxes.conf.tolist()
        labels = result.names  # Class labels
        
        for box, score in zip(boxes, scores):
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f'{labels[0]}: {score:.2f}'  # Modify label as needed
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if the job is finished
cap.release()
cv2.destroyAllWindows()