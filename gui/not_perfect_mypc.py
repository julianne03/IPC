import datetime
from tkinter import *
from tkinter import ttk
from DB.db_connect import DbConnect
from model.cal_time import CalTime

db_connect = DbConnect()

class NotPerfectMypc :
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)
        self.trv = ttk.Treeview(columns=(1, 2, 3, 4), show="headings", height="10")
        self.db_connect()

        did_not_start_mypc = Label(text='100점이 아닌 사람 리스트', bg='#ffffff', fg='#3F90CA',
                                   font=("Arial 18 bold"))
        did_not_start_mypc.place(x=50, y=100)

        self.trv.place(x=50, y=170)

        vsb = ttk.Scrollbar(self.window, orient="vertical", command=self.trv.yview)
        vsb.place(x=730 + 200 + 2, y=173, height=400 + 20)

        self.trv.configure(yscrollcommand=vsb.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial 15 bold"))
        style.configure("Treeview", rowheight=40)

        self.trv.tag_configure('style', font=("Arial 15"))

        self.trv.column("#1", width=200, anchor="center")
        self.trv.heading(1, text='학번', anchor="center")

        self.trv.column("#2", width=200, anchor="center")
        self.trv.heading(2, text='제출 시간', anchor="center")

        self.trv.column("#3", width=200, anchor="center")
        self.trv.heading(3, text='score', anchor="center")

        self.trv.column("#4", width=300, anchor="center")
        self.trv.heading(4, text='reason', anchor="center")

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_back, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        smurfs_image = PhotoImage(file='../image/smurf/smurfs_image.png')
        smurfs_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        smurfs_label.place(x=700, y=25)
        smurfs_label.config(image=smurfs_image)

        self.window.mainloop()

    def update(self, rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i, tag='style')

    # db connect
    def db_connect(self):
        cal_time = CalTime()

        start_date = cal_time.start_date
        pre_after_month = cal_time.pre_after_month
        print(pre_after_month)

        query = "SELECT hakbun, this_month, score, reason from mypc_table where 0<score and score<100"

        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        submit_time_list = []

        for i in range(len(rows)):
            slice_year = int(rows[i][1][:4])
            slice_month = int(rows[i][1][5:7])
            slice_day = int(rows[i][1][8:10])
            slice_hour = int(rows[i][1][11:13])
            slice_minute = int(rows[i][1][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            # 이번달 셋째주 목요일 00:00:00 ~ 다음달 셋째주 수요일 23:59:59 사이에 제출했으면
            if start_date < submit_time and pre_after_month > submit_time:
                # 100점이 아닌사람의 행을 넣음
                submit_time_list.append([rows[i][0], rows[i][1], rows[i][2], rows[i][3]])

        self.update(submit_time_list)

    def go_back(self):
        from gui.teacher_menu import TeacherMenu
        self.window.destroy()
        TeacherMenu()