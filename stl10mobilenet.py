import torch as torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models

def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

def initialize_model(model_name, num_classes, feature_extract, use_pretrained=True, HW=96):
    # Initialize these variables which will be set in this if statement. Each of these
    # variables is model specific.
    model_ft = models.mobilenet_v2(pretrained=use_pretrained)
    set_parameter_requires_grad(model_ft, feature_extract)
    num_ftrs = model_ft.classifier[1].in_features
    model_ft.classifier[1] = nn.Linear(in_features=num_ftrs, out_features=num_classes)
    input_size = HW
    return model_ft, input_size
