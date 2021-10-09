FROM python:3.7-slim-buster

WORKDIR /src
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--timeout=10", "--workers=4", "web.app:app"]

RUN apk-add curl

RUN pip3 install \
  gunicorn \
  flask \
  requests \
  webargs==4.1.2 \
  sqlalchemy==1.3.0b1 \
  https://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-8.0.18.zip#md5=e9c473418b52bcae9687dddb0b69369f
  
RUN ls -lh

COPY . /src
RUN cd /src && python3 setup.py develop
