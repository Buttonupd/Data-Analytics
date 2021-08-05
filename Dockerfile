FROM python:3.8-slim
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYCODE=1
WORKDIR /app
# install psycopg2 dependencies
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc postgresql-dev python3-dev musl-dev zlib-dev 	jpeg-dev && \
    apt clean && rm -rf /var/lib/apt/lists/*
  

RUN pip install --upgrade pip

COPY  requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

