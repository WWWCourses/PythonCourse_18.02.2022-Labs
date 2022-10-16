from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc


class LoginForm(qtw.QWidget):
	submit = qtc.pyqtSignal(str,str)
	cancel = qtc.pyqtSignal()


	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create child widgets:
		self.leUserName = qtw.QLineEdit(self)
		self.lePassword = qtw.QLineEdit(self)
		self.lePassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

		btnLogin = qtw.QPushButton('Login')
		btnLogin.clicked.connect(self.onLoginClick)

		btnCancel = qtw.QPushButton('Cancel')
		# btnCancel.clicked.connect(onCancelClick)
		btnCancel.clicked.connect(lambda :self.cancel.emit())

		# create buttons layout:
		btnLayout = qtw.QHBoxLayout()
		btnLayout.addWidget(btnLogin,1)
		btnLayout.insertStretch(1,1)
		btnLayout.addWidget(btnCancel, 1)

		# create main Form layout
		mainLayout = qtw.QFormLayout()
		mainLayout.addRow('User Name', self.leUserName)
		mainLayout.addRow('Password', self.lePassword)
		mainLayout.addRow('', btnLayout)

		# attach mainLayout to our LoginForm widget (self)
		self.setLayout(mainLayout)

		# set some properties of LoginForm widget(self)
		self.setWindowTitle('Login Form')
		self.resize(300, 150)
		# self.setGeometry(0, 0, 1024, 680)

	@qtc.pyqtSlot()
	def onLoginClick(self):
		print('Login clicked')
		self.submit.emit(self.leUserName.text(),self.lePassword.text())

	# @qtc.pyqtSlot()
	# def onCancelClick(self):
	# 	self.cancel.emit()

