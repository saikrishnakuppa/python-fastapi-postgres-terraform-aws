FROM python:3.12-alpine

ENV PORT=443

RUN apk update && apk upgrade && apk add --no-cache openssl bash

WORKDIR /app

RUN mkdir -p keystore

RUN openssl req -x509 -newkey rsa:2048 -keyout keystore/key.pem -out keystore/cert.pem -days 365 -nodes -subj "/C=US/ST=ShortHills/L=New Jersey/O=Kuppa/OU=Home/CN=saikuppa.local"

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /app/src

COPY start.sh /app/start.sh

RUN chmod +x /app/start.sh

EXPOSE $PORT

ENTRYPOINT ["/app/start.sh"]