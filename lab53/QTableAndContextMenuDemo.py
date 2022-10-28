import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from db import DB


class Table(qtw.QTableWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		data = self.get_data()

		for row_idx,row in enumerate(data):
			for col_idx,el in enumerate(row):
				# TODO: why not works
				print(type(data[row_idx][col_idx]))

				item = str(data[row_idx][col_idx])

				self.setItem(row_idx, col_idx, qtw.QTableWidgetItem(item))

		self.setColumnCount(len(data[0]))
		self.setRowCount(len(data))

		self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
		self.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

		self.resizeColumnsToContents()
		self.resizeRowsToContents()

		self.createTableAction()
		# self.set_style()

	def createTableAction(self):
		#  create our custom QActions
		self.add_above_action = qtg.QAction("Add row above", self)
		self.add_above_action.triggered.connect(lambda: self.insertRow(self.currentRow()))
		self.add_bellow_action = qtg.QAction("Add row bellow", self)
		self.add_bellow_action.triggered.connect(
			lambda: self.insertRow(self.currentRow()+1)
		)

	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_above_action)
		context_menu.addAction(self.add_bellow_action)

		# By passing the event's position as argument we ensure that the context menu appears at the expected position.
		context_menu.exec(event.globalPos())

	def get_data(self):
		db = DB()
		data = db.select_all_rows()

		return data

	def set_style(self):
		# Red:
		# 	0 - F = 0-15;
		# 	00 - FF = 0-65535;
		style = """
			QTableWidget{
				border: 10px outset #37f4ff
			}

			QTableWidget::item{
				border: 1px dotted #37f4ff
			}

			QTableWidget::item::selected{
				background-color: #F00;

			}
		"""

		self.setStyleSheet(style)

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.table = Table()
		self.table.setParent(self)

		self.setWindowTitle('')
		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
