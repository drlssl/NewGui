from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt

class GridWidget(QWidget):
    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.grid = [[QColor(255, 255, 255) for _ in range(columns)] for _ in range(rows)]

    def paintEvent(self, event):
        painter = QPainter(self)
        cell_width = self.width() // self.columns
        cell_height = self.height() // self.rows

        for row in range(self.rows):
            for col in range(self.columns):
                color = self.grid[row][col]
                painter.fillRect(col * cell_width, row * cell_height, cell_width, cell_height, color)

    def set_cell_color(self, row, col, color):
        self.grid[row][col] = color
        self.update()

def main():
    app = QApplication([])
    widget = GridWidget(10, 10)  # 创建一个 10x10 的网格小部件

    # 设置某些格子的颜色
    widget.set_cell_color(1, 1, QColor(255, 0, 0))  # 设置 (1, 1) 格子为红色
    widget.set_cell_color(2, 3, QColor(0, 255, 0))  # 设置 (2, 3) 格子为绿色
    widget.set_cell_color(3, 5, QColor(0, 0, 255))  # 设置 (3, 5) 格子为蓝色

    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
