FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /usr/src/app



# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/