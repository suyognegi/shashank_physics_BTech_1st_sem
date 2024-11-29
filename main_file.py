import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel, QPushButton, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
from mpmath import diff
from sympy import latex, sympify, symbols


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w1.ui", self)

        self.pushButton.clicked.connect(self.button_function)


    def button_function(self):
        print("1P pushButton clicked")
        call_window = Choice()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w_c.ui", self)


        self.pushButton.clicked.connect(self.second_page_button)


        self.pushButton_2.clicked.connect(self.third_page_button)


        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def second_page_button(self):
        print("2P pushButton clicked")
        call_window = SecondPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def third_page_button(self):
        print("2P pushButton clicked")
        call_window = ThirdPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w2_i.ui", self)

        self.pushButton.clicked.connect(self.button_function)



        self.label_5.setMouseTracking(True)
        self.label_5.enterEvent = self.mouseEntered
        self.label_5.leaveEvent = self.mouseLeft


        self.label_6.setVisible(False)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def mouseEntered(self, event):

        self.label_6.setVisible(True)
        event.accept()

    def mouseLeft(self, event):

        self.label_6.setVisible(False)
        event.accept()

    def button_function(self):
        print(f"2P pushButton clicked\n{self.lineEdit.text()}")
        call_window = SecondPageTwo(self.lineEdit.text())
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from sympy import symbols, sympify, diff, latex
import matplotlib.pyplot as plt




class SecondPageTwo(QMainWindow):
    def __init__(self, equation):
        super().__init__()
        loadUi("w2_ii.ui", self)


        self.calculate_and_display_derivative(equation)

        self.pushButton.clicked.connect(self.back)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def back(self):
        print("2P2 pushButton clicked")
        call_window = SecondPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def calculate_and_display_derivative(self, equation):
        try:
            x = symbols('x')

            expression = sympify(equation)

            derivative = diff(expression, x)


            expression_latex = latex(expression)
            derivative_latex = latex(derivative)


            fig, ax = plt.subplots()
            ax.axis("off")
            ax.text(0.0, 0.5,
                    f"Derivative of ${expression_latex}$ is:\n${derivative_latex}$",
                    fontsize=14, ha='right', va='center', color='white')


            output_path = "derivative_output.png"
            fig.savefig(output_path, bbox_inches='tight', pad_inches=0.1, dpi=150, transparent=True)
            plt.close(fig)


            pixmap = QPixmap(output_path)
            if pixmap.isNull():
                self.label_result.setText("Error loading image")
            else:
                self.label_result.setPixmap(pixmap)

        except Exception as e:

            QMessageBox.critical(None, "Calculation Error", f"Error : {e}")
            self.label_result.setText(f"Error: {e}")

class ThirdPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_i.ui",self)

        self.pushButton.clicked.connect(self.next)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def next(self):
        call_window=ThirdPageDiagram()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ThirdPageDiagram(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_d.ui",self)

        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        call_window=ThirdPageTwo()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        call_window=ThirdPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ThirdPageTwo(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_ii.ui", self)

        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def next(self):
        print("debug")
        call_window = ThirdPageThree()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("debug 2")


    def back(self):
        call_window = ThirdPageDiagram()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ThirdPageThree(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_iii.ui", self)

        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_HOME.clicked.connect(self.home_button)

    def home_button(self):
        call_window=FirstPage()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def next(self):

        call_window = ThirdPageForth()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        call_window = ThirdPageTwo()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ThirdPageForth(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_iv.ui", self)

        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.back)

    def next(self):
        call_window = ThirdPageFifth()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def back(self):
        call_window = ThirdPageThree()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ThirdPageFifth(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("w3_v.ui", self)


        self.pushButton_2.clicked.connect(self.back)


    def back(self):
        call_window = ThirdPageForth()
        widget.addWidget(call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_wind = FirstPage()
    widget.addWidget(main_wind)
    widget.setFixedSize(main_wind.size())
    widget.show()
    sys.exit(app.exec())
