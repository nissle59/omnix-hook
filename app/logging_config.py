import logging
import sys

from app.config import settings


class HealthCheckFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        # Пропускаем все логи в DEBUG режиме
        if record.levelno <= logging.DEBUG:
            return True

        # Фильтруем запросы к /health в не-DEBUG режиме
        message = getattr(record, 'message', '') or ''
        if '/health' in message:
            return False
        return True

def setup_logging(level=logging.INFO):
    """
    Единая настройка логирования для всего бота.
    По умолчанию INFO, но можно поднять/опустить уровень.
    """
    if settings.DEBUG:
        level = logging.DEBUG
    # формат логов
    log_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # --- Глушим болтливые библиотеки ---
    logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.dialects").setLevel(logging.ERROR)

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)


# удобный alias
logger = logging.getLogger("backend")
