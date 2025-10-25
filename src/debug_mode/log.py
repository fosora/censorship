import logging
import string
import sys
import time

class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG":    "\033[90m", 
        "INFO":     "\033[97m",
        "WARNING":  "\033[93m",
        "ERROR":    "\033[91m",
        "CRITICAL": "\033[31m"
    }
    RESET = "\033[0m"

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{log_color}{message}{self.RESET}"

class AppLogger:
    def __init__(
            self, 
            name="app", 
            log_path="./logs",
            log_file=f"app_{time.time()}.log", 
            level=logging.INFO
        ):
        mkdirs = __import__('os').makedirs
        mkdirs(log_path, exist_ok=True)
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        file_handler = logging.FileHandler(f"{log_path}/{log_file}")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        color_formatter = ColorFormatter("%(asctime)s [%(levelname)s] %(message)s")
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(color_formatter)
        self.logger.addHandler(stream_handler)

    def debug(self, message):
        self.logger.debug(message)
    def warning(self, message):
        self.logger.warning(message)
    def info(self, message):
        self.logger.info(message)
    def error(self, message):
        self.logger.error(message)
    def critical(self, message): 
        self.logger.critical(message)

    def progress_percent(self, action: string, current: int, total: int, bar_length: int = 30):
        percent = current / total
        filled_length = int(bar_length * percent)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        self.logger.info(f"{action}: |{bar}| {percent*100:.0f}%")
    def progress_fraction(self, action: string, current: int, total: int):
        self.logger.info(f"{action}: {current}/{total}")
