import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtNetwork import *
from PyQt5.QtCore import QUrl 
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtGui import *
import requests
import cv2
import threading
import time
from functools import partial

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Main Layout
        self.main_hbox_layout = QHBoxLayout()
        
        #CCTV View Layout
        self.main_hbox_layout.addLayout(self.cctv_view_init())
        
         #Parking Car Infomation View Layout
        self.main_hbox_layout.addLayout(self.parking_info_view_init())

        self.setLayout( self.main_hbox_layout )
        self.showMaximized()

        
    #CCTV Web View 로 보여줄 레이아웃 초기화
    def cctv_view_init(self):
        self.ccvt_view_layout = QVBoxLayout()
        self.cctv_widget = QLabel()

        #video stream
        self.ccvt_view_layout.addWidget(self.cctv_widget)
        view_thread = threading.Thread( target=self.cctv_streaming )
        view_thread.daemon = True
        view_thread.start()

        return self.ccvt_view_layout


    #주차정보 레이아웃 초기화
    def parking_info_view_init(self):
        self.parking_car_layout = QVBoxLayout()
        self.info_tab = QTabWidget()
        
        self.car_info_table = QTableWidget( 3 , 6 )
        self.car_info_table.setHorizontalHeaderLabels(["주차위치" ,"차번호", "들어온 시간","나간 시간", "가격", "결제"])
        self.car_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.car_info_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.info_tab.addTab( self.car_info_table , "결제기록")

        self.parking_car_layout.addWidget(self.info_tab)


        self.insert_btn = QPushButton("Refresh")
        self.insert_btn.clicked.connect(self.parking_list_table)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.insert_btn)
        self.button_layout.addWidget(self.remove_btn)
        self.parking_car_layout.addLayout( self.button_layout )

        return self.parking_car_layout


    def parking_list_table(self):
        response = requests.get("http://localhost:8080/ParkingServer/parking/list")
        data_list = response.json()
        rowCount = self.car_info_table.rowCount()
        for i in range(rowCount):
            self.car_info_table.removeRow(0)

        for i, data in enumerate(data_list):
            self.car_info_table.insertRow( i )
            self.car_info_table.setItem( i , 0 , QTableWidgetItem(data['parkingPosition']))
            self.car_info_table.setItem( i , 1 , QTableWidgetItem(data['carNumber']))
            self.car_info_table.setItem( i , 2 , QTableWidgetItem(data['enterTime']))
            if 'exitTime' in data.keys() : 
                self.car_info_table.setItem( i , 3 , QTableWidgetItem(data['exitTime']))
            if 'parkingPrice' in data.keys(): 
                self.car_info_table.setItem( i , 4 , QTableWidgetItem(str(data['parkingPrice'])))

            paymentData = None
            if data['payment'] == 'T':
                paymentData = QTableWidgetItem("결제완료")
                self.car_info_table.setItem( i , 5 , paymentData)
            else : 
                paymentData = QPushButton("결제")
                paymentData.clicked.connect(partial( self.payment_parking , data['id']))
                self.car_info_table.setCellWidget( i , 5 , paymentData)


            
    def cctv_streaming(self):
        time.sleep(1)
        self.cap = cv2.VideoCapture("http://192.168.137.6:8981/cam_pic_new.php")
        while True:
            ret , frame = self.cap.read()
            img = cv2.cvtColor(frame , cv2.COLOR_BGRA2RGB)
            convertFormat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap(convertFormat)

            self.cctv_widget.setPixmap(pixmap)


    def payment_parking(self , id):
        print( id )
        data = { "id": id}
        resp = requests.get("http://localhost:8080/ParkingServer/parking/payment" , params=data)
        self.parking_list_table()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MyApp()
    sys.exit(app.exec_())