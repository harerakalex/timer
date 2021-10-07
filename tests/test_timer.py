import unittest

from timer import __version__


class TestTimerVersion(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
