import http.server, socketserver, os
PORT = int(os.environ.get('PORT', 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('0.0.0.0', PORT), H) as httpd:
    print('Site Logiciel serving on port', PORT)
    httpd.serve_forever()
