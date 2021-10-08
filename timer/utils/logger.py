import logging


class CustomLogger:
    default_level = logging.DEBUG

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Logging in: {}".format(self.name)

    def create_console_handler(self):
        ch = logging.StreamHandler()
        ch.setLevel(self.default_level)

        formatter = self.create_formatter()
        ch.setFormatter(formatter)

        return ch

    def create_file_handler(self):
        fh = logging.FileHandler(filename="{}.log".format(self.name))
        fh.setLevel(self.default_level)

        formatter = self.create_formatter()
        fh.setFormatter(formatter)

        return fh

    def create_formatter(self):
        return logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m-%d-%Y %I:%M:%S %p",
        )

    def log(self, level: str = "warning", msg: str = "", file_log: bool = False):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.default_level)

        ch = self.create_console_handler()

        logger.addHandler(ch)

        if file_log:
            fh = self.create_file_handler()
            logger.addHandler(fh)

        return getattr(logger, level)(msg)
