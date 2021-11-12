from unittest import TestCase
from timer import __version__, timer
from timer.utils.helpers import format_time
from timer.utils.logger import CustomLogger


class TestTimerVersion(TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")


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
        res = format(1)

        self.assertEqual(res, "1")


class TestLogger(TestCase):
    def test_project_str(self) -> None:
        logger = CustomLogger(__name__)
        self.assertEqual(str(logger), "Logging in: {}".format(__name__))
