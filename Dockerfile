FROM ubuntu:16.04

LABEL maintainer="wirelessfuture2000@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y git

RUN mkdir /tmp/app
ADD . /tmp/app
WORKDIR /tmp/app

RUN git clone https://github.com/wirelessfuture/bitly-client.git

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
EXPOSE 5000