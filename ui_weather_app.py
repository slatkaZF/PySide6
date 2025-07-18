# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newgui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(u"WetterApp")
        MainWindow.resize(418, 196)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background: #F8CAD0;  /* Pale Pink */\n"
"    color: #2A2333;\n"
"    font-family: 'Segoe UI', Arial, sans-serif;\n"
"    font-size: 16px;\n"
"}\n"
" \n"
"QMainWindow {\n"
"    background: #F8CAD0;  /* Pale Pink */\n"
"}\n"
" \n"
"QLabel {\n"
"    color: #E4437D;  /* Deep Pink */\n"
"    font-weight: bold;\n"
"}\n"
" \n"
"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #F7A1B4,  /* Light Pink */\n"
"        stop:1 #F7B7C8   /* Carnation Pink */\n"
"    );\n"
"    color: #2A2333;\n"
"    border: 2px solid #F76A9A; /* Rose Pink */\n"
"    border-radius: 8px;\n"
"    padding: 1px 1px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #F79787,  /* Coral Pink */\n"
"        stop:1 #FFB8DF   /* Bubblegum Pink */\n"
"    );\n"
"    border: 2px solid #D87FC2; /* Fuchsia */\n"
"}\n"
"QPushButton:pressed {\n"
"    background"
                        ": qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #F79787,  /* Coral Pink */\n"
"        stop:1 #FFB8DF   /* Bubblegum Pink */\n"
"    );\n"
"}\n"
" \n"
"QLineEdit, QTextEdit {\n"
"    background: #FFF0F5; /* Very light pink */\n"
"    border: 2px solid #F7B6C3; /* Classic Pink */\n"
"    border-radius: 12px;\n"
"    padding: 2px;\n"
"    color: #2A2333;\n"
"    selection-background-color: #F76A9A; /* Rose Pink */\n"
"    font-size: 16px;\n"
"}\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 2px solid #E4437D; /* Deep Pink */\n"
"    background: #FFF0F5; /* Blush Pink */\n"
"}\n"
" \n"
"QComboBox {\n"
"    background: #E8A9CB; /* Lavender Pink */\n"
"    border: 2px solid #F7A3BC; /* Cherry Blossom */\n"
"    border-radius: 12px;\n"
"    padding: 6px 12px;\n"
"    color: #2A2333;\n"
"    font-size: 16px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: #F79CA9; /* Salmon Pink */\n"
"    border-radius: 0 12px 12px 0;\n"
"}\n"
"QComboBox QAbstractItemView "
                        "{\n"
"    background: #FFB8DF; /* Bubblegum Pink */\n"
"    color: #2A2333;\n"
"    selection-background-color: #D87FC2; /* Fuchsia */\n"
"}\n"
" \n"
"QTabWidget::pane {\n"
"    border: 2px solid #F7B2A1;\n"
"    background: #F8CAD0;\n"
"    border-radius: 14px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #F7B6C3;\n"
"    color: #2A2333;\n"
"    border-radius: 12px 12px 0 0;\n"
"    padding: 8px 24px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #F76A9A;\n"
"    color: #fff;\n"
"}\n"
" \n"
"QScrollBar:vertical {\n"
"    background: #F7A3BC;\n"
"    width: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #BE4E9C;\n"
"    border-radius: 8px;\n"
"    min-height: 40px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background: #F7A3BC;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #BE4E9C;\n"
"    borde"
                        "r-radius: 8px;\n"
"    min-width: 40px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"}\n"
" \n"
"/* Selection highlight */\n"
"QListView::item:selected, QTreeView::item:selected, QTableView::item:selected {\n"
"    background: #F75B7D; /* Watermelon */\n"
"    color: #fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.city_input = QLineEdit(self.centralwidget)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setGeometry(QRect(20, 20, 261, 31))
        self.weather_button = QPushButton(self.centralwidget)
        self.weather_button.setObjectName(u"weather_button")
        self.weather_button.setGeometry(QRect(290, 20, 91, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 101, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 131, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 150, 101, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 70, 1, 110))
        self.frame.setStyleSheet(u"QFrame  {\n"
"	background-color: #FFFFFF\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.temperature_label = QLabel(self.centralwidget)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setGeometry(QRect(190, 150, 231, 31))
        self.description_label = QLabel(self.centralwidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(190, 70, 231, 31))
        self.humidity_label = QLabel(self.centralwidget)
        self.humidity_label.setObjectName(u"humidity_label")
        self.humidity_label.setGeometry(QRect(190, 110, 221, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.city_input.setText("")
        self.city_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"z.B. Schweinfurt", None))
        self.weather_button.setText(QCoreApplication.translate("MainWindow", u"  Suchen", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wetter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Luftfeuchtigkeit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatur", None))
        self.temperature_label.setText("")
        self.description_label.setText("")
        self.humidity_label.setText("")
    # retranslateUi

