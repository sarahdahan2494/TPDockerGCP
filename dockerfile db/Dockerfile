FROM mariadb
WORKDIR /sql
COPY script.sql .
#ENV MARIADB_ROOT_PASSWORD=root
RUN mysql -u root -p$(MARIADB_ROOT_PASSWORD) \
"CREATE DATABASE test;" && mysql -u root test < scripts.sql 
