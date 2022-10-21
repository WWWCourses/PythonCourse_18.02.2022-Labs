from ast import main
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		lbl1 = qtw.QLabel('Welcome')
		self.btnSubmit = qtw.QPushButton('Submit')
		btnCancel = qtw.QPushButton('Cancel')
		btnCancel.setObjectName('btnCancel')

		btnCancel.setStyleSheet("""
			background-color:purple;
			padding:10px;
		""")

		btnCheck = qtw.QCheckBox()
		btnRadio = qtw.QRadioButton()


		mainLayout = qtw.QVBoxLayout(self)
		mainLayout.addWidget(lbl1)
		# mainLayout.addWidget(self.btnSubmit)
		mainLayout.addWidget(btnCancel)

		hLayout = qtw.QHBoxLayout()
		hLayout.addWidget(btnCheck)
		hLayout.addWidget(self.btnSubmit)
		mainLayout.addLayout(hLayout)
		mainLayout.addWidget(btnRadio)

		btnCheck.clicked.connect(self.changeStyle)

		self.applyStyleSheet()

		self.setWindowTitle('Style Sheet Demo')
		self.show()

	def changeStyle(self, checked):
		if checked:
			self.btnSubmit.setStyleSheet("""
				font-size:50px
			""")
		else:
			self.btnSubmit.setStyleSheet("""
				font-size:10px
			""")


	def applyStyleSheet(self):
		with open('./main.css','r') as f:
			mainStyle = f.read()

		self.setStyleSheet(mainStyle)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()


	sys.exit(app.exec())
