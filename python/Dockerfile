FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements/backend.txt .

RUN pip install --no-cache-dir -r backend.txt

COPY . .

RUN pip install --no-cache-dir -r ./requirements/backend.txt

EXPOSE 8080

CMD ["uvicorn", "spaceship.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]