import http.server
import socketserver

PORT = 8080  # Choose a port number (avoid those below 1024)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
