from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QTableView, QApplication
import sys


class DB:
  def __init__(self) -> None:
    self.conn()

  def conn(self):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')

    if not db.open():
      QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
        QtGui.qApp.tr("Unable to establish a database connection.\n"),
        QtGui.QMessageBox.Cancel)

      return False

    self.query = QSqlQuery()
    return True

  def createTable(self):
    q = QSqlQuery()
    q.exec(f"""
      CREATE TABLE radiotheaters(
        id int primary key,
        title varchar(20),
        content varchar(100),
        date TEXT
      )
    """)

  def insertRow(self, **kwargs):
    # Creating a query for later execution using .prepare()
    q = QSqlQuery()
    q.exec()
    q.prepare(
          """
          INSERT INTO radiotheaters (
                  title,
                  content,
                  date
          )
          VALUES (?, ?, ?)
          """
    )

    q.addBindValue(kwargs['title'])
    q.addBindValue(kwargs['content'])
    q.addBindValue(kwargs['date'])
    q.exec()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  db = DB()
  db.createTable()

  news_title = 'Title of news 1'
  content = 'Content Content ContentContent Content'
  date = '23.10.2022'

  db.insertRow(title=news_title, content=content, date=date)