FROM debian 

RUN apt-get update

RUN apt-get install python3 -y

WORKDIR /app${FTP_PROXY}

COPY exercice.py . 
RUN chmod +x exercice.py

CMD ["python3", "exercice.py"]