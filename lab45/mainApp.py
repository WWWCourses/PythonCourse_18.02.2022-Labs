# 1. import needed QtWidgets classes
import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import PyQt6.QtWidgets as qtw

# 2. the main app instance for our application.
app = qtw.QApplication(sys.argv)

# 3. Create Qt widget, which will be our main window.
window = qtw.QWidget()

btn = qtw.QPushButton('OK',window)
userNameLabel = qtw.QLabel(window,'User Name')



# 4. show the window
window.show()

# 5. Start the event loop
sys.exit( app.exec() )

