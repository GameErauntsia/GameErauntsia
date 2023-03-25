#!/bin/sh

set -eu

NEW_UID=$(stat -c '%u' /app)
NEW_GID=$(stat -c '%g' /app)

groupmod -g "$NEW_GID" -o gamerauntsia >/dev/null 2>&1
usermod -u "$NEW_UID" -o gamerauntsia >/dev/null 2>&1

exec chpst -u gamerauntsia:gamerauntsia -U gamerauntsia:gamerauntsia env HOME="/home/gamerauntsia" "$@"
