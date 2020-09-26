#!/bin/sh
#Wait for mysql to be ready
echo "Waiting for mysql to be ready"
while ! mysqladmin ping -h db --silent; do
    sleep 5
    echo "Retrying mysql connection"
done

# Run migrations and collect static files
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Run command specified when running the container
echo "Run: $@"
exec "$@"
