from time import asctime
from mushroom_soup import *
import requests
import os
from info_log import info_logger
from error_log import error_logger
from mushroom_soup import *
from urllib.parse import urljoin
from bs4 import BeautifulSoup

make_data_files('https://4chan.org')