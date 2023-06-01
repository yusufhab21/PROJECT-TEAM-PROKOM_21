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

def mainPage():
    main = Tk()
    main.geometry("920x500+170+80")
    main.resizable(False, False)
    main.configure(bg="#eeeeee")
    main.title("K21 Railway Access")

    def cekTanggal():
        global tanggal_hari_ini
        global tgl_banding
        tanggal_hari_ini    = datetime.date.today()
        tgl_pilih           = cal.get_date()
        tgl_pisah           = tgl_pilih.split('-')
        tgl_banding         = datetime.date(int(tgl_pisah[0]), int(tgl_pisah[1]), int(tgl_pisah[2]))
        if tgl_banding < tanggal_hari_ini:
            messagebox.showerror("Error!", "Tidak bisa memesan tiket untuk hari yang telah terlewat!")
            kalender.destroy()
        elif tgl_banding > tanggal_hari_ini + datetime.timedelta(days=30):
            messagebox.showerror("Error!", "Tiket belum tersedia!")
            kalender.destroy()
        else:
            kalender.destroy()
            gantiTextTgl()

    def pilihTanggal():
        global kalender
        global cal
        kalender = Tk()
        kalender.title("Pilih Tanggal")
        kalender.geometry("250x250+500+200")
        kalender.resizable(False, False)
        cal = Calendar(kalender, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack(pady=10)
        select_btn = Button(kalender, text="Pilih", command=cekTanggal)
        select_btn.pack()
        kalender.mainloop()
        
    def gantiTextTgl():
        Tanggal_pilih.configure(bg="#fff", fg="black", text=f"{tgl_banding}")
        
    frame_top = Frame(main, width=920, height=65, bg="#2f58cd")
    frame_top.pack(side=TOP)

    img = (Image.open("D:\Project Prokom\imgsrc\logokai.png"))
    img_resize = img.resize((100,40), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(img_resize)
    Label(frame_top, image=new_image1, bg="#2f58cd").place(x=407, y=12)

    frame1 = Frame(main, width=450, height=400, bg="#fff")
    frame1.place(x=230, y=75)

    img = (Image.open("D:\Project Prokom\imgsrc\kanan.png"))
    img_resize = img.resize((30,25), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(img_resize)
    Label(frame1, image=new_image2, bg="#fff").place(x=211, y=59)

    heading = Label(frame1, text="KA Antar Kota", bg="#fff", fg="black", font=("Verdana", 12))
    heading.place(x=168, y=10)

    Label_asal = Label(frame1, text="Asal", bg="#fff", fg="black", font=("Verdana", 10))
    Label_asal.place(x=35, y=60)
    Frame(frame1, width=163, height=1, bg="#a6a9b6", ).place(x=37, y=122)

    Label_tujuan = Label(frame1, text="Tujuan", bg="#fff", fg="black", font=("Verdana", 10))
    Label_tujuan.place(x=365, y=60)
    Frame(frame1, width=163, height=1, bg="#a6a9b6", ).place(x=253, y=122)

    Label_tgl_berangkat = Label(frame1, text="Tanggal Berangkat", bg="#fff", fg="black", font=("Verdana", 10))
    Label_tgl_berangkat.place(x=35, y=160)
    Frame(frame1, width=163, height=1, bg="#a6a9b6", ).place(x=37, y=217)

    Label_banyak_penumpang = Label(frame1, text="Banyak Penumpang", bg="#fff", fg="black", font=("Verdana", 10))
    Label_banyak_penumpang.place(x=283, y=160)
    Frame(frame1, width=163, height=1, bg="#a6a9b6", ).place(x=253, y=217)

    Kota = ["Jakarta", "Bandung", "Cirebon", "Purwokerto", "Yogyakarta", "Semarang", "Madiun", "Surabaya", "Jember"]

    Asal = StringVar(main)
    Asal.set("")
    OptionMenu_asal = OptionMenu(frame1, Asal,*Kota)
    OptionMenu_asal.configure(border=0, bg="#fff", width=20, fg="black")
    OptionMenu_asal.place(x=37, y=90)

    Tujuan = StringVar(main)
    Tujuan.set("")
    OptionMenu_tujuan = OptionMenu(frame1, Tujuan,*Kota)
    OptionMenu_tujuan.configure(border=0, bg="#fff", width=20)
    OptionMenu_tujuan.place(x=255, y=90)

    Tanggal_pilih = Button(frame1, bg="#fff", text="", width=22, border=0, command=pilihTanggal)
    Tanggal_pilih.place(x=36, y=190)

    jumlah = [1, 2, 3, 4, 5]

    banyakPenumpang = StringVar(main)
    banyakPenumpang.set("")
    OptionMenu_banyak_penumpang = OptionMenu(frame1, banyakPenumpang, *jumlah)
    OptionMenu_banyak_penumpang.configure(border=0, bg="#fff", width=20, fg="black")
    OptionMenu_banyak_penumpang.place(x=255, y=185)

    Button(frame1, width=54, pady=7, text="Cari Jadwal", fg="black", bg="#e57c23", border=1, borderwidth=0, font=("Vernada", 8, "bold")).place(x=35, y=300)

    main.mainloop() 