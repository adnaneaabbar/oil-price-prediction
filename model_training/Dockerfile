FROM python:3.7.2

WORKDIR /app

COPY requirements.txt requirements.txt 
COPY raw_data.csv raw_data.csv 
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY main.py main.py

ENTRYPOINT [ "bash" ]