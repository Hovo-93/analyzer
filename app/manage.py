import logging
import os
import sys
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from app.apps.router import router
from app.utils.migrations import run_migrations

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Запуск приложения...")

    try:
        logging.info("Запуск Alembic миграций...")
        run_migrations()
        yield
    except Exception as e:
        logging.error(f"Ошибка при запуске приложения: {e}")
        raise
    finally:
        logging.info("Завершение работы приложения.")


def init():
    app = FastAPI(
        title="Review",
        version="1.0.0",
        lifespan=lifespan,
    )
    app.include_router(prefix="/v1", router=router)

    logging.info("Запуск FastAPI сервера...")
    return app



if __name__ == "__main__":
    app = init()
    uvicorn.run(app, host='0.0.0.0', port=38046)


app = init()
