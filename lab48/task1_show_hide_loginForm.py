import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from loginForm import LoginForm


class MainWindow(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		btnShowHide = qtw.QPushButton('Show/hide output')
		# lblOutput = qtw.QLabel('Output')

		self.loginForm = LoginForm()
		# self.loginForm.show()

		mainLayout = qtw.QVBoxLayout()
		mainLayout.addWidget(btnShowHide)
		# mainLayout.addWidget(lblOutput)

		self.setLayout(mainLayout)
		self.setWindowTitle('Show Hide Task')

		# self.lblOutput = lblOutput
		self.show();

		btnShowHide.clicked.connect(self.onBtnClick )

	def onBtnClick(self):
		# get loginForm visibility
		outputVisibility = self.loginForm.isVisible()

		if outputVisibility == True:
			self.loginForm.hide()
		else:
			self.loginForm.show()


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)

	window = MainWindow()
	window.setGeometry(200, 400, 200, 200)



	sys.exit(app.exec())
