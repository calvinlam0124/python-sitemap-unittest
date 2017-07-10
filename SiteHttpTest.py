import unittest
import xml.etree.ElementTree as ET
from SiteHttp import SiteHttp

class SiteHttpTest(unittest.TestCase):
    def test_http_get(self):
        tree = ET.parse('sitemap.xml')
        root = tree.getroot()

        urls = []
        for item in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            names = item.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            for name in names:
                urls.append(name.text)


        for url in urls:
            # print(url)
            requests = SiteHttp.http_get(url)
            # print(requests.status_code)
            self.assertEqual(200, requests.status_code)
