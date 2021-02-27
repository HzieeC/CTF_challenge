#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer
from threading import Thread
import random
from secret import flag
import time

BUFSIZE = 1024
banner='''
 ____                                         _ 
|  _ \ _ __ __ ___      __   ___ __ _ _ __ __| |
| | | | '__/ _` \ \ /\ / /  / __/ _` | '__/ _` |
| |_| | | | (_| |\ V  V /  | (_| (_| | | | (_| |
|____/|_|  \__,_| \_/\_/    \___\__,_|_|  \__,_|
                                                
               _                 
 ___ _   _ ___| |_ ___ _ __ ___  
/ __| | | / __| __/ _ \ '_ ` _ \ 
\__ \ |_| \__ \ ||  __/ | | | | |
|___/\__, |___/\__\___|_| |_| |_|
     |___/                       

'''
class Task(BaseRequestHandler):
    def recvline(self,BUFSIZE):
        return self.request.recv(BUFSIZE).decode().split("\n")[0].strip()
    def init(self,SSR):
        #洗牌
        card_library=["R" for i in range(16)]
        card_library[SSR]="SSR"
        return card_library
    def draw_card(self):
        #8连抽
        seed=hex(random.getrandbits(32))[2:].strip("L").zfill(8)
        for i in seed:
            card_library=self.init(int(i,16))
            self.request.send("Please enter your choice by 0-15:".encode())
            message=self.recvline(BUFSIZE)
            choice=int(message)
            self.request.send(str(card_library).encode())
            if card_library[choice]=="SSR":
                self.SSR+=1
                self.request.send("You got one SSR!\n".encode())
            else:
                self.SSR=0#败者食尘
                self.request.send("You got one R!\n".encode())

    def get_ssr_num(self):
        return self.SSR
    def get_opportunity_num(self):
        return self.opportunity
    def get_flag(self):
        if self.SSR>100:
            self.SSR-=100
            return flag
        else:
            return "Please collect 100 SSRs!"
    def handle(self):
        self.opportunity=1000
        self.SSR=0
        menu = '''
1. draw card
2. show SSR num
3. show opportunity
4. 100 SSR TO exchange flag
5. exit
'''
        self.request.send(banner.encode())
        try:
            while True:
                self.request.send(menu.encode())
                choice=self.recvline(BUFSIZE)
                if choice=="1":
                    if self.opportunity>0:
                        self.draw_card()
                        self.opportunity-=1
                    else:
                        self.request.send("look forward to seeing you next time!".encode())
                    continue
                if choice=="2":
                    ssr_num=self.get_ssr_num()
                    self.request.send(("ssr_num:"+str(ssr_num)).encode())
                    continue
                if choice=="3":
                    opportunity=self.get_opportunity_num()
                    self.request.send(("opportunity:"+str(opportunity)).encode())
                    continue
                if choice=="4":
                    flag=self.get_flag()
                    self.request.send(flag.encode())
                    continue
                if choice=="5":
                    self.request.send("Bye!".encode())
                    return
        except:
            return False

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 9999
    server = ThreadingTCPServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()