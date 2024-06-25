from tkinter import *
from tkinter import ttk
import mysql.connector
import pymysql
from tkinter  import messagebox


class Student:
    # ---------------انشاء نافذه البرنامج-------------------
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x690+80+50')
        self.root.title('School Management System')
        self.root.configure(background='silver')
        self.root.iconbitmap("C:\\Users\\AHMED DAWOD\\Desktop\\student_logo.ico")
        self.root.resizable(False, False)
        title = Label(self.root, text='Student Registration System', bg='#1681C9', fg='white',
        font=('monospace', 12, 'bold'))
        title.pack(fill=X)
    #--------------------variables----------------------
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()
        self.moahel_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.search_var=StringVar()
        self.search_by=StringVar()
        self.del_var=StringVar()
    # -------------------ادوات التحكم بالبرنامج--------------------
        manage_frame=Frame(self.root,bg='white')
        manage_frame.place(x=1140,y=25,width=210,height=400)
        lbl_ID=Label(manage_frame,text='الرقم التسلسلي',bg='white')
        lbl_ID.pack()
        ID_Entry=Entry(manage_frame,textvariable=self.id_var,bd=2,justify='center')
        ID_Entry.pack()
        lbl_name = Label(manage_frame, text='اسم الطالب', bg='white')
        lbl_name.pack()
        Name_Entry = Entry(manage_frame,textvariable=self.name_var, bd=2, justify='center')
        Name_Entry.pack()
        lbl_email = Label(manage_frame, text='ايميل الطالب', bg='white')
        lbl_email.pack()
        email_Entry = Entry(manage_frame,textvariable=self.email_var, bd=2, justify='center')
        email_Entry.pack()
        lbl_phone = Label(manage_frame, text='هاتف الطالب', bg='white')
        lbl_phone.pack()
        phone_Entry = Entry(manage_frame,textvariable=self.phone_var, bd=2, justify='center')
        phone_Entry.pack()
        lbl_certi = Label(manage_frame, text='مؤهلات الطالب', bg='white')
        lbl_certi.pack()
        certi_Entry = Entry(manage_frame,textvariable=self.moahel_var, bd=2, justify='center')
        certi_Entry.pack()
        lbl_address = Label(manage_frame, text='عنوان الطالب', bg='white')
        lbl_address.pack()
        address_Entry = Entry(manage_frame,textvariable=self.address_var, bd=2, justify='center')
        address_Entry.pack()
        lbl_gender = Label(manage_frame, text='جنس الطالب', bg='white')
        lbl_gender.pack()
        combo_gender=ttk.Combobox(manage_frame,values=('ذكر','انثى'),state='readonly',textvariable=self.gender_var)
        combo_gender.pack()
        lbl_delete = Label(manage_frame, text='حذف طالب بالاسم', bg='white',fg='red')
        lbl_delete.pack()
        delete_Entry = Entry(manage_frame,textvariable=self.del_var, bd=2, justify='center')
        delete_Entry.pack()

    #-----------------الازرار ------------------------
        btn_frame=Frame(self.root,bg='white')
        btn_frame.place(x=1140,y=430,width=210,height=260)
        title1=Label(btn_frame,text='لوحه التحكم',font=('Deco',14),fg='white',bg='#2471A3')
        title1.pack(fill=X)
        add_btn=Button(btn_frame,text='اضافه طالب',bg='#AEB6BF',fg='white',command=self.add_student)
        add_btn.place(x=33,y=35,width=150,height=30)
        del_btn = Button(btn_frame, text='حذف طالب', bg='#AEB6BF',fg='white',command=self.delete)
        del_btn.place(x=33, y=70, width=150, height=30)
        update_btn = Button(btn_frame, text='تعديل بيانات طالب', bg='#AEB6BF',fg='white',command=self.update)
        update_btn.place(x=33, y=105, width=150, height=30)
        clear_btn = Button(btn_frame, text='افراغ الحقول', bg='#AEB6BF',fg='white',command=self.clear)
        clear_btn.place(x=33, y=140, width=150, height=30)
        about_btn = Button(btn_frame, text='من نحن', bg='#AEB6BF',fg='white',command=self.about )
        about_btn.place(x=33, y=175, width=150, height=30)
        exit_btn = Button(btn_frame, text='اغلاق البرنامج', bg='#AEB6BF',fg='white',command=root.quit)
        exit_btn.place(x=33, y=210, width=150, height=30)

    #----------------نظام البحث-----------------------------
        search_frame=Frame(self.root,bg='white')
        search_frame.place(x=1,y=25,width=1137,height=50)
        lbl_search=Label(search_frame,text='البحث عن طالب',bg='white')
        lbl_search.place(x=1037,y=12)
        combo_search=ttk.Combobox(search_frame,justify='right',values=('id','name','email','phone'),state='readonly',textvariable=self.search_by)
        combo_search.place(x=888,y=12)
        search_entry=Entry(search_frame,textvariable=self.search_var,justify='right',bd=2)
        search_entry.place(x=748,y=12)
        search_btn=Button(search_frame,text='بحث',bg='#2874A6',fg='white',command=self.search)
        search_btn.place(x=630,y=12,width=100,height=22)
    #--------------------عرض النتائج والبيانات------------------------
        Details_frame=Frame(self.root,bg='#F2F4F4')
        Details_frame.place(x=1,y=80,width=1137,height=609)

        scroll_x=Scrollbar(Details_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Details_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Details_frame,
        columns=('address','gender','certi','phone','email','name','ID'),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table.place(x=15,y=1,width=1135,height=590)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table['show']='headings'
        self.student_table.heading('ID', text='الرقم التسلسلي')
        self.student_table.heading('gender', text='جنس الطالب')
        self.student_table.heading('certi', text='مؤهلات الطالب')
        self.student_table.heading('phone', text='رقم الهاتف')
        self.student_table.heading('email', text='البريد الالكتروني')
        self.student_table.heading('name', text='اسم الطالب')
        self.student_table.heading('address', text='عنوان الطالب')
        self.student_table.column('address',width=125,anchor="center")
        self.student_table.column('gender',width=30,anchor="center")
        self.student_table.column('certi',width=65,anchor="center")
        self.student_table.column('phone',width=65,anchor="center")
        self.student_table.column('email',width=70,anchor="center")
        self.student_table.column('name',width=100,anchor="center")
        self.student_table.column('ID',width=17,anchor="center")
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_all()


#------------------------connect and add database------------------------
    def add_student(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
            )
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
            self.address_var.get(),
            self.gender_var.get(),
            self.moahel_var.get(),
            self.phone_var.get(),
            self.email_var.get(),
            self.name_var.get(),
            self.id_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()



    def fetch_all(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            if rows:
                for row in rows:
                    self.student_table.insert("", END, values=row)
            con.commit()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            con.close()


    def delete(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE name = %s", (self.del_var.get(),))
            con.commit()
            # Debug: print remaining items in the database
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            print("Remaining items after deletion:", rows)
            self.fetch_all()  # Refresh the table after deletion
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            con.close()
        self.clear()  # Clear the entry fields


    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.moahel_var.set('')
        self.gender_var.set('')
        self.address_var.set('')

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[6])
        self.name_var.set(row[5])
        self.email_var.set(row[4])
        self.phone_var.set(row[3])
        self.moahel_var.set(row[2])
        self.gender_var.set(row[1])
        self.address_var.set(row[0])

    def update(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        cur = con.cursor()
        cur.execute("update student set address=%s,gender=%s,moahel=%s,phone=%s,email=%s,name=%s where id=%s", (
            self.address_var.get(),
            self.gender_var.get(),
            self.moahel_var.get(),
            self.phone_var.get(),
            self.email_var.get(),
            self.name_var.get(),
            self.id_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def about(self):
        messagebox.showinfo("developer Ahmed Dawood","welcome to our first project")


    def search(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        cur=con.cursor()
        cur.execute("select * from student where " +
                    str(self.search_by.get())+" LIKE '%"+str(self.search_var.get())+"%'")

        rows =cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=Student(root)
root.mainloop()

'''
    def fetch_all(self):
        con=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        cur=con.cursor()
        cur.execute("select * from student")
        rows =cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()


    def delete(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        cur = con.cursor()
        cur.execute("delete from student where name =%s",self.del_var.get())
        con.commit()
        self.fetch_all()
        con.close()

'''
