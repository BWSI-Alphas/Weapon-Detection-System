from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO('yolov5s.pt')  # Replace with the appropriate pre-trained model file

# Print the model architecture
print(model)
