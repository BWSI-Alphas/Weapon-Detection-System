import torch

# Define or import your model class
# This is just a placeholder. You need the actual model class definition.
class YOLOv8Model(torch.nn.Module):
    def __init__(self):
        super(YOLOv8Model, self).__init__()
        # Define your model layers here

    def forward(self, x):
        # Define the forward pass here
        return x

# Path to your YOLOv8 model weights file (.pth)
model_path = r'C:\Users\Noah Lee\OneDrive\Documents\GitHub\Weapon-Detection-System\train_model\trained_model.pth'

# Instantiate your model
model = YOLOv8Model()

# Load the state dictionary
model.load_state_dict(torch.load(model_path))

# Set the model to evaluation mode
model.eval()
