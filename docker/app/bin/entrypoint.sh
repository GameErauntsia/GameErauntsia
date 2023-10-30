#!/bin/sh

# Run migrations and collect static files
python bin/manage.py collectstatic --noinput
python bin/manage.py migrate --noinput


# # Run command specified when running the container
echo "Run: $@"
exec "$@"
