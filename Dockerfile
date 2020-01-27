from alpine:latest

RUN apk add --no-cache python3-dev \
&& pip install -- upgrade pip

WORKDIR /app

COPY * /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8001

CMD ["python3", "app.py"]
