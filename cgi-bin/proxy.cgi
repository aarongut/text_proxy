#!/usr/bin/env python3

import cgi
import cgitb
import subprocess

from goose3 import Goose

cgitb.enable()

goose = Goose({'enable_image_fetching': True})

def fetch_site(url):
    return goose.extract(url=url)

def format_output(article):
    with open('template.html', 'r') as f:
        template = f.read()

    extra = ""
    if article.top_image:
        extra += """<img src="{}" />""".format(article.top_image.src)

    return template.format(
        title=article.title,
        body=article.cleaned_text,
        extra=extra)

def print_headers():
    print('Content-Type: text/html; charset=utf8\r\n\r\n')

def main():
    form = cgi.FieldStorage()

    url = form.getvalue('u', '')
    if not url:
        print('Status: 400 Bad Request\r\n\r\n')
        print('Missing required field\r\n\r\n')
        return

    data = fetch_site(url)

    print_headers()
    print(format_output(data))

if __name__ == '__main__':
    main()
