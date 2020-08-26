import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
import sys
import functools

class Main(QMainWindow):
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.w = QWidget()
		self.setCentralWidget(self.w)
		self.Vbox()
	
	def Vbox(self):
		self.vbox = QVBoxLayout()
		self.w.setLayout(self.vbox)
		self.vbox.setAlignment(Qt.AlignTop)
		self.display()
		self.inpu()
		self.Hbox()
	
	def  display(self):
		self.label = QLabel()
		self.label.setFixedSize(1050,500)
		self.label.setContentsMargins(-1,-1,-1,0)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setText('display')
		self.label.setStyleSheet("border: 5px solid black;")
		self.label.setWordWrap(True)
		self.vbox.addWidget(self.label)
		
		
	def inpu(self):
		self.edit = QPlainTextEdit()
		self.edit.setFixedSize(1050,800)
		self.edit.setPlaceholderText('type SQL commands')
		self.vbox.addWidget(self.edit)
		self.edit.setStyleSheet('border: 10px solid black;')
		self.vbox.setContentsMargins(-1,0,-1,-1)
		self.edit.resize(700,900)
	
	def Hbox(self):
		self.hbox = QHBoxLayout()
		self.vbox.addLayout(self.hbox)
		#self.hbox.setAlignment(Qt.AlignBottom)
		self.button()
	
	def button(self):
		self.btnexec = QPushButton()
		self.btnexec.setText('execute')
		self.btnexec.clicked.connect(self.command)
		self.hbox.addWidget(self.btnexec)
		
		self.btnclear = QPushButton()
		self.btnclear.setText('clear')
		self.btnclear.clicked.connect(self.edit.clear)
		self.hbox.addWidget(self.btnclear)
		self.btnfetch = QPushButton()
		self.btnfetch.setText('Fetch data')
		self.btnfetch.clicked.connect(self.fetch)
		self.vbox.addWidget(self.btnfetch)
		
	def connect(self):
		try:
			connection = sqlite3.connect('/storage/emulated/0/databasetutor/mydata.sqlite')
		except:
			self.label.setText('can\'t connect to database')
		
		return connection

	def command(self):
		if self.edit.toPlainText() != '':
			
			connection = self.connect()
			cursor = connection.cursor()
			try:
				cursor.execute(self.edit.toPlainText())
				connection.commit()
				self.label.setText('executed successfully')
				
			
			except:
				self.label.setText('an error occurred')
				
		else:
			self.label.setText('command empty!')
		
	
	def fetch (self):
		if self.edit.toPlainText() != '':
			
			connection = self.connect()
			cursor = connection.cursor()
			result = None
			data = []
			try:
				cursor.execute(self.edit.toPlainText())
				result = cursor.fetchall()
				for users in result:
					data.append(users)
				self.label.setText(str(data))
			except:
				self.label.setText('an error occurred')
				
		else:
			self.label.setText('command empty!')
		
		
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec())
	
	
	
	

	
		
	


