#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly cmd="$*"

# Create Database migrations
echo "Create database migration files"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Apply translation compilation
echo "Apply translation compilation"
python manage.py compilemessages --ignore site-packages

exec $cmd