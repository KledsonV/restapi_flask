FROM python:latest

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py Config.py application/ ./

CMD [ "python", "wsgi.py" ]