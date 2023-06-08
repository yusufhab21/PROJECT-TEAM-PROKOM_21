import tkinter as tk

def pembayaran():
    nominal_uang = float(entry_nominal.get())

    if nominal_uang == 50000:
        label_hasil.config(text="Pembayaran Berhasil!")
        tiket_button = tk.Button(window, text="CETAK ETIKET", command=cetak_tiket)
        tiket_button.pack()
    else:
        label_hasil.config(text="Nominal Uang Tidak Sesuai!\n Masukan Nominal Yang Sesuai!")

def cetak_tiket():
    nama_penumpang = "ABID"
    nama_kereta = "LOGAWA"
    kelas_kereta = "EKSEKUTIF"
    stasiun_asal ="LEMPUYANGAN"
    stasiun_tujuan = "SOLO BALAPAN"
    waktu_awal = "13:00"
    waktu_akhir = "15:00"

    # TAMPILAN TIKET
    tiket_window = tk.Toplevel(window)
    tiket_window.title("Tiket Kereta Api")
    
    label_title = tk.Label (tiket_window, text= "=====TIKET KERETA KRL 21=====")
    label_title.pack()
    
    label_nama = tk.Label(tiket_window, text="Nama Penumpang: " + nama_penumpang)
    label_nama.pack()

    label_kereta = tk.Label(tiket_window, text="Nama Kereta:"+ nama_kereta)
    label_kereta.pack()
    
    label_kelas = tk.Label(tiket_window, text="Kelas Kereta:"+ kelas_kereta)
    label_kelas.pack()

    label_asal = tk.Label(tiket_window, text="Stasiun Asal: " + stasiun_asal)
    label_asal.pack()
    
    label_tujuan = tk.Label(tiket_window, text="Stasiun Tujuan: " + stasiun_tujuan)
    label_tujuan.pack()

    label_awal = tk.Label(tiket_window, text="Waktu Berangkat: " + waktu_awal)
    label_awal.pack()

    label_akhir = tk.Label(tiket_window, text="Waktu Tiba:" + waktu_akhir)
    label_akhir.pack()

window = tk.Tk()
window.title("Cek Pembayaran")

label_nominal = tk.Label(window, text="Nominal Uang:")
label_nominal.pack()
entry_nominal = tk.Entry(window)
entry_nominal.pack()

tombol_cek = tk.Button(window, text="Cek Pembayaran", command=pembayaran)
tombol_cek.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()