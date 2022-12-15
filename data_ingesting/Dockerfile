FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY data_ingesting.py data_ingesting.py 

ENTRYPOINT [ "python", "data_ingesting.py" ]