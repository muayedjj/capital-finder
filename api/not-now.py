from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        cap = ''
        if 'word' in dic:
            word = dic['word']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + word)
            data = r.json()
            for word_data in data:
                definition = word_data[0]['name']['common']
                cap += definition

            message = str(cap)

        else:
            message = "Please provide me with a country or a capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
