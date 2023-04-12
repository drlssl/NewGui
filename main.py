# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
import sys
import os
import platform

from Processor.Processor import Processor

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
# widgets = None

import time
from datetime import datetime


# get time
# /////////////////////////////////////////////////////////////////
def getTime():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")
    return formatted_time


# ////////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # global widgets
        self.widgets = self.ui

        self.Processor = Processor()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Keyence VHX Automation"
        description = " Keyence VHX Automation"

        # APPLY TEXTS
        self.setWindowTitle(title)
        self.widgets.titleRightInfo.setText(description)

        # TOGGLE MENU: 左菜单是否可以展开
        # ///////////////////////////////////////////////////////////////
        self.widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # my operation list
        # ///////////////////////////////////////////////////////////////////
        self.AllOperations = [
            self.findLineTest,
            self.getSharpness,
            self.moveTest,
            self.clickTest,
            self.ocrTest,
            self.getWidthHeightTest,
            self.pipeLineTest01,
        ]

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # my own function connect to button

        self.widgets.startTestButton.clicked.connect(self.startTestButtonClicked)
        self.widgets.recordButton.clicked.connect(self.recordButtonClicked)
        # ////////////////////////////////////////////////////////////////////

        # LEFT MENUS
        self.widgets.btn_home.clicked.connect(self.buttonClick)
        self.widgets.btn_widgets.clicked.connect(self.buttonClick)

        self.widgets.btn_test.clicked.connect(self.buttonClick)
        self.widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        self.widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        self.widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)
        self.widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_test":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def add_log(self, msg):
        rowPosition = self.widgets.logger.rowCount()
        self.widgets.logger.insertRow(rowPosition)
        self.widgets.logger.setItem(rowPosition, 0, QTableWidgetItem(f"{getTime()}"))
        self.widgets.logger.setItem(rowPosition, 1, QTableWidgetItem(f"{msg}"))

    def add_widthHeight(self, width, height):
        rowPosition = self.widgets.widthHeightTable.rowCount()
        self.widgets.widthHeightTable.insertRow(rowPosition)
        self.widgets.widthHeightTable.setItem(rowPosition, 0, QTableWidgetItem(f"{width:.2f}μm"))
        self.widgets.widthHeightTable.setItem(rowPosition, 1, QTableWidgetItem(f"{height:.2f}μm"))

    def recordButtonClicked(self):
        #     通过pyautogui来录制屏幕
        self.add_log("点击录制按钮")
        if self.Processor.recordFlag:
            self.add_log("停止录制")
            self.add_log("录制完成")
            self.widgets.recordButton.setText("开始录制")
            self.Processor.recordFlag = False
        else:
            self.add_log("开始录制")
            self.widgets.recordButton.setText("结束录制")
            self.Processor.recordFlag = True
            self.Processor.recordScreen(getTime())

    def startTestButtonClicked(self):
        self.add_log(f"开始{self.widgets.modeSelector.currentText()}")
        currentIndex = self.widgets.modeSelector.currentIndex()
        self.AllOperations[currentIndex]()

    # 下面都是我对应于前面的operation list的函数内容
    # /////////////////////////////////////////////////////////////////////
    def findLineTest(self):
        # self.add_log('start find the line')
        self.showMinimized()
        time.sleep(1)
        self.Processor.findLine(self.add_log)
        self.showNormal()

    def getSharpness(self):
        # self.add_log('start calculate sharpness')
        self.showMinimized()
        time.sleep(1)
        self.Processor.getLineSharpness(self.add_log)
        self.showNormal()
        # self.add_log(f'res{res}')

    def moveTest(self):
        # self.add_log('start move test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.moveTest(self.add_log)
        self.showNormal()
        # self.add_log(f'res{res}')

    def clickTest(self):
        # self.add_log('start click test')
        self.showMinimized()
        time.sleep(1)
        # click the focus up and down
        self.Processor.clickTest(self.add_log)
        self.showNormal()
        # self.add_log(f'res{res}')

    def ocrTest(self):
        # self.add_log('start ocr test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.tesseractTest(self.add_log)
        self.showNormal()
        # self.add_log(f'res:{res}')

    def getWidthHeightTest(self):
        # self.add_log('start getting width and height')
        self.showMinimized()
        time.sleep(1)
        res = self.Processor.getWidthHeightTest(getOut=self.add_log, getOut02=self.add_widthHeight)
        self.showNormal()
        # self.add_log(f'res:{res}')

    def pipeLineTest01(self):
        # self.add_log('start pipeline test01')
        self.showMinimized()
        time.sleep(1)
        res = self.Processor.pipeLineTest01(getOut=self.add_log, getOut02=self.add_widthHeight)
        self.showNormal()
        self.add_log(f"res:{res}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("microscopeIcon.png"))
    window = MainWindow()
    sys.exit(app.exec())
