FROM python:3.8

COPY ./app /app

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod -R 777 /app

WORKDIR /app

RUN pip install -r requirements/dev.txt

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/sh","/entrypoint.sh"]