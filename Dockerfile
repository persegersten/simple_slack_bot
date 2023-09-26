FROM python:3.11-slim as builder
COPY requirements.txt /build/
WORKDIR /build/
RUN pip install -U pip && pip install -r requirements.txt

FROM python:3.11-slim as app
WORKDIR /app/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY ./src/*.py /app/
EXPOSE 80
ENTRYPOINT gunicorn --bind :80 --workers 1 --threads 2 --timeout 0 app:flask_app
