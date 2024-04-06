import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from torchvision.io import read_image
from torchvision.transforms import Compose, Resize, ToPILImage


class ImageManager:
    __OUTPUT_FILE_PREFIX = 'photos/outputs'
    __TRANSFORMER = Compose([
        Resize((416, 416)),
    ])

    def inference_input(self, image_path: str):
        """
        Подготовка изображения к инференсу
        :param image_path:
        :return:
        """
        image = read_image(image_path).float() / 255
        image = self.__TRANSFORMER(image)
        return image.unsqueeze(0)

    def __plt_input(self, image_path: str):
        """
        Подготовка изображения к отрисовке на нем результатов инференса
        :param image_path:
        :return:
        """
        image = read_image(image_path).float() / 255
        image = self.__TRANSFORMER(image)
        return ToPILImage()(image)

    def get_figured_output(self, image_path: str, prediction: list) -> str:
        """
        Отрисовываем результат инференса на картинке
        :param image_path:
        :param prediction:
        :return:
        """
        image = self.__plt_input(image_path)
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        ax.axis('off')  # Отключение осей

        for i in range(len(prediction[0]['boxes'])):
            box = prediction[0]['boxes'][i].numpy()
            score = prediction[0]['scores'][i].numpy()
            label = prediction[0]['labels'][i].numpy()

            if score > 0.5:  # Порог уверенности
                print(f"SURE Box: {box}, Score: {score}, Label: {label}")
                xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
                rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                         linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                plt.text(xmin, ymin, 'helmet' if label == 1 else 'head', color='white',
                         bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.2'))

        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        output_path = f'{self.__OUTPUT_FILE_PREFIX}/{os.path.basename(image_path)}'
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        return output_path
