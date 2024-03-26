import http.server
import socketserver
import psycopg2
from jinja2 import Environment, FileSystemLoader

from config import DATABASE_CONFIG


PORT = 8080
ENV = Environment(loader=FileSystemLoader("."))


class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.respond()
        else:
            super().do_GET()
  
    def respond(self):
        conn = psycopg2.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT * FROM data")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        template = ENV.get_template("index.html")
        content = template.render(data=rows)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


def main():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
