import sys
import requests

class SiteHttp:
    def http_get(url):
        r = requests.get(url)
        return r
