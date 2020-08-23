# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler
import time


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
        
    def do_GET(self):
        self.send_response(200)
        self.send_header('wc', 'ww')
        self.end_headers()
        self.wfile.write(bytes('asdasdasd', 'utf-8'))
        print('------------------------------')
        print(self.path)
        print(self.command)
        print('------------------------------')
        print(self.client_address)
        print('------------------------------')
        print(self.headers)
        print('==============================')
        # print(self.rfile.read())
        # self.respond()
        
    def do_POST(self):
        return

    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes('Hello World not found', 'UTF-8')

    def respond(self):
        content = self.handle_http(200, 'text/html')
        print(content)
        self.wfile.write(content)
        time.sleep(3)
        self.wfile.write(bytes('asdasdasd', 'utf-8'))
