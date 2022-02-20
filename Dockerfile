FROM alpine

WORKDIR /app

COPY . .

RUN set -x \
    && apk add py3-pip \
    && pip3 install -r requirements.txt 

CMD [ "/usr/bin/flask","run","--host=0.0.0.0", "--port=5000" ]
