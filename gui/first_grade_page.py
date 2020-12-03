from tkinter import *
import pymysql
import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib

from DB.db_connect import DbConnect

db_connect = DbConnect()

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

this_year = datetime.datetime.today().year
this_month = datetime.datetime.today().month
first_index = datetime.date(this_year, this_month, 1).weekday()  # 매달 1일의 인덱스
minus = (3 - first_index) + 15

date = datetime.datetime(this_year, this_month, minus, 16, 30, 0)
pre_date = datetime.datetime(this_year, this_month, minus, 0, 0, 0)
print(pre_date)

class FirstGradePage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        self.mypc_text = Label(text='[1학년] 이달의 우수반', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.mypc_text.place(x=390, y=50)

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        x = [1, 2, 3, 4, 5, 6]
        y = [int(class_1), int(class_2), int(class_3), int(class_4), int(class_5), int(class_6)]

        plt.bar(x, y, color='#FF6347')
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=180, y=120)

        print(y)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_menu, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        for i in range(len(y)):
            if y[i] == max(y):
                self.search_ip_text = Label(text=str(i+1) + "반이 기한내에 가장 빨리 제출했습니다.", bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
                self.search_ip_text.place(x=300, y=100)

        self.window.mainloop()

    def db_connect(self):

        query = "SELECT this_month from mypc_table where hakbun like '11%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 990
        class_1 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '12%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_2 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '13%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_3 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '14%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_4 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '15%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_5 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '16%'"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                            (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)
                print(round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600))


        avg = time_sum//720
        class_6 = str(avg)


        return class_1, class_2, class_3, class_4, class_5, class_6

    def go_menu(self):
        from gui.best_class_mypc import BestClassMypc
        self.window.destroy()
        BestClassMypc()