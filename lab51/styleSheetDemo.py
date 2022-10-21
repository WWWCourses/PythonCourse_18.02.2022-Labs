from ast import main
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		lbl1 = qtw.QLabel('Welcome')
		btnSubmit = qtw.QPushButton('Submit')

		mainLayout = qtw.QVBoxLayout(self)
		mainLayout.addWidget(lbl1)
		mainLayout.addWidget(btnSubmit)


		self.applyStyleSheet()

		self.setWindowTitle('Style Sheet Demo')
		self.show()

	def applyStyleSheet(self):
		with open('./main.css','r') as f:
			mainStyle = f.read()

		self.setStyleSheet(mainStyle)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
