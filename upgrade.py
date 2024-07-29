import torch

checkpoint = torch.load(r'c:\Users\Jack\Documents\GitHub\Home Security System Project\Weapon-Detection-System\train_model\new_trained_model.pt')
print(checkpoint.keys())