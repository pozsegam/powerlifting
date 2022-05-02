import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image



def versenyzoBeszur():
  if entryAzonosito.get() == "" or entryEdzoSzemelyi.get() == "" or entrySzemelyi.get() == "" or entryNev.get() == "" or entrySzuletesiDate.get() == "" or nemEntry.get() == "" or nemzetisegEntry.get() == "":
    MessageBox.showinfo("Info", "Minden mező kötelező")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('insert into versenyzo values("{}","{}","{}","{}","{}","{}","{}")'.format(entryAzonosito.get(), entryEdzoSzemelyi.get(), entrySzemelyi.get(), entrySzuletesiDate.get(), entryNev.get(), nemEntry.get(), nemzetisegEntry.get()))
    cursor.execute('commit')
    entryAzonosito.delete(0, 'end')
    entryEdzoSzemelyi.delete(0, 'end')
    entrySzemelyi.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryNev.delete(0, 'end')
    nemEntry.delete(0, 'end')
    nemzetisegEntry.delete(0, 'end')
    
    MessageBox.showinfo('Info', 'Sikeres beszúrás')
    con.close()



def versenyzoLeker():
  if entryAzonosito.get() == "":
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev, nemzetiseg from versenyzo')
    records = cursor.fetchall()
    for i in records:
      versenyzoListBox.insert(0,i)
  else:
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev from versenyzo where versenyzoID = {}'.format(entryAzonosito.get()))
    records = cursor.fetchmany(1)
    versenyzoListBox.delete(0, versenyzoListBox.size())
    versenyzoListBox.insert(0,records)
    con.close()

def versenyzoTorol():
  #versenyzot edzovel egyutt lehet torolni
  if entryAzonosito.get() == "" or entryEdzoSzemelyi=="":
    MessageBox.showinfo("Info", "ID mező kötelező")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('delete from edzo where EDZOszemelyi_szam = "{}"'.format(entryEdzoEdzoSzemelyi.get()  )    )
    cursor.execute('delete from versenyzo where versenyzoID="{}"'.format(entryAzonosito.get()))
    
    cursor.execute('commit')
    entryAzonosito.delete(0, 'end')
    entryEdzoSzemelyi.delete(0, 'end')
    entrySzemelyi.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryNev.delete(0, 'end')
    nemEntry.delete(0, 'end')
    versenyzoListBox.delete(0, versenyzoListBox.size())
    MessageBox.showinfo('Info', 'Törlés végrehajtva')
    con.close()

def versenyzoFrissit():
  if entryAzonosito.get() == "" or entryEdzoSzemelyi.get() == "" or entrySzemelyi.get() == "" or entryNev.get() == "" or entrySzuletesiDate.get() == "" or nemEntry.get() == "" or nemzetisegEntry.get() == "":
    MessageBox.showinfo("Info", "ID mező kötelező")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('update versenyzo set EDZOszemelyi_szam = "{}", szemelyi_szam ="{}", szuletesi_ido = "{}", nev = "{}", nem = "{}", nemzetiseg = "{}" where versenyzoID ="{}"'.format(entryEdzoSzemelyi.get(), entrySzemelyi.get(), entrySzuletesiDate.get(), entryNev.get(), nemEntry.get(), nemzetisegEntry.get(), entryAzonosito.get() ) )
    cursor.execute('commit')
    entryAzonosito.delete(0, 'end')
    entryEdzoSzemelyi.delete(0, 'end')
    entrySzemelyi.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryNev.delete(0, 'end')
    nemEntry.delete(0, 'end')
    nemzetisegEntry.delete(0, 'end')
    MessageBox.showinfo('Info', 'Frissites vegrehajtva')
    con.close()








def edzoBeszur():
  #csak versenyzovel egyutt lehet
  if entryEdzoEdzoSzemelyi.get() == "" or entryEdzoNev == "" or entryEdzoEdzoSzuldate.get() == "" or entryAzonosito.get() == "" or entryEdzoNemzetiseg.get() == "" or entryEdzoSzemelyi.get() == "" or entrySzemelyi.get() == "" or entryNev.get() == "" or entrySzuletesiDate.get() == "" or nemEntry.get() == "" or nemzetisegEntry.get() == "":
    MessageBox.showinfo("Info", "Edzot versenyzovel egyutt kell felvenni!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('insert into versenyzo values("{}","{}","{}","{}","{}","{}","{}")'.format(entryAzonosito.get(), entryEdzoSzemelyi.get(), entrySzemelyi.get(), entrySzuletesiDate.get(), entryNev.get(), nemEntry.get(), nemzetisegEntry.get()))
    cursor.execute('insert into edzo values("{}","{}","{}","{}")'.format(entryEdzoEdzoSzemelyi.get(), entryEdzoNev.get(), entryEdzoEdzoSzuldate.get(), entryEdzoNemzetiseg.get()  )  )
    cursor.execute('commit')
    entryEdzoSzemelyi.delete(0,'end')
    entryEdzoEdzoSzemelyi.delete(0, 'end')
    entryEdzoNev.delete(0, 'end')
    entryEdzoEdzoSzuldate.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryEdzoNemzetiseg.delete(0, 'end')
    entryAzonosito.delete(0, 'end')
    entrySzemelyi.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryNev.delete(0, 'end')
    nemEntry.delete(0, 'end')
    nemzetisegEntry.delete(0, 'end')

    
    MessageBox.showinfo('Info', 'Sikeres beszúrás')
    con.close()



def edzoLeker():
  if entryEdzoEdzoSzemelyi.get() == "":
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev from edzo')
    records = cursor.fetchall()
    for i in records:
      edzoListBox.insert(0,i)
    con.close()
  else:
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev from edzo where EDZOszemelyi_szam = "{}"'.format(  entryEdzoEdzoSzemelyi.get()  )  )
    records = cursor.fetchmany(1)
    edzoListBox.delete(0, edzoListBox.size())
    edzoListBox.insert(0,records)
    con.close()


def edzoTorol():
  
  if entryAzonosito.get() == "" or entryEdzoEdzoSzemelyi=="":
    MessageBox.showinfo("Info", "Versenyzovel egyutt lehet torlni!(ID + EdzoSzemelyi)")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('delete from edzo where EDZOszemelyi_szam = "{}"'.format(entryEdzoEdzoSzemelyi.get()  )    )
    cursor.execute('delete from versenyzo where versenyzoID="{}"'.format(entryAzonosito.get()))
    
    cursor.execute('commit')


    entryAzonosito.delete(0, 'end')
    entryEdzoSzemelyi.delete(0, 'end')
    entrySzemelyi.delete(0, 'end')
    entrySzuletesiDate.delete(0, 'end')
    entryNev.delete(0, 'end')
    nemEntry.delete(0, 'end')
    entryEdzoEdzoSzemelyi.delete(0, 'end')
    entryEdzoNev.delete(0, 'end')
    entryEdzoEdzoSzuldate.delete(0, 'end')
    entryEdzoNemzetiseg.delete(0, 'end')

    versenyzoListBox.delete(0, versenyzoListBox.size())
    MessageBox.showinfo('Info', 'Törlés végrehajtva')
    con.close()

def edzoModosit():
  if entryEdzoEdzoSzemelyi.get() == "":
    MessageBox.showinfo("Info", "szemelyi kötelező!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('update edzo set nev = "{}", szuletesi_ido = "{}", nemzetiseg = "{}" where EDZOszemelyi_szam ="{}"'.format( entryEdzoNev.get(), entryEdzoEdzoSzuldate.get(), entryEdzoNemzetiseg.get(), entryEdzoEdzoSzemelyi.get() )  )
    cursor.execute('commit')
    entryEdzoNev.delete(0, 'end')
    entryEdzoEdzoSzuldate.delete(0, 'end')
    entryEdzoNemzetiseg.delete(0, 'end')
    MessageBox.showinfo('Info', 'Frissites vegrehajtva')
    con.close()





def szovetsegBeszur():
  if entrySzovetsegNev.get() == "" or entrySzovetsegLetrehozas == "":
    MessageBox.showinfo("Info", "Minden mezo kitoltese kotelezo!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('insert into szovetseg values("{}","{}")'.format( entrySzovetsegNev.get(), entrySzovetsegLetrehozas.get()  ) )
    cursor.execute('commit')
    entrySzovetsegNev.delete(0,'end')
    entrySzovetsegLetrehozas.delete(0,'end')
    MessageBox.showinfo('Info', 'Sikeres beszúrás')


def szovetsegLeker():
  if entrySzovetsegNev.get() == "":
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev from szovetseg')
    records = cursor.fetchall()
    for i in records:
      szovetsegListBox.insert(0,i)
    con.close()
  else:
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select * from szovetseg where nev = "{}"'.format(  entrySzovetsegNev.get() )  )
    records = cursor.fetchmany(1)
    szovetsegListBox.delete(0, edzoListBox.size())
    szovetsegListBox.insert(0,records)
    entrySzovetsegNev.delete(0,'end')
    con.close()



def szovetsegModosit():
  if entrySzovetsegNev.get() == "":
    MessageBox.showinfo("Info", "nev kotelezo!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('update szovetseg set letrehozasDatuma ="{}" where nev = "{}"'.format( entrySzovetsegLetrehozas.get(), entrySzovetsegNev.get() ) )
    cursor.execute('commit')
    entrySzovetsegLetrehozas.delete(0,'end')
    entrySzovetsegNev.delete(0,'end')
    MessageBox.showinfo('Info', 'Frissites vegrehajtva')
    con.close()



def szovetsegTorol():
  if entrySzovetsegNev.get() == "":
    MessageBox.showinfo("Info", "Nev nelkul nem lehet mit torolni :)")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('delete from szovetseg where nev = "{}"'.format(entrySzovetsegNev.get()  )    )    
    cursor.execute('commit')

    entrySzovetsegNev.delete(0, 'end')
    MessageBox.showinfo('Info', 'Törlés végrehajtva')
    con.close()

#-----------------------------------

def biroBeszur():
  if entryBiroSzemelyi.get() == "" or entryBiroNev == "":
    MessageBox.showinfo("Info", "Minden mezo kitoltese kotelezo!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('insert into biro values("{}","{}")'.format( entryBiroSzemelyi.get(), entryBiroNev.get()  ) )
    cursor.execute('commit')
    entryBiroNev.delete(0,'end')
    entryBiroSzemelyi.delete(0,'end')
    MessageBox.showinfo('Info', 'Sikeres beszúrás')


def biroLeker():
  if entryBiroSzemelyi.get() == "":
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select nev from biro')
    records = cursor.fetchall()
    for i in records:
      biroListBox.insert(0,i)
    con.close()
  else:
    con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
    cursor = con.cursor()
    cursor.execute('select * from biro where szemelyi_szam = "{}"'.format(  entryBiroSzemelyi.get() )  )
    records = cursor.fetchmany(1)
    biroListBox.delete(0, biroListBox.size())
    biroListBox.insert(0,records)
    con.close()



def biroModosit():
  if entryBiroSzemelyi.get() == "":
    MessageBox.showinfo("Info", "nev kotelezo!")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('update biro set nev ="{}" where szemelyi_szam = "{}"'.format( entryBiroNev.get(), entryBiroSzemelyi.get() ) )
    cursor.execute('commit')
    entryBiroSzemelyi.delete(0,'end')
    entryBiroNev.delete(0,'end')
    MessageBox.showinfo('Info', 'Frissites vegrehajtva')
    con.close()


def biroTorol():
  if entryBiroNev.get() == "":
    MessageBox.showinfo("Info", "Nev nelkul nem lehet mit torolni :)")
  else:
    con = mysql.connect(host="localhost", user="root", database="eroemelo")
    cursor = con.cursor()
    cursor.execute('delete from biro where nev = "{}"'.format(entryBiroNev.get()  )    )    
    cursor.execute('commit')
    entryBiroNev.delete(0, 'end')
    MessageBox.showinfo('Info', 'Törlés végrehajtva')
    con.close()

def NemTrivialisMethod1():
  con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
  cursor = con.cursor()
  cursor.execute('SELECT versenyzo.nev, COUNT(megnyerte.VERSENYZOversenyzoID) AS HanyszorNyertVersenyt FROM megnyerte INNER JOIN versenyzo ON versenyzo.versenyzoID = megnyerte.VERSENYZOversenyzoID INNER JOIN verseny ON verseny.VERSENYnev = megnyerte.VERSENYnev GROUP BY megnyerte.VERSENYZOversenyzoID ORDER BY HanyszorNyertVersenyt ASC')
  records = cursor.fetchall()
  for i in records:
    ListBoxNemTrivialis1.insert(0,i)
  con.close()

def NemTrivialisMethod2():
  con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
  cursor = con.cursor()
  cursor.execute('SELECT biro.nev, COUNT(biral.BIROszemelyi_szam) AS alkalom FROM biro LEFT JOIN biral ON biral.BIROszemelyi_szam = biro.szemelyi_szam GROUP BY biro.nev ORDER BY alkalom DESC')
  records = cursor.fetchall()
  for i in records:
    ListBoxNemTrivialis2.insert(0,i)
  con.close()


def NemTrivialisMethod3():
  con = mysql.connect(host = "localhost", user = "root", database = "eroemelo")
  cursor = con.cursor()
  cursor.execute('SELECT biro.nev, versenyzokSzama FROM verseny INNER JOIN biral ON biral.VERSENYnev = verseny.VERSENYnev INNER JOIN biro ON biro.szemelyi_szam = biral.BIROszemelyi_szam WHERE versenyzokSzama > ( SELECT AVG(versenyzokSzama) FROM verseny) ORDER BY versenyzokSzama ASC')
  records = cursor.fetchall()
  for i in records:
    ListBoxNemTrivialis3.insert(0,i)
  con.close()
  


#main fuggveny
if __name__ == '__main__':
  #adatb import
  dbhost = 'localhost'
  dbuser = 'root'
  dbname = 'eroemelo'

  #alap objektum merete cime
  root = tk.Tk()
  root.geometry("900x1000")
  root.title("eroemelo eredmenyek")
  root['bg'] = '#49A'

  # kep beszurasa, helyezese
  #img = ImageTk.PhotoImage(Image.open("powerlift.gif"))
  
  
  
  #imgCimke = tk.Label(root, image=img)
  #imgCimke.place(x=20,y=800)

  
  
  #versenyzo tabla kezelese 

  tablanev1 = tk.Label(root, text='versenyzo', font=('Cooper Black', 10))
  tablanev1.place(x=180, y=5)

  #       azonosito
  azonosito = tk.Label(root, text='azonosito', font=('Cooper Black', 10))
  azonosito.place(x=10, y=30)

  entryAzonosito = tk.Entry()
  entryAzonosito.place(x=140, y=30)


#       nev

  nev = tk.Label(root, text='nev', font=('Cooper Black', 10))
  nev.place(x=10, y=60)

  entryNev = tk.Entry()
  entryNev.place(x=140, y=60)
  
  #versenyzo szemelyi szama
  
  szemelyi = tk.Label(root, text='szemelyi szam', font=('Cooper Black', 10))
  szemelyi.place(x=10, y=90)

  entrySzemelyi = tk.Entry()
  entrySzemelyi.place(x=140, y=90)



#       szuletesi ido
  szuletesiDate = tk.Label(root, text='szuletesi datum', font=('Cooper Black', 10))
  szuletesiDate.place(x=10, y=120)

  entrySzuletesiDate = tk.Entry()
  entrySzuletesiDate.place(x=140, y=120)

  #edzo szemelyiszam

  edzoSzemelyi = tk.Label(root, text='edzo szemelyi', font=('Cooper Black', 10))
  edzoSzemelyi.place(x=10, y=150)

  entryEdzoSzemelyi = tk.Entry()
  entryEdzoSzemelyi.place(x=140, y=150)


  # nem
  nem = tk.Label(root, text='nem', font=('Cooper Black', 10))
  nem.place(x=10, y=180)

  nemEntry = tk.Entry()
  nemEntry.place(x=140, y=180)


  #nemzetiseg
  nemzetiseg = tk.Label(root, text='nemzetiseg', font=('Cooper Black', 10))
  nemzetiseg.place(x=10, y=210)

  nemzetisegEntry = tk.Entry()
  nemzetisegEntry.place(x=140, y=210)




  beszurGomb1 = tk.Button(root, text="Beszúr", font=('bold', 10), bg="white", command=versenyzoBeszur)
  beszurGomb1.place(x = 80, y = 250)

  lekerGomb1 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command=versenyzoLeker)
  lekerGomb1.place(x = 150, y = 250)
  

  torolGomb1 = tk.Button(root, text="Torol", font=('bold', 10), bg="white", command=versenyzoTorol)
  torolGomb1.place(x = 290, y = 250)

  updateGomb1 = tk.Button(root, text="Modosit", font=('bold', 10), bg="white", command=versenyzoFrissit)
  updateGomb1.place(x = 220, y = 250)

  #listbox versenyzo tablanal
  versenyzoListBox= tk.Listbox(root, width = 40)
  versenyzoListBox.place(x=370, y=10)

  


#----------------- EDZO ------------------------------
  tablanev2 = tk.Label(root, text='edzo', font=('Cooper Black', 10))
  tablanev2.place(x=180, y=305)


#------Edzo entry
  Edzonev = tk.Label(root, text='edzo neve', font=('Cooper Black', 10))
  Edzonev.place(x=10, y=330)

  entryEdzoNev = tk.Entry()
  entryEdzoNev.place(x=140, y=330)
  

#--------Edzo szemelyi entry
  Edzo_Tabla_Szemelyi = tk.Label(root, text='edzo szemelyi', font=('Cooper Black', 10))
  Edzo_Tabla_Szemelyi.place(x=10, y=360)

  entryEdzoEdzoSzemelyi = tk.Entry()
  entryEdzoEdzoSzemelyi.place(x=140, y=360)


#---------Edzo szemelyi
  edzoSzuletesiDate = tk.Label(root, text='edzo szuletesi ido', font=('Cooper Black', 10))
  edzoSzuletesiDate.place(x=10, y=390)

  entryEdzoEdzoSzuldate = tk.Entry()
  entryEdzoEdzoSzuldate.place(x=140, y=390)


#--------Edzo nemzetiseg
  edzoNemzetiseg = tk.Label(root, text='nemzetiseg', font=('Cooper Black', 10))
  edzoNemzetiseg.place(x=10, y=420)

  entryEdzoNemzetiseg = tk.Entry()
  entryEdzoNemzetiseg.place(x=140, y=420)


#---------gombok
  beszurGomb2 = tk.Button(root, text="Beszúr", font=('bold', 10), bg="white", command=edzoBeszur)
  beszurGomb2.place(x = 80, y = 450)

  lekerGomb2 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command=edzoLeker)
  lekerGomb2.place(x = 150, y = 450)
  

  torolGomb2 = tk.Button(root, text="Torol", font=('bold', 10), bg="white", command=edzoTorol)
  torolGomb2.place(x = 290, y = 450)

  updateGomb2 = tk.Button(root, text="Modosit", font=('bold', 10), bg="white", command=edzoModosit)
  updateGomb2.place(x = 220, y = 450)

#listbox

  edzoListBox = tk.Listbox(root, width = 40)
  edzoListBox.place(x=370, y=310)




#-----------------------------  szovetseg tabla
  tablanev3 = tk.Label(root, text='szovetseg', font=('Cooper Black', 10))
  tablanev3.place(x=180, y=510)


#------ szovetseg entry
  szovetsegNev = tk.Label(root, text='szovetseg neve', font=('Cooper Black', 10))
  szovetsegNev.place(x=10, y=540)

  entrySzovetsegNev = tk.Entry()
  entrySzovetsegNev.place(x=140, y=540)
  

#-------- letrehozas entry
  SzovetsegLetrehozas = tk.Label(root, text='letrehozas datuma', font=('Cooper Black', 10))
  SzovetsegLetrehozas.place(x=10, y=570)

  entrySzovetsegLetrehozas = tk.Entry()
  entrySzovetsegLetrehozas .place(x=140, y=570)

# gombok szovetseg
  beszurGomb3 = tk.Button(root, text="Beszúr", font=('bold', 10), bg="white", command=szovetsegBeszur)
  beszurGomb3.place(x = 80, y = 600)

  lekerGomb3 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command=szovetsegLeker)
  lekerGomb3.place(x = 150, y = 600)
  

  torolGomb3 = tk.Button(root, text="Torol", font=('bold', 10), bg="white", command=szovetsegTorol)
  torolGomb3.place(x = 290, y = 600)

  updateGomb3 = tk.Button(root, text="Modosit", font=('bold', 10), bg="white", command=szovetsegModosit)
  updateGomb3.place(x = 220, y = 600)

  szovetsegListBox = tk.Listbox(root, width = 40)
  szovetsegListBox.place(x=370, y=490)




#-------------------------------  biro tabla
  biroSzemelyi = tk.Label(root, text='biro szemelyi szama', font=('Cooper Black', 10))
  biroSzemelyi.place(x=10, y=660)

  entryBiroSzemelyi = tk.Entry()
  entryBiroSzemelyi.place(x=140, y=660)


#-------- biro szemelyi
  biroNev = tk.Label(root, text='nev', font=('Cooper Black', 10))
  biroNev.place(x=10, y=690)

  entryBiroNev = tk.Entry()
  entryBiroNev.place(x=140, y=690)

#---------gombok
  beszurGomb4 = tk.Button(root, text="Beszúr", font=('bold', 10), bg="white", command=biroBeszur)
  beszurGomb4.place(x = 80, y = 720)

  lekerGomb4 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command=biroLeker)
  lekerGomb4.place(x = 150, y = 720)
  

  torolGomb4 = tk.Button(root, text="Torol", font=('bold', 10), bg="white", command=biroTorol)
  torolGomb4.place(x = 290, y = 720)

  updateGomb4 = tk.Button(root, text="Modosit", font=('bold', 10), bg="white", command=biroModosit)
  updateGomb4.place(x = 220, y = 720)

#listbox

  biroListBox = tk.Listbox(root, width = 40)
  biroListBox.place(x=370, y=660)




# -------------------       3 nem trivialis lekerdezes

#--------------------       NO1

nemTrivialis1 = tk.Label(root, text='hmm.. Vajon ki hanyszor nyert?', font=('bold', 10))
nemTrivialis1.place(x=680, y=10)

lekerGomb5 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command = NemTrivialisMethod1)
lekerGomb5.place(x = 740, y = 40)

ListBoxNemTrivialis1 = tk.Listbox(root, width = 30)
ListBoxNemTrivialis1.place(x=680, y = 70)

#------------------------------- NO2

nemTrivialis2 = tk.Label(root, text='...es ki volt a leglustabb biro,', font=('bold', 10))
nemTrivialis2.place(x= 680, y = 250)


nemTrivialis2b = tk.Label(root, text='aki nem rendezett versenyt,', font=('bold', 10))
nemTrivialis2b.place(x= 680, y = 270)

nemTrivialis2c = tk.Label(root, text='hogy tudjam a left joint hasznalni?,', font=('bold', 10))
nemTrivialis2c.place(x= 680, y = 290)



lekerGomb6 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command = NemTrivialisMethod2)
lekerGomb6.place(x = 740, y = 320)

ListBoxNemTrivialis2 = tk.Listbox(root, width = 30)
ListBoxNemTrivialis2.place(x=680, y = 350)


# -------------------------------   NO3

nemTrivialis3 = tk.Label(root, text='atlagon feluli versenyzoszam', font=('bold', 10))
nemTrivialis3.place(x= 680, y = 520)

nemTrivialis3B = tk.Label(root, text='=', font=('bold', 10))
nemTrivialis3B.place(x= 750, y = 540)

nemTrivialis3C = tk.Label(root, text='legstresszesebb birok', font=('bold', 10))
nemTrivialis3C.place(x= 680, y = 560)

lekerGomb7 = tk.Button(root, text="Leker", font=('bold', 10), bg="white", command = NemTrivialisMethod3)
lekerGomb7.place(x = 740, y = 590)

ListBoxNemTrivialis3 = tk.Listbox(root, width = 30)
ListBoxNemTrivialis3.place(x=680, y = 620)




root.mainloop() 


 