import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # --------------------------- your code starts here -------------------------- #
    # lblHello = qtw.QLabel(self, 'Hello')

    # ---------------------------- your code ends here --------------------------- #
    self.show();

  # ------------------------ create your methods here -------------------------- #

if __name__ == '__main__':
  app = qtw.QApplication(sys.argv);

  window = MainWindow()

  sys.exit(app.exec())