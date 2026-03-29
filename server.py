#!/usr/bin/env python3
import http.server
import socketserver
import sys
import os
import urllib.parse
import socket
import threading
import time
import gc

PORT = 8082
MAX_CONNECTIONS = 100
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CleanupHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    timeout = 5
    
    def log_message(self, format, *args):
        pass  # Silent logging to reduce output
    
    def translate_path(self, path):
        try:
            path = urllib.parse.unquote(path)
            
            # Handle absolute path redirects for the dev server
            # Map framework paths to root-level files
            if path.startswith('/search_data.js'):
                path = '/search_data.js'
            elif path.startswith('/search_logic.js'):
                path = '/search_logic.js'
            elif path.startswith('/_sdk/'):
                path = path  # Keep as is - points to root _sdk folder
            # Map /styles/* to ArisEdu Project Folder/styles/*
            elif path.startswith('/styles/'):
                path = '/ArisEdu Project Folder' + path
            # Map /scripts/* to ArisEdu Project Folder/scripts/* if it's not already
            elif path.startswith('/scripts/') and not path.startswith('/ArisEdu Project Folder/scripts/'):
                path = '/ArisEdu Project Folder' + path
            # /content_data/* stays as root-level
            # /translations/* stays as root-level
            # /ArisEdu Project Folder/* stays as is
            
            return super().translate_path(path)
        except:
            return super().translate_path(path)
    
    def end_headers(self):
        try:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Connection', 'close')
            super().end_headers()
        except:
            pass
    
    def do_GET(self):
        try:
            super().do_GET()
        except:
            pass
        finally:
            self.close_connection = True
    
    def version_string(self):
        return "Server/1.0"

class CleanupTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    max_connections = 0
    
    def __init__(self, *args, **kwargs):
        socketserver.TCPServer.__init__(self, *args, **kwargs)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def monitor_resources():
    """Monitor and clean up resources periodically"""
    while True:
        try:
            time.sleep(30)
            gc.collect()  # Force garbage collection
        except:
            pass

try:
    server = CleanupTCPServer(("127.0.0.1", PORT), CleanupHTTPRequestHandler)
    print(f"Server running: http://localhost:{PORT}/", flush=True)
    
    # Start resource monitor thread
    monitor_thread = threading.Thread(target=monitor_resources, daemon=True)
    monitor_thread.start()
    
    server.serve_forever()
except KeyboardInterrupt:
    print("Stopped", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
