FROM python:3.10

ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev unixodbc

RUN  mkdir /home/app

COPY . /home/app

RUN pip install --upgrade pip

RUN pip install -r /home/app/requirements.txt

CMD ["python","/home/app/main.py"]
#this is a test to see if a commit works