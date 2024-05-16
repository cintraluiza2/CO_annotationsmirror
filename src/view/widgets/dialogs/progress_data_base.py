# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py_progress_data_base.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_py_progress_data(object):
    def setupUi(self, py_progress_data):
        if not py_progress_data.objectName():
            py_progress_data.setObjectName(u"py_progress_data")
        py_progress_data.resize(449, 300)
        icon = QIcon()
        icon.addFile(u"./resources/images/icons/attention.svg", QSize(), QIcon.Normal, QIcon.Off)
        py_progress_data.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(py_progress_data)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(py_progress_data)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"./resources/images/logo.svg"))
        self.label_2.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(136, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(py_progress_data)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.frame)

        self.progress_data_base = QProgressBar(py_progress_data)
        self.progress_data_base.setObjectName(u"progress_data_base")
        self.progress_data_base.setValue(24)
        self.progress_data_base.setTextVisible(True)
        self.progress_data_base.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.progress_data_base)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(py_progress_data)

        QMetaObject.connectSlotsByName(py_progress_data)
    # setupUi

    def retranslateUi(self, py_progress_data):
        py_progress_data.setWindowTitle(QCoreApplication.translate("py_progress_data", u"Tela de Carregamento", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("py_progress_data", u"Conectando ao Banco de Dados...", None))
    # retranslateUi

    def set_progress(self, value):
        if value == -1:
            self.label.setText("ERRO DE CONEXÃO!\nTENTE NOVAMENTE MAIS TARDE")
            self.progress_data_base.setValue(0)
            
        elif value == -2:
            self.label.setText("ERRO NO CARREGAMENTO DOS DADOS!\nENTRE EM CONTATO COM OS DESENVOLVEDORES")
            self.progress_data_base.setValue(0)
            
        elif value == 50:
            self.label.setText("Carregando os Dados...")
            
        self.progress_data_base.setValue(value)
