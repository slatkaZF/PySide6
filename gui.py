## -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(455, 400)
        MainWindow.setStyleSheet(u"background-color: #FFDBE4;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 249, 316))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.city_input = QLineEdit(self.widget)
        self.city_input.setObjectName(u"city_input")
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(14)
        self.city_input.setFont(font)
        self.city_input.setStyleSheet(u"background-color: #FFFFFF; color: #7F3667; border: 6px solid #7F3667; border-radius: 8px;")

        self.verticalLayout.addWidget(self.city_input)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.weather_button = QPushButton(self.widget)
        self.weather_button.setObjectName(u"weather_button")
        font1 = QFont()
        font1.setFamilies([u"Terminal"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.weather_button.setFont(font1)
        self.weather_button.setStyleSheet(u"background-color:  #7F3667; color: #FFFFFF; border: 9px solid #A53E76; padding: 5px; border-radius: 5px;")

        self.verticalLayout.addWidget(self.weather_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.description_label = QLabel(self.widget)
        self.description_label.setObjectName(u"description_label")
        font2 = QFont()
        font2.setFamilies([u"Terminal"])
        font2.setBold(True)
        self.description_label.setFont(font2)
        self.description_label.setStyleSheet(u"color: #7F3667; font-size: 14px;")

        self.verticalLayout.addWidget(self.description_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.temperature_label = QLabel(self.widget)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setFont(font2)
        self.temperature_label.setStyleSheet(u"color: #7F3667; font-size: 14px;")

        self.verticalLayout.addWidget(self.temperature_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.humidity_label = QLabel(self.widget)
        self.humidity_label.setObjectName(u"humidity_label")
        self.humidity_label.setFont(font2)
        self.humidity_label.setStyleSheet(u"color: #7F3667; font-size: 14px;")

        self.verticalLayout_2.addWidget(self.humidity_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 455, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wetter-App", None))
        self.city_input.setText("")
        self.city_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stadt eingeben", None))
        self.weather_button.setText(QCoreApplication.translate("MainWindow", u"Wetter abrufen", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Wetter: -", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Temperatur: -", None))
        self.humidity_label.setText(QCoreApplication.translate("MainWindow", u"Luftfeuchtigkeit: -", None))
    # retranslateUi

