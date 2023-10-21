import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt

class DynamicElementsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Создание динамических элементов')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setAlignment(Qt.AlignTop)

        self.central_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.button = QPushButton('Создать кнопку', self.central_widget)
        self.textbox = QLineEdit('Создать текстовое поле', self.central_widget)

        self.button.hide()
        self.textbox.hide()

        layout.addWidget(self.button)
        layout.addWidget(self.textbox)

        self.central_widget.mousePressEvent = self.on_mouse_click

        self.x = 0
        self.y = 0  # Начальные координаты

    def create_button(self):
        button = QPushButton('Кнопка', self.central_widget)
        button.setGeometry(self.x, self.y, 162, 35)
        button.show()

        self.x += 30  # Увеличиваем координаты с шагом 30 по X
        self.y += 30  # Увеличиваем координаты с шагом 30 по Y

    def create_textbox(self, text):
        textbox = QLineEdit(text, self.central_widget)
        textbox.setGeometry(self.x, self.y, 162, 35)
        textbox.show()

        self.x += 30  # Увеличиваем координаты с шагом 30 по X
        self.y += 30  # Увеличиваем координаты с шагом 30 по Y

    def on_mouse_click(self, event):
        if event.button() == Qt.LeftButton:
            self.create_textbox('Текстовое поле')
        else:
            self.create_button()

    def resizeEvent(self, event):
        # При изменении размера окна, очищаем все элементы и сбрасываем координаты
        self.clear_elements()
        self.x = 0
        self.y = 0
        super().resizeEvent(event)

    def clear_elements(self):
        for widget in self.central_widget.findChildren(QWidget):
            widget.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DynamicElementsApp()
    ex.show()
    sys.exit(app.exec_())
