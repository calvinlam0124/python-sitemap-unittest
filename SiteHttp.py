import sys
import requests

class SiteHttp:
    def http_get(url):
        r = requests.get(url)
        return r

    def http_post(url):
        sys.exit()
        # TODO: function holder
        # data = {}
        # data['name'] = 'name'
        # data['phone'] = 'phone'
        #
        # files = {'file[1]': open('Media/jpg.jpg', 'rb'), 'file[0]': open('Media/pdf.pdf', 'rb')}
        #
        # r = requests.post(url, data=data, files=files)
        # return r
