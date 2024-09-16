FROM python:latest

WORKDIR /calculator_api/

RUN apt-get update -y ;\
    apt-get upgrade -y

COPY /lib/pip.conf /etc/pip.conf

RUN pip3 install \
         fastapi \
         fastapi[standard] \
         psutil

COPY /src/*.py .

EXPOSE 8080

CMD ["fastapi", "run"] 
