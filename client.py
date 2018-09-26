#!/usr/bin/env python3

import http.client, urllib.parse
import json
import time


def run():
    i=0
    while(1):
        i+=1
        post_head = {"Total": 1, "SEQUENCE": i}
        post_body = {"Function": 64, "PAID": 12345678, "VER": 12, "XD2": 3, "XD1": 2, "PANID": 12045, "BACK2": 0, "BACK3": 0, "BACK1": 0}
        post_data = [post_head, post_body]
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("localhost:8000")
        conn.request("POST", "", json.dumps(post_data), headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        print(response.read().decode())

        data = response.read()

        conn.close()
        time.sleep(5)

if __name__ == '__main__':
    run()
