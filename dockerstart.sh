#!/usr/bin/env sh
# if args provided, run them (e.g. pytest); otherwise launch Flask
if [ $# -gt 0 ]; then
  exec "$@"
else
  exec flask run
fi

