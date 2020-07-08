FROM python:3.7-alpine

RUN pip install boto3 PyYAML

RUN mkdir /code
WORKDIR /code

COPY bootstrap.py /code/

CMD ["python", "bootstrap.py"]
