from re import L
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from loginForm import LoginForm

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)



		self.lineEdit1 = qtw.QLineEdit()
		# self.btnShowForm()

		self.mainLayout = qtw.QVBoxLayout(self)

		self.setWindowTitle('')
		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()


	# loginForm = LoginForm()
	# loginForm.show()

	sys.exit(app.exec())
