FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

COPY insurance_api ./insurance_api

EXPOSE 10000

CMD ["uvicorn", "insurance_api.app.main:app", "--host", "0.0.0.0", "--port", "10000"]