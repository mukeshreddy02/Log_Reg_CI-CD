
FROM python:3

ADD . /app

WORKDIR /app



RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8001

CMD ["python3", "app.py"]
