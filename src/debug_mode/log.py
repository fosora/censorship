import logging
import string
import sys

class AppLogger:
    def __init__(self, name="app", log_file="app.log", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        # Handler para arquivo
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        # Handler para console
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)

    def debug(self, message):
        self.logger.debug(message)
    def warning(self, message):
        self.logger.warning(message)
    def info(self, message):
        self.logger.info(message)
    def error(self, message):
        self.logger.error(message)

    def progress_percent(self, action: string, current: int, total: int, bar_length: int = 30):
        percent = current / total
        filled_length = int(bar_length * percent)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        self.logger.info(f"{action}: |{bar}| {percent*100:.0f}%")
    def progress_fraction(self, action: string, current: int, total: int):
        self.logger.info(f"{action}: {current}/{total}")
