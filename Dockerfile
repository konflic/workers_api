FROM python:3.8-slim

WORKDIR /application

COPY requirements.txt .

RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 8888

COPY . .

CMD ["python", "main.py"]
