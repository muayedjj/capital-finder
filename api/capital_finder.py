from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'capital' in dic:

            capital = dic['capital']
            url = 'https://restcountries.com/v2/capital/'
            res = requests.get(url + capital)

            data = res.json()
            cap = str(data[0]["capital"]).capitalize()
            country = str(data[0]["name"]).capitalize()
            message = '{} is the capital city of {}'.format(cap, country)

            # r = requests.get(url + word)
            # data = r.json()
            # cap = data["name"]["common"]
            # cou = data['capital'][0]
            # message = '{} is the capital city of {}'.format(cap, cou)

        elif 'country' in dic:
            country = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            res = requests.get(url + country)

            data = res.json()[0]
            cou = str(data["name"]["common"]).capitalize()
            cap = str(data['capital'][0]).capitalize()
            message = f"The capital of {cou} is {cap}"
        else:
            message = "Please provide a country or a capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return


response = requests.get('https://restcountries.com/v3.1/capital/amman')
print(f'Response status code: {response.status_code}')
print(f'Response header: {response.headers}')
print(f'Response body : {json.dumps(response.json(), indent=4)}')
"""
body[0]["name"]["common"]
body[0]["capital"][0]
"""
