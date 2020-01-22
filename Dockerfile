FROM python:3.7-alpine
COPY requirements.txt src /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt
EXPOSE 8066
ENTRYPOINT ["python", "app.py"]
