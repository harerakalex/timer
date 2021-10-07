import logging


class CustomLogger:
    def __init__(self, name: str):
        self.name = name

    def log(self, level: str = "warning"):
        # create logger
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        # 'application' code
        if level == "debug":
            print("======", type(logger))
            logger["debug"]("debug message")
        if level == "info":
            logger.info("info message")
        if level == "warning":
            logger.warning("warn message")
        if level == "error":
            logger.error("error message")
        if level == "critiacal":
            logger.critical("critical message")
