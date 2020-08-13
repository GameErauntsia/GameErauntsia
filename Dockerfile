FROM python:3.5.2-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP_HOME=/app
WORKDIR $APP_HOME
RUN mkdir logs static media

COPY cronjobs $APP_HOME/
RUN cat cronjobs >> /etc/crontabs/root

RUN apk add --no-cache mysql-client mariadb-client-libs libjpeg
COPY requirements.txt $APP_HOME/
RUN apk add --no-cache --virtual .build-deps \
        mariadb-dev git \
        gcc python3-dev musl-dev jpeg-dev zlib-dev && \
    pip install -r requirements.txt --src $APP_HOME/lib && \
    apk del .build-deps

COPY . $APP_HOME/code/

WORKDIR $APP_HOME/code
ENTRYPOINT ["./entrypoint.sh"]
