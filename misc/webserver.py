from http.server import SimpleHTTPRequestHandler, HTTPServer


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"pong")
        else:
            super().do_GET()


HOST = "0.0.0.0"
PORT = 8080

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), CustomHandler)
    server.serve_forever()
