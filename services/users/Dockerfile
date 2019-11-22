# base image
FROM python:3.7.2-slim

# install dependencies
# RUN apk update && \
#     apk add --virtual build-deps gcc python-dev musl-dev && \
#     apk add postgresql-dev && \
#     apk add netcat-openbsd

# install netcat
RUN apt-get update && \
    # apt-get -y install python-dev gcc musl-dev \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# new
# run server
CMD ["/usr/src/app/entrypoint.sh"]
