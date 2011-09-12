# -*- encoding: utf-8 -*-
'''Servidor de teste para o PagSeguro.'''
import socket, cgi
import ssl
import BaseHTTPServer

from BaseHTTPServer import BaseHTTPRequestHandler

class HTTPSHandler(BaseHTTPRequestHandler):

    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

    def send(self,msg,code=200):
        '''Envia HTML para o client'''
        self.send_response(code)
        self.end_headers()
        self.wfile.write(msg)

    def do_POST(self):
        '''Responde a requisições POST'''
        if self.rfile:
            self.data=cgi.parse_qs(self.rfile.read(int(self.headers['Content-Length'])))
        else:
            self.data={}
        ret=self.process()
        self.send(ret)

    def process(self):
        '''Processa a requisição. Sobrescreva este método em suas subclasses.'''
        return "Hello world!"

    def do_GET(self):
        '''Apenas mostra uma mensagem de erro, uma vez que não deveríamos mesmo usar GET.'''
        self.send("Why GETting?")

#server.pem's location (containing the server private key and
#the server certificate).
fpem = 'server.pem'

def run(HandlerClass = HTTPSHandler):#, ServerClass = SecureHTTPServer):

    # Customização do servidor baseado em:
    #   http://www.piware.de/2011/01/creating-an-https-server-in-python/
    httpd = BaseHTTPServer.HTTPServer(('', 443), HandlerClass)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=fpem, server_side=True)
    httpd.serve_forever()

if __name__ == '__main__':
    run()

