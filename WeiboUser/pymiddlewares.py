import base64
import random
from WeiboUser.settings import PROXIES
import time

class ProxyMiddleware(object):
# overwrite process request
    def process_request(self, request, spider):
    # Set the location of the proxy
        p = random.choice(PROXIES)
        print('using proxy '+ p)
        request.meta['proxy'] = p