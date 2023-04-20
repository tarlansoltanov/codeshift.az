#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly cmd="$*"

# Cretate env file if not exists
if [ ! -f ./config/.env ]; then
    echo "Create .env file"
    cp ./config/.env.template ./config/.env
fi

# Create Database migrations
echo "Create database migration files"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

exec $cmd