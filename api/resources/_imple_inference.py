import numpy as np
import requests
import json
import os
from PIL import Image
import ssl
import urllib
import tqdm
import logging


#logging.basicConfig(level=logging.DEBUG)

def request(instances=None, cluster_ip=None, hostname=None, model_name=None, op='predict'):

    try:
        payload = {'instances': instances}

        # sending post request to TensorFlow Serving server
        headers = {'Host': hostname}
        url = f'http://{cluster_ip}/v1/models/{model_name}:{op}'
        print("Calling ", url)
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            resp = json.loads(response.content.decode('utf-8'))
            return resp
        else:
            raise Exception(
                f"Received : {response.status_code}, {response.content}"
            )
    except Exception as e:
        raise e
