import sys
import math
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class FunctionPlotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Графики нашей функции и произвольной функции')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.canvas = PlotCanvas(self.central_widget, width=5, height=4)
        layout.addWidget(self.canvas)

        self.plot_button = QPushButton('Построить графики', self.central_widget)
        layout.addWidget(self.plot_button)

        self.xmin_label = QLabel('Xmin:', self.central_widget)
        self.xmin_input = QLineEdit(self.central_widget)
        self.xmax_label = QLabel('Xmax:', self.central_widget)
        self.xmax_input = QLineEdit(self.central_widget)
        self.step_label = QLabel('Шаг:', self.central_widget)
        self.step_input = QLineEdit(self.central_widget)
        self.a_label = QLabel('A:', self.central_widget)
        self.a_input = QLineEdit(self.central_widget)

        layout.addWidget(self.xmin_label)
        layout.addWidget(self.xmin_input)
        layout.addWidget(self.xmax_label)
        layout.addWidget(self.xmax_input)
        layout.addWidget(self.step_label)
        layout.addWidget(self.step_input)
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_input)

        self.plot_button.clicked.connect(self.plot_functions)

    def plot_functions(self):
        Xmin = float(self.xmin_input.text())
        Xmax = float(self.xmax_input.text())
        Step = float(self.step_input.text())
        a = float(self.a_input.text())
        x = np.arange(Xmin, Xmax, Step)

        # Добавляем вычисленные значения для новой функции
        y_custom = [a + x_i ** (2 / 3) * math.cos(x_i + math.exp(x_i)) for x_i in x]

        # Добавляем вычисленные значения для второй произвольной функции
        y = [math.sin(x_i) * 0.5 + math.cos(x_i) * 0.25 for x_i in x]

        self.canvas.plot(x, y_custom, y)

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, x, y1, y2):
        self.axes.clear()
        self.axes.plot(x, y1, label='Our Function')
        self.axes.plot(x, y2, label='Custom Function')
        self.axes.set_title('Графики нашей функции и произвольной функции')
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.axes.grid(True)
        self.axes.legend()
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FunctionPlotApp()
    ex.show()
    sys.exit(app.exec_())
