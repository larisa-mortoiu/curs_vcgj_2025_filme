#!/usr/bin/env sh
if [ $# -gt 0 ]; then
  exec "$@"
else
  exec flask run
fi
