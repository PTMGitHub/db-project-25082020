FROM python:3
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip3 install -r requirements.txt

# COPY . /usr/src/app
# WORKDIR /usr/src/app
# RUN pip3 install --upgrade pip3
# COPY ./requirements.txt /usr/src/app/requirements.txt
# RUN pip3 install -r requirements.txt

            
# FROM library/postgres
# ENV POSTGRES_USER postgres
# ENV POSTGRES_PASSWORD root
# ENV POSTGRES_DB D_db