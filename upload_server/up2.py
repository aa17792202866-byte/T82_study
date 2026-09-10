import http.server
import socketserver
import cgi

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']}
        )
        if 'file' in form:
            file_item = form['file']
            with open(file_item.filename, 'wb') as f:
                f.write(file_item.file.read())
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"File '{file_item.filename}' uploaded successfully!".encode())
        else:
            self.send_response(400)
            self.end_headers()

    def do_GET(self):
        super().do_GET()

if __name__ == '__main__':
    with socketserver.TCPServer(("", 8000), UploadHandler) as httpd:
        print("Serving at http://0.0.0.0:8000")
        httpd.serve_forever()