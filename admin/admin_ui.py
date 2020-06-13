import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtNetwork import *
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_grid = QVBoxLayout()
        
        car_info_grid = QGridLayout()
        
        cctv_frame = QGridLayout()
        #CCTV Web View 
        self.setLayout(main_grid)


        self.webview=QtWebEngineWidgets.QWebEngineView()
        #cctv_frame.addWidget(self.webview, 0 , 0 )
        self.webview.setUrl(QUrl("http://169.254.154.104:8981/cam_pic_new.php"))
        self.webview.resize(400 , 100)

        #출차 정보 Grid_Layout 
        self.info_list = QListView()
        #info_list.resize( 10 , 10)
        #car_info_grid.addWidget( info_list , 0,0)


        #main layout에 넣기
        main_grid.addWidget( self.webview   )
        #main_grid.addWidget( self.info_list )
        
        self.setWindowTitle('Park Admin')
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())