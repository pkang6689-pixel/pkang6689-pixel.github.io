"""No-cache dev server — every refresh serves the latest file from disk."""
import http.server

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    print("Serving on http://127.0.0.1:8081  (no-cache)")
    http.server.HTTPServer(('', 8081), NoCacheHandler).serve_forever()
