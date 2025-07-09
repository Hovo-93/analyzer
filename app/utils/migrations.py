import os
import subprocess

from app.core.settings import logger


def run_migrations():
    try:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        alembic_cfg_path = os.path.join(current_dir, "../..",  "alembic.ini")

        if not os.path.isfile(alembic_cfg_path):
            raise FileNotFoundError(f"alembic.ini not found at: {alembic_cfg_path}")

        logger.info(f"🧭 Используем alembic.ini: {alembic_cfg_path}")

        # Запускаем Alembic
        result = subprocess.run(
            ["alembic", "-c", alembic_cfg_path, "upgrade", "head"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(alembic_cfg_path),
            env={**os.environ}

        )

        if result.returncode != 0:
            logger.error(f"Alembic upgrade failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
            raise RuntimeError("Alembic migration failed")

        logger.info("✅ Alembic миграции успешно применены")
    except Exception as e:
        logger.error(f"❌ Ошибка при миграции: {e}")
        raise
