from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import time
from termcolor import colored

PORT = 3000

# TIMEOUT = int(os.getenv('HTTP_SERVER_TIMEOUT', '30'))


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._log_request()

    def do_POST(self):
        self._log_request()

    def do_PUT(self):
        self._log_request()

    def do_DELETE(self):
        self._log_request()

    def _log_request(self):
        start_time = time.time()
        content_length = int(self.headers.get('Content-Length', '0'))
        body = self.rfile.read(content_length)
        logging.info('Request Method: %s', self.command)
        logging.info('Request Path: %s', colored(self.path, 'yellow'))
        logging.info('Request Headers: %s', self.headers)
        logging.info('Request Body: %s', body.decode('utf-8'))
        timeout = int(os.environ.get('HTTP_SERVER_TIMEOUT', '30'))
        time.sleep(timeout)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

        # Log the response and time duration
        end_time = time.time()
        duration = end_time - start_time
        logging.info('Time duration: %.2f seconds', duration)
        print("-----------------------------------\n\n\n")

logging.basicConfig(level=logging.INFO)
server = HTTPServer(('0.0.0.0', PORT), RequestHandler)
logging.info('Server listening on port %s', PORT)
server.serve_forever()

