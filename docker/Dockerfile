FROM python:3.8.1-alpine as base

# set work directory
WORKDIR /usr/src/app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
  POETRY_VERSION=1.1.5

FROM base as builder 

RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev

# install poetry
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

# install dependencies
COPY poetry.lock pyproject.toml ./
COPY todo_app                   ./todo_app
RUN . /venv/bin/activate && poetry install --no-root --no-dev
RUN . /venv/bin/activate && poetry build 

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app/dist .
COPY docker/entrypoint.sh ./entrypoint.sh
COPY asgi.py              ./asgi.py

ENV PATH="/venv/bin:${PATH}"
RUN . /venv/bin/activate && pip install *.whl

ENTRYPOINT "./entrypoint.sh"
