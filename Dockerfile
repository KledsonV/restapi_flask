FROM python:latest

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application
COPY wsgi.py Config.py ./

CMD [ "python", "wsgi.py" ]