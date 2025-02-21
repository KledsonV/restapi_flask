FROM python:latest

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py .
COPY Config.py .
COPY application application

CMD [ "python", "wsgi.py" ]