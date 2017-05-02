#!/usr/bin/env python

from BaseHTTPServer import (
    BaseHTTPRequestHandler,
    HTTPServer
)
from os.path import isfile
import argparse
import json

DEFAULT_ADDR = "127.0.0.1"
DEFAULT_PORT = 8080
DEFAULT_RESPONSES = {
    "GET":{
        "/api/hello": {
            "status": 200,
            "body": "Hello world!",
            "headers": {"Content-type": "text/plain"}
        },
        "/api/hello.html": {
            "status": 200,
            "body": "<html><body><h1>Hello World!</h1></body></html>",
            "headers": {"Content-type": "text/html"}
        },
        "/api/hello.json": {
            "status": 200,
            "body": {"message":"Hello World!"},
            "headers": {"Content-type": "application/json"}
        },
    }
}

# By default, let's use this example dictionary
RESPONSES = DEFAULT_RESPONSES

class FFFA(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, headers={}):
        self.send_response(status)

        for key in headers.keys():
            self.send_header(key, headers.get(key))

        self.end_headers()


    def _parse_request(self, path="/api/hello", method="GET"):
        endpoints = RESPONSES.get(method, None)

        if endpoints:
            data = endpoints.get(path, {})
            body = data.get('body', {})
            headers =  data.get('headers', {})
            status =  data.get('status', 200)

            self._set_headers(status, headers)
            self.wfile.write(body)
        else:
            # This method doesn't have endpoints
            self._set_headers()

        return None


    ###
    # HTTP VERBS
    #

    def do_GET(self):
        self._parse_request(self.path, 'GET')

    def do_POST(self):
        self._parse_request(self.path, 'POST')

    def do_PUT(self):
        self._parse_request(self.path, 'PUT')

    def do_DELETE(self):
        self._parse_request(self.path, 'DELETE')

    def do_HEAD(self):
        self._parse_request(self.path, 'HEAD')

    def do_OPTIONS(self):
        self._parse_request(self.path, 'OPTIONS')


def run(server_class=HTTPServer, handler_class=FFFA, addr=DEFAULT_ADDR, port=DEFAULT_PORT):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr',
                        type=str,
                        required=False,
                        default=DEFAULT_ADDR,
                        help="Serve on this address. Default: 127.0.0.1. Optional.")
    parser.add_argument('-p', '--port',
                        type=str,
                        required=False,
                        default=DEFAULT_PORT,
                        help="Serve on this port. Default: 8080. Optional.")
    parser.add_argument('-f', '--file',
                        type=str,
                        required=False,
                        help="Use responses from this file.")
    args = parser.parse_args()

    if args.file and isfile(args.file):
        RESPONSES = json.loads(u"".join(open(args.file).readlines()))
        if isinstance(RESPONSES, list):
            RESPONSES = RESPONSES.pop()

    run(addr=args.addr, port=int(args.port))
