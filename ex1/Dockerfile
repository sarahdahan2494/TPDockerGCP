FROM debian 

ARG FLAG="y"
RUN apt-get update && apt-get upgrade vim ${FLAGS} 

RUN apt-get install vim $(FLAG)

CMD ["bash"]
