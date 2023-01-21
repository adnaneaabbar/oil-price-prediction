FROM python:3.9.13

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install -r requirements.txt

CMD ["python", "app.py"]