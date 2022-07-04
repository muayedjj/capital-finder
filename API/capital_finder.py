from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def do_get(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        cap = ''
        if 'capital' in dic:
            capital = dic['capital']
            url = f'https://restcountries.com/v3.1/capital/{capital}'
            req = requests.get(url)
            data = req.json()
            for capital_data in data:
                definition = capital_data['meanings'][0]['cap'][0]['definition']
                cap.append(definition)

            message = str(cap)

        else:
            message = "Please provide me with a word"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
