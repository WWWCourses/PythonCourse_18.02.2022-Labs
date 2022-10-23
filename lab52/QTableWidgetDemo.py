import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		data = [
			['a1aaaaaaaaaaaaaaaa@@@','b1','c1'],
			['a2','b2','c2']
		]

		table = qtw.QTableWidget(self)
		table.setColumnCount(len(data[0]))
		table.setRowCount(len(data))

		# table.setItem(0,0, qtw.QTableWidgetItem(data[0][0]))

		for row_idx,row in enumerate(data):
			for col_idx,el in enumerate(row):
				table.setItem(row_idx, col_idx, qtw.QTableWidgetItem(data[row_idx][col_idx]))

		table.resizeColumnsToContents()
		table.resizeRowsToContents()

		self.createTableAction()
		# self.contextMenuEvent()

		self.setWindowTitle('QTableWidget Demo')
		self.show()

	def createTableAction(self):
		#  create our custom QActions
		self.add_above_action = qtg.QAction("Add row above", self)
		self.add_above_action.triggered.connect(lambda: self.insertRow(self.currentRow()))


	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_above_action)

		# By passing the event's position as argument we ensure that the context menu appears at the expected position.
		context_menu.exec(event.globalPos())


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
