FROM python:latest

WORKDIR /calculator_api/

RUN apt-get update -y ;\
    apt-get upgrade -y

RUN pip3 install \
         fastapi \
         uvicorn[standard] \
         python-multipart \
         prometheus-fastapi-instrumentator \
         pymongo \
         redis \
         psutil

COPY ./main/api.py .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"] 

EXPOSE 80/tcp
