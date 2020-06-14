#hidden text string in a jpg



#sostituire AAAAAAAAAAAAAAAAAAAAAA
#es: "AApasswordtuaAAAAAAAAA"



__author__      = "Alex Lom"
__copyright__   = "Copyright  © 2019"
__version__     = "1.0.0" 


import easygui
import base64
import os



def decode():
    
    foto = easygui.fileopenbox(msg="Seleziona foto")
    f = open(foto,"rb").read()
    c = base64.encodebytes(f)
    o = easygui.codebox(c)
    os = easygui.textbox(o)
    scr = open("fll.txt","w")#crea doc.txt 
    scr.write(str(os))
    scr.close()
    salva(scr)



def salva(scr):

    testo = easygui.fileopenbox()
    f = open(testo,"rb").read()
    fo = open("crypt.jpg","wb") #nome foto da salvare
    fo.write(base64.decodebytes(f))
    
    
    fo.close()
    remove = easygui.fileopenbox(title="Rimuovi file")#rimuove/elimina file doc.txt
    os.remove(remove)



decode()

