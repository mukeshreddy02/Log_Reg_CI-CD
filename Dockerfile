
FROM ubuntu:16.04

MAINTAINER Mukesh "mukeshram1995@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
