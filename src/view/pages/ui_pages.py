# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_Pages(object):
    def setupUi(self, Pages):
        if not Pages.objectName():
            Pages.setObjectName(u"Pages")
        Pages.resize(1005, 902)
        self.table_news_page = QWidget()
        self.table_news_page.setObjectName(u"table_news_page")
        self.verticalLayout = QVBoxLayout(self.table_news_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_10 = QFrame(self.table_news_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.title_page_news = QLabel(self.frame_10)
        self.title_page_news.setObjectName(u"title_page_news")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.title_page_news.setFont(font)

        self.horizontalLayout_9.addWidget(self.title_page_news)

        self.button_sync = QPushButton(self.frame_10)
        self.button_sync.setObjectName(u"button_sync")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sync.sizePolicy().hasHeightForWidth())
        self.button_sync.setSizePolicy(sizePolicy)
        self.button_sync.setMinimumSize(QSize(150, 25))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.button_sync.setFont(font1)
        self.button_sync.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #1B4269;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 12px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #1B5A69;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #3E5369;\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_sync)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.frame_10)

        self.table_news = QTableView(self.table_news_page)
        self.table_news.setObjectName(u"table_news")
        font2 = QFont()
        font2.setFamilies([u"Roboto Light"])
        font2.setPointSize(12)
        self.table_news.setFont(font2)
        self.table_news.setFrameShape(QFrame.NoFrame)
        self.table_news.setLineWidth(1)
        self.table_news.setAutoScroll(True)
        self.table_news.setAutoScrollMargin(16)
        self.table_news.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_news.setDragEnabled(False)
        self.table_news.setAlternatingRowColors(True)
        self.table_news.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_news.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_news.setTextElideMode(Qt.ElideRight)
        self.table_news.setShowGrid(True)
        self.table_news.setGridStyle(Qt.CustomDashLine)
        self.table_news.setSortingEnabled(True)
        self.table_news.setWordWrap(False)
        self.table_news.horizontalHeader().setDefaultSectionSize(140)
        self.table_news.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_news)

        self.frame = QFrame(self.table_news_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(187, 0))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.button_note = QPushButton(self.frame)
        self.button_note.setObjectName(u"button_note")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_note.sizePolicy().hasHeightForWidth())
        self.button_note.setSizePolicy(sizePolicy1)
        self.button_note.setMinimumSize(QSize(187, 40))
        self.button_note.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(13)
        self.button_note.setFont(font3)
        self.button_note.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #77966D;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 20px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #6E9673;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #89966E;\n"
"}")

        self.horizontalLayout.addWidget(self.button_note)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        Pages.addWidget(self.table_news_page)
        self.classification_page = QWidget()
        self.classification_page.setObjectName(u"classification_page")
        self.classification_page.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.verticalLayout_3 = QVBoxLayout(self.classification_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_article = QLabel(self.classification_page)
        self.title_article.setObjectName(u"title_article")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_article.sizePolicy().hasHeightForWidth())
        self.title_article.setSizePolicy(sizePolicy2)
        self.title_article.setMinimumSize(QSize(600, 0))
        self.title_article.setSizeIncrement(QSize(0, 0))
        self.title_article.setBaseSize(QSize(0, 0))
        self.title_article.setFont(font1)
        self.title_article.setStyleSheet(u"background-color: #FFFFFF; \n"
"border-radius: 8px")
        self.title_article.setLineWidth(1)
        self.title_article.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title_article)

        self.frame_2 = QFrame(self.classification_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_publication = QLabel(self.frame_2)
        self.label_publication.setObjectName(u"label_publication")
        self.label_publication.setFont(font1)
        self.label_publication.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_publication)

        self.data_publication = QLabel(self.frame_2)
        self.data_publication.setObjectName(u"data_publication")
        self.data_publication.setFont(font1)
        self.data_publication.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-radius: 7px;")
        self.data_publication.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.data_publication)

        self.label_update = QLabel(self.frame_2)
        self.label_update.setObjectName(u"label_update")
        self.label_update.setFont(font1)
        self.label_update.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_update)

        self.data_update = QLabel(self.frame_2)
        self.data_update.setObjectName(u"data_update")
        self.data_update.setFont(font1)
        self.data_update.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-radius: 7px;")
        self.data_update.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.data_update)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.machine_class = QLabel(self.frame_2)
        self.machine_class.setObjectName(u"machine_class")
        self.machine_class.setFont(font1)
        self.machine_class.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-radius: 7px;")
        self.machine_class.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.machine_class)

        self.label_confidence = QLabel(self.frame_2)
        self.label_confidence.setObjectName(u"label_confidence")
        self.label_confidence.setFont(font1)
        self.label_confidence.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_confidence)

        self.confidence_machine = QLabel(self.frame_2)
        self.confidence_machine.setObjectName(u"confidence_machine")
        self.confidence_machine.setFont(font1)
        self.confidence_machine.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-radius: 7px;")
        self.confidence_machine.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.confidence_machine)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.classification_page)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.text_box_article = QTextBrowser(self.frame_4)
        self.text_box_article.setObjectName(u"text_box_article")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.text_box_article.sizePolicy().hasHeightForWidth())
        self.text_box_article.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        self.text_box_article.setFont(font4)
        self.text_box_article.setAutoFillBackground(False)
        self.text_box_article.setStyleSheet(u"QTextBrowser {\n"
"        background-color: #FFFFFF; \n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        font-family: 'Roboto';\n"
"        font-size: 20px; \n"
"        text-align: justify; \n"
"        word-spacing: 5px;\n"
"    }")

        self.horizontalLayout_14.addWidget(self.text_box_article)

        self.frame_infos = QFrame(self.frame_4)
        self.frame_infos.setObjectName(u"frame_infos")
        sizePolicy2.setHeightForWidth(self.frame_infos.sizePolicy().hasHeightForWidth())
        self.frame_infos.setSizePolicy(sizePolicy2)
        self.frame_infos.setMaximumSize(QSize(16777215, 16777215))
        self.frame_infos.setFont(font1)
        self.frame_infos.setStyleSheet(u"")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_infos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_class = QFrame(self.frame_infos)
        self.frame_class.setObjectName(u"frame_class")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_class.sizePolicy().hasHeightForWidth())
        self.frame_class.setSizePolicy(sizePolicy6)
        self.frame_class.setFont(font1)
        self.frame_class.setFrameShape(QFrame.StyledPanel)
        self.frame_class.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_class)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.frame_class)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border: none;")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.button_accept_news = QRadioButton(self.groupBox)
        self.button_accept_news.setObjectName(u"button_accept_news")
        sizePolicy.setHeightForWidth(self.button_accept_news.sizePolicy().hasHeightForWidth())
        self.button_accept_news.setSizePolicy(sizePolicy)
        self.button_accept_news.setFont(font1)

        self.horizontalLayout_15.addWidget(self.button_accept_news)

        self.button_reject_news = QRadioButton(self.groupBox)
        self.button_reject_news.setObjectName(u"button_reject_news")
        sizePolicy.setHeightForWidth(self.button_reject_news.sizePolicy().hasHeightForWidth())
        self.button_reject_news.setSizePolicy(sizePolicy)
        self.button_reject_news.setFont(font1)

        self.horizontalLayout_15.addWidget(self.button_reject_news)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.button_query = QCheckBox(self.frame_class)
        self.button_query.setObjectName(u"button_query")
        sizePolicy.setHeightForWidth(self.button_query.sizePolicy().hasHeightForWidth())
        self.button_query.setSizePolicy(sizePolicy)
        self.button_query.setFont(font1)

        self.horizontalLayout_3.addWidget(self.button_query)


        self.verticalLayout_2.addWidget(self.frame_class)

        self.frame_extraction = QFrame(self.frame_infos)
        self.frame_extraction.setObjectName(u"frame_extraction")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_extraction.sizePolicy().hasHeightForWidth())
        self.frame_extraction.setSizePolicy(sizePolicy7)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        self.frame_extraction.setFont(font5)
        self.frame_extraction.setFrameShape(QFrame.StyledPanel)
        self.frame_extraction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_extraction)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.frame_extraction)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy8)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_country = QLabel(self.frame_6)
        self.label_country.setObjectName(u"label_country")
        self.label_country.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_country)

        self.combo_country = QComboBox(self.frame_6)
        self.combo_country.setObjectName(u"combo_country")
        sizePolicy.setHeightForWidth(self.combo_country.sizePolicy().hasHeightForWidth())
        self.combo_country.setSizePolicy(sizePolicy)
        self.combo_country.setMinimumSize(QSize(150, 0))
        self.combo_country.setMaximumSize(QSize(150, 16777215))
        self.combo_country.setFont(font1)
        self.combo_country.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_4.addWidget(self.combo_country)

        self.label_region = QLabel(self.frame_6)
        self.label_region.setObjectName(u"label_region")
        self.label_region.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_region)

        self.combo_region = QComboBox(self.frame_6)
        self.combo_region.setObjectName(u"combo_region")
        sizePolicy.setHeightForWidth(self.combo_region.sizePolicy().hasHeightForWidth())
        self.combo_region.setSizePolicy(sizePolicy)
        self.combo_region.setMinimumSize(QSize(150, 0))
        self.combo_region.setMaximumSize(QSize(150, 16777215))
        self.combo_region.setFont(font1)
        self.combo_region.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_4.addWidget(self.combo_region)

        self.label_city = QLabel(self.frame_6)
        self.label_city.setObjectName(u"label_city")
        self.label_city.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_city)

        self.combo_city = QComboBox(self.frame_6)
        self.combo_city.setObjectName(u"combo_city")
        sizePolicy.setHeightForWidth(self.combo_city.sizePolicy().hasHeightForWidth())
        self.combo_city.setSizePolicy(sizePolicy)
        self.combo_city.setMinimumSize(QSize(150, 0))
        self.combo_city.setMaximumSize(QSize(150, 16777215))
        self.combo_city.setFont(font1)
        self.combo_city.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_4.addWidget(self.combo_city)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_extraction)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy6.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy6)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.latitude = QLineEdit(self.frame_8)
        self.latitude.setObjectName(u"latitude")
        sizePolicy4.setHeightForWidth(self.latitude.sizePolicy().hasHeightForWidth())
        self.latitude.setSizePolicy(sizePolicy4)
        self.latitude.setMinimumSize(QSize(150, 0))
        self.latitude.setMaximumSize(QSize(280, 16777215))
        self.latitude.setFont(font1)
        self.latitude.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_5.addWidget(self.latitude)

        self.button_geo_city = QPushButton(self.frame_8)
        self.button_geo_city.setObjectName(u"button_geo_city")
        sizePolicy7.setHeightForWidth(self.button_geo_city.sizePolicy().hasHeightForWidth())
        self.button_geo_city.setSizePolicy(sizePolicy7)
        self.button_geo_city.setMinimumSize(QSize(0, 0))
        self.button_geo_city.setMaximumSize(QSize(80, 16777215))
        self.button_geo_city.setFont(font1)
        self.button_geo_city.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);")

        self.horizontalLayout_5.addWidget(self.button_geo_city)

        self.button_maps = QPushButton(self.frame_8)
        self.button_maps.setObjectName(u"button_maps")
        self.button_maps.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.button_maps.sizePolicy().hasHeightForWidth())
        self.button_maps.setSizePolicy(sizePolicy7)
        self.button_maps.setMinimumSize(QSize(0, 0))
        self.button_maps.setMaximumSize(QSize(80, 16777215))
        self.button_maps.setFont(font1)
        self.button_maps.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);")

        self.horizontalLayout_5.addWidget(self.button_maps)

        self.button_pesquisar = QPushButton(self.frame_8)
        self.button_pesquisar.setObjectName(u"button_pesquisar")
        self.button_pesquisar.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.button_pesquisar.sizePolicy().hasHeightForWidth())
        self.button_pesquisar.setSizePolicy(sizePolicy7)
        self.button_pesquisar.setMinimumSize(QSize(0, 0))
        self.button_pesquisar.setMaximumSize(QSize(80, 16777215))
        self.button_pesquisar.setFont(font1)
        self.button_pesquisar.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);")

        self.horizontalLayout_5.addWidget(self.button_pesquisar)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_extraction)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_date_event = QLabel(self.frame_9)
        self.label_date_event.setObjectName(u"label_date_event")
        sizePolicy8.setHeightForWidth(self.label_date_event.sizePolicy().hasHeightForWidth())
        self.label_date_event.setSizePolicy(sizePolicy8)
        self.label_date_event.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_date_event)

        self.input_date_event = QDateEdit(self.frame_9)
        self.input_date_event.setObjectName(u"input_date_event")
        sizePolicy.setHeightForWidth(self.input_date_event.sizePolicy().hasHeightForWidth())
        self.input_date_event.setSizePolicy(sizePolicy)
        self.input_date_event.setFont(font1)
        self.input_date_event.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_6.addWidget(self.input_date_event)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_conflict = QLabel(self.frame_9)
        self.label_conflict.setObjectName(u"label_conflict")
        sizePolicy8.setHeightForWidth(self.label_conflict.sizePolicy().hasHeightForWidth())
        self.label_conflict.setSizePolicy(sizePolicy8)
        self.label_conflict.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_conflict)

        self.check_conflict = QCheckBox(self.frame_9)
        self.check_conflict.setObjectName(u"check_conflict")
        self.check_conflict.setEnabled(True)
        sizePolicy.setHeightForWidth(self.check_conflict.sizePolicy().hasHeightForWidth())
        self.check_conflict.setSizePolicy(sizePolicy)
        self.check_conflict.setFont(font1)

        self.horizontalLayout_6.addWidget(self.check_conflict)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_deaths = QLabel(self.frame_9)
        self.label_deaths.setObjectName(u"label_deaths")
        sizePolicy8.setHeightForWidth(self.label_deaths.sizePolicy().hasHeightForWidth())
        self.label_deaths.setSizePolicy(sizePolicy8)
        self.label_deaths.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_deaths)

        self.input_deaths = QSpinBox(self.frame_9)
        self.input_deaths.setObjectName(u"input_deaths")
        sizePolicy.setHeightForWidth(self.input_deaths.sizePolicy().hasHeightForWidth())
        self.input_deaths.setSizePolicy(sizePolicy)
        self.input_deaths.setFont(font1)
        self.input_deaths.setStyleSheet(u"background-color: #FFFFFF; ")
        self.input_deaths.setMaximum(1000)

        self.horizontalLayout_6.addWidget(self.input_deaths)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.groupBox_narcotic_1 = QGroupBox(self.frame_extraction)
        self.groupBox_narcotic_1.setObjectName(u"groupBox_narcotic_1")
        sizePolicy6.setHeightForWidth(self.groupBox_narcotic_1.sizePolicy().hasHeightForWidth())
        self.groupBox_narcotic_1.setSizePolicy(sizePolicy6)
        self.groupBox_narcotic_1.setStyleSheet(u"")
        self.groupBox_narcotic_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_narcotic_1.setFlat(True)
        self.groupBox_narcotic_1.setCheckable(True)
        self.groupBox_narcotic_1.setChecked(False)
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_narcotic_1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_type_narcotic = QLabel(self.groupBox_narcotic_1)
        self.label_type_narcotic.setObjectName(u"label_type_narcotic")
        sizePolicy8.setHeightForWidth(self.label_type_narcotic.sizePolicy().hasHeightForWidth())
        self.label_type_narcotic.setSizePolicy(sizePolicy8)
        self.label_type_narcotic.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_type_narcotic)

        self.combo_narcotic_1 = QComboBox(self.groupBox_narcotic_1)
        self.combo_narcotic_1.setObjectName(u"combo_narcotic_1")
        self.combo_narcotic_1.setFont(font1)
        self.combo_narcotic_1.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_18.addWidget(self.combo_narcotic_1)

        self.label_qty_narcotic = QLabel(self.groupBox_narcotic_1)
        self.label_qty_narcotic.setObjectName(u"label_qty_narcotic")
        sizePolicy8.setHeightForWidth(self.label_qty_narcotic.sizePolicy().hasHeightForWidth())
        self.label_qty_narcotic.setSizePolicy(sizePolicy8)
        self.label_qty_narcotic.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_qty_narcotic)

        self.input_qty_narcotic_1 = QSpinBox(self.groupBox_narcotic_1)
        self.input_qty_narcotic_1.setObjectName(u"input_qty_narcotic_1")
        self.input_qty_narcotic_1.setFont(font1)
        self.input_qty_narcotic_1.setStyleSheet(u"background-color: #FFFFFF; ")
        self.input_qty_narcotic_1.setMaximum(100000)

        self.horizontalLayout_18.addWidget(self.input_qty_narcotic_1)


        self.verticalLayout_4.addWidget(self.groupBox_narcotic_1)

        self.groupBox_narcotic_2 = QGroupBox(self.frame_extraction)
        self.groupBox_narcotic_2.setObjectName(u"groupBox_narcotic_2")
        sizePolicy6.setHeightForWidth(self.groupBox_narcotic_2.sizePolicy().hasHeightForWidth())
        self.groupBox_narcotic_2.setSizePolicy(sizePolicy6)
        self.groupBox_narcotic_2.setFlat(True)
        self.groupBox_narcotic_2.setCheckable(True)
        self.groupBox_narcotic_2.setChecked(False)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_narcotic_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_20 = QLabel(self.groupBox_narcotic_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy8.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy8)
        self.label_20.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_20)

        self.combo_narcotic_2 = QComboBox(self.groupBox_narcotic_2)
        self.combo_narcotic_2.setObjectName(u"combo_narcotic_2")
        self.combo_narcotic_2.setFont(font1)
        self.combo_narcotic_2.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_7.addWidget(self.combo_narcotic_2)

        self.label_21 = QLabel(self.groupBox_narcotic_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy8.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy8)
        self.label_21.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_21)

        self.input_qty_narcotic_2 = QSpinBox(self.groupBox_narcotic_2)
        self.input_qty_narcotic_2.setObjectName(u"input_qty_narcotic_2")
        self.input_qty_narcotic_2.setFont(font1)
        self.input_qty_narcotic_2.setStyleSheet(u"background-color: #FFFFFF; ")
        self.input_qty_narcotic_2.setMaximum(100000)

        self.horizontalLayout_7.addWidget(self.input_qty_narcotic_2)


        self.verticalLayout_4.addWidget(self.groupBox_narcotic_2)

        self.groupBox_narcotic_3 = QGroupBox(self.frame_extraction)
        self.groupBox_narcotic_3.setObjectName(u"groupBox_narcotic_3")
        sizePolicy6.setHeightForWidth(self.groupBox_narcotic_3.sizePolicy().hasHeightForWidth())
        self.groupBox_narcotic_3.setSizePolicy(sizePolicy6)
        self.groupBox_narcotic_3.setFlat(True)
        self.groupBox_narcotic_3.setCheckable(True)
        self.groupBox_narcotic_3.setChecked(False)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_narcotic_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_22 = QLabel(self.groupBox_narcotic_3)
        self.label_22.setObjectName(u"label_22")
        sizePolicy8.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy8)
        self.label_22.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.combo_narcotic_3 = QComboBox(self.groupBox_narcotic_3)
        self.combo_narcotic_3.setObjectName(u"combo_narcotic_3")
        self.combo_narcotic_3.setFont(font1)
        self.combo_narcotic_3.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_8.addWidget(self.combo_narcotic_3)

        self.label_23 = QLabel(self.groupBox_narcotic_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy8.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy8)
        self.label_23.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_23)

        self.input_qty_narcotic_3 = QSpinBox(self.groupBox_narcotic_3)
        self.input_qty_narcotic_3.setObjectName(u"input_qty_narcotic_3")
        self.input_qty_narcotic_3.setFont(font1)
        self.input_qty_narcotic_3.setStyleSheet(u"background-color: #FFFFFF; ")
        self.input_qty_narcotic_3.setMaximum(100000)

        self.horizontalLayout_8.addWidget(self.input_qty_narcotic_3)


        self.verticalLayout_4.addWidget(self.groupBox_narcotic_3)

        self.frame_5 = QFrame(self.frame_extraction)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_10)

        self.input_weapons = QLineEdit(self.frame_5)
        self.input_weapons.setObjectName(u"input_weapons")
        sizePolicy2.setHeightForWidth(self.input_weapons.sizePolicy().hasHeightForWidth())
        self.input_weapons.setSizePolicy(sizePolicy2)
        self.input_weapons.setMaximumSize(QSize(100, 16777215))
        self.input_weapons.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.input_weapons)

        self.btt_add_weapons = QPushButton(self.frame_5)
        self.btt_add_weapons.setObjectName(u"btt_add_weapons")
        sizePolicy.setHeightForWidth(self.btt_add_weapons.sizePolicy().hasHeightForWidth())
        self.btt_add_weapons.setSizePolicy(sizePolicy)
        self.btt_add_weapons.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);")

        self.horizontalLayout_16.addWidget(self.btt_add_weapons)

        self.btt_rmv_weapons = QPushButton(self.frame_5)
        self.btt_rmv_weapons.setObjectName(u"btt_rmv_weapons")
        sizePolicy.setHeightForWidth(self.btt_rmv_weapons.sizePolicy().hasHeightForWidth())
        self.btt_rmv_weapons.setSizePolicy(sizePolicy)
        self.btt_rmv_weapons.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);")

        self.horizontalLayout_16.addWidget(self.btt_rmv_weapons)

        self.list_weapons = QListWidget(self.frame_5)
        self.list_weapons.setObjectName(u"list_weapons")
        sizePolicy8.setHeightForWidth(self.list_weapons.sizePolicy().hasHeightForWidth())
        self.list_weapons.setSizePolicy(sizePolicy8)
        self.list_weapons.setMaximumSize(QSize(150, 200))
        self.list_weapons.setFont(font1)
        self.list_weapons.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_weapons.setProperty("isWrapping", False)
        self.list_weapons.setResizeMode(QListView.Fixed)
        self.list_weapons.setSpacing(2)
        self.list_weapons.setSortingEnabled(True)

        self.horizontalLayout_16.addWidget(self.list_weapons)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_extraction)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.name_actor_1 = QLineEdit(self.frame_13)
        self.name_actor_1.setObjectName(u"name_actor_1")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.name_actor_1.sizePolicy().hasHeightForWidth())
        self.name_actor_1.setSizePolicy(sizePolicy9)
        self.name_actor_1.setFont(font1)
        self.name_actor_1.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_10.addWidget(self.name_actor_1)


        self.horizontalLayout_17.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.name_actor_2 = QLineEdit(self.frame_14)
        self.name_actor_2.setObjectName(u"name_actor_2")
        self.name_actor_2.setFont(font1)
        self.name_actor_2.setStyleSheet(u"background-color: #FFFFFF; ")
        self.name_actor_2.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.name_actor_2)


        self.horizontalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy6.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy6)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_type_relation = QLabel(self.frame_15)
        self.label_type_relation.setObjectName(u"label_type_relation")
        sizePolicy3.setHeightForWidth(self.label_type_relation.sizePolicy().hasHeightForWidth())
        self.label_type_relation.setSizePolicy(sizePolicy3)
        self.label_type_relation.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_type_relation)

        self.combo_type_relation = QComboBox(self.frame_15)
        self.combo_type_relation.setObjectName(u"combo_type_relation")
        sizePolicy3.setHeightForWidth(self.combo_type_relation.sizePolicy().hasHeightForWidth())
        self.combo_type_relation.setSizePolicy(sizePolicy3)
        self.combo_type_relation.setFont(font1)
        self.combo_type_relation.setStyleSheet(u"background-color: #FFFFFF; ")

        self.horizontalLayout_12.addWidget(self.combo_type_relation)


        self.horizontalLayout_17.addWidget(self.frame_15)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_extraction)


        self.horizontalLayout_14.addWidget(self.frame_infos)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.classification_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.button_back = QPushButton(self.frame_3)
        self.button_back.setObjectName(u"button_back")
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMinimumSize(QSize(150, 40))
        self.button_back.setFont(font3)
        self.button_back.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #1B4269;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 20px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #1B5A69;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #3E5369;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./resources/images/icons/arrow_return.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_back.setIcon(icon)
        self.button_back.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.button_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.button_finish = QPushButton(self.frame_3)
        self.button_finish.setObjectName(u"button_finish")
        self.button_finish.setMinimumSize(QSize(200, 40))
        self.button_finish.setFont(font3)
        self.button_finish.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #77966D;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 20px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #6E9673;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #89966E;\n"
"}")

        self.horizontalLayout_13.addWidget(self.button_finish)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.button_cancel = QPushButton(self.frame_3)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMinimumSize(QSize(200, 40))
        self.button_cancel.setFont(font3)
        self.button_cancel.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #941C2F;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 20px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #8B1A2B;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #470E16;\n"
"}")

        self.horizontalLayout_13.addWidget(self.button_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.button_next = QPushButton(self.frame_3)
        self.button_next.setObjectName(u"button_next")
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        self.button_next.setMinimumSize(QSize(150, 40))
        self.button_next.setFont(font3)
        self.button_next.setStyleSheet(u"QPushButton{\n"
"            color: #FFFFFF;\n"
"            background-color: #1B4269;\n"
"            text-align: center;\n"
"            border: solid;\n"
"            border-radius: 20px;\n"
"}\n"
"\n"
" QPushButton::hover{\n"
"            background-color: #1B5A69;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"            background-color: #3E5369;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./resources/images/icons/arrow_next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_next.setIcon(icon1)
        self.button_next.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.button_next)


        self.verticalLayout_3.addWidget(self.frame_3)

        Pages.addWidget(self.classification_page)

        self.retranslateUi(Pages)

        Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Pages)
    # setupUi

    def retranslateUi(self, Pages):
        Pages.setWindowTitle(QCoreApplication.translate("Pages", u"StackedWidget", None))
        self.title_page_news.setText(QCoreApplication.translate("Pages", u"Not\u00edcias", None))
        self.button_sync.setText(QCoreApplication.translate("Pages", u"Sincronizar Tabela", None))
        self.label_2.setText("")
        self.button_note.setText(QCoreApplication.translate("Pages", u"Anotar", None))
        self.label.setText("")
        self.title_article.setText(QCoreApplication.translate("Pages", u"<html><head/><body><p><span style=\" font-size:12pt;\">Titulo</span></p></body></html>", None))
        self.label_publication.setText(QCoreApplication.translate("Pages", u"Publica\u00e7\u00e3o:", None))
        self.data_publication.setText(QCoreApplication.translate("Pages", u"00-00-0000", None))
        self.label_update.setText(QCoreApplication.translate("Pages", u"Atualiza\u00e7\u00e3o:", None))
        self.data_update.setText(QCoreApplication.translate("Pages", u"00-00-0000", None))
        self.label_6.setText(QCoreApplication.translate("Pages", u"Classe de Maquina:", None))
        self.machine_class.setText(QCoreApplication.translate("Pages", u"SClasse", None))
        self.label_confidence.setText(QCoreApplication.translate("Pages", u"Confian\u00e7a:", None))
        self.confidence_machine.setText(QCoreApplication.translate("Pages", u"00.00%", None))
        self.text_box_article.setHtml(QCoreApplication.translate("Pages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:20px; font-weight:400; font-style:normal; word-spacing:5px;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans','Arial','sans-serif'; font-size:12pt; font-weight:700; color:#000000; background-color:#ffffff; word-spacing:5px;\">Lorem Ipsum</span><span style=\" font-family:'Open Sans','Arial','sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff; word-spacing:5px;\">\u00a0is simply dummy text of the printing and typesetting"
                        " industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans','Arial','sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff; word-spacing:5px;\">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney Co"
                        "llege in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of &quot;de Finibus Bonorum et Malorum&quot; (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, &quot;Lorem ipsum dolor sit amet..&quot;, comes from a line in section 1.10.32.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Arial','sans-serif'; font-size:12pt; color:#000000; background-color:#ffffff; word-spacing:5px;\">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from &quot;de Fini"
                        "bus Bonorum et Malorum&quot; by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham</span></p></body></html>", None))
        self.groupBox.setTitle("")
        self.button_accept_news.setText(QCoreApplication.translate("Pages", u"Relevante", None))
        self.button_reject_news.setText(QCoreApplication.translate("Pages", u"Irrelevante", None))
        self.button_query.setText(QCoreApplication.translate("Pages", u"D\u00favida", None))
        self.label_country.setText(QCoreApplication.translate("Pages", u"Pa\u00eds", None))
        self.label_region.setText(QCoreApplication.translate("Pages", u"Regi\u00e3o", None))
        self.label_city.setText(QCoreApplication.translate("Pages", u"Munic\u00edpio", None))
        self.latitude.setInputMask("")
        self.latitude.setText("")
        self.latitude.setPlaceholderText(QCoreApplication.translate("Pages", u"Latitude, Longitude", None))
        self.button_geo_city.setText(QCoreApplication.translate("Pages", u"Padr\u00e3o", None))
        self.button_maps.setText(QCoreApplication.translate("Pages", u"Maps", None))
        self.button_pesquisar.setText(QCoreApplication.translate("Pages", u"Pesquisar", None))
        self.label_date_event.setText(QCoreApplication.translate("Pages", u"Data", None))
        self.label_conflict.setText(QCoreApplication.translate("Pages", u"Houve Conflito", None))
        self.check_conflict.setText(QCoreApplication.translate("Pages", u"Sim", None))
        self.label_deaths.setText(QCoreApplication.translate("Pages", u"Mortes", None))
        self.groupBox_narcotic_1.setTitle("")
        self.label_type_narcotic.setText(QCoreApplication.translate("Pages", u"Tipo de Droga", None))
        self.label_qty_narcotic.setText(QCoreApplication.translate("Pages", u"Quantidade", None))
        self.input_qty_narcotic_1.setSuffix(QCoreApplication.translate("Pages", u"g", None))
        self.groupBox_narcotic_2.setTitle("")
        self.label_20.setText(QCoreApplication.translate("Pages", u"Tipo de Droga", None))
        self.label_21.setText(QCoreApplication.translate("Pages", u"Quantidade", None))
        self.input_qty_narcotic_2.setSuffix(QCoreApplication.translate("Pages", u"g", None))
        self.groupBox_narcotic_3.setTitle("")
        self.label_22.setText(QCoreApplication.translate("Pages", u"Tipo de Droga", None))
        self.label_23.setText(QCoreApplication.translate("Pages", u"Quantidade", None))
        self.input_qty_narcotic_3.setSuffix(QCoreApplication.translate("Pages", u"g", None))
        self.label_10.setText(QCoreApplication.translate("Pages", u"Armas Aprendidas:", None))
        self.input_weapons.setText("")
        self.btt_add_weapons.setText(QCoreApplication.translate("Pages", u"Adicionar", None))
        self.btt_rmv_weapons.setText(QCoreApplication.translate("Pages", u"Remover", None))
        self.name_actor_1.setPlaceholderText(QCoreApplication.translate("Pages", u"Primeiro Ator", None))
        self.name_actor_2.setPlaceholderText(QCoreApplication.translate("Pages", u"Segundo Ator", None))
        self.label_type_relation.setText(QCoreApplication.translate("Pages", u"Rela\u00e7\u00e3o Entre Atores", None))
        self.button_back.setText("")
        self.button_finish.setText(QCoreApplication.translate("Pages", u"Finalizar", None))
        self.button_cancel.setText(QCoreApplication.translate("Pages", u"Cancelar", None))
        self.button_next.setText("")
        
        expr_regu = QRegularExpressionValidator(QRegularExpression(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"))
        
        self.latitude.setValidator(expr_regu)
    # retranslateUi

