from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x600")

changefont = tkinter.font.Font(size=20)
judl = Label(root,text = "REGISTER",font =changefont)
judl.place(x =80,y = 10)

labelfr = LabelFrame(root,text = "result",padx=20,pady=20)
labelfr.place(x = 60,y = 380)

nama = Label(root,text = "First Name")
nama2 = Label(root,text = "Last Name")
age = Label(root,text = "Age")
username = Label(root,text = "Username")
email = Label(root,text = "Email")
password = Label(root,text = "password" )
gender = Label(root,text = "Gender")

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)
e6 = Entry(root,width=40,show="*")

nama.place(x = 20, y =50)
nama2.place(x = 20, y =90)
age.place(x = 20, y =130)
username.place(x = 20, y =170)
email.place(x = 20, y =210)
password.place(x = 20, y =250)
gender.place(x = 20, y =290)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)
e6.place(x = 20, y = 270)

r = StringVar()
r.set("male")

rb = Radiobutton(root,text = "male",variable=r,value="male").place(x = 20,y =310 )
rb2 = Radiobutton(root,text = "female",variable=r,value="female").place(x = 80,y =310 )

def cetak():
    class orang:
        def __init__(self,nama,nama2,age,username,email,pas,gender):
            self.nama = nama
            self.nama2 = nama2
            self.age = age
            self.username = username
            self.email = email
            self.password = pas
            self.gender = gender
        def hasil(self):
            lbl = Label(labelfr,text="first name ="+self.nama+"\nlast name ="+self.nama2+"\nage ="+self.age+"\nusername = "+self.username+"\nemail ="+self.email+"\npassword ="+self.password+"\ngender ="+self.gender).grid()
    ditampilkan = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),r.get())
    ditampilkan.hasil()



btn = Button(root,text = "submit",command=cetak).place(x = 100,y = 350)


root.mainloop()