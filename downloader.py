#temp
import urllib.parse, urllib.request, urllib.error
 
def download_File():
    print ("link esempio--->  python/mypy  ")#https://github.com/python/mypy
    link_D = str(input(">>> "))#nome file originale
    nomeFile = str(input(">>> inserisci nome file "))
    url = ("https://raw.githubusercontent.com/"+link_D+"/master/"+nomeFile)
    h = urllib.request.urlopen(url)
    salva(download_Zip, download_File,h)
   
 
 
       
def download_Zip():
    print ("link esempio--->github.com/example/example-example")
    link_D = str(input(">>> "))
    url = ("https://codeload."+link_D+"/zip/master")
    h = urllib.request.urlopen(url)
    salva(download_Zip, download_File,h)
 
def salva(download_Zip, download_File, h):
   
 
    renameFile = str(input("rinomina file"))
    file = open("C:\\Users\\posta\\Desktop\\"+renameFile,"wb")
    size = 0
    while True:
        info = h.read(100000)
        if len(info) < 1:
            break
        size = size +len(info)
        file.write(info)
 
    file.close()
 
def scelta_D():
    print("scegliere 'file' o zipfile")
    scelta = str(input(">>> "))
    if scelta == "zipfile":
        download_Zip()
    if scelta == "file":
        download_File()
 
 
def main():
 
   
    scelta_D()
   
main()
