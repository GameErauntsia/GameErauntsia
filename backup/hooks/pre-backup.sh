#!/bin/sh
mkdir -p /data/db
mysqldump --host db -u"${MYSQL_BACKUP_USER}" -p"${MYSQL_BACKUP_USER_PASSWORD}" --databases "${MYSQL_DATABASE}" > /data/db/backup.sql
