import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	# main = qtw.QWidget(cursor=qtc.Qt.CursorShape.WaitCursor)
	# main.setCursor(qtc.Qt.CursorShape.WaitCursor)

	label1 = qtw.QLabel(main)
	label1.setText('Hello World')

	leUserName = qtw.QLineEdit(main)
	main.show()

	sys.exit(app.exec())
