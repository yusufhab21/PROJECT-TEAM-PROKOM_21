from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import Calendar
import datetime
import json

def loginAkun():
    global login
    login = Tk()
    login.title("K21 Railway Access")
    login.configure(bg="#fff")
    login.geometry("920x500+170+80")
    login.resizable(False, False)

    ##################################

    img = (Image.open("D:\Project Prokom\imgsrc\kaicnth.png"))
    img_resize = img.resize((440,230), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(img_resize)
    Label(login, image=new_image2, bg="white").place(x=35, y=127)

    ##################################

    frame = Frame(login, width=350, height=350, bg="white")
    frame.place(x=520, y=70)

    ##################################

    heading = Label(frame, text="Sign In", bg="white",fg="#57a1f8", font=("Microsoft YaHei UI Light", 20, "bold"))
    heading.place(x=115, y=8)
    
    Button(login, text="Light", width=4, height=1, bg="#fff", fg="#333333" ,command=ganti_login_light, border=1).place(x=870, y=10)

    ##################################

    def cekAkun():
        with open('D:/Project Prokom/data.akun.k21.json', 'r') as file:
            data_akun = json.load(file)
        Username = str(user.get())
        Password = str(pw.get())
        for i in range(0, len(data_akun["akun"])):
            if Username == data_akun["akun"][i]["username"] and Password == data_akun["akun"][i]["password"]:    
                login.destroy()
                mainPage()
                break
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")

    ################################## 
    
    def isiuser(e):
        user.delete(0, "end")
    def tidakisiuser(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")
    user = Entry(frame, width=37, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", isiuser)
    user.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    #################################
    
    def isiuser(e):
        pw.delete(0, "end")
    def tidakisiuser(e):
        name = pw.get()
        if name == "":
            pw.insert(0, "Password")
    pw = Entry(frame, width=37, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    pw.place(x=30, y=150)
    pw.insert(0, "Password")
    pw.bind("<FocusIn>", isiuser)
    pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    #################################

    Button(frame, width=42, pady=7, text="Sign In", bg="#57a1f8", border=0, command=cekAkun).place(x=24, y=204)
    label_regis = Label(frame, text="Belum punya akun?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label_regis.place(x=83, y=250)
    regis_button = Button(frame, width=6, text="Sign Up", border=0, fg="#57a1f8", bg="white", cursor="hand2", command=ganti_regis)
    regis_button.place(x=200, y=250)

    login.mainloop()


def bikinAkun():
    global regis
    regis = Tk()
    regis.title("K21 Railway Access")
    regis.geometry("920x500+170+80")
    regis.configure(bg="#fff")
    regis.resizable(False, False)

    ####################################
    
    frame = Frame(regis, width=350, height=350, bg="#fff")
    frame.place(x=285, y=40)

    ####################################

    heading = Label(frame, text="Sign Up", bg="white",fg="#57a1f8", font=("Microsoft YaHei UI Light", 20, "bold"))
    heading.place(x=130, y=3)

    Button(regis, text="light", width=4, height=1, bg="#fff", fg="black" ,command=ganti_regis_light, border=1).place(x=870, y=10)

    #####################################

    def cekSignUp():
        Username = user.get()
        Password = pw.get()
        confirm_pw = conf_pw.get()
        if Username == "Username" and Password == "Password" and confirm_pw == "Confirm Password":
            messagebox.showerror("Failed", "Harap diisi terlebih dahulu")
        elif Username == "Username":
            messagebox.showerror("Failed", "Username harus diisi!")
        elif Password == confirm_pw:
            y = {}
            y.update({"username": Username})
            y.update({"password": Password})
            Addjson(y)
        else:
            messagebox.showerror("Failed", "Password yang Anda masukkan berbeda!")

    #####################################
    
    def Addjson(new_data, filename='data.akun.k21.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data["akun"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        messagebox.showinfo("Success", "Akun berhasil dibuat!")
        ganti_login()
                
    ####################################

    def isiuser(e):
        user.delete(0, "end")
    def tidakisiuser(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")
    user = Entry(frame, width=37, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=40, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", isiuser)
    user.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=107)

    ####################################

    def isiuser(e):
        pw.delete(0, "end")
    def tidakisiuser(e):
        name = pw.get()
        if name == "":
            pw.insert(0, "Password")
    pw = Entry(frame, width=37, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    pw.place(x=40, y=140)
    pw.insert(0, "Password")
    pw.bind("<FocusIn>", isiuser)
    pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=167)

    ####################################

    def isiuser(e):
        conf_pw.delete(0, "end")
    def tidakisiuser(e):
        name = conf_pw.get()
        if name == "":
            conf_pw.insert(0, "Confirm Password")
    conf_pw = Entry(frame, width=37, fg="Black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    conf_pw.place(x=40, y=200)
    conf_pw.insert(0, "Confirm Password")
    conf_pw.bind("<FocusIn>", isiuser)
    conf_pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=227)

    ####################################

    Button(frame, width=42, pady=7, text="Sign Up", bg="#57a1f8", border=0, command=cekSignUp).place(x=38, y=255)
    label_login = Label(frame, text="Sudah memiliki akun?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label_login.place(x=95, y=300)
    login_button = Button(frame, width=6, text="Sign In", border=0, fg="#57a1f8", bg="white", cursor="hand2", command=ganti_login)
    login_button.place(x=220, y=300)

    regis.mainloop()


def loginDark():
    global login
    login = Tk()
    login.title("K21 Railway Access")
    login.configure(bg="#333333")
    login.geometry("920x500+170+80")
    login.resizable(False, False)

    ##################################

    img = (Image.open("D:\Project Prokom\imgsrc\kaicnth.png"))
    img_resize = img.resize((440,230), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(img_resize)
    Label(login, image=new_image2, bg="#333333").place(x=35, y=127)

    ##################################

    frame = Frame(login, width=350, height=350, bg="#333333")
    frame.place(x=520, y=70)

    ##################################

    heading = Label(frame, text="Sign In", bg="#333333",fg="#57a1f8", font=("Microsoft YaHei UI Light", 20, "bold"))
    heading.place(x=115, y=8)

    Button(login, text="Dark", width=4, height=1, bg="#333333", fg="white" ,command=ganti_login_dark).place(x=870, y=10)
    ##################################

    def cekAkun():
        with open('D:/Project Prokom/data.akun.k21.json', 'r') as file:
            data_akun = json.load(file)
        Username = str(user.get())
        Password = str(pw.get())
        for i in range(0, len(data_akun["akun"])):
            if Username == data_akun["akun"][i]["username"] and Password == data_akun["akun"][i]["password"]:    
                login.destroy()
                mainPage()
                break
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")

    ################################## 
    
    def isiuser(e):
        user.delete(0, "end")
    def tidakisiuser(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")
    user = Entry(frame, width=37, fg="white", border=0, bg="#333333", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", isiuser)
    user.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    #################################
    def isiuser(e):
        pw.delete(0, "end")
    def tidakisiuser(e):
        name = pw.get()
        if name == "":
            pw.insert(0, "Password")
    pw = Entry(frame, width=37, fg="white", border=0, bg="#333333", font=("Microsoft YaHei UI Light", 11))
    pw.place(x=30, y=150)
    pw.insert(0, "Password")
    pw.bind("<FocusIn>", isiuser)
    pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    #################################

    Button(frame, width=42, pady=7, text="Sign In", bg="#57a1f8", border=0, command=cekAkun).place(x=24, y=204)
    label_regis = Label(frame, text="Belum punya akun?", fg="white", bg="#333333", font=("Microsoft YaHei UI Light", 9))
    label_regis.place(x=83, y=250)
    regis_button = Button(frame, width=6, text="Sign Up", border=0, fg="#57a1f8", bg="#333333", cursor="hand2", command=login_regis_dark)
    regis_button.place(x=200, y=250)

    login.mainloop()


def bikinAkunDark():
    global regis
    regis = Tk()
    regis.title("K21 Railway Access")
    regis.geometry("920x500+170+80")
    regis.configure(bg="#333")
    regis.resizable(False, False)

    ####################################
    
    frame = Frame(regis, width=350, height=350, bg="#333")
    frame.place(x=285, y=40)

    ####################################

    heading = Label(frame, text="Sign Up", bg="#333333",fg="#57a1f8", font=("Microsoft YaHei UI Light", 20, "bold"))
    heading.place(x=130, y=3)
    
    
    Button(regis, text="Dark", width=4, height=1, bg="#333333", fg="white" ,command=ganti_regis_dark).place(x=870, y=10)

    #####################################

    def cekSignUp():
        Username = user.get()
        Password = pw.get()
        confirm_pw = conf_pw.get()
        if Username == "Username" and Password == "Password" and confirm_pw == "Confirm Password":
            messagebox.showerror("Failed", "Harap diisi terlebih dahulu")
        elif Username == "Username":
            messagebox.showerror("Failed", "Username harus diisi!")
        elif Password == confirm_pw:
            y = {}
            y.update({"username": Username})
            y.update({"password": Password})
            Addjson(y)
        else:
            messagebox.showerror("Failed", "Password yang Anda masukkan berbeda!")

    #####################################
    
    def Addjson(new_data, filename='data.akun.k21.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data["akun"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        messagebox.showinfo("Success", "Akun berhasil dibuat!")
        ganti_login_light2()
                
    ####################################

    def isiuser(e):
        user.delete(0, "end")
    def tidakisiuser(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")
    user = Entry(frame, width=37, fg="white", border=0, bg="#333333", font=("Microsoft YaHei UI Light", 11))
    user.place(x=40, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", isiuser)
    user.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=107)

    ####################################

    def isiuser(e):
        pw.delete(0, "end")
    def tidakisiuser(e):
        name = pw.get()
        if name == "":
            pw.insert(0, "Password")
    pw = Entry(frame, width=37, fg="white", border=0, bg="#333333", font=("Microsoft YaHei UI Light", 11))
    pw.place(x=40, y=140)
    pw.insert(0, "Password")
    pw.bind("<FocusIn>", isiuser)
    pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=167)

    ####################################

    def isiuser(e):
        conf_pw.delete(0, "end")
    def tidakisiuser(e):
        name = conf_pw.get()
        if name == "":
            conf_pw.insert(0, "Confirm Password")
    conf_pw = Entry(frame, width=37, fg="white", border=0, bg="#333333", font=("Microsoft YaHei UI Light", 11))
    conf_pw.place(x=40, y=200)
    conf_pw.insert(0, "Confirm Password")
    conf_pw.bind("<FocusIn>", isiuser)
    conf_pw.bind("<FocusOut>", tidakisiuser)
    Frame(frame, width=295, height=2, bg="black").place(x=40, y=227)

    ####################################

    Button(frame, width=42, pady=7, text="Sign Up", bg="#57a1f8", border=0, command=cekSignUp).place(x=38, y=255)
    label_login = Label(frame, text="Sudah memiliki akun?", fg="white", bg="#333333", font=("Microsoft YaHei UI Light", 9))
    label_login.place(x=95, y=300)
    login_button = Button(frame, width=6, text="Sign In", border=0, fg="#57a1f8", bg="#333333", cursor="hand2", command=ganti_login_light2)
    login_button.place(x=220, y=300)

    regis.mainloop()


def ganti_regis_dark():
    regis.destroy()
    bikinAkun()
    
def ganti_regis_light():
    regis.destroy()
    bikinAkunDark()

def login_regis_dark():
    login.destroy()
    bikinAkunDark()
    
def ganti_login_dark():
    login.destroy()
    loginAkun()
    
def ganti_login_light():
    login.destroy()
    loginDark()

def ganti_login_dark2():
    regis.destroy()
    loginAkun()
    
def ganti_login_light2():
    regis.destroy()
    loginDark()
    
def ganti_login():
    regis.destroy()
    loginAkun()

def ganti_regis():
    login.destroy()
    bikinAkun()