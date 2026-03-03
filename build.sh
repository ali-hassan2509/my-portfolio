#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Manually create the static directory to prevent errors
mkdir -p static
mkdir -p staticfiles

# Convert static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
python manage.py createsuperuser --no-input || true
