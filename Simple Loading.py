from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(451, 195)
		MainWindow.setMinimumSize(QtCore.QSize(451, 195))
		MainWindow.setMaximumSize(QtCore.QSize(451, 195))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
		self.progressBar.setGeometry(QtCore.QRect(10, 10, 441, 31))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.loadit())
		self.pushButton.setGeometry(QtCore.QRect(150, 110, 161, 41))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(20)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	i=1
	def loadit(self):
		global i
		self.progressBar.setProperty("value",self.i)
		if self.i!=100:
			self.i+=1
			QtCore.QTimer.singleShot(100,self.loadit)
		else:
			return
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Start Loading"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
