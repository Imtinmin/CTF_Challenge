#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/1/2019 2:58 PM
# @Author  : fz
# @Site    : 
# @File    : agent.py
# @Software: PyCharm

import json
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from subprocess import Popen, PIPE


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print("request_path :", request_path)
        print("self.headers :", self.headers)
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()

        result = self._func()
        self.wfile.write(json.dumps(result))


    def do_POST(self):
        request_path = self.path

        # print("\n----- Request Start ----->\n")
        print("request_path : %s", request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        # print("length :", length)

        print("request_headers : %s" % request_headers)
        print("content : %s" % self.rfile.read(length))
        # print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        result = self._func()
        self.wfile.write(json.dumps(result))

    def _func(self):
        netstat = Popen(['netstat', '-tlnp'], stdout=PIPE)
        netstat.wait()

        ps_list = netstat.stdout.readlines()
        result = []
        for item in ps_list[2:]:
            tmp = item.split()
            Local_Address = tmp[3]
            Process_name = tmp[6]
            tmp_dic = {'local_address': Local_Address, 'Process_name': Process_name}
            result.append(tmp_dic)
        return result
        # return 'mysqld'
    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8123
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = (
        "Creates an http-server that will echo out any GET or POST parameters, and respond with dummy data\n"
        "Run:\n\n")
    (options, args) = parser.parse_args()

    main()