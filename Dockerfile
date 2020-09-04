FROM python:3
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip3 install -r requirements.txt

# add the 'postgres' admin role
#USER postgres

# expose Postgres port
EXPOSE 5432

# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]