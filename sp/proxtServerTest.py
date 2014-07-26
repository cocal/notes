# -*- coding: utf-8 -*-
'''
Created on 2014年7月26日

@author: cocal
'''
import tornado.web
import socket


# class ProxyHandler(tornado.web.RequestHandler):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
#     upstream = tornado.iostream.IOStream(s)
#     upstream.connect((host, int(port)), start_tunnel)


def startProxy(port):
    def get():
        print 'hjeh'
        
startProxy(0)