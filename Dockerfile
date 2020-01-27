
FROM ubuntu:16.04

MAINTANER Mukesh "mukeshram1995@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8001

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
