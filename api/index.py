from http.server import BaseHTTPRequestHandler
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        f = open("requirements.txt", "r")
        message = cow.Cowacter().milk(f.read())
        self.wfile.write(message.encode())
        return
