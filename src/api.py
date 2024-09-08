from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import redis
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import psutil

try:
    uri = 'mongodb+srv://nomoreops_mongo_sa:1hl75TRa0BmrpCiy@nomoreops-mongo.vb3psxx.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

try:
    r = redis.Redis(
        host='redis-14962.c114.us-east-1-4.ec2.cloud.redislabs.com',
        port=14962,
        password='SxYjSXczUARk1yQWxQ8QyKLaPq5H3aCu'
    )
    r.ping()
    print('Connected to redis redis-14962.c114.us-east-1-4.ec2.cloud.redislabs.com')
except Exception as e:
    print(e)

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def keepalive():
    """Alive"""
    return {"Alive!"}

@app.get("/")
def list_devices():
    devices = psutil.disk_partitions(all=True)
    for device in devices:
        print(f"Device: {device.device}")
        print(f"  Mountpoint: {device.mountpoint}")
        print(f"  File system type: {device.fstype}")
        print()




if __name__ == "__main__":
    list_devices()
