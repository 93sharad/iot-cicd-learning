from http.server import BaseHTTPRequestHandler, HTTPServer


def get_message():
    return "Mondelez IoT application is running"


class IoTHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(get_message().encode())

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), IoTHandler)
    print("Mondelez IoT application listening on port 8080")
    server.serve_forever()
