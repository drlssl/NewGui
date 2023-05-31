import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFrame, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_size = 20  # 方格的数量
        self.grid_colors = [[QColor(255, 255, 255) for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        layout = QVBoxLayout()
        self.label = QLabel("Hello, World!")  # 创建一个QLabel显示文本
        layout.addWidget(self)
        layout.addWidget(self.label)  # 将QLabel添加到布局中

        # 创建一个Frame用于容纳ColorGrid和Label
        frame = QFrame()
        frame.setLayout(layout)

        # 创建主窗口并设置Frame作为中心部件
        self.window = QMainWindow()
        self.window.setWindowTitle("Color Grid")
        self.window.setCentralWidget(frame)
        self.window.setGeometry(100, 100, self.grid_size * 100, self.grid_size * 100)
        self.window.show()



    def paintEvent(self,event):
        painter = QPainter(self)
        cell_width = self.width() // self.grid_size
        cell_height = self.height() // self.grid_size
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = self.grid_colors[i][j]
                painter.fillRect(i * cell_width, j * cell_height, cell_width, cell_height, color)

    def mousePressEvent(self, event):
        cell_width = self.width() // self.grid_size
        cell_height = self.height() // self.grid_size

        x = event.x() // cell_width
        y = event.y() // cell_height

        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            color = QColor(255, 0, 0)  # 设置为红色
            self.grid_colors[x][y] = color
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
