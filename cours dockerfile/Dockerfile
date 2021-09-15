###---
FROM ubuntu

#--- pour ajouter des metadonnées
LABEL version="1.0" maintener="sarah dahan"

#-- pour se deplacer à l'interieur de l'image
WORKDIR /app 

#--- pour copier des elements à l'interieur de l'image

COPY test.txt .

#--- Declaration de variables locales au dockerfile
ARG APT_FLAGS='-y'

ENV TOTO="tata"
#--- pour executer des commandes à l'interieur de l'image
RUN apt-get update && apt-get install sqlite3 ${APT_FLAGS}

#RUN apt-get install sqlite3 -y
#-- exploser des ports 
EXPOSE 5000

CMD ["bash"]
