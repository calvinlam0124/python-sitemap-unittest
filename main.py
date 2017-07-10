import unittest
from SiteHttpTest import SiteHttpTest

suite = unittest.TestLoader().loadTestsFromTestCase(SiteHttpTest)
unittest.TextTestRunner(verbosity=2).run(suite)
