from unittest import TestCase

from timer import timer
from timer.logger import CustomLogger
from timer.utils import format_time
from timer.version import __version__

version = "0.1.0"


class TestTimerVersion(TestCase):
    def test_version(self):
        self.assertEqual(__version__, version)


class TestTimer(TestCase):
    def setUp(self):
        @timer(file_log=True, exp_time=0)
        def func(x):
            return x

        self.decorated = func

    def test_timer(self):
        self.assertEqual(self.decorated(1), 1)


class TestTimeHelper(TestCase):
    def test_munite(self):
        res = format_time(120)

        self.assertEqual(res, "2 min and 0 secs")

    def test_seconds(self):
        res = format_time(1)

        self.assertEqual(res, "1.00 secs")


class TestLogger(TestCase):
    def test_project_str(self) -> None:
        logger = CustomLogger(__name__)
        self.assertEqual(str(logger), "Logging in: {}".format(__name__))
