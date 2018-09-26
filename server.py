#!/usr/bin/env python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import fcntl

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        resp_head = {"Next": 0, "SEQUENCE": 0}
        resp_body = {"Status": 0, "INDEX": 0}
        resp_obj = []
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data)
        post_obj = json.loads(post_data)
        fd = open("task_table", "r+")
        # if fcntl.flock(fd.fileno(), fcntl.LOCK_NB | fcntl.LOCK_EX) != IOError:
        if True:
            read_len = 0
            task = fd.readline()
            read_len = len(task)
            print(task)
            # find task
            find_task = False
            fd.readline()
            #lines = fd.readlines()
            while(1):
                line = fd.readline()
                if line == "":
                    break;
                if line.strip() == task.strip():
                    print("find task")
                    find_task = True
                    break;
            if find_task == True:
                json_str = ""
                while(1):
                    line = fd.readline()
                    if line == "":
                        break;
                    json_line = line.strip()
                    if json_line != "":
                        json_str += json_line
                    else:
                        break;
                print(json_str)
                resp_obj = json.loads(str.encode(json_str))
                resp_obj[0]['SEQUENCE'] = post_obj[0]['SEQUENCE']
        else:
            resp_head['SEQUENCE'] = post_obj[0]['SEQUENCE']
            resp_obj = [resp_head, resp_body]
        fd.close()
        resp = str.encode(json.dumps(resp_obj));

        self._set_response()
        self.wfile.write(resp)

def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
