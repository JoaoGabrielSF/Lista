FROM python:latest 

WORKDIR /Django-DockerTest

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY models.py .

COPY manage.py .

COPY admin.py . 



CMD ["python","manage.py","run","server","--host", "0.0.0.0"]
