import torch
import torch.nn as nn
from torchvision.models.detection import ssd300_vgg16
from torchvision.models.detection.ssd import SSD300_VGG16_Weights
from torchvision.io import read_image
from torchvision.transforms import Compose, Resize


class HelmetRecognitionModel:

    def __init__(self, model_path: str):
        # __MODEL_PATH = 'models/model_openblas.pth'
        self.__MODEL_PATH = model_path

    def get_model(self):
        model = ssd300_vgg16(weights=SSD300_VGG16_Weights.COCO_V1)
        num_classes = 3
        for idx, block in enumerate(model.head.classification_head.children()):
            if isinstance(block, nn.Sequential):
                old_layer = block[-1]
                new_layer = nn.Conv2d(old_layer.in_channels, num_classes, kernel_size=old_layer.kernel_size,
                                      stride=old_layer.stride, padding=old_layer.padding)
                new_layer.weight.data.normal_(0, 0.01)
                new_layer.bias.data.zero_()
                block[-1] = new_layer

        model.load_state_dict(torch.load(self.__MODEL_PATH))
        model.eval()  # Переключение модели в режим инференса
        return model


def prepare_image(image_path):
    transforms = Compose([
        Resize((416, 416)),
    ])
    image = read_image(image_path).float() / 255
    image = transforms(image)
    return image.unsqueeze(0)


#todo обернуть в класс
def recognise(model, image):
    with torch.no_grad():
        return model(image)

