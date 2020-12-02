from tkinter import *
import pymysql
import socket

class SearchIp:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)
        self.new_s = StringVar()
        self.new_ip = StringVar()
        self.new_phone = StringVar()
        self.check_ip = StringVar()
        self.check_phone = StringVar()

        self.question = Label(text="학번을 입력하세요(ex.1101)", bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.question.place(x=125, y=50)

        self.ent = Entry(bg='#272727', fg='#51F591', font=("Arial 18 bold"),textvariable=self.new_s)
        self.ent.place(x=125, y=90)

        search_btn_image = PhotoImage(file='../image/search_btn.png')
        search_btn_click = Button(borderwidth=0, command=self.search, bg='#272727', activebackground='#272727')
        search_btn_click.place(x=805, y=50)
        search_btn_click.config(image=search_btn_image)

        ip_container_image = PhotoImage(file='../image/ip_container.png')
        ip_container_click = Button(borderwidth=0, bg='#272727', activebackground='#272727')
        ip_container_click.place(x=125, y=180)
        ip_container_click.config(image=ip_container_image)

        self.pc_ip_first_text = Label(text='255. 255. 248. 0', bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.pc_ip_first_text.place(x=200, y=350)
        self.pc_ip_second_text = Label(text='10. 96. 120. 254', bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.pc_ip_second_text.place(x=200, y=400)
        self.pc_ip_change = Label(textvariable=self.new_ip, bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.pc_ip_change.place(x=200, y=300)

        self.phone_ip_first_text = Label(text='255. 255. 248. 0', bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.phone_ip_first_text.place(x=580, y=350)
        self.phone_ip_second_text = Label(text='10. 96. 120. 254', bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.phone_ip_second_text.place(x=580, y=400)
        self.phone_ip_change = Label(textvariable=self.new_phone, bg='#6C6C6C', fg='#51F591', font=("Arial 22 bold"))
        self.phone_ip_change.place(x=580, y=300)

        self.check_ip_text = Label(text='사용 여부 : ', bg='#6C6C6C', fg='#F64F4F', font=("Arial 18 bold"))
        self.check_ip_text.place(x=220, y=550)

        self.check_ip_change = Label(textvariable=self.check_ip, bg='#6C6C6C', fg='#F64F4F', font=("Arial 18 bold"))
        self.check_ip_change.place(x=350, y=550)

        self.check_phone_text = Label(text='사용 여부 : ', bg='#6C6C6C', fg='#F64F4F', font=("Arial 18 bold"))
        self.check_phone_text.place(x=600, y=550)

        self.check_phone_change = Label(textvariable=self.check_phone, bg='#6C6C6C', fg='#F64F4F', font=("Arial 18 bold"))
        self.check_phone_change.place(x=750, y=550)

        self.window.mainloop()

    def search(self):
        mydb = pymysql.connect(host="localhost", user="root", password="s2019w36", db="ipc")
        cursor = mydb.cursor()
        hakbun = self.new_s.get()
        query = "select hakbun,pc,phone from ip_table where hakbun=%s"
        cursor.execute(query, (hakbun))
        rows = cursor.fetchall()
        data_list = list(rows[0])
        new_ip = data_list[1]
        new_phone = data_list[2]

        self.update(new_ip,new_phone)
        self.check_internet(new_ip,new_phone)

    def update(self,*data):
        self.new_ip.set(data[0])
        self.new_phone.set(data[1])


    def check_internet(self,ip,phone):
        try :
            socket.gethostbyaddr(ip)
            self.check_ip.set("O")
            print("connected")
        except socket.herror :
            self.check_ip.set("X")
            print("Not connected")

        try :
            socket.gethostbyaddr(phone)
            self.check_phone.set("O")
            print("connected")
        except socket.herror :
            self.check_phone.set("X")
            print ("Unknown host")