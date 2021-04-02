#!/bin/sh

trap 'exit 0' SIGTERM
uvicorn asgi:app --reload --host=0.0.0.0 --port=8000
