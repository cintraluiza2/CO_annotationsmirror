# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginqjJSFs.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
            
        Login.setWindowIcon(QIcon('resources/images/icons/icon_logo.svg'))
        
        Login.resize(488, 500)
        Login.setMinimumSize(QSize(0, 500))
        Login.setMaximumSize(QSize(488, 500))
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(Login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"resources/images/user_login.svg"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.txt_user = QLineEdit(self.frame_2)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy1)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"background-color: rgb(234, 238, 242);\n"
"border-radius: 8px;\n"
"padding-left: 1em;")

        self.verticalLayout.addWidget(self.txt_user)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.txt_password = QLineEdit(self.frame_3)
        self.txt_password.setObjectName(u"txt_password")
        sizePolicy1.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy1)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"background-color: rgb(234, 238, 242);\n"
"border-radius: 8px;\n"
"padding-left: 1em;")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.txt_password)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.butons_access = QPushButton(self.frame_4)
        self.butons_access.setObjectName(u"butons_access")
        self.butons_access.setMaximumSize(QSize(150, 30))
        self.butons_access.setFont(font)
        self.butons_access.setStyleSheet(u" QPushButton{\n"
"	background-color: rgb(66, 79, 91);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
" QPushButton::hover{\n"
"	background-color: rgb(114, 135, 157);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #89966E;\n"
"}")

        self.horizontalLayout.addWidget(self.butons_access)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"OCNewsAnnotator", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Digite seu email", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Senha", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha de 8 d\u00edgitos", None))
        self.butons_access.setText(QCoreApplication.translate("Login", u"Acessar", None))
    # retranslateUi

