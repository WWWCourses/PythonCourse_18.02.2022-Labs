import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		btn1 = qtw.QPushButton('Click me')
		le1 = qtw.QLineEdit()
		le2 = qtw.QLineEdit()
		self.leOutput = qtw.QLabel('Output')

		btnClose = qtw.QPushButton('Exit')

		# connect clicked signal to onBtnClick:
		btn1.clicked.connect( self.someSlot1 )
		btn1.clicked.connect( self.someSlot2 )
		# btn1.clicked.connect( self.close )

		# le1.textChanged.connect(self.someSlot1 )
		le1.textChanged.connect( lambda text:  print(text.upper()) )


		mainLayout = qtw.QVBoxLayout()
		mainLayout.addWidget(btn1)
		mainLayout.addWidget(le1)
		mainLayout.addWidget(self.leOutput)
		mainLayout.addWidget(le2)
		mainLayout.addWidget(btnClose)

		self.setLayout(mainLayout)
		self.setWindowTitle('')

		self.show();

	# custom slot
	def someSlot1(self, text):
		print(text.upper())


	def someSlot2(self):
		print('someSlot2 called!')



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
