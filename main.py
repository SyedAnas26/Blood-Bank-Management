import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import pymysql


def donor_list(blood_group, area):
    view = Tk()
    view.title('Donors List')

    # setup treeview
    columns = ('ID', 'First_Name', 'Last_Name', 'Age', 'Gender', 'Mobile_Number', 'City')

    tree = ttk.Treeview(view, height=20, columns=columns, show='headings')
    tree.grid(row=0, column=0, sticky='news')

    # setup columns attributes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=CENTER)

    con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
    cur = con.cursor()
    cur.execute(
        "select * from donors where blood_group ='" + blood_group + "' and ( city like '%" + area + "%' or address like '%" + area + "%' )")
    rows = cur.fetchall()

    # populate data to treeview
    for rec in rows:
        tree.insert('', 'end', value=rec)

    # scrollbar
    sb = Scrollbar(view, orient=VERTICAL, command=tree.yview)
    sb.grid(row=0, column=1, sticky='ns')
    tree.config(yscrollcommand=sb.set)

    btn = Button(view, text='Exit', command=view.destroy, width=20, bd=2, fg='#eb4d4b')
    btn.grid(row=1, column=0, columnspan=2)


def user_dashboard(user_name):
    def logout():
        dash.destroy()
        login_page()

    dash = Tk()
    dash.title("Dashboard Blood Bank")
    dash.maxsize(width=800, height=500)
    dash.minsize(width=800, height=500)

    bgimg = PhotoImage(file="img/dash.png")
    limg = Label(dash, image=bgimg)
    limg.image = bgimg
    limg.pack()

    # heading label
    heading = Label(dash, text=f"User Name : {user_name.get()}", font='Verdana 15 bold')
    heading.place(x=5, y=25)

    f = Frame(dash, height=1, width=800, bg="green")
    f.place(x=0, y=95)

    con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
    cur = con.cursor()

    cur.execute("select * from donors where user_name ='" + user_name.get() + "'")
    row = cur.fetchall()

    a = Frame(dash, height=1, width=410, bg="green")
    a.place(x=0, y=195)

    b = Frame(dash, height=100, width=1, bg="green")
    b.place(x=410, y=97)

    for data in row:
        first_name_label = Label(dash, text=f"First Name : {data[1]}", font='Verdana 10 bold')
        first_name_label.place(x=20, y=100)

        last_name_label = Label(dash, text=f"Last Name : {data[2]}", font='Verdana 10 bold')
        last_name_label.place(x=20, y=130)

        age_label = Label(dash, text=f"Age : {data[3]}", font='Verdana 10 bold')
        age_label.place(x=20, y=160)

        gender_label = Label(dash, text=f"ID : {data[0]}", font='Verdana 10 bold')
        gender_label.place(x=250, y=100)

        city_label = Label(dash, text=f"City : {data[6]}", font='Verdana 10 bold')
        city_label.place(x=250, y=130)

    # LABELS
    heading_label = Label(dash, text="Search Donors", font='Verdana 16 bold')
    heading_label.place(x=250, y=230)

    blood_label = Label(dash, text="Blood Group:", font='Verdana 10 bold')
    blood_label.place(x=195, y=290)

    area_label = Label(dash, text="Search in Area:", font='Verdana 10 bold')
    area_label.place(x=180, y=340)

    # Variables / Values
    blood_group = StringVar(dash, value="A+")
    area = StringVar(dash)

    # Entries
    blood_entry = OptionMenu(dash, blood_group, *options)
    blood_entry.place(x=300, y=287)

    area_entry = Entry(dash, width=30, textvariable=area)
    area_entry.place(x=300, y=340)

    btn = Button(dash, text="Search", font='Verdana 10 bold', width=20,
                 command=lambda: donor_list(blood_group.get(), area.get()))
    btn.place(x=250, y=400)

    logout_btn = Button(dash, text="Logout", command=logout)
    logout_btn.place(x=730, y=20)


def hosp_dashboard(user_name):
    def logout():
        dash.destroy()
        login_page()

    dash = Tk()
    dash.title("Dashboard Blood Bank")
    dash.maxsize(width=800, height=500)
    dash.minsize(width=800, height=500)

    bgimg = PhotoImage(file="img/dash.png")
    limg = Label(dash, image=bgimg)
    limg.image = bgimg
    limg.pack()

    f = Frame(dash, height=1, width=800, bg="green")
    f.place(x=0, y=95)

    con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
    cur = con.cursor()

    cur.execute("select * from hospital where user_name ='" + user_name.get() + "'")
    row = cur.fetchall()

    # heading label
    heading = Label(dash, text=f"{row[0][1]}", font='Verdana 15 bold')
    heading.place(x=290, y=25)

    # LABELS
    heading_label = Label(dash, text="Search Donors", font='Verdana 16 bold')
    heading_label.place(x=310, y=145)

    blood_label = Label(dash, text="Blood Group:", font='Verdana 10 bold')
    blood_label.place(x=275, y=205)

    area_label = Label(dash, text="Search in Area:", font='Verdana 10 bold')
    area_label.place(x=260, y=255)

    # Variables / Values
    blood_group = StringVar(dash, value="A+")
    area = StringVar()

    # Entries
    blood_entry = OptionMenu(dash, blood_group, *options)
    blood_entry.place(x=380, y=203)

    area_entry = Entry(dash, width=30, textvariable=area)
    area_entry.place(x=380, y=255)

    btn = Button(dash, text="Search", font='Verdana 10 bold', width=15,
                 command=lambda: donor_list(blood_group.get(), area.get()))
    btn.place(x=325, y=300)

    logout_btn = Button(dash, text="Logout", command=logout)
    logout_btn.place(x=730, y=20)


# ----------------------------------------------------------- Signup Window -----------------------------------------

def user_signup():
    # signup database connect
    def action():
        if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" \
                or user_name.get() == "" or password.get() == "" or verify_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != verify_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
                cur = con.cursor()

                cur.execute("select * from donors where user_name=%s", user_name.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                else:
                    cur.execute(
                        "insert into donors(first_name,last_name,age,gender,mobile_number,city,address,user_name,"
                        "password,blood_group) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            age.get(),
                            gender.get(),
                            mobile.get(),
                            city.get(),
                            add.get(),
                            user_name.get(),
                            password.get(),
                            blood_group.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        age_entry.delete(0, END)
        city_entry.delete(0, END)
        add_entry.delete(0, END)
        user_name_entry.delete(0, END)
        password_entry.delete(0, END)
        verify_pass_entry.delete(0, END)

    # start Signup Window
    winsignup = Toplevel()
    winsignup.title("Blood Bank Management")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    bgimg = PhotoImage(file="img/reg.png")
    limg = Label(winsignup, image=bgimg)
    limg.pack()

    # heading label
    heading_label = Label(winsignup, text="Signup", font='Verdana 20 bold')
    heading_label.place(x=80, y=60)

    # Form data labels ------------------------------------------------------------------

    first_name_label = Label(winsignup, text="First Name :", font='Verdana 10 bold')
    first_name_label.place(x=80, y=130)

    last_name_label = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
    last_name_label.place(x=80, y=160)

    age_label = Label(winsignup, text="Age :", font='Verdana 10 bold')
    age_label.place(x=80, y=190)

    gender_label = Label(winsignup, text="Gender :", font='Verdana 10 bold')
    gender_label.place(x=80, y=220)

    mobile_label = Label(winsignup, text="Mobile :", font='Verdana 10 bold')
    mobile_label.place(x=80, y=260)

    city_label = Label(winsignup, text="City :", font='Verdana 10 bold')
    city_label.place(x=80, y=290)

    address_label = Label(winsignup, text="Address :", font='Verdana 10 bold')
    address_label.place(x=80, y=320)

    user_name_label = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name_label.place(x=80, y=350)

    password_label = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password_label.place(x=80, y=380)

    very_pass_label = Label(winsignup, text="Verify Pass:", font='Verdana 10 bold')
    very_pass_label.place(x=80, y=410)

    blood_group_label = Label(winsignup, text="Blood group:", font='Verdana 10 bold')
    blood_group_label.place(x=80, y=445)

    # Variables / Values ------------------------------------------------------------------

    first_name = StringVar(winsignup)
    last_name = StringVar(winsignup)
    city = StringVar(winsignup)
    add = StringVar(winsignup)
    user_name = StringVar(winsignup)
    password = StringVar(winsignup)
    verify_pass = StringVar(winsignup)
    mobile = StringVar(winsignup)

    age = IntVar(winsignup, value=0)
    gender = StringVar(winsignup, value='Male')
    blood_group = StringVar(winsignup, value="A+")

    # Entry Box ------------------------------------------------------------------

    first_name_entry = Entry(winsignup, width=40, textvariable=first_name)
    first_name_entry.place(x=200, y=133)

    last_name_entry = Entry(winsignup, width=40, textvariable=last_name)
    last_name_entry.place(x=200, y=163)

    age_entry = Entry(winsignup, width=40, textvariable=age)
    age_entry.place(x=200, y=193)

    male_entry = ttk.Radiobutton(winsignup, text="Male", variable=gender, value='Male')
    male_entry.place(x=200, y=220)

    female_entry = ttk.Radiobutton(winsignup, text="Female", variable=gender, value='Female')
    female_entry.place(x=200, y=238)

    mobile_entry = Entry(winsignup, width=40, textvariable=mobile)
    mobile_entry.place(x=200, y=263)

    city_entry = Entry(winsignup, width=40, textvariable=city)
    city_entry.place(x=200, y=293)

    add_entry = Entry(winsignup, width=40, textvariable=add)
    add_entry.place(x=200, y=323)

    user_name_entry = Entry(winsignup, width=40, textvariable=user_name)
    user_name_entry.place(x=200, y=353)

    password_entry = Entry(winsignup, width=40, show="*", textvariable=password)
    password_entry.place(x=200, y=383)

    verify_pass_entry = Entry(winsignup, width=40, show="*", textvariable=verify_pass)
    verify_pass_entry.place(x=200, y=410)

    blood_group_entry = OptionMenu(winsignup, blood_group, *options)
    blood_group_entry.place(x=200, y=442)

    # Buttons ------------------------------------------------------------------

    btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=action)
    btn_signup.place(x=180, y=500)

    btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=270, y=500)

    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()


# ------------------------------------------------------------End Singup Window--------------------


def hospital_signup():
    # signup database connect
    def hsp_action():
        if hosp_name.get() == "" or contact.get() == "" or city.get() == "" or add.get() == "" \
                or user_.get() == "" or passw.get() == "" or verify_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required %s %s %s %s" % (
                hosp_name.get(), contact.get(), city.get(), user_.get()), parent=winsignup)
        elif passw.get() != verify_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
                cur = con.cursor()

                cur.execute("select * from hospital where user_name=%s", user_.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User name Already Exits", parent=winsignup)
                else:
                    cur.execute(
                        "insert into hospital(hosp_name,contact_number,city,address,user_name,"
                        "password) values(%s,%s,%s,%s,%s,%s)",
                        (
                            hosp_name.get(),
                            contact.get(),
                            city.get(),
                            add.get(),
                            user_.get(),
                            passw.get(),
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        hosp_name_entry.delete(0, END)
        contact_entry.delete(0, END)
        city_entry.delete(0, END)
        add_entry.delete(0, END)
        user_name_entry.delete(0, END)
        password_entry.delete(0, END)
        verify_pass_entry.delete(0, END)

    # start Signup Window
    winsignup = Toplevel()

    winsignup.title("Blood Bank Management")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    bgimg = PhotoImage(file="img/reg.png")
    limg = Label(winsignup, image=bgimg)
    limg.pack()

    # heading label
    heading_label = Label(winsignup, text="Signup For Hospital", font='Verdana 20 bold')
    heading_label.place(x=80, y=68)

    # Form data labels ------------------------------------------------------------------

    hosp_name_label = Label(winsignup, text="Hospital Name :", font='Verdana 10 bold')
    hosp_name_label.place(x=80, y=130)

    contact_label = Label(winsignup, text="Contact No :", font='Verdana 10 bold')
    contact_label.place(x=80, y=160)

    city_label = Label(winsignup, text="City :", font='Verdana 10 bold')
    city_label.place(x=80, y=190)

    address_label = Label(winsignup, text="Address :", font='Verdana 10 bold')
    address_label.place(x=80, y=220)

    user_name_label = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name_label.place(x=80, y=250)

    password_label = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password_label.place(x=80, y=280)

    very_pass_label = Label(winsignup, text="Verify Pass:", font='Verdana 10 bold')
    very_pass_label.place(x=80, y=310)

    # Variables / Values ------------------------------------------------------------------

    hosp_name = StringVar(winsignup)
    contact = StringVar(winsignup)
    city = StringVar(winsignup)
    add = StringVar(winsignup)
    user_ = StringVar(winsignup)
    passw = StringVar(winsignup)
    verify_pass = StringVar(winsignup)

    # Entry Box ------------------------------------------------------------------

    hosp_name_entry = Entry(winsignup, width=40, textvariable=hosp_name)
    hosp_name_entry.place(x=200, y=133)

    contact_entry = Entry(winsignup, width=40, textvariable=contact)
    contact_entry.place(x=200, y=163)

    city_entry = Entry(winsignup, width=40, textvariable=city)
    city_entry.place(x=200, y=193)

    add_entry = Entry(winsignup, width=40, textvariable=add)
    add_entry.place(x=200, y=223)

    user_name_entry = Entry(winsignup, width=40, textvariable=user_)
    user_name_entry.place(x=200, y=253)

    password_entry = Entry(winsignup, width=40, show="*", textvariable=passw)
    password_entry.place(x=200, y=283)

    verify_pass_entry = Entry(winsignup, width=40, show="*", textvariable=verify_pass)
    verify_pass_entry.place(x=200, y=313)

    # Buttons ------------------------------------------------------------------

    btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=hsp_action)
    btn_signup.place(x=180, y=400)

    btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=270, y=400)

    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()


# ------------------------------------------------------------ Login Window -----------------------------------------

options = [
    "A+",
    "A-",
    "B+",
    "B-",
    "O+",
    "O-",
    "AB+",
    "AB-"
]


def login_page():
    def clear():
        userentry.delete(0, END)
        passentry.delete(0, END)

    def close():
        win.destroy()

    def login():
        if user_name.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Enter User Name And Password", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="password", database="blood_bank")
                cur = con.cursor()

                if hospital.get() == 0:
                    cur.execute("select * from donors where user_name=%s and password = %s",
                                (user_name.get(), password.get()))
                    row = cur.fetchone()
                else:
                    cur.execute("select * from hospital where user_name=%s and password = %s",
                                (user_name.get(), password.get()))
                    row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

                else:
                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    close()
                    if hospital.get() == 0:
                        user_dashboard(user_name)
                    else:
                        hosp_dashboard(user_name)

                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)

    win = Tk()

    # app title
    win.title("Blood Bank Management")

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    bgimg = PhotoImage(file="img/login.png")
    limg = Label(win, image=bgimg)
    limg.pack()

    # heading label
    heading = Label(win, text="Login", font='Verdana 25 bold')
    heading.place(x=80, y=150)

    username = Label(win, text="User Name :", font='Verdana 10 bold')
    username.place(x=80, y=220)

    userpass = Label(win, text="Password :", font='Verdana 10 bold')
    userpass.place(x=80, y=260)

    # Entry Box
    password = StringVar()
    user_name = StringVar()
    hospital = IntVar(value=0)

    userentry = Entry(win, width=40, textvariable=user_name)
    userentry.focus()
    userentry.place(x=200, y=223)

    passentry = Entry(win, width=40, show="*", textvariable=password)
    passentry.place(x=200, y=260)

    hospital_check = Checkbutton(win, text="Hospital Login", variable=hospital,
                                 onvalue=1, offvalue=0)
    hospital_check.place(x=200, y=293)
    # button login and clear

    btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
    btn_login.place(x=200, y=333)

    btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=260, y=333)

    # signup button

    sign_up_btn = Button(win, text="Switch To Donor Sign up", command=user_signup)
    sign_up_btn.place(x=330, y=20)

    sign_up_btn = Button(win, text="Switch To Hospital Sign up", command=hospital_signup)
    sign_up_btn.place(x=330, y=50)

    win.mainloop()


login_page()

# -------------------------------------------------------------------------- End Login Window ------------------------
