import unittest
from SiteHttpTest import SiteHttpTest

suite = unittest.TestLoader().loadTestsFromTestCase(SiteHttpTest)
unittest.TextTestRunner(verbosity=2).run(suite)


# import xml.etree.ElementTree as ET
# tree = ET.parse('sitemap.xml')
# root = tree.getroot()
# for item in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
#     names = item.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
#     for name in names:
#         print(name.text)
#
# print("end")

# import xml.etree.ElementTree as ET
# f = open("sitemap.xml")
# content = f.read()
# root = ET.fromstring(content)
# urls = root.findall("//loc")
