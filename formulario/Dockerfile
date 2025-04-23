FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app /app
COPY templates /app/templates
COPY static /app/static

CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0"]
