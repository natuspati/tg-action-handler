FROM python:3.12

WORKDIR /app

COPY pyproject.toml pyproject.lock* /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --no-interaction

COPY src/ /app/

COPY .env /app/

CMD ["poetry", "run", "python", "main.py"]
