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

namaKereta = "Mutiara Selatan Priority"
hargaKereta = "Rp1.250.000"
kelasKereta = "Ekonomi"
userAsal = "Bandung"
userTujuan = "Yogyakarta"
waktuBerangkat = "12:50"
waktuSampai = "20:50"
userJumlah = 4
tgl_banding = datetime.datetime(2021, 7, 24)

def tanggalTiket():
    hari = tgl_banding.strftime("%a")
    tanggal = tgl_banding.strftime("%d")
    bulan = tgl_banding.strftime("%b")
    tahun = tgl_banding.strftime("%y")
    x = f"{hari}, {tanggal} {bulan} {tahun}"
    return x
def hitungDurasi(): 
    from datetime import datetime
    durasi = datetime.strptime(waktuSampai, "%H:%M") - datetime.strptime(waktuBerangkat, "%H:%M")
    durasiTampil = "{}j {}m".format(((datetime.strptime(str(durasi), "%H:%M:%S")).strftime("%H")).replace("0", ""), ((datetime.strptime(str(durasi), "%H:%M:%S")).strftime("%M")).replace("0", ""))
    return durasiTampil
def inisialKelas():
    kelas = kelasKereta[0:3].upper()
    return kelas
def hitungHarga():
    global nominalBayar
    def split(word):
        return list(word)
    nominal = int("".join(hargaKereta[2:].split(".")))
    nominalBayar = userJumlah * nominal
    if len(str(nominalBayar)) == 7:
        gantiRp = split(str(nominalBayar))
        gantiRp.insert(1, ".")
        gantiRp.insert(5, ".")
        nominalTampil = "Rp{}".format("".join(gantiRp))
    elif len(str(nominalBayar)) == 6:
        gantiRp = split(str(nominalBayar))
        gantiRp.insert(3, ".")
        nominalTampil = "Rp{}".format("".join(gantiRp))
    else:
        gantiRp = split(str(nominalBayar))
        gantiRp.insert(2, ".")
        nominalTampil = "Rp{}".format("".join(gantiRp))
    return nominalTampil

def pembayaran():
    payment.withdraw()
    def bayarback():
        bayar.destroy()
        payment.after(700)
        payment.deiconify()
    def ya():
        confirm.destroy()
        bayar.destroy()
        payment.destroy()
        messagebox.showinfo("Success!", "Pembayaran berhasil!")
    def tidak():
        confirm.destroy()
        bayar.after(400)
        bayar.deiconify()
    def cekUserBayar():
        global confirm
        isiBayar = userBayar.get()
        if isiBayar == "":
            messagebox.showerror("Error!", "Harap diisi terlebih dahulu!")
        elif (isiBayar.isnumeric()) == True:
            bandingNominal = int(isiBayar)
            if bandingNominal < nominalBayar:
                messagebox.showerror("Error!", "Nominal yang Anda masukkan kurang!")
            elif bandingNominal == nominalBayar:
                messagebox.showinfo("Success!", "Pembayaran berhasil!")
                bayar.destroy()
                print("Berhasil!")
            else:
                bayar.withdraw()
                confirm = Toplevel()
                confirm.geometry("200x100+550+270")
                confirm.resizable(False, False)
                Label(confirm, text="Nominal yang Anda masukkan lebih\ndari tagihan\nApakah lanjut?").place(x=2, y=10)
                CTkButton(confirm, width=47, height=28, text="Ya", font=("Vernada", 12),text_color="black", fg_color="#ff8400", hover_color="#ff6000", border_spacing=0, corner_radius=7, cursor="hand2", command=ya).place(x=35, y=62)
                CTkButton(confirm, width=40, height=28, text="Tidak", font=("Vernada", 12),text_color="black", fg_color="#ff8400", hover_color="#ff6000", border_spacing=0, corner_radius=7, cursor="hand2", command=tidak).place(x=120, y=62)
                confirm.mainloop()
                
    bayar = Toplevel()
    bayar.geometry("250x100+520+270")
    bayar.title("K21 Railway Access")
    bayar.configure(bg="#dfdfde")
    Label(bayar, text="Masukkan nominal yang dibayarkan:", bg="#dfdfde").place(x=25, y=15)
    userBayar = Entry(bayar, width=25, font=("Calibri", 11))
    userBayar.place(x=35, y=40)
    CTkButton(bayar, text="", image=button_img, width=0, height=0, cursor="hand2", fg_color="#dfdfde", bg_color="#dfdfde", border_spacing=0, hover_color="#dfdfde", command=bayarback).place(x=0, y=0)
    
    CTkButton(bayar, width=65, height=28, text="Bayar", font=("Vernada", 12),text_color="black", fg_color="#ff8400", hover_color="#ff6000", border_spacing=0, corner_radius=7, cursor="hand2", command=cekUserBayar).place(x=95, y=68)

    bayar.mainloop()

payment = Tk()
payment.geometry("920x500+170+80")
payment.resizable(False, False)
payment.configure(bg="#dfdfde")
payment.title("K21 Railway Access")

Frame(payment, width=920, height=30, bg="#57a1f8").place(x=0, y=0)
img = (Image.open("D:\Project Prokom\imgsrc\kembali.png"))
img_resize = img.resize((23,23), Image.LANCZOS)
button_img = ImageTk.PhotoImage(img_resize)
CTkButton(payment, text="", image=button_img, width=0, height=0, cursor="hand2", fg_color="#57a1f8", bg_color="#57a1f8", border_spacing=0, hover_color="#57a1f8").place(x=0, y=0)

img = (Image.open("D:\Project Prokom\imgsrc\ekanan.png"))
img_resize = img.resize((10,20), Image.LANCZOS)
kanan_img = ImageTk.PhotoImage(img_resize)

wrapper1 = CTkFrame(payment, width=400, height=200, fg_color="#f5f5f5", corner_radius=10)
wrapper1.place(x=262, y=42)

Label(wrapper1, text="{}".format(namaKereta), fg="#2F58CD", bg="#f5f5f5", font=("Calibri", 22)).place(x=14, y=7)
Frame(wrapper1, width=360, height=1, bg="#999999").place(x=20, y=53)

Label(wrapper1, text="{}\n                      ".format(userAsal), fg="#444444", bg="#f5f5f5", font=("Calibri", 11),justify="left").place(x=22, y=57)
Label(wrapper1, text="{}\n                              ".format(userTujuan), fg="#444444", bg="#f5f5f5", font=("Calibri", 11), justify="right").place(x=282, y=57)
Label(wrapper1, text="{}".format(waktuBerangkat), fg="#205295", bg="#f5f5f5", font=("Microsoft YaHei UI Light", 26)).place(x=21, y=93)
Label(wrapper1, text="{}\n          ".format(waktuSampai), fg="#205295", bg="#f5f5f5", font=("Microsoft YaHei UI Light", 26), justify="right").place(x=275, y=93)
Label(wrapper1, image=kanan_img, font=30, bg="#f5f5f5").place(x=195, y=106)
Label(wrapper1, text=f"{tanggalTiket()}\n                        ", fg="#444444", bg="#f5f5f5", font=("Microsoft JengHei", 10), justify="left").place(x=23, y=160)
Label(wrapper1, text=f"{tanggalTiket()}\n                        ", fg="#444444", bg="#f5f5f5", font=("Microsoft JengHei", 10), justify="right").place(x=278, y=160)
Label(wrapper1, text="Durasi {}\n                                  ".format(hitungDurasi()), fg="#444444", bg="#f5f5f5", font=("Arial", 9), justify="center").place(x=147, y=140)

#################################################################
Label(payment, text="Detail Harga", fg="#2F58CD", bg="#dfdfde", font=("Calibri", 14, "bold")).place(x=262, y=247)

wrapper2 = CTkFrame(payment, width=400, height=160, fg_color="#f5f5f5", corner_radius=10)
wrapper2.place(x=262, y=280)

Label(wrapper2, text="{} / {}".format(namaKereta, inisialKelas()), fg="#000000", bg="#f5f5f5", font=("Calibri", 17)).place(x=16, y=9)
Label(wrapper2, text=f"Penumpang x {userJumlah}", fg="#444444", bg="#f5f5f5", font=("Calibri", 11),justify="left").place(x=19, y=60)
Label(wrapper2, text=f"{hitungHarga()}\n                        ", fg="#444444", bg="#f5f5f5", font=("Microsoft JengHei", 10), justify="right").place(x=278, y=60)
Label(wrapper2, text="Total Harga", fg="#2F58CD", bg="#f5f5f5", font=("Calibri", 14, "bold")).place(x=20, y=110)
Label(wrapper2, text=f"{hitungHarga()}\n                                     ", fg="#2F58CD", bg="#f5f5f5", font=("Calibri", 14, "bold"), justify="right").place(x=228, y=110)

Frame(wrapper2, width=360, height=1, bg="#999999").place(x=20, y=95)

##################################################################

CTkButton(payment, width=402, height=30, text="Bayar", font=("Vernada", 12),text_color="black", fg_color="#ff8400", hover_color="#ff6000", border_spacing=0, corner_radius=10, cursor="hand2", command=pembayaran).place(x=261, y=448)

payment.mainloop()