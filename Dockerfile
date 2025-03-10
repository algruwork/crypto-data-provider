FROM python:3.11.2-alpine

EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without test

ENTRYPOINT ["poetry", "run", "uvicorn", "crypto_data_provider.main:app", "--host", "0.0.0.0", "--port", "8000"] #CMD