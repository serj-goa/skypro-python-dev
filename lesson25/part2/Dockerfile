FROM python:3.11.1

WORKDIR /app

RUN pip install redis

COPY . .

CMD ["python", "calculator.py"]