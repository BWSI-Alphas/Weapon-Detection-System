from ultralytics import YOLO
import torch

# Verify GPU availability
print(torch.__version__)  # Check PyTorch version
print(torch.cuda.is_available())  # Check if CUDA is available
print(torch.backends.mps.is_available())  # Check if Metal Performance Shaders (Apple Silicon) is available

# Load a model (ensure correct path and model type)
model = YOLO("yolov8n.pt")  # Use a pre-trained model, not a config file

# Move the model to GPU if available
device = torch.device('cuda')
model = model.to(device)

# Specify data path
data_path = r'C:\Users\Noah Lee\OneDrive\Documents\GitHub\Weapon-Detection-System\config.yaml'

# Train the model
model.train(data=data_path, epochs=1, device=device)  # Ensure 'device' is passed correctly
