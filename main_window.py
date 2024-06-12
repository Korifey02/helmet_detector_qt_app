from PySide6.QtWidgets import QMainWindow, QFileDialog, QButtonGroup
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

from ui_mainwindow import Ui_MainWindow
from model import HelmetRecognitionModel
from image_manager import ImageManager


class MainWindow(QMainWindow):
    __BASE_PLACEHOLDER = ':/images/res/before_load_image.png'

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # classes initialisation
        self.model = HelmetRecognitionModel()
        self.image_manager = ImageManager()
        # self.model = None

        # for BLAS selection
        self.ui.mklBlasBtn.toggled.connect(lambda: self.radio_button_click(self.ui.mklBlasBtn))
        self.ui.openBlasBtn.toggled.connect(lambda: self.radio_button_click(self.ui.openBlasBtn))
        self.ui.blisBlasBtn.toggled.connect(lambda: self.radio_button_click(self.ui.blisBlasBtn))

        # for open photo/video triggers connection
        self.ui.actionOpenPhoto.triggered.connect(self.open_image_button_click)

        # button triggers
        self.ui.onRecognitionBtnClick.clicked.connect(self.recognition_button_click)
        self.ui.onCleanBtnClick.clicked.connect(self.clean_button_click)

        # init radio buttons
        self.__init_radio_buttons()
        # disable recognition button
        self.ui.onRecognitionBtnClick.setDisabled(True)

        # local variables
        self.__input_image_path = ''
        self.__blas_selected = False

        self.show()

    def radio_button_click(self, radio_button):
        """
        Листенер нажатия на любую radio button, по выбору BLAS версии
        :param radio_button:
        :return:
        """
        if radio_button.isChecked():
            selected_model_version = radio_button.text()
            self.model.set_model_version(selected_model_version)
            self.__blas_selected = True
            self.__check_button_disabled()

    def open_image_button_click(self):
        """
        Листенер диалогового окна по нажатию на открытие фото
        :return:
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Image Files (*.png *.jpg *.jpeg)")
        self.__input_image_path = file_path
        if file_path:
            self.__set_image_into_label(file_path, self.ui.inputPhotoLabel)
        self.__check_button_disabled()

    def recognition_button_click(self):
        """
        Обрабтчик нажатия на кнопку проверки
        :return:
        """
        inference_input = self.image_manager.inference_input(self.__input_image_path)
        prediction = self.model.inference(inference_input)
        result_file_path = self.image_manager.get_figured_output(self.__input_image_path, prediction)
        self.__set_image_into_label(result_file_path, self.ui.outputPhotoLabel)

    def clean_button_click(self):
        """
        Обработчик нажатия на кнопку очищения
        :return:
        """
        self.__input_image_path = ''
        self.__blas_selected = False
        self.reset_visual()
        self.__uncheck_all_radio_buttons()
        self.ui.onRecognitionBtnClick.setDisabled(True)

    def reset_visual(self):
        """
        Установка базовых картинок в label фото
        :return:
        """
        self.__set_image_into_label(self.__BASE_PLACEHOLDER, self.ui.inputPhotoLabel)
        self.__set_image_into_label(self.__BASE_PLACEHOLDER, self.ui.outputPhotoLabel)

    @staticmethod
    def __set_image_into_label(file_path: str, label):
        """
        Загрузка фото в передаваемый label
        :param file_path:
        :param label:
        :return:
        """
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(416, 416, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def __init_radio_buttons(self):
        """
        Создаем группу кнопок из радиобатонов, по выбору BLAS
        :return:
        """
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.blisBlasBtn)
        self.button_group.addButton(self.ui.mklBlasBtn)
        self.button_group.addButton(self.ui.openBlasBtn)

    def __uncheck_all_radio_buttons(self):
        """
        Очищаю выбранную пользователем BLAS версию
        :return:
        """
        self.button_group.setExclusive(False)
        for radioButton in self.button_group.buttons():
            radioButton.setChecked(False)
        self.button_group.setExclusive(True)

    def __check_button_disabled(self):
        """
        Проверка на доступность кнопку для инеференса
        :return:
        """
        if self.__input_image_path and self.__blas_selected:
            self.ui.onRecognitionBtnClick.setEnabled(True)
