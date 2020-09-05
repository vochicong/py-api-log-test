FROM tiangolo/uvicorn-gunicorn-fastapi
RUN python --version

COPY scripts/install-poetry.sh ./
RUN bash ./install-poetry.sh

COPY ./app/pyproject.toml* ./app/poetry.lock* /app/
RUN poetry install --no-root --no-dev

COPY ./app /app

# ENV APP_MODULE="main:app"
ENV TZ Asia/Tokyo
