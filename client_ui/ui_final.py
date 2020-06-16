#-*-coding:utf-8-*-
import tkinter as tk
import datetime, time
import socket,threading
import sys
import requests

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("parking system")
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.upper_widgets()
        self.right_widgets()
        self.left_widgets()


    def upper_widgets(self):
        self.upper_frame = tk.Frame(self.master, background="snow")
        self.upper_frame.place(width=800, height=100,relx = 0, rely=0)


        self.car_img = tk.PhotoImage(file="car_img.png")
        self.image_label = tk.Label(self.upper_frame,image=self.car_img, background = "snow")
        self.image_label.place(width=100, height=80, x=30, y=0)


        self.name_label = tk.Label(self.upper_frame, text="Easy parking & pay", font = ("Cabin", 20),fg = "DodgerBlue2",background="snow")
        self.name_label.place(width=300, height=80, x=250, y=0)

        self.now = datetime.datetime.now()
        self.date = self.now.strftime('%Y-%m-%d')
        self.date_label = tk.Label(self.upper_frame, text = self.date, font = ("cabin",13,'bold'), fg = "green3",background="snow")
        self.date_label.place(width = 200, height = 20, x=550, y=15)

        self.time = self.now.strftime('%H:%M')
        self.time_label = tk.Label(self.upper_frame,text=self.time, font = ("cabin",13,'bold'), fg = "green3",background="snow")
        self.time_label.place(width = 200, height = 20, x = 550, y = 35)

        self.exit_btn = tk.Button(self.upper_frame, text="exit", command=self.quit, background="snow" )
        self.exit_btn.place(width=60, height=30, x=730, y=30)

    def left_widgets(self):
        self.left_frame = tk.Frame(self.master, background="snow3")
        self.left_frame.place(width=400, height=530, relx = 0,rely=0.12)

        self.here_img=tk.PhotoImage(file = "icon.png")
        self.out_img = tk.PhotoImage(file = "car_out.png")
        self.in_img = tk.PhotoImage(file = "car_in.png")
        self.pk_lot = []
        self.pk_lot_id = []
        self.pk_lot_state = [] #입출차 여부(0,1)
        #self.pk_lot_cnt =30
        px = 20
        py=30

        for i in range(0,30):
            self.pk_lot_state.append(0) # 입출차 여부(0,1)
            self.pk_lot_id.append("A"+str(i))
            self.pk_lot.append(tk.Label(self.left_frame, text = self.pk_lot_id[i] ,font=('Cabin', 10,'bold'),fg = "blue",image = self.out_img, background = "snow3" ))
            self.pk_lot[i]["compound"]="top"
            self.pk_lot[i].place(width = 60, height = 100, x= px, y = py)
            px += 70
            if(px>350) :
                px = 20
                py+=120
            if(py>500):
                break



    def right_widgets(self):
        self.right_frame = tk.Frame(self.master, background="snow2")
        self.right_frame.place(width=400, height=530, relx = 0.5, rely=0.12)

        self.search_label = tk.Label(self.right_frame, text = "차랑 번호를 입력하세요. (예 : 123가 4567)", background="snow2",
                                     fg="SteelBlue3",font = ("Cabin",10),anchor='w')
        self.search_label.place(x=80, y = 30, width = 300, height=30)


        self.car_num =""
        self.search_ent = tk.Entry(self.right_frame)
        self.search_ent.place(x=80, y= 70, width = 170, height=30)
        self.search_btn = tk.Button(self.right_frame, text="search", relief="raised", background="SteelBlue2")
        self.search_btn.bind("<Button-1>", self.car_check)
        self.search_btn.place(x=280, y = 70, width = 70, height=30)

        self.car_num_label = tk.Label(self.right_frame, text="", background="snow2",anchor='center')
        self.car_num_label.place(x=80, y=110, width=200, height=40)

        self.park_time=""
        self.park_time_label = tk.Label(self.right_frame, text=self.park_time,background="snow2",
                                     fg="SteelBlue3",font = ("Cabin",10),anchor='w' )
        self.park_time_label.place(x=80, y=160, width = 280, height = 20)

        self.park_cost = ""
        self.park_cost_label = tk.Label(self.right_frame, text = self.park_cost,background="snow2",
                                     fg="SteelBlue3",font = ("Cabin",10),anchor='w')
        self.park_cost_label.place(x=80, y=190, width=280, height=20)

        self.park_locate=""
        self.park_locate_label = tk.Label(self.right_frame, text="", background="snow2",
                                        fg="SteelBlue3", font=("Cabin", 10),anchor='w')
        self.park_locate_label.place(x=80, y=220, width=220, height=20)

        self.default_photo = tk.PhotoImage(file = "parking-lot.png")
        #self.car_photo=tk.PhotoImage(file = "car_photo.png")
        self.park_photo_label = tk.Label(self.right_frame, image = self.default_photo, background="snow2", relief="solid")
        self.park_photo_label.place(x=80, y=260, width = 250, height=200)

        self.reset_btn = tk.Button(self.right_frame, text="reset",relief="raised", background="SteelBlue2" )
        self.reset_btn.bind("<Button-1>", self.reset)
        self.reset_btn.place(x=170, y=480, width=70, height=30)



    def exit(self):
       print("프로그램 종료")
       import sys
       sys.exit()

    #날짜, 시간 update
    def now_widgets(self):
        self.time = self.now.strftime('%H:%M')
        self.date = self.now.strftime('%Y-%m-%d')
        self.time_label.configure(text = self.time)
        self.date_label.configure(text = self.date)
        self.upper_frame.after(1000, self.now_widgets)

    #입출차 여부에 따라서 차 색깔 바꾸기
    def change_state(self, i, flag):
        if(not flag):
            self.pk_lot[i].configure(image=self.out_img)
            self.pk_lot_state[i]=0
        else:
            self.pk_lot[i].configure(image=self.in_img)
            self.pk_lot_state[i] = 1


    # 차량 검색 입력값 받기(->전송)
    def car_check(self, event):
        self.car_num=str(self.search_ent.get())
        self.car_num_label.configure(text = "[ "+self.car_num+" ]의 주차 정보 검색 중" )
        msg2 = app.car_num
        param = {'car_number': msg2}
        response = requests.get("http://192.168.22.97:8080/ParkingServer/parking/search", params=param)
        data3 = response.json()
        print(data3)
        self.information(data3)

    def information(self,data3):
        self.p_position = data3['parkingPosition']
        c_num=data3['carNumber']
        e_time=data3['enterTime']
        p_price=str(data3['parkingPrice'])
        self.car_num_label.configure(text="[ " + self.car_num + " ]의 주차 정보")
        self.set_location(self.p_position)
        self.set_time(e_time)
        self.set_cost(p_price)



    #주차된 구역 알려주기(위치 이미지, 구역 출력)
    def set_location(self,loc):
        self.loc=loc
        self.park_locate_label.configure(text = "주차 위치 > "+self.loc )
        idx = self.pk_lot_id.index(self.loc)
        #self.pk_lot_state[idx]=2
        print(self.pk_lot_state[idx])
        self.pk_lot[idx].configure(image=self.here_img)
        #break


     #주차 시각 출력
    def set_time(self, park_time):
        self.park_time_label.configure(text = "주차 시작 시각 > "+park_time)


    def set_cost(self, park_cost):
        #minute=1000
        #start=100
        #end=10
        self.park_cost= park_cost
        self.park_cost_label.configure(text = "예상 주차 요금 > " + self.park_cost+"원" )

    #주차장 영상 출력(open cv)
    def set_photo(self):
        self.park_photo_label['image']=self.car_photo

    #주차 정보 입력 초기화 버튼 이벤트
    def reset(self,event):
        self.car_num=""
        self.car_num_label.configure(text="")
        idx = self.pk_lot_id.index(self.loc)
        self.pk_lot[idx].configure(image=self.in_img)
        #self.pk_lot_state[idx] = 1
        self.park_locate_label.configure(text="")
        self.park_cost_label.configure(text = "" )
        self.park_time_label.configure(text = "")





root = tk.Tk()
app = Application(master=root)

def check_state(client_socket):
    msg = "2"
    client_socket.sendall(msg.encode())
    while True:
        print('data in')
        data = client_socket.recv(1024)
        if not data:
            break
        data2=data.decode('utf-8')
        print('Received from', data2)
        #data2_form [A1:null] 0r[A1:123가4567]
        car = data2.split(":")
        info=car[0]
        flag = car[1] != "NULL"
        print(flag)
        idx = app.pk_lot_id.index(info)
        app.change_state(idx, flag)






HOST='192.168.22.97'
PORT=9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
print('connect')

#주차 상황 실시간 받기
t=threading.Thread(target=check_state, args=(client_socket,))
t.start()





app.mainloop()
