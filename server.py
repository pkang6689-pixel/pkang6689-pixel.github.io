#!/usr/bin/env python3
import http.server
import socketserver
import sys
import os
import traceback
import threading
import urllib.parse

PORT = 8082
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    timeout = 30  # Increase timeout
    
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}", flush=True)
    
    def translate_path(self, path):
        # Properly decode URL-encoded paths (e.g., %20 for spaces)
        path = urllib.parse.unquote(path)
        return super().translate_path(path)
    
    def end_headers(self):
        try:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Connection', 'keep-alive')
            super().end_headers()
        except Exception as e:
            print(f"Error sending headers: {e}", flush=True)
    
    def do_GET(self):
        try:
            super().do_GET()
        except ConnectionResetError:
            print("Client disconnected", flush=True)
        except BrokenPipeError:
            print("Broken pipe", flush=True)
        except Exception as e:
            print(f"Error handling GET: {type(e).__name__}: {e}", flush=True)
    
    def version_string(self):
        return "Server/1.0"

class ThreadedTCPServer(socketserver.ThreadingTCPServer):
    daemon_threads = False  # Changed to keep threads alive
    allow_reuse_address = True
    
    def handle_error(self, request, client_address):
        print(f"Server error: {sys.exc_info()[0].__name__}", flush=True)

try:
    httpd = ThreadedTCPServer(("", PORT), MyHTTPRequestHandler)
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Serving from: {os.getcwd()}")
    print("Using threaded server with keep-alive", flush=True)
    print("Press Ctrl+C to stop", flush=True)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped", flush=True)
    sys.exit(0)
except Exception as e:
    print(f"Fatal error: {e}", file=sys.stderr, flush=True)
    traceback.print_exc()
    sys.exit(1)
