# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainQQBahb.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 730)
        MainWindow.setMinimumSize(QSize(964, 730))
        MainWindow.setMaximumSize(QSize(964, 730))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(940, 730))
        self.styleSheet.setMaximumSize(QSize(16777215, 730))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: #333;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #3"
                        "33;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #4169E1;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #4169E1;\n"
"}\n"
"#topLogo {\n"
"	background-color: #4169E1;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt "
                        "\"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px sol"
                        "id #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #4169E1;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #4169E1;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: #e75f2c\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extr"
                        "aLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #4169E1;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #4169E1;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: #e75f2c;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////"
                        "////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #4169E1;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #4169E1; }\n"
"#themeSettingsTopDetail { background-color: #4169E1; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #4169E1 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSett"
                        "ings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #4169E1;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: #e75f2c;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #e75f2c;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	backgrou"
                        "nd-color: #4169E1;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #4169E1;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #4169E1;\n"
"	background-color: #4169E1;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #4169E1;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #4169E1;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #4169E1;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* //////////////////////////"
                        "///////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #4169E1;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #4169E1;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #e75f2c;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::ad"
                        "d-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: #4169E1;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #4169E1;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #e75f2c;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-l"
                        "ine:vertical {\n"
"     border: none;\n"
"    background: none;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: none;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: #4169E1;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #4169E1;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #4169E1;\n"
"}\n"
"QCheckBox::indicator"
                        ":hover {\n"
"    border: 3px solid #4169E1;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #4169E1;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #4169E1;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid #4169E1;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #4169E1;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #4169E1;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"Q"
                        "ComboBox:hover{\n"
"	border: 2px solid #4169E1;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #4169E1;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #4169E1;\n"
"	padding: 10px;\n"
"	selection-background-color: #4169E1;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #4169E1;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #4169E1;\n"
"}\n"
"QSlider::handle:horizontal {"
                        "\n"
"    background-color: #e75f2c;\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #4169E1;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #4169E1;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #e75f2c;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
                        "\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #4169E1;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: #e75f2c;\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #4169E1;\n"
"	border-radius: 5px;	\n"
"	background-color: #4169E1;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #4169E1;\n"
"	border: 2px solid #4169E1;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #e75f2c;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 7, 35, 35))
        self.topLogo.setMinimumSize(QSize(35, 35))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/microscope02.png);\n"
"                           background-position: centered;\n"
"                           background-repeat: no-repeat;\n"
"                       ")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.toggleButton.setFont(font4)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font4)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_details = QPushButton(self.topMenu)
        self.btn_details.setObjectName(u"btn_details")
        sizePolicy.setHeightForWidth(self.btn_details.sizePolicy().hasHeightForWidth())
        self.btn_details.setSizePolicy(sizePolicy)
        self.btn_details.setMinimumSize(QSize(0, 45))
        self.btn_details.setFont(font4)
        self.btn_details.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_details.setLayoutDirection(Qt.LeftToRight)
        self.btn_details.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_details)

        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setMinimumSize(QSize(60, 45))
        self.btn_history.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-history.png);")

        self.verticalLayout_8.addWidget(self.btn_history)

        self.btn_settings = QPushButton(self.topMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font4)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font4)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font4)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font4)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.titleRightInfo.setFont(font5)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font6)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font7 = QFont()
        font7.setFamilies([u"\u96b6\u4e66"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        self.stackedWidget.setFont(font7)
        self.stackedWidget.setStyleSheet(u"background: transparent")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color:#FFFFFF")
        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, -10, 351, 491))
        self.label_2.setStyleSheet(u"image:url(:/images/images/images/solar_panel06.png)")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 260, 311, 371))
        self.label_3.setStyleSheet(u"image:url(:/images/images/images/vhx.png)")
        self.pushButton_2 = QPushButton(self.page_home)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 460, 91, 41))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        self.pushButton_2.setFont(font8)
        self.pushButton_2.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-cursor-move.png);\n"
"background-origin: content;\n"
"background-position: left center;\n"
"padding-top: 8px;\n"
"padding-left:10px;\n"
"background-repeat: no-repeat;\n"
"background-color: #4169E1;\n"
"text-align:bottom;\n"
"padding-bottom:10px")
        self.label_4 = QLabel(self.page_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-20, 20, 461, 181))
        self.label_4.setStyleSheet(u"image:url(:/images/images/images/companyLogo.png)")
        self.startButton = QPushButton(self.page_home)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(580, 460, 91, 41))
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(12)
        self.startButton.setFont(font9)
        self.startButton.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-media-play.png);\n"
"background-origin: content;\n"
"background-position: left center;\n"
"padding-top: 8px;\n"
"padding-left:10px;\n"
"background-repeat: no-repeat;\n"
"background-color: #4169E1;\n"
"text-align:bottom;\n"
"padding-bottom:10px")
        self.pushButton_4 = QPushButton(self.page_home)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(710, 460, 91, 41))
        self.pushButton_4.setFont(font9)
        self.pushButton_4.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-media-stop.png);\n"
"background-origin: content;\n"
"background-position: left center;\n"
"padding-top: 8px;\n"
"padding-left:10px;\n"
"background-repeat: no-repeat;\n"
"background-color: #4169E1;\n"
"text-align:bottom;\n"
"padding-bottom:10px")
        self.label_5 = QLabel(self.page_home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 560, 351, 31))
        font10 = QFont()
        font10.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font10.setPointSize(11)
        self.label_5.setFont(font10)
        self.label_5.setStyleSheet(u"background-color: 		#1E90FF;\n"
"text-align:center;\n"
"padding-left:10px\n"
"")
        self.stackedWidget.addWidget(self.page_home)
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.startButton.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.stackedWidget.addWidget(self.page_history)
        self.page_details = QWidget()
        self.page_details.setObjectName(u"page_details")
        self.startDetectBtn = QPushButton(self.page_details)
        self.startDetectBtn.setObjectName(u"startDetectBtn")
        self.startDetectBtn.setGeometry(QRect(200, 60, 141, 41))
        self.startDetectBtn.setFont(font8)
        self.startDetectBtn.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-media-play.png);\n"
                                          "                               background-origin: content;\n"
                                          "                               background-position: left center;\n"
                                          "                               padding-top: 8px;\n"
                                          "                               padding-left:10px;\n"
                                          "                               background-repeat: no-repeat;\n"
                                          "                               background-color: #4169E1;\n"
                                          "                               text-align:bottom;\n"
                                          "                               padding-bottom:10px\n"
                                          "                           ")
        self.setWorkSpaceBtn = QPushButton(self.page_details)
        self.setWorkSpaceBtn.setObjectName(u"setWorkSpaceBtn")
        self.setWorkSpaceBtn.setGeometry(QRect(20, 10, 131, 41))
        self.setWorkSpaceBtn.setFont(font8)
        self.setWorkSpaceBtn.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-save.png);\n"
                                           "background-origin: content;\n"
                                           "background-position: left center;\n"
                                           "padding-top: 8px;\n"
                                           "padding-left:10px;\n"
                                           "background-repeat: no-repeat;\n"
                                           "background-color: #4169E1;\n"
                                           "text-align:bottom;\n"
                                           "padding-bottom:10px")
        self.logger02 = QTableWidget(self.page_details)
        if (self.logger02.columnCount() < 2):
            self.logger02.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.logger02.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.logger02.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.logger02.rowCount() < 1):
            self.logger02.setRowCount(1)
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font11);
        self.logger02.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.logger02.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.logger02.setItem(0, 1, __qtablewidgetitem4)
        self.logger02.setObjectName(u"logger02")
        self.logger02.setGeometry(QRect(370, 190, 481, 431))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logger02.sizePolicy().hasHeightForWidth())
        self.logger02.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(100, 149, 237, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.logger02.setPalette(palette)
        self.logger02.setFont(font)
        self.logger02.setStyleSheet(u"background-color: 	#6495ED;\n"
"color:#ffffff")
        self.logger02.setFrameShape(QFrame.NoFrame)
        self.logger02.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logger02.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.logger02.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.logger02.setSelectionMode(QAbstractItemView.SingleSelection)
        self.logger02.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.logger02.setShowGrid(True)
        self.logger02.setGridStyle(Qt.SolidLine)
        self.logger02.setSortingEnabled(False)
        self.logger02.horizontalHeader().setVisible(False)
        self.logger02.horizontalHeader().setCascadingSectionResizes(False)
        self.logger02.horizontalHeader().setDefaultSectionSize(99)
        self.logger02.horizontalHeader().setHighlightSections(True)
        self.logger02.horizontalHeader().setStretchLastSection(True)
        self.logger02.verticalHeader().setVisible(False)
        self.logger02.verticalHeader().setCascadingSectionResizes(False)
        self.logger02.verticalHeader().setHighlightSections(False)
        self.logger02.verticalHeader().setStretchLastSection(False)
        self.analyseBtn = QPushButton(self.page_details)
        self.analyseBtn.setObjectName(u"analyseBtn")
        self.analyseBtn.setGeometry(QRect(20, 60, 131, 41))
        self.analyseBtn.setFont(font8)
        self.analyseBtn.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-align-center.png);\n"
"background-origin: content;\n"
"background-position: left center;\n"
"padding-top: 8px;\n"
"padding-left:10px;\n"
"background-repeat: no-repeat;\n"
"background-color: #4169E1;\n"
"text-align:bottom;\n"
"padding-bottom:10px")
        self.widthHeightTable02 = QTableWidget(self.page_details)
        if (self.widthHeightTable02.columnCount() < 4):
            self.widthHeightTable02.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.widthHeightTable02.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.widthHeightTable02.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.widthHeightTable02.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.widthHeightTable02.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        if (self.widthHeightTable02.rowCount() < 1):
            self.widthHeightTable02.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font11);
        self.widthHeightTable02.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.widthHeightTable02.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.widthHeightTable02.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.widthHeightTable02.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.widthHeightTable02.setItem(0, 3, __qtablewidgetitem13)
        self.widthHeightTable02.setObjectName(u"widthHeightTable02")
        self.widthHeightTable02.setGeometry(QRect(20, 120, 301, 491))
        sizePolicy3.setHeightForWidth(self.widthHeightTable02.sizePolicy().hasHeightForWidth())
        self.widthHeightTable02.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.widthHeightTable02.setPalette(palette1)
        self.widthHeightTable02.setFont(font)
        self.widthHeightTable02.setStyleSheet(u"background-color: #6495ED;\n"
"color:#ffffff")
        self.widthHeightTable02.setFrameShape(QFrame.NoFrame)
        self.widthHeightTable02.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.widthHeightTable02.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.widthHeightTable02.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.widthHeightTable02.setSelectionMode(QAbstractItemView.SingleSelection)
        self.widthHeightTable02.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.widthHeightTable02.setShowGrid(True)
        self.widthHeightTable02.setGridStyle(Qt.SolidLine)
        self.widthHeightTable02.setSortingEnabled(False)
        self.widthHeightTable02.horizontalHeader().setVisible(False)
        self.widthHeightTable02.horizontalHeader().setCascadingSectionResizes(False)
        self.widthHeightTable02.horizontalHeader().setDefaultSectionSize(65)
        self.widthHeightTable02.horizontalHeader().setHighlightSections(True)
        self.widthHeightTable02.horizontalHeader().setStretchLastSection(True)
        self.widthHeightTable02.verticalHeader().setVisible(False)
        self.widthHeightTable02.verticalHeader().setCascadingSectionResizes(False)
        self.widthHeightTable02.verticalHeader().setHighlightSections(False)
        self.widthHeightTable02.verticalHeader().setStretchLastSection(False)
        self.label = QLabel(self.page_details)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 0, 91, 31))
        self.label.setStyleSheet(u"background-repeat: no-repeat;\n"
                                 "                                     background-color: #4169E1;\n"
                                 "                                     text-align:center;\n"
                                 "                                     color:#ffffff\n"
                                 "                                 ")
        self.label_6 = QLabel(self.page_details)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 40, 91, 31))
        self.label_6.setStyleSheet(u"background-repeat: no-repeat;\n"
                                   "                                     background-color: #4169E1;\n"
                                   "                                     text-align:center;\n"
                                   "                                     color:#ffffff\n"
                                   "                                 ")
        self.editWidthStd = QLineEdit(self.page_details)
        self.editWidthStd.setObjectName(u"editWidthStd")
        self.editWidthStd.setGeometry(QRect(560, 0, 61, 31))
        self.editWidthStd.setStyleSheet(u"background-repeat: no-repeat;\n"
                                        "                                     background-color: #6495ED;\n"
                                        "                                     color:#ffffff\n"
                                        "                                 ")
        self.editHeightStd = QLineEdit(self.page_details)
        self.editHeightStd.setObjectName(u"editHeightStd")
        self.editHeightStd.setGeometry(QRect(560, 40, 61, 31))
        self.editHeightStd.setStyleSheet(u"background-repeat: no-repeat;\n"
                                         "                                     background-color: #6495ED;\n"
                                         "                                     color:#ffffff\n"
                                         "                                 ")
        self.label_7 = QLabel(self.page_details)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(640, 0, 91, 31))
        self.label_7.setStyleSheet(u"background-repeat: no-repeat;\n"
                                   "                                     background-color: #4169E1;\n"
                                   "                                     text-align:center;\n"
                                   "                                     color:#ffffff\n"
                                   "                                 ")
        self.label_8 = QLabel(self.page_details)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(640, 40, 91, 31))
        self.label_8.setStyleSheet(u"background-repeat: no-repeat;\n"
                                   "                                     background-color: #4169E1;\n"
                                   "                                     text-align:center;\n"
                                   "                                     color:#ffffff\n"
                                   "                                 ")
        self.editWidthErr = QLineEdit(self.page_details)
        self.editWidthErr.setObjectName(u"editWidthErr")
        self.editWidthErr.setGeometry(QRect(750, 0, 61, 31))
        self.editWidthErr.setStyleSheet(u"background-repeat: no-repeat;\n"
                                        "                                     background-color: #6495ED;\n"
                                        "                                     color:#ffffff\n"
                                        "                                 ")
        self.editHeightErr = QLineEdit(self.page_details)
        self.editHeightErr.setObjectName(u"editHeightErr")
        self.editHeightErr.setGeometry(QRect(750, 40, 61, 31))
        self.editHeightErr.setStyleSheet(u"background-repeat: no-repeat;\n"
                                         "                                     background-color: #6495ED;\n"
                                         "                                     color:#ffffff\n"
                                         "                                 ")
        self.detectModeSelector = QComboBox(self.page_details)
        self.detectModeSelector.addItem("")
        self.detectModeSelector.addItem("")
        self.detectModeSelector.setObjectName(u"detectModeSelector")
        self.detectModeSelector.setEnabled(True)
        self.detectModeSelector.setGeometry(QRect(200, 10, 141, 41))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.detectModeSelector.sizePolicy().hasHeightForWidth())
        self.detectModeSelector.setSizePolicy(sizePolicy4)
        self.detectModeSelector.setFont(font1)
        self.detectModeSelector.setStyleSheet(u"background-color: #4169E1;\n"
                                              "                                     color:#ffffff\n"
                                              "                                 ")
        self.label_9 = QLabel(self.page_details)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(450, 80, 91, 31))
        self.label_9.setStyleSheet(u"background-repeat: no-repeat;\n"
                                   "                                     background-color: #4169E1;\n"
                                   "                                     text-align:center;\n"
                                   "                                     color:#ffffff\n"
                                   "                                 ")
        self.label_10 = QLabel(self.page_details)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(640, 80, 91, 31))
        self.label_10.setStyleSheet(u"background-repeat: no-repeat;\n"
                                    "                                     background-color: #4169E1;\n"
                                    "                                     text-align:center;\n"
                                    "                                     color:#ffffff\n"
                                    "                                 ")
        self.label_11 = QLabel(self.page_details)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(450, 120, 91, 31))
        self.label_11.setStyleSheet(u"background-repeat: no-repeat;\n"
                                    "                                     background-color: #4169E1;\n"
                                    "                                     text-align:center;\n"
                                    "                                     color:#ffffff\n"
                                    "                                 ")
        self.editLineNum = QLineEdit(self.page_details)
        self.editLineNum.setObjectName(u"editLineNum")
        self.editLineNum.setGeometry(QRect(560, 80, 61, 31))
        self.editLineNum.setStyleSheet(u"background-repeat: no-repeat;\n"
                                       "                                     background-color: #6495ED;\n"
                                       "                                     color:#ffffff\n"
                                       "                                 ")
        self.editCurveNum = QLineEdit(self.page_details)
        self.editCurveNum.setObjectName(u"editCurveNum")
        self.editCurveNum.setGeometry(QRect(560, 120, 61, 31))
        self.editCurveNum.setStyleSheet(u"background-repeat: no-repeat;\n"
                                        "                                     background-color: #6495ED;\n"
                                        "                                     color:#ffffff\n"
                                        "                                 ")
        self.editPosNum = QLineEdit(self.page_details)
        self.editPosNum.setObjectName(u"editPosNum")
        self.editPosNum.setGeometry(QRect(750, 80, 61, 31))
        self.editPosNum.setStyleSheet(u"background-repeat: no-repeat;\n"
                                      "                                     background-color: #6495ED;\n"
                                      "                                     color:#ffffff\n"
                                      "                                 ")
        self.confirmParamSettingBtn = QPushButton(self.page_details)
        self.confirmParamSettingBtn.setObjectName(u"confirmParamSettingBtn")
        self.confirmParamSettingBtn.setGeometry(QRect(650, 120, 141, 51))
        self.confirmParamSettingBtn.setFont(font8)
        self.confirmParamSettingBtn.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-settings.png);\n"
                                                  "                               background-origin: content;\n"
                                                  "                               background-position: left center;\n"
                                                  "                               \n"
                                                  "                               padding-left:10px;\n"
                                                  "                               background-repeat: no-repeat;\n"
                                                  "                               background-color: #4169E1;\n"
                                                  "                               text-align:center;\n"
                                                  "                               \n"
                                                  "                           ")
        self.stackedWidget.addWidget(self.page_details)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font4)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u"QScrollBar:vertical { background: rgb(52, 59,\n"
"                                                        72);\n"
"                                                        }\n"
"                                                        QScrollBar:horizontal { background: rgb(52, 59, 72); }\n"
"                                                    ")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setFont(font4)
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"                                                        background: rgb(52, 59, 72);\n"
"                                                        }\n"
"                                                        QScrollBar:horizontal {\n"
"                                                        background: rgb(52, 59, 72);\n"
"                                                        }\n"
"                                                    ")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
                                                    "	border: none;\n"
                                                    "    background: rgb(52, 59, 72);\n"
                                                    "    width: 14px;\n"
                                                    "    margin: 21px 0 21px 0;\n"
                                                    "	border-radius: 0px;\n"
                                                    " }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font4)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font11);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem37)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        brush3 = QBrush(QColor(51, 51, 51, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 0))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush6 = QBrush(QColor(51, 51, 51, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.tableWidget.setPalette(palette2)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.colorFrame = QFrame(self.page_test)
        self.colorFrame.setObjectName(u"colorFrame")
        self.colorFrame.setGeometry(QRect(50, 60, 771, 501))
        self.colorFrame.setFrameShape(QFrame.StyledPanel)
        self.colorFrame.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_test)
        self.page_before = QWidget()
        self.page_before.setObjectName(u"page_before")
        self.modeSelector = QComboBox(self.page_before)
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.modeSelector.setObjectName(u"modeSelector")
        self.modeSelector.setEnabled(True)
        self.modeSelector.setGeometry(QRect(70, 20, 161, 61))
        sizePolicy4.setHeightForWidth(self.modeSelector.sizePolicy().hasHeightForWidth())
        self.modeSelector.setSizePolicy(sizePolicy4)
        self.modeSelector.setFont(font1)
        self.modeSelector.setStyleSheet(u"background-color: #4169E1;\n"
"color:#ffffff")
        self.recordButton = QPushButton(self.page_before)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(580, 20, 171, 61))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setKerning(True)
        self.recordButton.setFont(font12)
        self.recordButton.setStyleSheet(u"background-color: #4169E1;")
        self.startTestButton = QPushButton(self.page_before)
        self.startTestButton.setObjectName(u"startTestButton")
        self.startTestButton.setGeometry(QRect(320, 20, 161, 61))
        self.startTestButton.setFont(font1)
        self.startTestButton.setStyleSheet(u"background-color: #4169E1;")
        self.horizontalLayoutWidget = QWidget(self.page_before)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 110, 511, 331))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logger = QTableWidget(self.horizontalLayoutWidget)
        if (self.logger.columnCount() < 2):
            self.logger.setColumnCount(2)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.logger.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.logger.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        if (self.logger.rowCount() < 1):
            self.logger.setRowCount(1)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font11);
        self.logger.setVerticalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.logger.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.logger.setItem(0, 1, __qtablewidgetitem42)
        self.logger.setObjectName(u"logger")
        sizePolicy3.setHeightForWidth(self.logger.sizePolicy().hasHeightForWidth())
        self.logger.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.logger.setPalette(palette3)
        self.logger.setStyleSheet(u"background-color: 	#6495ED;\n"
"color:#ffffff")
        self.logger.setFrameShape(QFrame.NoFrame)
        self.logger.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.logger.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.logger.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.logger.setSelectionMode(QAbstractItemView.SingleSelection)
        self.logger.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.logger.setShowGrid(True)
        self.logger.setGridStyle(Qt.SolidLine)
        self.logger.setSortingEnabled(False)
        self.logger.horizontalHeader().setVisible(False)
        self.logger.horizontalHeader().setCascadingSectionResizes(False)
        self.logger.horizontalHeader().setDefaultSectionSize(150)
        self.logger.horizontalHeader().setHighlightSections(True)
        self.logger.horizontalHeader().setStretchLastSection(True)
        self.logger.verticalHeader().setVisible(False)
        self.logger.verticalHeader().setCascadingSectionResizes(False)
        self.logger.verticalHeader().setHighlightSections(False)
        self.logger.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_6.addWidget(self.logger)

        self.horizontalLayoutWidget_2 = QWidget(self.page_before)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(569, 110, 221, 331))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widthHeightTable = QTableWidget(self.horizontalLayoutWidget_2)
        if (self.widthHeightTable.columnCount() < 3):
            self.widthHeightTable.setColumnCount(3)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.widthHeightTable.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.widthHeightTable.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.widthHeightTable.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        if (self.widthHeightTable.rowCount() < 1):
            self.widthHeightTable.setRowCount(1)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFont(font11);
        self.widthHeightTable.setVerticalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.widthHeightTable.setItem(0, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.widthHeightTable.setItem(0, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.widthHeightTable.setItem(0, 2, __qtablewidgetitem49)
        self.widthHeightTable.setObjectName(u"widthHeightTable")
        sizePolicy3.setHeightForWidth(self.widthHeightTable.sizePolicy().hasHeightForWidth())
        self.widthHeightTable.setSizePolicy(sizePolicy3)
        self.widthHeightTable.setMinimumSize(QSize(150, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.widthHeightTable.setPalette(palette4)
        self.widthHeightTable.setStyleSheet(u"background-color: 	#6495ED;\n"
"color:#ffffff")
        self.widthHeightTable.setFrameShape(QFrame.NoFrame)
        self.widthHeightTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.widthHeightTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.widthHeightTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.widthHeightTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.widthHeightTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.widthHeightTable.setShowGrid(True)
        self.widthHeightTable.setGridStyle(Qt.SolidLine)
        self.widthHeightTable.setSortingEnabled(False)
        self.widthHeightTable.horizontalHeader().setVisible(False)
        self.widthHeightTable.horizontalHeader().setCascadingSectionResizes(False)
        self.widthHeightTable.horizontalHeader().setDefaultSectionSize(64)
        self.widthHeightTable.horizontalHeader().setHighlightSections(True)
        self.widthHeightTable.horizontalHeader().setStretchLastSection(True)
        self.widthHeightTable.verticalHeader().setVisible(False)
        self.widthHeightTable.verticalHeader().setCascadingSectionResizes(False)
        self.widthHeightTable.verticalHeader().setHighlightSections(False)
        self.widthHeightTable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_7.addWidget(self.widthHeightTable)

        self.stackedWidget.addWidget(self.page_before)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.developerButton = QPushButton(self.page_settings)
        self.developerButton.setObjectName(u"developerButton")
        self.developerButton.setGeometry(QRect(730, 570, 121, 31))
        self.developerButton.setStyleSheet(u"background-color: #4169E1")
        self.progressColorButton = QPushButton(self.page_settings)
        self.progressColorButton.setObjectName(u"progressColorButton")
        self.progressColorButton.setGeometry(QRect(730, 520, 121, 31))
        self.progressColorButton.setStyleSheet(u"background-color: #4169E1")
        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font4)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font4)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font4)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setBold(False)
        font13.setItalic(False)
        self.creditsLabel.setFont(font13)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_20.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.detectModeSelector.setCurrentIndex(-1)
        self.modeSelector.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u663e\u5fae\u955c\u81ea\u52a8\u5316\u6d4b\u8bd5", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Microscope automated testing", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_details.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                             </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                              </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> </span><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">\u663e\u5fae\u955c\u81ea\u52a8\u5316\u6d4b\u8bd5</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                                                          </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> </span><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created for operating Keyence VHX                             microscope automatically</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                              </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> </span><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                              </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\"> </span><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">http://zjut.waymove.net</span><span style=\" font-family:'Segoe UI'; font-size:10pt;\">                          </span></p></body></html>", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6821\u51c6", None))
        self.label_4.setText("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;color:white;\">\u6b63\u5728\u8fd0\u884c\u4e2d</span></p></body></html>",
                                                        None))
        self.startDetectBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.setWorkSpaceBtn.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u8bbe\u7f6e", None))
        ___qtablewidgetitem = self.logger02.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.logger02.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.logger02.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.logger02.isSortingEnabled()
        self.logger02.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.logger02.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.logger02.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None));
        self.logger02.setSortingEnabled(__sortingEnabled)

        self.analyseBtn.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7edf\u8ba1", None))
        ___qtablewidgetitem5 = self.widthHeightTable02.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem6 = self.widthHeightTable02.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.widthHeightTable02.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem8 = self.widthHeightTable02.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.widthHeightTable02.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.widthHeightTable02.isSortingEnabled()
        self.widthHeightTable02.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.widthHeightTable02.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None));
        ___qtablewidgetitem11 = self.widthHeightTable02.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6", None));
        ___qtablewidgetitem12 = self.widthHeightTable02.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5ea6", None));
        ___qtablewidgetitem13 = self.widthHeightTable02.item(0, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u9762\u79ef", None));
        self.widthHeightTable02.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("MainWindow", u"  \u6805\u7ebf\u5bbd\u6807\u51c6\u503c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  \u6805\u7ebf\u9ad8\u6807\u51c6\u503c", None))
        self.editWidthStd.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.editHeightStd.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  \u7ebf\u5bbd\u8bef\u5dee\u9608\u503c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"  \u7ebf\u9ad8\u8bef\u5dee\u9608\u503c", None))
        self.editWidthErr.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.editHeightErr.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.detectModeSelector.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                          u"\u5feb\u901f\u5355\u70b9\u68c0\u6d4b",
                                                                          None))
        self.detectModeSelector.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                          u"\u53cc\u7ebf\u6807\u51c6\u68c0\u6d4b",
                                                                          None))

        self.detectModeSelector.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u6a21\u5f0f\u9009\u62e9", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"     \u6805\u7ebf\u6761\u6570", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"  \u6805\u7ebf\u70b9\u4f4d\u4e2a\u6570", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"  \u70b9\u4f4d\u66f2\u7ebf\u4e2a\u6570", None))
        self.editLineNum.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.editCurveNum.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.editPosNum.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165", None))
        self.confirmParamSettingBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u786e\u8ba4", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem34 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem35 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem36 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem37 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.modeSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"\u94f6\u7ebf\u8bc6\u522b\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6e05\u6670\u5ea6\u8ba1\u7b97", None))
        self.modeSelector.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u79fb\u52a8\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u79fb\u52a8\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(4, QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(5, QCoreApplication.translate("MainWindow", u"OCR\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5bbd\u9ad8\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(7, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u9875\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(8, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u9875\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(9, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u9875\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(10, QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u9875\u6d4b\u8bd5", None))
        self.modeSelector.setItemText(11, QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b\u6d4b\u8bd501", None))
        self.modeSelector.setItemText(12, QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b\u6d4b\u8bd502", None))
        self.modeSelector.setItemText(13, QCoreApplication.translate("MainWindow", u"\u6cbf\u6805\u7ebf\u68c0\u6d4b", None))
        self.modeSelector.setItemText(14, QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u6805\u7ebf\u68c0\u6d4b", None))

        self.modeSelector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6d4b\u8bd5\u5185\u5bb9", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5236", None))
        self.startTestButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5", None))
        ___qtablewidgetitem38 = self.logger.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem39 = self.logger.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem40 = self.logger.verticalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.logger.isSortingEnabled()
        self.logger.setSortingEnabled(False)
        ___qtablewidgetitem41 = self.logger.item(0, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem42 = self.logger.item(0, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None));
        self.logger.setSortingEnabled(__sortingEnabled3)

        ___qtablewidgetitem43 = self.widthHeightTable.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem44 = self.widthHeightTable.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem45 = self.widthHeightTable.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem46 = self.widthHeightTable.verticalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.widthHeightTable.isSortingEnabled()
        self.widthHeightTable.setSortingEnabled(False)
        ___qtablewidgetitem47 = self.widthHeightTable.item(0, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6", None));
        ___qtablewidgetitem48 = self.widthHeightTable.item(0, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5ea6", None));
        ___qtablewidgetitem49 = self.widthHeightTable.item(0, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u9762\u79ef", None));
        self.widthHeightTable.setSortingEnabled(__sortingEnabled4)

        self.developerButton.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165\u5f00\u53d1\u8005\u6a21\u5f0f", None))
        self.progressColorButton.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6\u67e5\u770b\uff08\u6d4b\u8bd5\uff09", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"http://zjut.waymove.net", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

