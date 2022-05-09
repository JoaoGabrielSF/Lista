FROM python:latest 

WORKDIR /Django-DockerTest

COPY requirements.txt . 

COPY lista . 
 
COPY manage.py .

CMD ["python","manage.py","run","server","--host", "0.0.0.0"]
