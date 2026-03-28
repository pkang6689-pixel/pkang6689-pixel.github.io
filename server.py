#!/usr/bin/env python3
import http.server
import socketserver
import sys
import os
import traceback
import threading
import urllib.parse
import signal
import time
import socket

PORT = 8082
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    timeout = 10  # Reduced timeout for quicker disconnects
    
    def log_message(self, format, *args):
        try:
            print(f"[{self.log_date_time_string()}] {format % args}", flush=True)
        except:
            pass
    
    def translate_path(self, path):
        try:
            path = urllib.parse.unquote(path)
            return super().translate_path(path)
        except Exception as e:
            print(f"Path error: {e}", flush=True)
            return super().translate_path(path)
    
    def end_headers(self):
        try:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Connection', 'close')  # Force connection close
            super().end_headers()
        except Exception as e:
            print(f"Headers error: {e}", flush=True)
    
    def do_GET(self):
        try:
            super().do_GET()
        except (ConnectionResetError, BrokenPipeError):
            pass
        except Exception as e:
            try:
                self.send_error(500)
            except:
                pass
    
    def version_string(self):
        return "Server/1.0"

class ResilientTCPServer(socketserver.ThreadingTCPServer):
    daemon_threads = False
    allow_reuse_address = True
    
    def __init__(self, *args, **kwargs):
        socketserver.TCPServer.__init__(self, *args, **kwargs)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def run_server():
    try:
        with ResilientTCPServer(("127.0.0.1", PORT), MyHTTPRequestHandler) as httpd:
            print(f"✓ Server ready at http://localhost:{PORT}/", flush=True)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped", flush=True)
        sys.exit(0)
    except Exception as e:
        print(f"✗ Error: {e}", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    run_server()
