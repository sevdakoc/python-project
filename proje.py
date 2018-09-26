print("""
[S]=========İP GUIDE==========[-][O][X]
|
|       Welcome To Program!
|         sürüm python 3.5
|          SEVDA KOÇ
|       koc.sevda.koc@gmail.com
|
[K]=====================================
""")


from tkinter import *
import sqlite3
import os
from tkinter import messagebox
import time

denemeHakki = 3
zaman = 0
bilgiler = ("demo", "1")

#öncelikle bir giriş ekranı yapallım...
 
def veri_girisi():
    def ikisi():
        command=veri_sil()
        tabloya_ekle()
        pencere.destroy()
        
    pencere = Tk()
    pencere.wm_iconbitmap("hourglass")
    
    def girisYap():
        global denemeHakki, zaman
        if denemeHakki <= 0:
            if time.time()-zaman >= 10:
                denemeHakki = 3
            else:
                sonuc.config(text = u"Please 10 second wait.") #Lutfen 10 saniye bekleyiniz
                return False
        
        kAdi = isim.get()
        parola = sifre.get()
        print(kAdi, " - ", parola)
        print("Kontrol ediliyor ...")
        if kAdi == bilgiler[0] and parola == bilgiler[1]:
            print("Bilgiler dogru!")
            sonuc.config(text = u"Oturum acma islemi basarılı\n Yapacağın işlemler veritabanına "+
                         "işlenecek \n işlemi gerçekleştirmek istediğinden emin misin?")
            ekraniTemizle()
            buton.config(text="YES",command=ikisi)
            buton1.pack(side=BOTTOM,pady=10)
            buton1.config(text = u"NO",fg="white",command = pencere.destroy)
            
        else:
            print("Bilgiler yanlis!")
            denemeHakki -= 1
            if denemeHakki == 0:
                zaman = time.time()
            sonuc.config(text = u"Information incorrent. The remaining attempts : %d" %denemeHakki)
            

    def ekraniTemizle():
        karsilama.config(text = u"Welcome, Demo!")
        isimSor.destroy()
        isim.destroy()
        sifreSor.destroy()
        sifre.destroy()
        
    pencere.title(u"DATABASE LOGIN SCREEN")
    pencere.geometry("290x200+100+100")
    pencere.configure(background="lightsalmon")

    karsilama = Label(pencere,bg="lightsalmon")
    karsilama.config(text = u"Welcome, please log in ")
    karsilama.pack(pady=1)#please log in

    isimSor = Label(pencere,bg="lightyellow")
    isimSor.config(text = "User Name:")
    isimSor.pack(pady=1)

    isim = Entry(pencere)
    isim.pack(pady=1)
    isim.focus_set()


    sifreSor = Label(pencere,bg="lightyellow")
    sifreSor.config(text= u"Your password:")
    sifreSor.pack(pady=1)

    sifre = Entry(pencere)
    sifre.pack(pady=1)


    buton = Button(pencere,bg="lightgreen")
    buton.config(text = u"Sign in!", command = girisYap)
    buton.pack(side=BOTTOM,pady=20)

    sonuc = Label(pencere,bg="lightyellow")
    sonuc.config(text = u"Made entry.") #giriş yapamadız
    sonuc.pack(pady=2)

    buton1= Button(pencere,bg="firebrick")
    
    mainloop ()

click=0

baglanti=sqlite3.connect("tablo.db")
imlec=baglanti.cursor()

pencere=Tk()
pencere.wm_iconbitmap("info")

pencere.geometry("400x400")
pencere.title("Ip Application Programming Interface Guide")
pencere.configure(background="cadetblue")

label1 = Label(text="ID : ")
label2 = Label(text="DEVİCE : ")
label3= Label(text="IP ADDRESS : ")
label4=Label(text="GATEWAY : ")
label5=Label(text="PORT NO : ")

yazma1= Entry()
yazma1["state"]=NORMAL
yazma1.delete(0,END) # ne varsa siler 

    
yazma2 = Entry()
yazma2["state"]=NORMAL
yazma2.delete(0,END)

yazma3= Entry()
yazma3["state"]=NORMAL
yazma3.delete(0,END)

yazma4 = Entry()
yazma4["state"]=NORMAL
yazma4.delete(0,END)


yazma5 = Entry()
yazma5["state"]=NORMAL
yazma5.delete(0,END)


# seçme olayını fare tıklama yolu ile kontrol ettim ....

def tablo_oku(event):
    yazma1.delete(0,END)
    yazma2.delete(0,END)
    yazma3.delete(0,END)
    yazma4.delete(0,END)
    yazma5.delete(0,END)
    global click
    os.system('cls')
    click=click+1
    imlec.execute("""SELECT * FROM iplerim""")  # imlec burda veri tabanı üzerinde dolanır .... bunun için tanımlandı
    veriler=imlec.fetchall()
    a=(len(veriler))
    if a<=click-1:
        return 
    else:
        
        idim,cihaz_adi,ip_adresi,gateway,port=veriler[click-1] 
           
        yazma1.insert(END,idim)
        
        yazma2.insert(END,cihaz_adi) # ekleme yapar 

        yazma3.insert(END,ip_adresi)

        yazma4.insert(END,gateway)

        yazma5.insert(END,port)

        return True
      
def tabloya_ekle():
    idim=yazma1.get()
    cihaz=yazma2.get()
    ip=yazma3.get()
    gateway=yazma4.get()
    port=yazma5.get()
    imlec.execute("""INSERT INTO iplerim(ID,CIHAZ,IP,GATEWAY,PORT)
VALUES (?,?,?,?,?)""",(idim,cihaz,ip,gateway,port))
    baglanti.commit()
    messagebox.showinfo("INSERT","İşleminiz gerçekleşmiştir ,"+
                        "yeni bir işlem gerçekleştirmek ister misiniz ?")
##İşleminiz gerçekleşmiştir yeni bir işlem gerçekleştirmek ister misiniz ?
    yazma1.delete(0,END)
    yazma2.delete(0,END)
    yazma3.delete(0,END)
    yazma4.delete(0,END)
    yazma5.delete(0,END)

    

def veri_sil():
    sil=yazma1.get()
    imlec.execute("""DELETE FROM iplerim WHERE ID = '%s';""" % sil.strip())
    baglanti.commit()

def penar_yerlestir(penar, c, r=0, p=20):
    #Daha önce oluşturduğumuz "Label" ve "Entry" 
    #araçlarını pencere üzerine topluca yerleştiriyoruz.
    while r < 5:
        for i in penar:
            i.grid(row    = r, 
                   column = c, 
                   pady   = p, 
                   padx   = p, 
                   sticky = W)
            r += 1      


btn1=Button(text="INSERT",bg="bisque",command=veri_girisi)
btn1.grid(row=10, column=0, columnspan=1, pady=10)

btn2=Button(text="SELECT",bg="bisque")
btn2.grid(row=10, column=1, columnspan=1, pady=10)
btn2.bind("<Button-1>",tablo_oku)


btn3=Button(text="DELETE",bg="bisque",command=veri_girisi)#command=veri_sil
btn3.grid(row=10, column=2, columnspan=1, pady=10,padx=5)

btn4=Button(text="QUİT",bg="firebrick",fg="white",command=pencere.destroy)
btn4.grid(padx=2,row=15, column=5, columnspan=4, pady=4)
 
penar_yerlestir([label1,label2,label3,label4,label5], 0)
penar_yerlestir([yazma1,yazma2,yazma3,yazma4,yazma5], 1)

pencere.mainloop()


