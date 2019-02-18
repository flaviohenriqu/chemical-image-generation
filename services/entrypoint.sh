#!/bin/sh

echo "API Chemical Images started"

gunicorn -b 0.0.0.0:5000 manage:app
