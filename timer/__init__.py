import time
from functools import wraps
from typing import Any, Callable, Optional

from timer.utils.logger import CustomLogger
from timer.utils.helpers import format_time

logger = CustomLogger(__name__)

level = "info"


def timer(
    file_log: Optional[bool] = False, exp_time: Optional[float] = None
) -> Callable[[Any], None]:
    def decorator(func) -> Callable[[Any], None]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            finish_time = time.time()

            used_time = finish_time - start_time

            if exp_time is not None and exp_time <= used_time:
                global level
                level = "warning"

            logger.log(
                level=level,
                msg="{} function ran in {}".format(
                    func.__name__, format_time(used_time)
                ),
                file_log=file_log,
            )

            return result

        return wrapper

    return decorator
