# coding=utf-8
import json
import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


logging.basicConfig(format='%(levelname)5s %(asctime)-15s #%(filename)-20s@%(funcName)-20s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GenApi(object):
    """
    """
    def __init__(self, method="GET", endpoint="www.baidu.com", **kwargs):
        """
        :param endpoint:
        :param args:
        :param kwargs:
        """
        self.end_point = endpoint
        self.s = requests.Session()
        self.retries = Retry(total=3, backoff_factor=0.2, status_forcelist=[500, 502, 503, 504])
        self.s.mount('https://', HTTPAdapter(max_retries=self.retries))

        self.method = method
        self.dict_params = kwargs

    def run(self):
        logging.info(f"endpoint: {self.end_point} dict params : {self.dict_params} method: {self.method}")
        if "payload" in self.dict_params.keys():
            payload = self.dict_params['payload']
        else:
            payload = ""
        if "payload_json" in self.dict_params.keys():
            payload_json = self.dict_params['payload_json']
        else:
            payload_json = ""
        if "headers" in self.dict_params.keys():
            headers = self.dict_params['headers']
        else:
            headers = ""
        if "params" in self.dict_params.keys():
            params = self.dict_params['params']
        else:
            params = ""

        if payload_json == "":
            response = self.s.request(self.method, self.end_point, data=payload, headers=headers, params=params)
        else:
            response = self.s.request(self.method, self.end_point, json=payload_json, headers=headers, params=params)
        logging.info(f"{response.text}")


if __name__ == "__main__":
    gen_api = GenApi(endpoint="", payload="test payload")
    gen_api.run()
