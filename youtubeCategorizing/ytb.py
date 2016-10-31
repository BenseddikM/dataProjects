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

videos_caracteristics = []
videos_ids = []

key = open('key_yt.config', 'r').read().replace('\n', '')
search_topic = "top"
r = requests.get(
    "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + search_topic + "&type=video&maxResults=50&key=" + key)

r.text.replace('\n', '')
data = json.loads(r.text.replace('\n', ''))

np.arange(len(data['items']))
data = json.loads(r.text)

videos_ids = list(map(lambda x: data['items'][x]['id'][
                  'videoId'], np.arange(len(data['items']))))

videos_ids

url_stats = list(map(
    lambda x: "https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&id=" + videos_ids[0] + "&maxResults=50&key=" + key, videos_ids))
url_stats

r_stats = requests.get(url_stats)
r_stats.text

stats = json.loads(r_stats.text)
