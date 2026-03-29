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
        # Minimal logging - only show errors
        if 'error' in format.lower() or args and 'error' in str(args).lower():
            print(f"[{self.log_date_time_string()}] {format % args}", flush=True)
    
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
        except Exception as e:
            print(f"[translate_path error] {e}", flush=True)
            return super().translate_path(path)
    
    def end_headers(self):
        try:
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Connection', 'close')
            super().end_headers()
        except Exception as e:
            print(f"[end_headers error] {e}", flush=True)
    
    def do_GET(self):
        try:
            super().do_GET()
        except Exception as e:
            print(f"[do_GET error on {self.path}] {e}", flush=True)
        finally:
            self.close_connection = True
    
    def version_string(self):
        return "Server/1.0"
    
    def handle_error(self):
        """Override to log errors instead of printing to stderr"""
        print(f"[request error] {self.client_address} - {self.path}", flush=True)
        super().handle_error()

class CleanupTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = False  # Changed to False so we can track threads
    max_connections = 0
    _connection_count = 0
    timeout = 1  # 1-second timeout for handle_request()
    
    def __init__(self, *args, **kwargs):
        socketserver.TCPServer.__init__(self, *args, **kwargs)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def handle_timeout(self):
        """Handle socket timeout gracefully"""
        pass
    
    def server_bind(self):
        """Override to handle bind errors"""
        try:
            super().server_bind()
        except Exception as e:
            print(f"[BIND ERROR] {e}", flush=True)
            raise
    
    def process_request_thread(self, request, client_address):
        """Override to track active connections"""
        CleanupTCPServer._connection_count += 1
        try:
            super().process_request_thread(request, client_address)
        finally:
            CleanupTCPServer._connection_count -= 1

def monitor_resources():
    """Monitor and clean up resources periodically"""
    while True:
        try:
            time.sleep(10)
            gc.collect()
            active_threads = threading.active_count()
            print(f"[MONITOR] Active threads: {active_threads}, Connections: {CleanupTCPServer._connection_count}", flush=True)
            
            # If too many threads, this is a problem
            if active_threads > 50:
                print(f"[WARNING] Excessive threads detected: {active_threads}", flush=True)
        except Exception as e:
            print(f"[MONITOR ERROR] {e}", flush=True)

try:
    server = CleanupTCPServer(("127.0.0.1", PORT), CleanupHTTPRequestHandler)
    print(f"Server running: http://localhost:{PORT}/", flush=True)
    
    # Start resource monitor thread
    monitor_thread = threading.Thread(target=monitor_resources, daemon=True)
    monitor_thread.start()
    
    # Use serve_forever with timeout handling
    server.timeout = 1  # Set timeout for server.handle_request()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...", flush=True)
except KeyboardInterrupt:
    print("Stopped", flush=True)
except Exception as e:
    print(f"[STARTUP ERROR] {e}", flush=True)
finally:
    try:
        server.server_close()
        print("Server closed", flush=True)
    except:
        pass
