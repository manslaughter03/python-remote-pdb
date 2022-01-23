FROM python:3.10-alpine

WORKDIR /usr/src

#COPY requirements.txt .

#RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./setup.py .

RUN pip install .

ENTRYPOINT ["python"]
CMD ["-m" , "example_pkg"]
