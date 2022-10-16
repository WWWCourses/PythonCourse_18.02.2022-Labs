import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from loginForm import LoginForm
from db import DB

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.db = DB(user='test', password='test1234', db='pyqtDemos')

		self.loginForm = LoginForm(self)
		# connect form submit with onLoginFormSubmit
		self.loginForm.submit.connect(self.onLoginFormSubmit)
		self.loginForm.cancel.connect(self.close)

		self.setWindowTitle('Login Form with DB')
		self.show();

	@qtc.pyqtSlot(str,str)
	def onLoginFormSubmit(self, userName, password):
		print('onLoginFormSubmit')
		# print(userName, password)
		authenticated = self.db.authenticate(userName, password)

		if authenticated:
			qtw.QMessageBox.information(self, 'Login Successful', 'Welcome')
		else:
			qtw.QMessageBox.critical(self, 'Error', 'Login Failed')

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	winodw = MainWindow()

	sys.exit(app.exec())
