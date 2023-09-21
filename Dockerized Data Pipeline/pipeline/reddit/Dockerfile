FROM python:3.11-alpine

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r req.txt

CMD ["python","read_posts.py"]