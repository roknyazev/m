from http.server import HTTPServer, CGIHTTPRequestHandler
import os

address = ('localhost', 8000)
srv = HTTPServer(address, CGIHTTPRequestHandler)
srv.serve_forever()
