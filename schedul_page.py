from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from customtkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar
import datetime
import json
with open('D:/Project Prokom/data.kereta.json', 'r') as file:
    jadwalKereta = json.load(file)

schedul = ThemedTk(theme="arc")
schedul.geometry("920x500+170+80")
schedul.resizable(False, False)
schedul.title("K21 Railway Access")
schedul.configure(bg="#fff")
style = ttk.Style()
style.theme_use('default')
style.configure("Vertical.TScrollbar", background="#57a1f8", bordercolor="#000000", arrowcolor="#fff", troughcolor="white")
rute = "Jakarta - Yogyakarta"

wrapper = CTkFrame(schedul)
wrapper.pack(side=BOTTOM, fill=BOTH, expand=YES, pady=30, padx=250)
heading = Frame(schedul, width=920, height=30, bg="#57a1f8")
heading.place(x=0, y=0)
img = (Image.open("D:\Project Prokom\imgsrc\kembali.png"))
img_resize = img.resize((23,23), Image.ANTIALIAS)
button_img = ImageTk.PhotoImage(img_resize)
button_back = CTkButton(master=heading, text="",image=button_img, width=0, height=0, cursor="hand2", fg_color="#57a1f8", hover_color="#146c94")
button_back.place(x=-2, y=-1)
heading_text = Label(heading, bg="#57a1f8", fg="black", text=f"Schedul Jakarta - Yogyakarta at {datetime.date.today()}")
heading_text.place(x=348, y=4)

mycanvas = Canvas(wrapper, bg="#dde6de")
mycanvas.pack(side=LEFT, fill=BOTH, expand="yes")

yscrollbar = ttk.Scrollbar(wrapper, orient=VERTICAL, cursor="hand2",command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill=Y)

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

myframe = Frame(mycanvas, bg="#dde6de")
mycanvas.create_window((0,0), window=myframe, anchor="nw")

def userPilih1():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][0]["nama"]
    hargaKereta     = jadwalKereta[rute][0]["harga"]
    waktuBerangkat  = jadwalKereta[rute][0]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][0]["waktu_akhir"]
def userPilih2():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][1]["nama"]
    hargaKereta     = jadwalKereta[rute][1]["harga"]
    waktuBerangkat  = jadwalKereta[rute][1]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][1]["waktu_akhir"]
def userPilih3():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][2]["nama"]
    hargaKereta     = jadwalKereta[rute][2]["harga"]
    waktuBerangkat  = jadwalKereta[rute][2]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][2]["waktu_akhir"]
def userPilih4():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][3]["nama"]
    hargaKereta     = jadwalKereta[rute][3]["harga"]
    waktuBerangkat  = jadwalKereta[rute][3]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][3]["waktu_akhir"]
def userPilih5():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][4]["nama"]
    hargaKereta     = jadwalKereta[rute][4]["harga"]
    waktuBerangkat  = jadwalKereta[rute][4]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][4]["waktu_akhir"]
def userPilih6():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][5]["nama"]
    hargaKereta     = jadwalKereta[rute][5]["harga"]
    waktuBerangkat  = jadwalKereta[rute][5]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][5]["waktu_akhir"]
def userPilih7():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][6]["nama"]
    hargaKereta     = jadwalKereta[rute][6]["harga"]
    waktuBerangkat  = jadwalKereta[rute][6]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][6]["waktu_akhir"]
def userPilih8():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][7]["nama"]
    hargaKereta     = jadwalKereta[rute][7]["harga"]
    waktuBerangkat  = jadwalKereta[rute][7]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][7]["waktu_akhir"]
def userPilih9():
    global namaKereta
    global hargaKereta
    global waktuBerangkat
    global waktuSampai
    namaKereta      = jadwalKereta[rute][8]["nama"]
    hargaKereta     = jadwalKereta[rute][8]["harga"]
    waktuBerangkat  = jadwalKereta[rute][8]["waktu_awal"]
    waktuSampai     = jadwalKereta[rute][8]["waktu_akhir"]
    
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][0]["nama"], jadwalKereta[rute][0]["kelas"]+"      "+jadwalKereta[rute][0]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][0]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][0]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih1).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][1]["nama"], jadwalKereta[rute][1]["kelas"]+"      "+jadwalKereta[rute][1]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][1]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][1]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih2).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][2]["nama"], jadwalKereta[rute][2]["kelas"]+"      "+jadwalKereta[rute][2]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][2]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][2]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih3).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][3]["nama"], jadwalKereta[rute][3]["kelas"]+"      "+jadwalKereta[rute][3]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][3]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][3]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih4).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][4]["nama"], jadwalKereta[rute][4]["kelas"]+"      "+jadwalKereta[rute][4]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][4]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][4]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih5).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][5]["nama"], jadwalKereta[rute][5]["kelas"]+"      "+jadwalKereta[rute][5]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][5]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][5]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih6).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)    
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][6]["nama"], jadwalKereta[rute][6]["kelas"]+"      "+jadwalKereta[rute][6]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][6]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][6]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih7).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][7]["nama"], jadwalKereta[rute][7]["kelas"]+"      "+jadwalKereta[rute][7]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][7]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][7]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih8).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)
try:
    CTkButton(myframe,cursor="hand2", text="{}\n\n{}\n\n{}\n\n{}".format(jadwalKereta[rute][8]["nama"], jadwalKereta[rute][8]["kelas"]+"      "+jadwalKereta[rute][8]["harga"]+"/pax", "Waktu Berangkat                Waktu Sampai",jadwalKereta[rute][8]["waktu_awal"]+"                 ->              "+jadwalKereta[rute][8]["waktu_akhir"]), width=394, height=130, border_spacing=0, fg_color="#fff", text_color="black", hover_color="#efefef", command=userPilih9).pack(expand=YES, pady=6, padx=5)
except:
    CTkButton(myframe, text="Jadwal Kosong", width=394, height=130, border_spacing=0).pack(expand=YES, pady=6, padx=5)

schedul.mainloop()