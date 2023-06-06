from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image,ImageTk
from tkcalendar import Calendar
import datetime
import json
with open('D:/Project Prokom/data.kereta.json', 'r') as file:
    jadwalKereta = json.load(file)

rute = "Jakarta - Yogyakarta"
jumlahPenumpang = 1

def transisi1():
    iden.withdraw()
    isiIdentitas1()
def transisi2():
    iden.withdraw()
    isiIdentitas2()
def transisi3():
    iden.withdraw()
    isiIdentitas3()
def transisi4():
    iden.withdraw()
    isiIdentitas4()
def transisi5():
    iden.withdraw()
    isiIdentitas5()

def isiIdentitas1():
    global isi
    global nama_user
    isi = Tk()
    isi.geometry("920x500+170+80")
    isi.resizable(False, False)
    isi.configure(bg="#efefef")
    isi.title("K21 Railway Access")
    
    def gantiButton1():
        global namaPenumpang1
        global emailPenumpang1
        global noHpPenumpang1
        global tipePenumpang1
        namaPenumpang1 = nama_user.get()
        emailPenumpang1 = email_user.get()
        noHpPenumpang1 = nohp_user.get()
        tipePenumpang1 = tipe_penumpang.get()
        if noHpPenumpang1.isnumeric() == True:
            identitas1.configure(text="{}\n\n{}\n\n{}".format(namaPenumpang1+"   /   "+tipePenumpang1, emailPenumpang1, noHpPenumpang1))
            isi.destroy()
            iden.after(1000)
            iden.deiconify()
        else:
            messagebox.showerror("Error!", "Masukkan No. Handphone dengan benar!")
            
            
    Label(isi, text="Penumpang 1", font=("vernada", 17), bg="#efefef").place(x=218, y=35)
    wrapper = Frame(isi, width=480, height=350, bg="#f5f5f5")
    wrapper.place(x=220, y=70)
    
    nama_kereta = Label(wrapper, fg="#57a1f8", bg="#f5f5f5",font=("bold", 19), text="{}".format(jadwalKereta[rute][8]["nama"]))
    nama_kereta.place(x=19, y=14)
    kelas_kereta = Label(wrapper,  fg="black", bg="#f5f5f5",font=("bold", 9), text="{}".format(jadwalKereta[rute][8]["kelas"]))
    kelas_kereta.place(x=21, y=50)
    harga_kereta = Label(wrapper, fg="black", bg="#f5f5f5",font=("bold", 10), text="{}".format(jadwalKereta[rute][8]["harga"]))
    harga_kereta.place(x=394, y=23)
    
    Label(wrapper, text="Nama Lengkap", fg="black", bg="#f5f5f5", font=("Vernada", 12)).place(x=21, y=95)
    nama_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#f5f5f5", font=("Vernada", 11))
    nama_user.place(x=24, y=127)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=149)
    
    Label(wrapper, text="Email", fg="black", bg="#f5f5f5", font=("Vernada", 12)).place(x=21, y=163)
    email_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#f5f5f5", font=("Vernada", 11))
    email_user.place(x=24, y=195)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=217)
    
    Label(wrapper, text="No. Handphone", fg="black", bg="#f5f5f5", font=("Vernada", 12)).place(x=21, y=231)
    nohp_user = Entry(wrapper, width=27, fg="#333333", border=0, bg="#f5f5f5", font=("Vernada", 11))
    nohp_user.place(x=24, y=263)
    Frame(wrapper, width=205, height=1, bg="#999999").place(x=25, y=285)
    
    Label(wrapper, text="Tipe Penumpang", fg="black", bg="#f5f5f5", font=("Vernada", 12)).place(x=334, y=231)
    Frame(wrapper, width=100, height=1, bg="#999999").place(x=354, y=285)
    Tipe = ["Dewasa", "Pelajar"]
    tipe_penumpang = StringVar(isi)
    tipe_penumpang.set("")
    OptionMenu_tipe = OptionMenu(wrapper, tipe_penumpang, *Tipe)
    OptionMenu_tipe.configure(border=0, bg="#f5f5f5", width=8)
    OptionMenu_tipe.place(x=366, y=255)
    
    Button(isi, width=68, height=2, bg="#ff8400", text="Tambahkan", fg="black", border=0, command=gantiButton1, cursor="hand2", font=("Vernada", 8, "bold")).place(x=219, y=425)
def isiIdentitas2():
    global isi
    global nama_user
    isi = Tk()
    isi.geometry("920x500+170+80")
    isi.resizable(False, False)
    isi.configure(bg="#dfdfde")
    isi.title("K21 Railway Access")
    
    def gantiButton2():
        global namaPenumpang2
        global emailPenumpang2
        global noHpPenumpang2
        global tipePenumpang2
        namaPenumpang2 = nama_user.get()
        emailPenumpang2 = email_user.get()
        noHpPenumpang2 = nohp_user.get()
        tipePenumpang2 = tipe_penumpang.get()
        if noHpPenumpang2.isnumeric() == True:
            identitas2.configure(text="{}\n\n{}\n\n{}".format(namaPenumpang2+"   /   "+tipePenumpang2, emailPenumpang2, noHpPenumpang2))
            isi.destroy()
            iden.after(1000)
            iden.deiconify()
        else:
            messagebox.showerror("Error!", "Masukkan No. Handphone dengan benar!")
        
    Label(isi, text="Penumpang 2", font=("vernada", 17), bg="#dfdfde").place(x=218, y=35)
    wrapper = Frame(isi, width=480, height=350, bg="#efefef")
    wrapper.place(x=220, y=70)
    
    nama_kereta = Label(wrapper, fg="#57a1f8", bg="#f6f1f1",font=("bold", 19), text="{}".format(jadwalKereta[rute][8]["nama"]))
    nama_kereta.place(x=19, y=14)
    kelas_kereta = Label(wrapper,  fg="black", bg="#f6f1f1",font=("bold", 9), text="{}".format(jadwalKereta[rute][8]["kelas"]))
    kelas_kereta.place(x=21, y=50)
    harga_kereta = Label(wrapper, fg="black", bg="#f6f1f1",font=("bold", 10), text="{}".format(jadwalKereta[rute][8]["harga"]))
    harga_kereta.place(x=394, y=23)
    
    Label(wrapper, text="Nama Lengkap", fg="black", font=("Vernada", 12)).place(x=21, y=95)
    nama_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nama_user.place(x=24, y=127)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=149)
    
    Label(wrapper, text="Email", fg="black", font=("Vernada", 12)).place(x=21, y=163)
    email_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    email_user.place(x=24, y=195)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=217)
    
    Label(wrapper, text="No. Handphone", fg="black", font=("Vernada", 12)).place(x=21, y=231)
    nohp_user = Entry(wrapper, width=27, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nohp_user.place(x=24, y=263)
    Frame(wrapper, width=205, height=1, bg="#999999").place(x=25, y=285)
    
    Label(wrapper, text="Tipe Penumpang", fg="black", font=("Vernada", 12)).place(x=334, y=231)
    Frame(wrapper, width=100, height=1, bg="#999999").place(x=354, y=285)
    Tipe = ["Dewasa", "Pelajar"]
    tipe_penumpang = StringVar(isi)
    tipe_penumpang.set("")
    OptionMenu_tipe = OptionMenu(wrapper, tipe_penumpang, *Tipe)
    OptionMenu_tipe.configure(border=0, bg="#efefef", width=8)
    OptionMenu_tipe.place(x=366, y=255)
    
    Button(isi, width=68, height=2, bg="#ff8400", text="Tambahkan", fg="black", border=0, command=gantiButton2, cursor="hand2", font=("Vernada", 8, "bold")).place(x=219, y=425)
def isiIdentitas3():
    global isi
    global nama_user
    isi = Tk()
    isi.geometry("920x500+170+80")
    isi.resizable(False, False)
    isi.configure(bg="#dfdfde")
    isi.title("K21 Railway Access")
    
    def gantiButton3():
        global namaPenumpang3
        global emailPenumpang3
        global noHpPenumpang3
        global tipePenumpang3
        namaPenumpang3 = nama_user.get()
        emailPenumpang3 = email_user.get()
        noHpPenumpang3 = nohp_user.get()
        tipePenumpang3 = tipe_penumpang.get()
        if noHpPenumpang3.isnumeric() == True:
            identitas3.configure(text="{}\n\n{}\n\n{}".format(namaPenumpang3+"   /   "+tipePenumpang3, emailPenumpang3, noHpPenumpang3))
            isi.destroy()
            iden.after(1000)
            iden.deiconify()
        else:
            messagebox.showerror("Error!", "Masukkan No. Handphone dengan benar!")
        
    Label(isi, text="Penumpang 3", font=("vernada", 17), bg="#dfdfde").place(x=218, y=35)
    wrapper = Frame(isi, width=480, height=350, bg="#efefef")
    wrapper.place(x=220, y=70)
    
    nama_kereta = Label(wrapper, fg="#57a1f8", bg="#f6f1f1",font=("bold", 19), text="{}".format(jadwalKereta[rute][8]["nama"]))
    nama_kereta.place(x=19, y=14)
    kelas_kereta = Label(wrapper,  fg="black", bg="#f6f1f1",font=("bold", 9), text="{}".format(jadwalKereta[rute][8]["kelas"]))
    kelas_kereta.place(x=21, y=50)
    harga_kereta = Label(wrapper, fg="black", bg="#f6f1f1",font=("bold", 10), text="{}".format(jadwalKereta[rute][8]["harga"]))
    harga_kereta.place(x=394, y=23)
    
    Label(wrapper, text="Nama Lengkap", fg="black", font=("Vernada", 12)).place(x=21, y=95)
    nama_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nama_user.place(x=24, y=127)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=149)
    
    Label(wrapper, text="Email", fg="black", font=("Vernada", 12)).place(x=21, y=163)
    email_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    email_user.place(x=24, y=195)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=217)
    
    Label(wrapper, text="No. Handphone", fg="black", font=("Vernada", 12)).place(x=21, y=231)
    nohp_user = Entry(wrapper, width=27, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nohp_user.place(x=24, y=263)
    Frame(wrapper, width=205, height=1, bg="#999999").place(x=25, y=285)
    
    Label(wrapper, text="Tipe Penumpang", fg="black", font=("Vernada", 12)).place(x=334, y=231)
    Frame(wrapper, width=100, height=1, bg="#999999").place(x=354, y=285)
    Tipe = ["Dewasa", "Pelajar"]
    tipe_penumpang = StringVar(isi)
    tipe_penumpang.set("")
    OptionMenu_tipe = OptionMenu(wrapper, tipe_penumpang, *Tipe)
    OptionMenu_tipe.configure(border=0, bg="#efefef", width=8)
    OptionMenu_tipe.place(x=366, y=255)
    
    Button(isi, width=68, height=2, bg="#ff8400", text="Tambahkan", fg="black", border=0, command=gantiButton3, cursor="hand2", font=("Vernada", 8, "bold")).place(x=219, y=425)
def isiIdentitas4():
    global isi
    global nama_user
    isi = Tk()
    isi.geometry("920x500+170+80")
    isi.resizable(False, False)
    isi.configure(bg="#dfdfde")
    isi.title("K21 Railway Access")
    
    def gantiButton4():
        global namaPenumpang4
        global emailPenumpang4
        global noHpPenumpang4
        global tipePenumpang4
        namaPenumpang4 = nama_user.get()
        emailPenumpang4 = email_user.get()
        noHpPenumpang4 = nohp_user.get()
        tipePenumpang4 = tipe_penumpang.get()
        if noHpPenumpang4.isnumeric() == True:
            identitas4.configure(text="{}\n\n{}\n\n{}".format(namaPenumpang4+"   /   "+tipePenumpang4, emailPenumpang4, noHpPenumpang4))
            isi.destroy()
            iden.after(1000)
            iden.deiconify()
        else:
            messagebox.showerror("Error!", "Masukkan No. Handphone dengan benar!")
        
    Label(isi, text="Penumpang 4", font=("vernada", 17), bg="#dfdfde").place(x=218, y=35)
    wrapper = Frame(isi, width=480, height=350, bg="#efefef")
    wrapper.place(x=220, y=70)
    
    nama_kereta = Label(wrapper, fg="#57a1f8", bg="#f6f1f1",font=("bold", 19), text="{}".format(jadwalKereta[rute][8]["nama"]))
    nama_kereta.place(x=19, y=14)
    kelas_kereta = Label(wrapper,  fg="black", bg="#f6f1f1",font=("bold", 9), text="{}".format(jadwalKereta[rute][8]["kelas"]))
    kelas_kereta.place(x=21, y=50)
    harga_kereta = Label(wrapper, fg="black", bg="#f6f1f1",font=("bold", 10), text="{}".format(jadwalKereta[rute][8]["harga"]))
    harga_kereta.place(x=394, y=23)
    
    Label(wrapper, text="Nama Lengkap", fg="black", font=("Vernada", 12)).place(x=21, y=95)
    nama_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nama_user.place(x=24, y=127)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=149)
    
    Label(wrapper, text="Email", fg="black", font=("Vernada", 12)).place(x=21, y=163)
    email_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    email_user.place(x=24, y=195)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=217)
    
    Label(wrapper, text="No. Handphone", fg="black", font=("Vernada", 12)).place(x=21, y=231)
    nohp_user = Entry(wrapper, width=27, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nohp_user.place(x=24, y=263)
    Frame(wrapper, width=205, height=1, bg="#999999").place(x=25, y=285)
    
    Label(wrapper, text="Tipe Penumpang", fg="black", font=("Vernada", 12)).place(x=334, y=231)
    Frame(wrapper, width=100, height=1, bg="#999999").place(x=354, y=285)
    Tipe = ["Dewasa", "Pelajar"]
    tipe_penumpang = StringVar(isi)
    tipe_penumpang.set("")
    OptionMenu_tipe = OptionMenu(wrapper, tipe_penumpang, *Tipe)
    OptionMenu_tipe.configure(border=0, bg="#efefef", width=8)
    OptionMenu_tipe.place(x=366, y=255)
    
    Button(isi, width=68, height=2, bg="#ff8400", text="Tambahkan", fg="black", border=0, command=gantiButton4, cursor="hand2", font=("Vernada", 8, "bold")).place(x=219, y=425)
def isiIdentitas5():
    global isi
    global nama_user
    isi = Tk()
    isi.geometry("920x500+170+80")
    isi.resizable(False, False)
    isi.configure(bg="#dfdfde")
    isi.title("K21 Railway Access")
    
    def gantiButton5():
        global namaPenumpang5
        global emailPenumpang5
        global noHpPenumpang5
        global tipePenumpang5
        namaPenumpang5 = nama_user.get()
        emailPenumpang5 = email_user.get()
        noHpPenumpang5 = nohp_user.get()
        tipePenumpang5 = tipe_penumpang.get()
        if noHpPenumpang5.isnumeric() == True:
            identitas5.configure(text="{}\n\n{}\n\n{}".format(namaPenumpang5+"   /   "+tipePenumpang5, emailPenumpang5, noHpPenumpang5))
            isi.destroy()
            iden.after(1000)
            iden.deiconify()
        else:
            messagebox.showerror("Error!", "Masukkan No. Handphone dengan benar!")
        
    Label(isi, text="Penumpang 5", font=("vernada", 17), bg="#dfdfde").place(x=218, y=35)
    wrapper = Frame(isi, width=480, height=350, bg="#efefef")
    wrapper.place(x=220, y=70)
    
    nama_kereta = Label(wrapper, fg="#57a1f8", bg="#f6f1f1",font=("bold", 19), text="{}".format(jadwalKereta[rute][8]["nama"]))
    nama_kereta.place(x=19, y=14)
    kelas_kereta = Label(wrapper,  fg="black", bg="#f6f1f1",font=("bold", 9), text="{}".format(jadwalKereta[rute][8]["kelas"]))
    kelas_kereta.place(x=21, y=50)
    harga_kereta = Label(wrapper, fg="black", bg="#f6f1f1",font=("bold", 10), text="{}".format(jadwalKereta[rute][8]["harga"]))
    harga_kereta.place(x=394, y=23)
    
    Label(wrapper, text="Nama Lengkap", fg="black", font=("Vernada", 12)).place(x=21, y=95)
    nama_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nama_user.place(x=24, y=127)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=149)
    
    Label(wrapper, text="Email", fg="black", font=("Vernada", 12)).place(x=21, y=163)
    email_user = Entry(wrapper, width=54, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    email_user.place(x=24, y=195)
    Frame(wrapper, width=430, height=1, bg="#999999").place(x=25, y=217)
    
    Label(wrapper, text="No. Handphone", fg="black", font=("Vernada", 12)).place(x=21, y=231)
    nohp_user = Entry(wrapper, width=27, fg="#333333", border=0, bg="#efefef", font=("Vernada", 11))
    nohp_user.place(x=24, y=263)
    Frame(wrapper, width=205, height=1, bg="#999999").place(x=25, y=285)
    
    Label(wrapper, text="Tipe Penumpang", fg="black", font=("Vernada", 12)).place(x=334, y=231)
    Frame(wrapper, width=100, height=1, bg="#999999").place(x=354, y=285)
    Tipe = ["Dewasa", "Pelajar"]
    tipe_penumpang = StringVar(isi)
    tipe_penumpang.set("")
    OptionMenu_tipe = OptionMenu(wrapper, tipe_penumpang, *Tipe)
    OptionMenu_tipe.configure(border=0, bg="#efefef", width=8)
    OptionMenu_tipe.place(x=366, y=255)
    
    Button(isi, width=68, height=2, bg="#ff8400", text="Tambahkan", fg="black", border=0, command=gantiButton5, cursor="hand2", font=("Vernada", 8, "bold")).place(x=219, y=425)
    
    
def penumpangSatu():
    global iden
    global identitas1
    iden = Tk()
    iden.geometry("920x500+170+80")
    iden.resizable(False, False)
    iden.configure(bg="#fff")
    iden.title("K21 Railway Access")
    wrapper = LabelFrame(iden)
    wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=47, padx=250)

    mycanvas = Canvas(wrapper, bg="#dde6de")
    mycanvas.pack(fill=BOTH, expand="yes")
    
    identitas1 = Button(mycanvas, text="Penumpang 1", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi1)
    identitas1.pack(expand=TRUE, padx=5)
        
    iden.mainloop()

def penumpangDua():
    global iden
    global identitas1
    global identitas2
    iden = Tk()
    iden.geometry("920x500+170+80")
    iden.resizable(False, False)
    iden.configure(bg="#fff")
    iden.title("K21 Railway Access")
    wrapper = LabelFrame(iden)
    wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=47, padx=250)

    mycanvas = Canvas(wrapper, bg="#dde6de")
    mycanvas.pack(fill=BOTH, expand="yes")
    
    identitas1 = Button(mycanvas, text="Penumpang 1", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi1)
    identitas1.pack(expand=TRUE, padx=5)
    identitas2 = Button(mycanvas, text="Penumpang 2", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi2)
    identitas2.pack(expand=TRUE, padx=5)
        
    iden.mainloop()
    
def penumpangTiga():
    global iden
    global identitas1
    global identitas2
    global identitas3
    iden = Tk()
    iden.geometry("920x500+170+80")
    iden.resizable(False, False)
    iden.configure(bg="#fff")
    iden.title("K21 Railway Access")
    wrapper = LabelFrame(iden)
    wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=47, padx=250)

    mycanvas = Canvas(wrapper, bg="#dde6de")
    mycanvas.pack(fill=BOTH, expand="yes")
    
    myframe = Frame(mycanvas, bg="#dde6de")
    mycanvas.create_window((0,0), window=myframe, anchor="nw")
    
    identitas1 = Button(mycanvas, text="Penumpang 1", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi1)
    identitas1.pack(expand=TRUE, padx=5)
    identitas2 = Button(mycanvas, text="Penumpang 2", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi2)
    identitas2.pack(expand=TRUE, padx=5)
    identitas3 = Button(mycanvas, text="Penumpang 3", width=57, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi3)
    identitas3.pack(expand=TRUE, padx=5)
    
    iden.mainloop()
    
def penumpangEmpat():
    global iden
    global identitas1
    global identitas2
    global identitas3
    global identitas4
    iden = Tk()
    iden.geometry("920x500+170+80")
    iden.resizable(False, False)
    iden.configure(bg="#fff")
    iden.title("K21 Railway Access")
    wrapper = LabelFrame(iden)
    wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=47, padx=250)

    mycanvas = Canvas(wrapper, bg="#dde6de")
    mycanvas.pack(side=LEFT, fill=BOTH, expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper, orient=VERTICAL, command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe = Frame(mycanvas, bg="#dde6de")
    mycanvas.create_window((0,0), window=myframe, anchor="nw")
    
    identitas1 = Button(myframe, text="Penumpang 1", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi1)
    identitas1.pack(expand=TRUE, pady=4,padx=5)
    identitas2 = Button(myframe, text="Penumpang 2", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi2)
    identitas2.pack(expand=TRUE, pady=4,padx=5)
    identitas3 = Button(myframe, text="Penumpang 3", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi3)
    identitas3.pack(expand=TRUE, pady=4,padx=5)
    identitas4 = Button(myframe, text="Penumpang 4", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi4)
    identitas4.pack(expand=TRUE, pady=4,padx=5)
        
    iden.mainloop()
    
def penumpangLima():
    global iden
    global identitas1
    global identitas2
    global identitas3
    global identitas4
    global identitas5
    iden = Tk()
    iden.geometry("920x500+170+80")
    iden.resizable(False, False)
    iden.configure(bg="#fff")
    iden.title("K21 Railway Access")
    wrapper = LabelFrame(iden)
    wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=47, padx=250)

    mycanvas = Canvas(wrapper, bg="#dde6de")
    mycanvas.pack(side=LEFT, fill=BOTH, expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper, orient=VERTICAL, command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

    myframe = Frame(mycanvas, bg="#dde6de")
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    identitas1 = Button(myframe, text="Penumpang 1", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi1)
    identitas1.pack(expand=TRUE, pady=4, padx=5)
    identitas2 = Button(myframe, text="Penumpang 2", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi2)
    identitas2.pack(expand=TRUE, pady=4, padx=5)
    identitas3 = Button(myframe, text="Penumpang 3", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi3)
    identitas3.pack(expand=TRUE, pady=4, padx=5)
    identitas4 = Button(myframe, text="Penumpang 4", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi4)
    identitas4.pack(expand=TRUE, pady=4, padx=5)
    identitas5 = Button(myframe, text="Penumpang 5", width=54, height=8, border=0, cursor="hand2", bg="#fff", fg="black", command=transisi5)
    identitas5.pack(expand=TRUE, pady=4, padx=5)
   
    iden.mainloop()

penumpangEmpat()