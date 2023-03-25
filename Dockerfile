FROM python:3.6.12-alpine AS base

ENV APP_HOME=/app
WORKDIR $APP_HOME

RUN mkdir logs static media

# Setup cron
COPY cronjobs $APP_HOME/
RUN cat cronjobs >> /etc/crontabs/root && \
    crond -b

# Install system dependencies
RUN apk add --no-cache mysql-client mariadb-connector-c-dev libjpeg

#-------------------------------------------------------------------------------
FROM base AS requirement-compiler-common

RUN pip install pip==20.0.2 && \
    apk add mariadb-dev git gcc python3-dev musl-dev jpeg-dev zlib-dev

COPY requirements/common.txt requirements/common.txt

RUN  pip install --user --src $APP_HOME/req-src --requirement requirements/common.txt

#-------------------------------------------------------------------------------
FROM requirement-compiler-common AS requirement-compiler-dev

COPY requirements/dev.txt requirements/dev.txt

RUN  pip install --user --src $APP_HOME/req-src --requirement requirements/dev.txt

#--------------------------------------------------------------------------------
FROM base AS development

RUN apk add runit shadow && \
    addgroup gamerauntsia && \
    adduser -D -h /home/gamerauntsia -s /bin/sh -G gamerauntsia gamerauntsia && \
    chown -R gamerauntsia:gamerauntsia /app

COPY docker/run-as-user.sh /usr/local/bin/run-as-user.sh
COPY start-web.sh /usr/local/bin/start-web.sh

COPY --from=requirement-compiler-dev --chown=gamerauntsia:gamerauntsia /root/.local /home/gamerauntsia/.local
COPY --from=requirement-compiler-dev --chown=gamerauntsia:gamerauntsia $APP_HOME/req-src $APP_HOME/req-src

ENTRYPOINT ["run-as-user.sh"]
WORKDIR $APP_HOME/code
CMD start-web.sh \
    python manage.py runserver 0.0.0.0:8000

#--------------------------------------------------------------------------------
FROM base AS production

COPY start-web.sh /usr/local/bin/start-web.sh

COPY --from=requirement-compiler-common /root/.local /root/.local
COPY --from=requirement-compiler-common $APP_HOME/req-src $APP_HOME/req-src

COPY . $APP_HOME/code/

WORKDIR $APP_HOME/code
CMD start-web.sh \
    gunicorn gamerauntsia.wsgi:application --bind 0.0.0.0:8000 --workers=4
