FROM debian 

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install mysql-connector-python 

WORKDIR /app
COPY script.py .
RUN chmod +x script.py

CMD ["python", "script.py"]