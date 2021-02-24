#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer
from threading import Thread
from secret import flag
from Crypto.Util.number import *
import base64
BUFSIZE = 1024
banner='''
                  _                 _             _                 
  __ _  __ _  ___| |__   __ _   ___| |_ __ _ _ __| |_    ___  _ __  
 / _` |/ _` |/ __| '_ \ / _` | / __| __/ _` | '__| __|  / _ \| '_ \ 
| (_| | (_| | (__| | | | (_| | \__ \ || (_| | |  | |_  | (_) | | | |
 \__, |\__,_|\___|_| |_|\__,_| |___/\__\__,_|_|   \__|  \___/|_| |_|
 |___/                                                              

'''
class Task(BaseRequestHandler):
    def recvline(self,BUFSIZE):
        return self.request.recv(BUFSIZE).decode().split("\n")[0].strip()
    def init(self):#向RSA之神祈祷吧
        self.SSR=0
        self.p=getPrime(512)
        self.q=getPrime(512)
        self.n=self.p*self.q
        self.e=0x10001
        self.d=inverse(self.e,(self.p-1)*(self.q-1))
        self.c=pow(bytes_to_long(flag.encode()),self.e,self.n)
        self.card_library=["N","R","SR","SSR"]
    def draw_card(self):
        self.request.send("What do you want to say to God:".encode())
        message=self.recvline(BUFSIZE)
        try:
            choice=pow(int(message),self.d,self.n)%4
        except :
            choice=0
        if self.card_library[choice]=="SSR":
            self.SSR+=1
            self.request.send("You got one SSR!\n".encode())
        else:
            self.SSR=0#败者食尘
            self.request.send("You got one {}!\n".format(self.card_library[choice]).encode())
    def get_ssr_num(self):
        return self.SSR
    def get_treasure(self):
        return "You got the treasure!\n{}\n{}".format(str(self.n),str(self.c))
    def handle(self):
        self.init()
        menu = '''
1. draw card
2. show SSR num
3. get treasure
4. exit
>'''
        self.request.send(banner.encode())
        try:
            while True:
                self.request.send(menu.encode())
                choice=self.recvline(BUFSIZE)
                if choice=="1":
                    self.draw_card()
                    continue
                if choice=="2":
                    ssr_num=self.get_ssr_num()
                    self.request.send(("ssr_num:{}".format(str(ssr_num))).encode())
                    continue
                if choice=="3":
                    treasure=self.get_treasure()
                    self.request.send(treasure.encode())
                    continue
                if choice=="4":
                    self.request.send("Bye!".encode())
                    return
        except:
            return False

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 9999
    server = ThreadingTCPServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()