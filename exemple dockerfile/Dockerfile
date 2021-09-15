FROM debian

RUN apt-get update
WORKDIR /application

COPY . .

RUN chmod +x test.sh 
ENV TOTO="tata"
CMD ["./test.sh"]
