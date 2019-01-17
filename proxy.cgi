#!/usr/bin/env python3

import cgi
import cgitb
import subprocess

cgitb.enable()

def fetch_site(url):
    data = subprocess.check_output(['w3m', '-dump', url])
    return output.decode()

def format_output(url, data):
    with open('template.html', 'r') as f:
        template = f.read()

    return template.format(url, data)

def print_headers():
    print('Content-Type: text/html; charset=utf8\r\n\r\n')

def main():
    form = cgi.FieldStorage()

    url = form.getValue('u', '')
    if not url:
        print('Status: 400 Bad Request\r\n\r\n')
        print('Missing required field\r\n\r\n')
        return

    data = fetch_site(url)

    print(format_output(url, data))

if __name__ == '__main__':
    main()
