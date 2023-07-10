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


# color grid
# ////////////////////////////////////////////////////////
class ColorGrid(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_size = 25
        self.grid_colors = [[QColor('#6495ED') for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def paintEvent(self, event):
        painter = QPainter(self)
        cell_width = self.width() // self.grid_size
        cell_height = self.height() // self.grid_size
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = self.grid_colors[i][j]
                painter.fillRect(i * cell_width, j * cell_height, cell_width, cell_height, color)

    def set_cell_color(self, row, col):
        self.grid_colors[self.grid_size - row][self.grid_size - col] = QColor('#e75f2c')
        self.update()


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
        title = "太阳能栅线自动化检"
        description = "太阳能栅线自动化检测"

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

        # color grid test
        # ////////////////////////////
        self.grid_size = 3
        self.grid_colors = [[QColor(255, 255, 255) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.color_grid = ColorGrid()
        self.color_grid.setParent(self.widgets.colorFrame)
        self.color_grid.set_cell_color(1, 1)
        # /////////////////////////////

        # my operation list
        # ///////////////////////////////////////////////////////////////////
        self.AllOperations = [
            self.findLineTest,
            self.getSharpness,
            self.verticalMoveTest,
            self.horizontalMoveTest,
            self.clickTest,
            self.ocrTest,
            self.getWidthHeightTest,
            self.firstPageTest,
            self.secondPageTest,
            self.thirdPageTest,
            self.fourthPageTest,
            self.pipelineTest01,
            self.pipelineTest02,
        ]

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # my own function connect to button

        self.widgets.startTestButton.clicked.connect(self.startTestButtonClicked)
        self.widgets.startButton.clicked.connect(self.startButtonClicked)
        self.widgets.recordButton.clicked.connect(self.recordButtonClicked)
        self.widgets.developerButton.clicked.connect(self.developerButtonClicked)
        self.widgets.progressColorButton.clicked.connect(self.progressColorButtonClicked)
        self.widgets.fileReportBtn.clicked.connect(self.fileReportBtnClicked)
        # ////////////////////////////////////////////////////////////////////

        # LEFT MENUS
        self.widgets.btn_home.clicked.connect(self.buttonClick)
        # self.widgets.btn_widgets.clicked.connect(self.buttonClick)
        self.widgets.btn_details.clicked.connect(self.buttonClick)
        self.widgets.btn_settings.clicked.connect(self.buttonClick)
        self.widgets.btn_history.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        # self.widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        # self.widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

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
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_home)
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
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_details":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_details)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_history":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_test)
            # print("close BTN clicked!")
            # self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_history)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == 'btn_settings':
            print('settings btn clicked')
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_settings)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

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
    def fileReportBtnClicked(self):
        dir=QFileDialog.getExistingDirectory(self,"选择文件夹"," ")
        if dir:
            print(f"选择的文件夹是：{dir}")
            self.Processor.savedPath=dir
            self.add_log(f"设置导出文件的目录为：{dir}")


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def progressColorButtonClicked(self):
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_test)
        UIFunctions.resetStyle(self,'btn_settings')
        self.widgets.btn_settings.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_settings.styleSheet()))

    def developerButtonClicked(self):
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_before)
        UIFunctions.resetStyle(self, 'btn_settings')
        self.widgets.btn_settings.setStyleSheet(UIFunctions.selectMenu(self.widgets.btn_settings.styleSheet()))

    def add_log(self, msg):
        rowPosition01 = self.widgets.logger.rowCount()
        self.widgets.logger.insertRow(rowPosition01)
        self.widgets.logger.setItem(rowPosition01, 0, QTableWidgetItem(f"{getTime()}"))
        self.widgets.logger.setItem(rowPosition01, 1, QTableWidgetItem(f"{msg}"))

        rowPosition02 = self.widgets.logger02.rowCount()
        self.widgets.logger02.insertRow(rowPosition02)
        self.widgets.logger02.setItem(rowPosition02, 0, QTableWidgetItem(f"{getTime()}"))
        self.widgets.logger02.setItem(rowPosition02, 1, QTableWidgetItem(f"{msg}"))

    def add_widthHeight(self, width, height):
        rowPosition01 = self.widgets.widthHeightTable.rowCount()
        self.widgets.widthHeightTable.insertRow(rowPosition01)
        self.widgets.widthHeightTable.setItem(rowPosition01, 0, QTableWidgetItem(f"{width:.2f}μm"))
        self.widgets.widthHeightTable.setItem(rowPosition01, 1, QTableWidgetItem(f"{height:.2f}μm"))

        rowPosition02 = self.widgets.widthHeightTable02.rowCount()
        self.widgets.widthHeightTable02.insertRow(rowPosition02)
        self.widgets.widthHeightTable02.setItem(rowPosition02,
                                                0,
                                                QTableWidgetItem(
                                                    f"{self.Processor.currentLineIndex}-{self.Processor.currentPosIndex}-{self.Processor.currentCurveIndex}"
                                                ))
        self.widgets.widthHeightTable02.setItem(rowPosition02, 1, QTableWidgetItem(f"{width:.2f}μm"))
        self.widgets.widthHeightTable02.setItem(rowPosition02, 2, QTableWidgetItem(f"{height:.2f}μm"))

    def recordButtonClicked(self):
        #     通过pyautogui来录制
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

    def startButtonClicked(self):
        self.showMinimized()
        time.sleep(1)
        self.Processor.pipelineTest02(
            getOut01=self.add_log,
            getOut02=self.add_widthHeight,
            draw=self.color_grid.set_cell_color,
            # lineCounts=3,
            # posCounts=3
        )
        self.showNormal()

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

    def verticalMoveTest(self):
        # self.add_log('start move test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.verticalMoveTest(self.add_log)
        self.showNormal()
        # self.add_log(f'res{res}')

    def horizontalMoveTest(self):
        self.showMinimized()
        time.sleep(5)
        self.Processor.horizontalMoveTest(self.add_log)
        self.showNormal()

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

    def firstPageTest(self):
        self.add_log('start first page test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.firstPageProcess(getOut=self.add_log)
        self.showNormal()

    def secondPageTest(self):
        self.add_log('start second page test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.secondPageProcess(getOut=self.add_log)
        self.showNormal()

    def thirdPageTest(self):
        self.add_log('start third page test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.thirdPageProcess(getOut01=self.add_log, getOut02=self.add_widthHeight)
        self.showNormal()

    def fourthPageTest(self):
        self.add_log('start fourth page test')
        self.showMinimized()
        time.sleep(1)
        self.Processor.fourthPageProgress(getOut=self.add_log)
        self.showNormal()

    def pipelineTest01(self):
        self.add_log('start pipeline test01')
        self.showMinimized()
        time.sleep(1)
        self.Processor.pipelineTest01(
            getOut01=self.add_log,
            getOut02=self.add_widthHeight,
            draw=self.color_grid.set_cell_color)
        self.showNormal()

    def pipelineTest02(self):
        self.add_log('start pipeline test02')
        self.showMinimized()
        time.sleep(1)
        self.Processor.pipelineTest02(
            getOut01=self.add_log,
            getOut02=self.add_widthHeight,
            draw=self.color_grid.set_cell_color,
            # lineCounts=3,
            # posCounts=3
        )
        self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("microscopeIcon.png"))
    window = MainWindow()
    sys.exit(app.exec_())
