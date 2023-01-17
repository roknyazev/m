from http.server import HTTPServer, CGIHTTPRequestHandler

address = ('localhost', 8000)
srv = HTTPServer(address, CGIHTTPRequestHandler)
srv.serve_forever()
