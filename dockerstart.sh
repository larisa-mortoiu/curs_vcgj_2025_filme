#!/bin/sh

. .venv/bin/activate

exec flask run --host=0.0.0.0 --port=5011

