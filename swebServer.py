#inserendo ip locale e numero porta, si crea un semplice webserver


import easygui
import http.server
import socketserver

a = easygui.enterbox(title="INSERT INFO",msg="enter ip and port\n es: IP:PORT")
sp = a.split(":")
ip = sp[0]
port = int(sp[1])
def tool(serv):
    op = easygui.choicebox(msg="scelta", choices=["server"])
    if "server" in op:
        
        easygui.msgbox(msg="SERVER STARTED", title="Avviso", ok_button="PREMI")
        serv()
         



def serv():
    h = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer((ip,port),h)#ciao
    server.serve_forever()

tool(serv)
