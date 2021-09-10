From python:3.8-slim-buster


WORKDIR /app


Copy requirements.txt requirements.txt 

Run pip3 install -r requirements.txt 

Copy . .

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
