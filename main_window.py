import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision.io import read_image
from torchvision.transforms import Compose, Resize, ToPILImage

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt


from ui_mainwindow import Ui_MainWindow
from model_utils.model import HelmetRecognitionModel, prepare_image, recognise


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('res/worker.ico'))
        self.setWindowTitle('Распознание рабочих в касках')

        self.reset_visual()

        # self.model = HelmetRecognitionModel()
        self.image_path = ''

        self.ui.actionOpenPhoto.triggered.connect(self.open_image_dialog)
        self.ui.onRecognitionBtnClick.clicked.connect(self.run_recognition)
        # code
        self.show()

    def reset_visual(self):
        pixmap = QPixmap('res/image_416px.png')
        pixmap = pixmap.scaled(416, 416, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.ui.inputPhotoLabel.setPixmap(pixmap)
        self.ui.inputPhotoLabel.setScaledContents(True)
        self.ui.outputPhotoLabel.setPixmap(pixmap)
        self.ui.outputPhotoLabel.setScaledContents(True)

    def open_image_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                  "Image Files (*.png *.jpg *.jpeg)")
        self.image_path = file_path
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path: str):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(416, 416, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.ui.inputPhotoLabel.setPixmap(pixmap)
        self.ui.inputPhotoLabel.setScaledContents(True)  # Масштабировать изображение по размеру QLabel

    def run_recognition(self):
        image = prepare_image(self.image_path)
        prediction = recognise(self.model, image)

        transforms = Compose([
            Resize((416, 416)),  # Используйте те же размеры, что и при обучении
        ])
        image = read_image(self.image_path).float() / 255  # Загрузка и нормализация изображения
        image = transforms(image)

        image = ToPILImage()(image)
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        ax.axis('off')  # Отключение осей

        for i in range(len(prediction[0]['boxes'])):
            box = prediction[0]['boxes'][i].numpy()
            score = prediction[0]['scores'][i].numpy()
            label = prediction[0]['labels'][i].numpy()

            # Пример фильтрации предсказаний по уверенности и вывода информации
            if score > 0.5:  # Порог уверенности
                print(f"SURE Box: {box}, Score: {score}, Label: {label}")
                xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
                rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                         linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                # todo подпись в зависимости от класса
                plt.text(xmin, ymin, 'helmet' if label == 1 else 'head', color='white',
                         bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.2'))

        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        output_filename = "result.png"
        plt.savefig('aaa.png', bbox_inches='tight', pad_inches=0)

        # fig.savefig('aaa.png')
        plt.close(fig)

        pixmap = QPixmap('aaa.png')
        pixmap = pixmap.scaled(416, 416, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.ui.outputPhotoLabel.setPixmap(pixmap)
        self.ui.outputPhotoLabel.setScaledContents(True)

