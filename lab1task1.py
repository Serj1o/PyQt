import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
import math

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Калькулятор')

        self.a_label = QLabel('Введи значение A:', self)
        self.a_label.setGeometry(10, 10, 120, 20)
        self.a_input = QLineEdit(self)
        self.a_input.setGeometry(150, 10, 100, 20)

        self.c_label = QLabel('Введи значение C:', self)
        self.c_label.setGeometry(10, 40, 120, 20)
        self.c_input = QLineEdit(self)
        self.c_input.setGeometry(150, 40, 100, 20)

        self.d_label = QLabel('Введи значение D:', self)
        self.d_label.setGeometry(10, 70, 120, 20)
        self.d_input = QLineEdit(self)
        self.d_input.setGeometry(150, 70, 100, 20)

        self.x_label = QLabel('Введи значение X:', self)
        self.x_label.setGeometry(10, 100, 120, 20)
        self.x_input = QLineEdit(self)
        self.x_input.setGeometry(150, 100, 100, 20)

        self.x_label = QLabel('Результат выполнения программы: ', self)
        self.x_label.setGeometry(10, 130, 200, 20)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(10, 150, 380, 200)
        self.result_text.setReadOnly(True)

        self.calculate_button = QPushButton('Выполнить', self)
        self.calculate_button.setGeometry(150, 360, 100, 30)
        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        try:
            a = float(self.a_input.text())
            c = float(self.c_input.text())
            d = float(self.d_input.text())
            x = float(self.x_input.text())

            self.result_text.clear()
            self.result_text.append(f'A = {a}')
            self.result_text.append(f'C = {c}')
            self.result_text.append(f'D = {d}')
            self.result_text.append(f'X = {x}')

            y = (math.sqrt((c - d * x**2) / x) + math.log(x**2 + c) / (0.7 * x + a * d) - 10**(-2) / (c - d * x**3))

            self.result_text.append(f'Результат Y = {y}')
        except ValueError:
            self.result_text.clear()
            self.result_text.append('Пожалуйста, введите корректные числовые значения для A, C, D и X.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec_())
