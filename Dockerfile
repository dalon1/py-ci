FROM python:3.7-alpine

MAINTAINER dannel

RUN mkdir -p app
WORKDIR app


#Copy src code...
COPY src src
COPY test test

#Install dependencies...
RUN pip install flask
EXPOSE 8066
ENTRYPOINT ["python", "src/app.py"]
