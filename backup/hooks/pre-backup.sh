#!/bin/sh
mkdir -p /data/db
mariadb-dump --host db -u"${MYSQL_BACKUP_USER}" -p="${MYSQL_BACKUP_USER_PASSWORD}" --databases "${MYSQL_DATABASE}" --skip_ssl > /data/db/backup.sql
mariadb-dump --host db -u"${MYSQL_BACKUP_USER}" -p="${MYSQL_BACKUP_USER_PASSWORD}" --databases "matomo" --skip_ssl > /data/db/matomosql
