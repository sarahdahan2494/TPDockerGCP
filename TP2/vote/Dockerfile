FROM python:3.6-slim

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 80

CMD ["gunicorn <module_name>:<instance_name > "-b "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0."]
