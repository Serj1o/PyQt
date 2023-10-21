import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit

class FunctionTableApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Табулирование функции')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.result_text = QTextEdit(central_widget)
        layout.addWidget(self.result_text)

        self.calculate_button = QPushButton('Вычислить и вывести таблицу', central_widget)
        layout.addWidget(self.calculate_button)
        self.calculate_button.clicked.connect(self.calculate_and_display)

        self.x0_label = QLabel('x(0):', central_widget)
        self.x0_input = QLineEdit(central_widget)
        layout.addWidget(self.x0_label)
        layout.addWidget(self.x0_input)

        self.xk_label = QLabel('x(k):', central_widget)
        self.xk_input = QLineEdit(central_widget)
        layout.addWidget(self.xk_label)
        layout.addWidget(self.xk_input)

        self.dx_label = QLabel('dx:', central_widget)
        self.dx_input = QLineEdit(central_widget)
        layout.addWidget(self.dx_label)
        layout.addWidget(self.dx_input)

        self.a_label = QLabel('a:', central_widget)
        self.a_input = QLineEdit(central_widget)
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_input)

    def calculate_and_display(self):
        x0 = float(self.x0_input.text())
        xk = float(self.xk_input.text())
        dx = float(self.dx_input.text())
        a = float(self.a_input.text())

        result = "x\t\ty(x)\n"

        x = x0
        while x <= xk + dx / 2:
            y = a + x ** (2 / 3) * math.cos(x + math.exp(x))
            result += f"{x:.2f}\t\t{y:.2f}\n"
            x += dx

        self.result_text.setPlainText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FunctionTableApp()
    ex.show()
    sys.exit(app.exec_())
