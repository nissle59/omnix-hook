from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.logging_config import setup_logging
from app.middleware import CustomAccessLogMiddleware
from app.routers import webhook

setup_logging(level="INFO")  # INFO / WARNING / ERROR


# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator:
#     # запускаем задачу в фоне при старте приложения
#     task = asyncio.create_task(sync_devices_with_subscriptions())
#     yield
#     # корректно завершаем при остановке
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Фоновая задача остановлена")


app = FastAPI(title="OmniX Side App API") #, lifespan=lifespan)

app.add_middleware(CustomAccessLogMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook.router, prefix="/auth", tags=["webhook"])


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
