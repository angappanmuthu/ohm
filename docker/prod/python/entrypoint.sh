#!/bin/sh

set -e

python test_project/manage.py collectstatic --noinput

echo "Runnig command '$*'"

exec $*