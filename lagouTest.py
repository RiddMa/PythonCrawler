#!/usr/bin/env python
# encoding=utf-8

import codecs
import json


import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'


def download_page(url):
    header = 'application/x-www-form-urlencoded; charset=UTF-8'
    return requests.post(DOWNLOAD_URL, 'first=true&pn=1&kd=Python', headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.80 Safari/537.36 '
    }).content


json_obj = json.loads("{'key': 'value'}")  # 字符串到对象
json_str = json.dumps(json_obj)            # 对象到字符串