"""ml-challenge-api"""

from fastapi import FastAPI
import psutil
from ..scripts.module import clean_folder

app = FastAPI()

@app.get("/")
def alive():
    """Keep Alive"""
    return "Alive!"

@app.get("/list_devices/")
def list_devices(mountpoint: str | None = None):
    """List Devices"""
    class DeviceObject:
        """Device Object"""
        def __init__(self, device, mountpoint, disk_usage):
            self.device = device
            self.mountpoint = mountpoint
            self.disk_usage = disk_usage

    devices_list = list()
    devices = psutil.disk_partitions(all=False)
    for item in devices:
        devices_list.append(
            DeviceObject(
                item.device,
                item.mountpoint, 
                psutil.disk_usage(item.mountpoint)
            ),
        )

    if mountpoint:
        return list(filter(lambda DeviceObject: DeviceObject.mountpoint == mountpoint, devices_list))
    return devices_list

@app.post("/clean_tmp")
def empty_tmp():
    """Clean /tmp Folder"""
    return clean_folder('/tmp')
