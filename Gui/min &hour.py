from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class main(QMainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.w = QWidget()
		self.setCentralWidget(self.w)
		self.setStyleSheet('background-color:#efefe0;')
		self.setFocus(True)
		self.createHlay()
		
	def createHlay(self):
		self.hlay = QVBoxLayout()
		self.w.setLayout(self.hlay)
		self.hlay.setAlignment(Qt.AlignTop)
		self.Display()
		self.Select()
		self.inpu()
		self.butt()
	
	def Display(self):
		self.display = QLabel()
		self.display.setText('')
		self.display.setFixedSize(1050,500)
		self.display.setAlignment(Qt.AlignCenter)
		self.display.setStyleSheet('border: 10px solid black; color: red; border-radius:30px; font-size:120px; font-weight:bolder;')
		self.display.setContentsMargins(-1,-1,-1,0)
		self.display.setWordWrap(True)
		self.hlay.addWidget(self.display)
	
	def Select(self):
		
		self.div= QPushButton()
		self.div.setStyleSheet('border: 44px solid red; margin-top: 500px;')
		self.div.setFixedSize(1050,90)
		self.hlay.addWidget(self.div)
		
		self.select = QRadioButton('min')
		self.select.setChecked(True)
		#self.select.setAlignment(Qt.AlignTop)
		self.select.toggled.connect(lambda:self.ischecked(self.select.text()))
		self.hlay.addWidget(self.select)
		
		self.select2 = QRadioButton('hour')
		#self.select.setAlignment(Qt.AlignTop)
		self.select.toggled.connect(lambda:self.ischecked(self.select2.text()))
		self.hlay.addWidget(self.select2)
		
		self.div= QPushButton()
		self.div.setStyleSheet('border: 0px solid #fffff1; margin-top: 10px; background-color:red;')
		self.div.setFixedSize(1050,90)
		self.hlay.addWidget(self.div)
		
		self.value = 'min'
	
	def inpu(self):
		self.edit = QLineEdit()
		self.edit.setFixedSize(1050,200)
		self.edit.setStyleSheet('border: 7px solid black;font-weight:bolder; font-size:60px;')
		self.edit.setAlignment(Qt.AlignCenter)
		self.edit.setPlaceholderText('enter sec')
		self.hlay.addWidget(self.edit)
	
	def butt(self):
		self.btn = QPushButton()
		self.btn.setStyleSheet('border: 4px solid black; top: 500px;')
		
		self.btn.setFixedSize(1050,90)
		self.btn.setText('convert')
		self.btn.clicked.connect(self.think)
		self.hlay.addWidget(self.btn)
	
	def think(self):
		data = self.edit.text()
		if data != '':
			try:
				data = int(data)
				if self.value == 'hour':
					self.display.setText(str(Tiime.convert_to_hour(data)))
				else: 
					self.display.setText(str(Tiime.convert_to_min(data)))
			except:
				self.display.setText('invalid characters')
		

	def ischecked(self,x):
		if x == 'min':
				if self.select.isChecked() ==True:
					self.value = x
			
		if x == 'hour':
				if self.select2.isChecked() == True:
					self.value = x
				
class Tiime():
		def convert_to_min(x):
			min = str(x//60)
			sec = str(x % 60)
			return min+':'+sec
		
		def convert_to_hour(x):
			hr = str((x//60)//60)
			
			if x >= 3600:
				min = str(((x//60)%(int(hr)*60)))
			else:	
				min = str(x//60)
			
			sec = str(x%60)
			return hr+':'+min+':'+sec

app = QApplication(sys.argv)
q = main()
q.show()
sys.exit(app.exec())