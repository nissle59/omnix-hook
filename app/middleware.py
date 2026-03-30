import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Отключаем стандартный access log
logging.getLogger("uvicorn.access").disabled = True


class CustomAccessLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Логируем только не-health запросы или в DEBUG режиме
        if request.url.path != "/health" or logging.getLogger().level <= logging.DEBUG:
            if response.status_code != 200:
                logging.info(
                    f'{request.client.host if request.client else "-"} - '
                    f'"{request.method} {request.url.path} HTTP/{request.scope.get("http_version", "1.1")}" '
                    f'{response.status_code}'
                )

        return response