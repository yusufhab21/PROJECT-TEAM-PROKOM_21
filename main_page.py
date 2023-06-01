from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import Calendar
import datetime

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