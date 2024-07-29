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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
data_path = '/Users/franklee/Documents/GitHub/Weapon-Detection-System/data/config.yaml'
=======
data_path = r'c:\Users\Jack\Documents\GitHub\Home Security System Project\Weapon-Detection-System\config.yaml'
>>>>>>> Stashed changes
=======
# Path to your YOLOv8 model weights file (.pth)
model_path = r'C:\Users\Noah Lee\OneDrive\Documents\GitHub\Weapon-Detection-System\train_model\trained_model.pth'
>>>>>>> Stashed changes

# Instantiate your model
model = YOLOv8Model()

# Load the state dictionary
model.load_state_dict(torch.load(model_path))

# Set the model to evaluation mode
model.eval()
