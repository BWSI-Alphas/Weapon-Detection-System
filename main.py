from ultralytics import YOLO 
import torch

print(torch.__version__)  # Check PyTorch version
print(torch.cuda.is_available())  # Should be True if ROCm is working correctly

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

data_path = r'c:\Users\Jack\Documents\GitHub\Weapon-Detection-System\data\config.yaml'

# Move the model to GPU
#device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
#model = model.to(device)

# Use the model
model.train(data=data_path, epochs=1)  # train the model