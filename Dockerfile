FROM python:3.8

# RUN apk add python3-dev

ADD ./app /app
ADD ./requirements.txt /app

RUN chmod -R 777 /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","test_project/manage.py","runserver","0.0.0.0:8000"]