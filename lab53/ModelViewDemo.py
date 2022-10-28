import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from db import DB


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)


		self.setupModelView()

		self.setWindowTitle('')
		self.show();

	def get_data(self):
		db = DB()
		data = db.select_all_rows()

		return data

	def setupModelView(self):
		# initialize the model
		self.model = qtg.QStandardItemModel()

		# setup table view
		table_view = qtw.QTableView()
		# table_view.SelectionMode(3)

		# set up the view to display items in the model
		table_view.setModel(self.model)

		# Set initial row and column values
		self.model.setRowCount(3)
		self.model.setColumnCount(4)

		# load data
		rows = self.get_data()

		for i, row in enumerate(rows):
			items = [qtg.QStandardItem(item) for item in row]
			self.model.insertRow(i, items)

		v_box = qtw.QVBoxLayout()
		v_box.addWidget(table_view)
		self.setLayout(v_box)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
