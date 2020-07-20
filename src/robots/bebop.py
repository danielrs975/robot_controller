'''
Contains the necessary code to control bebop 2
'''
import olympe
import time
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from olympe.messages.camera import (
    set_camera_mode,
    set_photo_mode,
    take_photo,
    photo_progress,
)
import os
import re
import requests
import shutil
import tempfile
import xml.etree.ElementTree as ET

DRONE_IP = "10.202.0.1" # This is the IP for the simulated drone
DRONE_URL = "http://{}/".format(DRONE_IP)

# Drone media web API URL
DRONE_MEDIA_API_URL = DRONE_URL + "api/v1/media/medias/"

XMP_TAGS_OF_INTEREST = (
    "CameraRollDegree",
    "CameraPitchDegree",
    "CameraYawDegree",
    "CaptureTsUs",
    # NOTE: GPS metadata is only present if the drone has a GPS fix
    # (i.e. they won't be present indoor)
    "GPSLatitude",
    "GPSLongitude",
    "GPSAltitude",
)

class Bebop():
    def __init__(self, client):
        '''
        Constructor
        '''
        # This topic modify the angular speed of the rotors
        self.drone = client
        self.drone.connect()
        self.setup_photo_burst_mode()

    
    def takeoff(self):
        '''
        Method to take off the drone
        '''
        self.drone(TakeOff())
        time.sleep(10)

    def land(self):
        '''
        Method to land the drone
        '''
        self.drone(Landing()).wait()
        time.sleep(10)

    def take_photo(self):
        '''
        This method take a photo of the environment
        '''
        # take a photo burst and get the associated media_id
        photo_saved = self.drone(photo_progress(result="photo_saved", _policy="wait"))
        self.drone(take_photo(cam_id=0)).wait()
        photo_saved.wait()
        media_id = photo_saved.received_events().last().args["media_id"]
        self.save_photo(media_id)

    def save_photo(self, media_id):
        '''
        This method save the photo in the directory
        '''
        # download the photos associated with this media id
        media_info_response = requests.get(DRONE_MEDIA_API_URL + media_id)
        media_info_response.raise_for_status()
        download_dir = './'
        
        for resource in media_info_response.json()["resources"]:
            image_response = requests.get(DRONE_URL + resource["url"], stream=True)
            download_path = os.path.join(download_dir, 'env_observation_parrot')
            image_response.raise_for_status()
            with open(download_path, "wb") as image_file:
                shutil.copyfileobj(image_response.raw, image_file)
    
            # parse the xmp metadata
            with open(download_path, "rb") as image_file:
                image_data = image_file.read()
                image_xmp_start = image_data.find(b"<x:xmpmeta")
                image_xmp_end = image_data.find(b"</x:xmpmeta")
                image_xmp = ET.fromstring(image_data[image_xmp_start : image_xmp_end + 12])
                for image_meta in image_xmp[0][0]:
                    xmp_tag = re.sub(r"{[^}]*}", "", image_meta.tag)
                    xmp_value = image_meta.text
                    # only print the XMP tags we are interested in
                    if xmp_tag in XMP_TAGS_OF_INTEREST:
                        print(resource["resource_id"], xmp_tag, xmp_value)

    def setup_photo_burst_mode(self):
        '''
        This method set up the drone to use the camera only to
        capturing photos
        '''
        self.drone(set_camera_mode(cam_id=0, value="photo")).wait()
        # For the file_format: jpeg is the only available option
        # dng is not supported in burst mode
        self.drone(
            set_photo_mode(
                cam_id=0,
                mode="burst",
                format="rectilinear",
                file_format="jpeg",
                burst="burst_14_over_1s",
                bracketing="preset_1ev",
                capture_interval=0.0,
            )
        ).wait()