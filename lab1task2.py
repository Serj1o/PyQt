import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QGroupBox, QRadioButton, QVBoxLayout
import math

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 450)
        self.setWindowTitle('Калькулятор')

        self.x_label = QLabel('Введите значение X:', self)
        self.x_label.setGeometry(10, 10, 120, 20)
        self.x_input = QLineEdit(self)
        self.x_input.setGeometry(150, 10, 100, 20)

        self.y_label = QLabel('Введите значение Y:', self)
        self.y_label.setGeometry(10, 40, 120, 20)
        self.y_input = QLineEdit(self)
        self.y_input.setGeometry(150, 40, 100, 20)

        self.z_label = QLabel('Введите значение Z:', self)
        self.z_label.setGeometry(10, 70, 120, 20)
        self.z_input = QLineEdit(self)
        self.z_input.setGeometry(150, 70, 100, 20)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(10, 100, 380, 200)
        self.result_text.setReadOnly(True)
        self.result_text.setLineWrapMode(QTextEdit.WidgetWidth)

        self.calculate_button = QPushButton('Пуск', self)
        self.calculate_button.setGeometry(250, 310, 100, 30)
        self.calculate_button.clicked.connect(self.calculate)

        # Создаем GroupBox для радиокнопок
        self.function_group = QGroupBox('Выберите функцию f(x):', self)
        self.function_group.setGeometry(10, 320, 180, 90)

        # Создаем радиокнопки
        self.sh_radio = QRadioButton('sh(x)', self.function_group)
        self.x_radio = QRadioButton('x^2', self.function_group)
        self.exp_radio = QRadioButton('exp^x', self.function_group)

        # Группируем радиокнопки
        self.function_group_layout = QVBoxLayout()
        self.function_group_layout.addWidget(self.sh_radio)
        self.function_group_layout.addWidget(self.x_radio)
        self.function_group_layout.addWidget(self.exp_radio)
        self.function_group.setLayout(self.function_group_layout)

    def calculate(self):
        try:
            x = float(self.x_input.text())
            y = float(self.y_input.text())
            z = float(self.z_input.text())

            self.result_text.clear()
            self.result_text.append("Результаты работы программы")
            self.result_text.append(f"При X = {x}")
            self.result_text.append(f"При Y = {y}")
            self.result_text.append(f"При Z = {z}")

            selected_function = None
            selected_function_name = ""

            if self.sh_radio.isChecked():
                selected_function = math.sinh
                selected_function_name = "sh(x)"
            elif self.x_radio.isChecked():
                selected_function = lambda x: x**2
                selected_function_name = "x^2"
            elif self.exp_radio.isChecked():
                selected_function = lambda x: math.exp(x)
                selected_function_name = "exp^x"

            if selected_function is not None:
                self.result_text.append(f"Выбрана функция: {selected_function_name}")

                f_x = selected_function(x)
                r = max(min(f_x, y), z)

                self.result_text.append(f"r = {r:.4f}")
            else:
                self.result_text.append("Не выбрана функция")

        except ValueError:
            self.result_text.clear()
            self.result_text.append('Пожалуйста, введите корректные числовые значения для X, Y и Z.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec_())
