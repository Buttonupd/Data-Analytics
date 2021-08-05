FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYCODE=1
WORKDIR /app
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev g++
    
RUN pip install psycopg2-binary

RUN apk add zlib-dev jpeg-dev gcc musl-dev
#install pip for the docker image
RUN pip install --upgrade pip

COPY  requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

