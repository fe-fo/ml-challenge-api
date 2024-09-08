"""ml-challenge-api"""

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import psutil

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/list_devices/")
def list_devices(mountpoint: str | None = None):
    """List Devices"""
    class DeviceObject:
        def __init__(self, device, mountpoint, diskUsage):
            self.device = device
            self.mountpoint = mountpoint
            self.diskUsage = diskUsage

    devicesList = list()
    devices = psutil.disk_partitions(all=False)
    for item in devices:
        devicesList.append(
            DeviceObject(
                item.device,
                item.mountpoint, 
                psutil.disk_usage(item.mountpoint)
            ),
        )

    if mountpoint:
        return list(filter(lambda DeviceObject: DeviceObject.mountpoint == mountpoint, devicesList))
    return devicesList
