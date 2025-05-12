import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"本地伺服器運行中：http://127.0.0.1:{PORT}")
    httpd.serve_forever()