FROM python:3.10-slim

# Install Poetry
ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Prepare project subfolder
RUN mkdir /app
WORKDIR /app

# Add Dependencies
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-interaction --no-root

# Add remainder of Project
COPY . .
RUN poetry install --no-interaction

ENTRYPOINT ["poetry", "run", "navigator-notify"]
