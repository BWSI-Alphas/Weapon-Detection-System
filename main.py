from ultralytics import YOLO 
import torch
import os

print(torch.__version__)  # Check PyTorch version
print(torch.cuda.is_available())  # Should be True if ROCm is working correctly

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

data_path = '/Users/franklee/Documents/GitHub/Weapon-Detection-System/data/config.yaml'

# Move the model to GPU
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
model = model.to(device)

# Train the model
model.train(data=data_path, epochs=35)

# Define the directory and filename for saving the model
save_dir = '/Users/franklee/Documents/GitHub/Weapon-Detection-System/train_model'
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, 'trained_model.pth')

# Save the model
torch.save(model.state_dict(), save_path)

print(f"Model saved to {save_path}")
