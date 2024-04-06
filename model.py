import torch
import torch.nn as nn
from torchvision.models.detection import ssd300_vgg16
from torchvision.models.detection.ssd import SSD300_VGG16_Weights


class HelmetRecognitionModel:
    __MKL_PATH = 'models/model_mkl.pth'
    __OPENBLAS_PATH = 'models/model_openblas.pth'
    __BLIS_PATH = 'models/model_blis.pth'

    def __init__(self):
        self.base_model = None
        self.model = None
        self.__base_model_init()

    def __base_model_init(self):
        """
        Инициализирую базовую модель основанную на ssd300_vgg16
        :return:
        """
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
        self.base_model = model

    def __get_model_path(self, blas_version: str) -> str:
        """
        Получаю путь до модели по выбранной версии реализации BLAS
        :param blas_version:
        :return:
        """
        match blas_version:
            case 'MKL':
                return self.__MKL_PATH
            case 'OpenBLAS':
                return self.__OPENBLAS_PATH
            case 'BLIS':
                return self.__BLIS_PATH

    def set_model_version(self, blas_version: str):
        """
        Загружаем в базовую модель веса из выбранной версии модели
        :param blas_version:
        :return:
        """
        model_path = self.__get_model_path(blas_version)
        model = self.base_model
        model.load_state_dict(torch.load(model_path))
        model.eval()
        self.model = model

    def inference(self, image: str):
        """
        Получаем инференс по входной картинке
        :param image:
        :return:
        """
        with torch.no_grad():
            return self.model(image)
