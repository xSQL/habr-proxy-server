"""Habr proxy server"""

import http.server
import requests

from settings import PORT, SITES
from utils import HabrParser


class HabrProxy(http.server.SimpleHTTPRequestHandler):
    """Habr.com proxy server class"""

    def do_GET(self):
        """Main proxy logic"""

        params = self.path.split('/')
        site = SITES.get(params[1])
        path_params = '/'.join(params[2:])

        if not site:
            site = SITES.get('')
            path_params = '/'.join(params[1:])

        if site.get('origin'):
            site_url = SITES.get(site.get('origin')).get('url')
        else:
            site_url = site.get('url')

        request_url = '{0}/{1}'.format(site_url, path_params)
        response = requests.get(request_url)
        content_type = response.headers.get('Content-Type', 'text/html')
        content = response.content

        if content_type.split(';')[0]=='text/html':
            content = HabrParser.process_html(content)

        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content)
        return


try:
    print('Starting server!')
    httpd = http.server.HTTPServer(("", PORT), HabrProxy)
    httpd.serve_forever()
except:
    print('Stopping server!')
    httpd.shutdown()
