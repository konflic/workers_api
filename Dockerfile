FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY init_db.py .
RUN python init_db.py

EXPOSE 8080

COPY . .

CMD ["python", "main.py"]
