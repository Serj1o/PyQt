import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit

class MatrixSumApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Сумма элементов вне главной диагонали')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.matrix1_label = QLabel('Матрица 1:', self.central_widget)
        self.matrix1_input = QTextEdit(self.central_widget)
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix1_input)

        self.matrix2_label = QLabel('Матрица 2:', self.central_widget)
        self.matrix2_input = QTextEdit(self.central_widget)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.matrix2_input)

        self.result_button = QPushButton('Вычислить сумму', self.central_widget)
        layout.addWidget(self.result_button)

        self.result_label = QLabel('', self.central_widget)
        layout.addWidget(self.result_label)

        self.result_button.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        matrix1_text = self.matrix1_input.toPlainText()
        matrix2_text = self.matrix2_input.toPlainText()

        matrix1 = [[int(num) for num in row.split()] for row in matrix1_text.split('\n')]
        matrix2 = [[int(num) for num in row.split()] for row in matrix2_text.split('\n')]

        sum1 = self.calculate_diagonal_sum(matrix1)
        sum2 = self.calculate_diagonal_sum(matrix2)

        self.result_label.setText(f'Сумма элементов вне главной диагонали матрицы 1: {sum1}\n'
                                 f'Сумма элементов вне главной диагонали матрицы 2: {sum2}')

    def calculate_diagonal_sum(self, matrix):
        total_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != j:
                    total_sum += matrix[i][j]
        return total_sum

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MatrixSumApp()
    ex.show()
    sys.exit(app.exec_())
