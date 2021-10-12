FROM python:3.9-alpine

COPY ./requirements.txt .
COPY ./.env env_file
RUN export $(cat ./env_file | xargs)

RUN apk add --no-cache --virtual .build-deps build-base \
    linux-headers \
    libxslt-dev \
    build-base \
    tzdata \
    jpeg-dev \
    zlib-dev \
    bash

RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime

RUN pip3 install Pillow
RUN pip3 install -r ./requirements.txt

WORKDIR /app
COPY ./ /app

CMD ["bash", "-c", "export $(cat ./.env | xargs) && python3 ./app/app.py"]
