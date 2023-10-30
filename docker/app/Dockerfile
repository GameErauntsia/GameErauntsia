FROM python:3.10.10-alpine as base

# # This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# # This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

ENV APP_HOME=/app

WORKDIR $APP_HOME
RUN mkdir src bin logs
RUN touch ./logs/event.log
COPY ./docker/app/requirements/ $APP_HOME/requirements
COPY ./docker/app/bin $APP_HOME/bin
COPY ./src $APP_HOME/src
# Setup cron
RUN cat ./bin/cronjobs >> /etc/crontabs/root && \
    crond -b

RUN apk update
# mysqlclient instalazioan errorea kentzeko (alpine irudia bada)
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache mariadb-dev
RUN apk add git
RUN apk add --no-cache jpeg-dev
RUN apk add --no-cache libjpeg-turbo-dev
RUN python -m pip install --upgrade pip

# RUN pip install --editable $APP_HOME/src/django-forum-app

#-------------------------------------------------------------------------------
FROM base AS requirement-compiler-common

RUN pip install pip==20.0.2 && \
    apk add mariadb-dev git gcc python3-dev musl-dev jpeg-dev zlib-dev

COPY ./docker/app/requirements/common.txt requirements/common.txt

RUN  pip install --user --src $APP_HOME/req-src --requirement requirements/common.txt

#-------------------------------------------------------------------------------
FROM requirement-compiler-common AS requirement-compiler-dev

COPY ./docker/app/requirements/dev.txt requirements/dev.txt

RUN  pip install --user --src $APP_HOME/req-src --requirement requirements/dev.txt

#--------------------------------------------------------------------------------
FROM base AS development

RUN apk add runit shadow && \
    addgroup gamerauntsia && \
    adduser -D -h /home/gamerauntsia -s /bin/sh -G gamerauntsia gamerauntsia && \
    chown -R gamerauntsia:gamerauntsia /app

COPY docker/run-as-user.sh /usr/local/bin/run-as-user.sh
# COPY start-web.sh /usr/local/bin/start-web.sh

COPY --from=requirement-compiler-dev --chown=gamerauntsia:gamerauntsia /root/.local /home/gamerauntsia/.local
COPY --from=requirement-compiler-dev --chown=gamerauntsia:gamerauntsia $APP_HOME/req-src $APP_HOME/req-src

COPY ./docker/app/bin/entrypoint.sh $APP_HOME/bin
WORKDIR $APP_HOME/

ENTRYPOINT [ "./bin/entrypoint.sh" ]

#--------------------------------------------------------------------------------
FROM base AS production

# COPY start-web.sh /usr/local/bin/start-web.sh

COPY --from=requirement-compiler-common /root/.local /root/.local
COPY --from=requirement-compiler-common $APP_HOME/req-src $APP_HOME/req-src

COPY ./docker/app/bin/entrypoint.sh $APP_HOME/bin

COPY . $APP_HOME/code/
WORKDIR $APP_HOME/


ENTRYPOINT [ "./bin/entrypoint.sh" ]
