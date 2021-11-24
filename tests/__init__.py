import unittest

from . import test_timer

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(test_timer))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)
