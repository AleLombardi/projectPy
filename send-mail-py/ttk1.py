#Python 3.7


from tkinter import *
from tkinter.ttk import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image

import smtplib

def new():
    
    messagebox.showinfo("info","Il programma funziona inserendo\n"
                        "le proprie credenziali di accesso Gmail\n"
                        "Esempio: (To: Tua mail@gmail.com)\n"
                        "(Password: 'password' gmail account)")
def ab():
    messagebox.showinfo("About","Python-Send Mail\n"
                        "Version 0.0.1\n"
                        "Copyright © 2019 Alex Lom\n"
                        "All rights reserved")
    
def send():
    
    
    try:    
        
    
        
        a = text.get()
        b = text1.get()
        c = text2.get()
        d = text3.get()#Subject
        e = text4.get()
    
        
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(b,c)
    
    
        testo = "Subject: "+ d +"\n"+e
        s.sendmail(b,a,testo.encode("utf-8"))
        messagebox.showinfo("Gmail","Mail inviata con successo!")
        s.close()


    except:
        messagebox.showerror("Controllo campi", "Uno dei seguenti campi è\n"
                             "vuoto oppure errati.\n"
                             "Controllare la sezione mail o la password\n")
        
    

    

root = Tk()
root.title("Client di PostaElettronica")
root.geometry("400x200")
root.config(bg='AntiqueWhite1')
root.resizable(0,0)


menu = Menu(root)

root.config(menu=menu)



file = Menu(menu)
menu.add_cascade(label="Help",menu=file)
file.add_command(label="info", command=new)
file.add_separator()

helpm = Menu(menu)
menu.add_cascade(label="About",menu=helpm)
helpm.add_command(label="info", command=ab)


i =Image.open("client.jpg")
render = ImageTk.PhotoImage(i)
img = Label(root, image=render)
img.place(x=0, y=0)



lb1 = Label(root, text="To:  ", background="red").grid(row=0, column=0)
lb1 = Label(root, text="From:  ", background="yellow").grid(row=1, column=0)
lb1 = Label(root, text="Password:  ",background="green").grid(row=2, column=0)
lb1 = Label(root, text="Subject:  ",background="violet").grid(row=3, column=0)
lb1 = Label(root, text="Testo:  ",background="violet").grid(row=4, column=0)




text = StringVar(root)
en = Entry(root,textvariable=text).grid(row=0, column=1)


text1 = StringVar(root)
en1 = Entry(root,textvariable=text1).grid(row=1, column=1)
text1.set("username Gmail")

text2 = StringVar(root)
en2 = Entry(root,textvariable=text2, show="*").grid(row=2, column=1)
#text2.set("password Gmail")

text3 = StringVar(root)
en3 = Entry(root,textvariable=text3).grid(row=3, column=1)

text4 = StringVar(root)
en4 = Entry(root,textvariable=text4).grid(row=4, column=1)

tkinter.ttk.Style(root)


bt1 = tkinter.Button(root,text="send",bg="green",fg="white", command=send)
bt1.grid(row=5,column=0)
bt2=tkinter.Button(root,text="Chiudi",bg="violet",fg="red",command=root.destroy)
bt2.grid(row=5,column=1,columnspan=2, rowspan=2, sticky=W+E+N+S, padx=20, pady=50)



root.mainloop()
