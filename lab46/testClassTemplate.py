import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('My App')

		label1 = qtw.QLabel(self)
		# label1.setText('Hello World')

		leUserName = qtw.QLineEdit(self)
		self.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow(cursor=qtc.Qt.CursorShape.WaitCursor)

	sys.exit(app.exec())
