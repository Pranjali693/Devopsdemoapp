FROM python:3.8-slim-buster

WORKDIR /FLASK-APP-DEVOPS 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]