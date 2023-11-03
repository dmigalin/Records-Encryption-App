FROM python:3.11-alpine3.18

WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

