FROM debian as builder 
RUN apt-get update 

WORKDIR /app

RUN touche index.js

FROM debian

RUN apt-get update && apt-get install nodejs -y

WORKDIR /web

COPY --from=builder /app .

CMD ["bash"]