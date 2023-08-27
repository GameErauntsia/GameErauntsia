#!/bin/bash

set -eu -o pipefail
mysql -uroot -p${MYSQL_ROOT_PASSWORD} <<EOF
GRANT ALL ON test_gamerauntsia.* TO ${MYSQL_USER}@'%';
EOF
