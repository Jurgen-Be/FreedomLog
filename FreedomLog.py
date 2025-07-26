# PyLog module
"""
Een makkelijk te gebruiken logger module welke ook veel vrijheid geeft aan
de gebruiker.
"""

# Import modules
from loguru import logger as _base_logger
from pathlib import Path

class FreedomLog:
    def __init__(self):
        self.initialized = False

    def init(self, *, path="logs", filename="app", max_size="10 MB",
             backups=5, console=True, format_option=1):
        if self.initialized:
            return

        formats = {
            1: "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            2: "{time:YYYY-MM-DD HH:mm:ss} | {level} | [{file}:{function}:{line}] {message}",
            3: '{{"time": "{time}", "level": "{level}", "message": "{message}"}}'
        }
        log_format = formats.get(format_option, formats[1])

        Path(path).mkdir(parents=True, exist_ok=True)
        log_file = Path(path) / f"{filename}.log"

        _base_logger.remove()
        _base_logger.add(
            log_file,
            rotation=max_size,
            retention=backups,
            format=log_format,
            enqueue=True,
        )

        if console:
            _base_logger.add(lambda msg: print(msg, end=""), format=log_format)

        self.initialized = True

    def __getattr__(self, name):
        return getattr(_base_logger, name)

# Module instance
_logger_instance = FreedomLog()

# Exporteer init en logging functies als module-niveau
init = _logger_instance.init
debug = _logger_instance.debug
info = _logger_instance.info
warning = _logger_instance.warning
error = _logger_instance.error
exception = _logger_instance.exception
critical = _logger_instance.critical
success = _logger_instance.success