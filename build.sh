# exit on error
set -o errexit

pip install -r requirements.txt

# Clean old static files and create fresh directories
rm -rf staticfiles
mkdir -p static
mkdir -p staticfiles

python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser (as discussed before)
python manage.py createsuperuser --no-input || true
