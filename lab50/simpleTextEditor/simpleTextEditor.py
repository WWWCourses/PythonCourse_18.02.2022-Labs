import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.textedit = qtw.QTextEdit()

		self.setCentralWidget(self.textedit)

		self.create_menubar()
		self.create_toolbar()
		self.create_dock_widget()
		self.create_status_bar()
		self.add_actions()

		self.textedit.textChanged.connect(lambda: self.charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
		)

		self.setWindowTitle('My text editor')
		self.show()

	def create_menubar(self):
		# set the menu bar
		self.menubar = self.menuBar()

		# add menu items
		self.file_menu = self.menubar.addMenu('File')
		self.edit_menu = self.menubar.addMenu('Edit')
		self.help_menu = self.menubar.addMenu('Help')

	def create_toolbar(self):
		self.toolbar = self.addToolBar('File')

		self.toolbar.setMovable(True)
		self.toolbar.setFloatable(True)

		# for Qt6:
		self.toolbar.setAllowedAreas(
			qtc.Qt.ToolBarArea.TopToolBarArea |
			qtc.Qt.ToolBarArea.BottomToolBarArea
		)

	def create_dock_widget(self):
		self.dock = qtw.QDockWidget("Replace")
		self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

		# set dock widget to move and float (but not closeable)
		self.dock.setFeatures(
			# for pyqt6
			qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
			qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable |
			qtw.QDockWidget.DockWidgetFeature.DockWidgetClosable
		)

		self.replace_widget = qtw.QWidget()
		self.replace_widget.setLayout(qtw.QVBoxLayout())

		self.search_text_input = qtw.QLineEdit()
		self.search_text_input.setPlaceholderText('search')
		self.replace_text_input = qtw.QLineEdit()
		self.replace_text_input.setPlaceholderText('replace')

		search_and_replace_btn = qtw.QPushButton(
			"Search and Replace",
		)
		search_and_replace_btn.clicked.connect(self.search_and_replace)

		# create image
		img = qtg.QPixmap('./github.png')
		imgLabel = qtw.QLabel()
		imgLabel.setPixmap(img)


		self.replace_widget.layout().addWidget(self.search_text_input)
		self.replace_widget.layout().addWidget(self.replace_text_input)
		self.replace_widget.layout().addWidget(search_and_replace_btn)
		self.replace_widget.layout().addWidget(imgLabel)
		self.replace_widget.layout().addStretch()

		self.dock.setWidget(self.replace_widget)

	def create_status_bar(self):
		# create status bar widget and atach it to main window:
		self.status_bar = qtw.QStatusBar()
		self.setStatusBar(self.status_bar)

		# show temporary message for 3 second:
		self.status_bar.showMessage('Welcome to My Text Editor',3000)

		# permanent message:
		self.charcount_label = qtw.QLabel("chars: 0")
		self.status_bar.addPermanentWidget(self.charcount_label)

	def add_actions(self):
		# add File actions
		self.open_action = self.file_menu.addAction('Open')
		self.open_action.triggered.connect(self.open_file)

		self.save_action = self.file_menu.addAction('Save')

		# add separator
		self.file_menu.addSeparator()

		quit_action = self.file_menu.addAction('Quit', self.close)

		# add Edit actions
		undo_action = self.edit_menu.addAction('Undo', self.textedit.undo)

		# create a QAction manually
		redo_action = qtg.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)

		self.edit_menu.addAction(redo_action)

		self.edit_menu.addAction('Set Font…', self.set_font)
		self.edit_menu.addAction('Settings…', self.show_settings)

		# add Help actions
		self.about_action = qtg.QAction(
			self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton),
			'About',
			self  # important to pass the parent!
		)

		self.about_action.triggered.connect(lambda : qtw.QMessageBox.information(self,'About','@2022'))

		self.toolbar.addAction(self.about_action)
		self.help_menu.addAction(self.about_action)

		self.toolbar.addAction(self.open_action)


	def open_file(self):
		self.file_path, filter_type = qtw.QFileDialog.getOpenFileName(self, "Open new file","", "All files (*)")
		if self.file_path:
			with open(self.file_path, "r") as f:
				file_contents = f.read()
				self.setWindowTitle(self.file_path)
				self.textedit.setText(file_contents)

	def set_font(self):
		pass

	def show_settings(self):
		pass

	def search_and_replace(self):
		pass

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
