#!/bin/bash
set -e
export PYTHONPATH=/app
echo "Migrando banco de dados"
poetry run alembic upgrade head

echo "Iniciando seeder"
poetry run python -m backend.seeder 

echo "Iniciando aplicação"
exec poetry run uvicorn --host 0.0.0.0 --port 8000 backend.app:app