#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import re
import requests

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


key = open('key_yt.config', 'r').read().replace('\n', '')
r = requests.get(
    "https://www.googleapis.com/youtube/v3/search?part=id&q=League&type=video&maxResults=50&key=" + key)

data = json.loads(r.text)

np.arange(len(data['items']))
data = json.loads(r.text)
data
videos_ids = list(map(lambda x: data['items'][x]['id'][
                  'videoId'], np.arange(len(data['items']))))

videos_ids

url_stats = list(map(
    lambda x: "https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&id=" + videos_ids[0] + "&maxResults=50&key=" + key, videos_ids))
url_stats

r_stats = requests.get(url_stats)
r_stats.text

stats = json.loads(r_stats.text)
