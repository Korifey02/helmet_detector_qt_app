# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import images_rc
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 667)
        MainWindow.setMinimumSize(QSize(860, 667))
        MainWindow.setMaximumSize(QSize(900, 667))
        icon = QIcon()
        icon.addFile(u":/images/res/worker.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionOpenPhoto = QAction(MainWindow)
        self.actionOpenPhoto.setObjectName(u"actionOpenPhoto")
        self.actionOpenVideo = QAction(MainWindow)
        self.actionOpenVideo.setObjectName(u"actionOpenVideo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.inputPhotoLabel = QLabel(self.centralwidget)
        self.inputPhotoLabel.setObjectName(u"inputPhotoLabel")
        self.inputPhotoLabel.setMinimumSize(QSize(416, 416))
        self.inputPhotoLabel.setMaximumSize(QSize(416, 416))
        self.inputPhotoLabel.setPixmap(QPixmap(u":/images/res/before_load_image.png"))
        self.inputPhotoLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.inputPhotoLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.outputPhotoLabel = QLabel(self.centralwidget)
        self.outputPhotoLabel.setObjectName(u"outputPhotoLabel")
        self.outputPhotoLabel.setMinimumSize(QSize(416, 416))
        self.outputPhotoLabel.setMaximumSize(QSize(416, 416))
        self.outputPhotoLabel.setPixmap(QPixmap(u":/images/res/before_load_image.png"))
        self.outputPhotoLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.outputPhotoLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mklBlasBtn = QRadioButton(self.groupBox)
        self.mklBlasBtn.setObjectName(u"mklBlasBtn")

        self.verticalLayout_2.addWidget(self.mklBlasBtn)

        self.openBlasBtn = QRadioButton(self.groupBox)
        self.openBlasBtn.setObjectName(u"openBlasBtn")

        self.verticalLayout_2.addWidget(self.openBlasBtn)

        self.blisBlasBtn = QRadioButton(self.groupBox)
        self.blisBlasBtn.setObjectName(u"blisBlasBtn")

        self.verticalLayout_2.addWidget(self.blisBlasBtn)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer = QSpacerItem(363, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 82, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.onCleanBtnClick = QPushButton(self.frame_3)
        self.onCleanBtnClick.setObjectName(u"onCleanBtnClick")

        self.verticalLayout.addWidget(self.onCleanBtnClick)

        self.onRecognitionBtnClick = QPushButton(self.frame_3)
        self.onRecognitionBtnClick.setObjectName(u"onRecognitionBtnClick")

        self.verticalLayout.addWidget(self.onRecognitionBtnClick)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.actionOpenPhoto)
        self.menu_2.addAction(self.actionOpenVideo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0432 \u043a\u0430\u0441\u043a\u0430\u0445", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.actionOpenPhoto.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e", None))
        self.actionOpenVideo.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.inputPhotoLabel.setText("")
        self.outputPhotoLabel.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 BLAS \u0438\u043c\u043f\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044e", None))
        self.mklBlasBtn.setText(QCoreApplication.translate("MainWindow", u"MKL", None))
        self.openBlasBtn.setText(QCoreApplication.translate("MainWindow", u"OpenBLAS", None))
        self.blisBlasBtn.setText(QCoreApplication.translate("MainWindow", u"BLIS", None))
        self.onCleanBtnClick.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.onRecognitionBtnClick.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

