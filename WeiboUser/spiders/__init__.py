# # This package will contain the spiders of your Scrapy project
# #
# # Please refer to the documentation for information on how to create and manage
# # your spiders.175.155.24.55	808111.155.116.202	8123
# import  urllib
# from urllib import request
# from http.client import RemoteDisconnected
# from urllib.error import URLError, HTTPError
# import json
# import time
#
# proxies = [
#     # https proxy
#     # 60.172.124.96:808
#     # 115.221.112.90:808
#     '175.155.240.241:808',
#     '218.64.93.197:808',
#     '183.31.71.207:9000',
#     '218.64.93.217:808',
#     '120.34.46.47:808',
#     '183.1.86.11:8118',
#     '117.44.102.66:8118',
#     '171.13.36.107:808',
#     '114.239.144.207:808',
#     '121.204.102.131:808',
#     '122.192.66.50:808',
#     '113.121.244.253:808',
#     '114.99.23.232:808',
#     '122.241.74.203:808',
#     '115.203.67.59:808',
#     '121.40.208.69:1080',
#     '1.61.41.62:80',
#     '122.245.68.201:808',
#     '106.92.41.94:8118',
#     '115.220.7.250:808',
#     '116.28.104.209:808',
#     '59.54.227.189:8118',
#     '220.166.242.94:8118',
#     '123.163.128.132:808',
#     '114.99.5.212:808',
#     '114.99.72.178:808',
#     '183.153.38.161:808',
#     '175.155.136.72:808',
#     '222.85.39.4:808',
#     '61.153.7.204:3128',
#     '171.44.251.150:808',
#     '122.241.73.117:808',
#     '113.3.82.84:8118',
#     '175.155.24.118:808',
#     '113.93.184.216:808',
#     '115.213.246.112:808',
#     '115.215.71.35:808',
#     '218.64.93.25:808',
#     '115.203.82.129:808',
#     '36.99.207.139:808',
#     '218.64.92.63:808',
#     '36.249.26.232:808',
#     '115.213.203.25:808',
#     '110.83.46.89:808',
#     '115.220.148.37:808',
#     '115.202.181.243:808',
#     '171.13.37.53:808',
#     '183.144.194.101:3128',
#     '1.68.143.56:808',
#     '115.202.181.186:808',
#     '59.62.96.188:808',
#     '101.67.63.155:80',
#     '115.220.150.99:808',
#     '183.153.0.44:808',
#     '112.250.87.27:8080',
#     '114.239.1.196:808',
#     '115.203.92.55:808',
#     '60.178.87.168:808',
#     '183.153.23.53:808',
#     '117.43.1.234:808',
#     '221.229.47.86:808',
#     '183.36.40.243:808',
#     '182.37.16.12:808',
#     '60.167.20.155:808',
#     '121.226.160.74:808',
#     '115.215.69.80:808',
#     '115.213.201.213:808',
#     '220.179.210.208:808',
#     '59.62.124.82:808',
#     '183.128.138.241:3128',
#     '110.73.48.174:8123',
#     '113.121.247.188:808',
#     '114.239.150.223:808',
#     '171.12.164.120:808',
#     '182.38.96.92:808',
#     '114.232.154.120:808',
#     '115.202.175.190:808',
#     '27.8.11.190:808',
#     '115.212.59.115:808',
#     '171.12.139.91:808',
#     '115.220.1.202:808',
#     '221.229.47.240:808',
#     '122.241.75.253:808',
#     '123.170.255.154:808',
#     '114.253.205.163:8118',
#     '140.250.84.93:808',
#     '123.163.130.195:808',
#     '218.64.92.214:808',
#     '171.12.166.147:808',
#     '115.215.70.66:808',
#     '42.123.69.154:8080',
#     '171.13.37.151:808',
#     '115.213.177.204:808',
#     '14.211.125.74:9797',
#     '117.91.138.151:808',
#     '114.239.2.22:808',
#     '117.43.0.65:808',
#     '123.55.185.29:808',
#     '183.153.21.138:808',
#     '218.64.92.50:808',
#     '113.69.167.30:808',
#     '114.99.8.147:808',
#     '222.95.23.93:808',
#     '119.29.207.56:80',
#     '175.155.226.87:808',
#     '222.76.144.139:39541',
#     '115.213.238.243:808',
#     '27.31.102.145:808',
#     '218.64.92.180:808',
#     '218.64.92.130:808',
#     '119.5.1.24:808',
#     '113.69.164.59:808',
#     '175.154.50.108:808',
#     '222.94.147.209:808',
#     '222.94.151.175:808',
#     '222.95.21.24:808',
#     '171.38.170.131:8123',
#     '121.226.173.188:808',
#     '119.5.150.122:808',
#     '117.43.1.124:808',
#     '114.238.144.75:808',
#     '171.38.34.165:8123',
#     '171.38.129.21:8123',
#     '114.235.76.29:808',
#     '171.38.34.216:8123',
#     '171.38.99.251:8123',
#     '115.220.144.211:808',
#     '117.43.42.80:808',
#     '222.94.144.142:808',
#     '123.55.176.127:808',
#     '115.213.201.64:808',
#     '180.125.98.3:26804',
#     '117.89.94.174:808',
#     '115.220.146.206:808',
#     '60.184.174.65:808',
#     '115.202.175.252:808',
#     '218.64.93.209:808',
#     '180.118.240.20:808',
#     '110.86.103.64:808',
#     '115.46.67.15:8123',
#     '122.245.66.101:808',
#     '123.55.191.53:808',
#     '180.110.190.253:808',
#     '122.245.71.233:808',
#     '125.89.123.127:808',
#     '101.205.14.220:808',
#     '113.121.247.128:808',
#     '113.121.41.8:808',
#     '119.7.79.145:808',
#     '111.72.245.43:808',
#     '113.58.234.159:808',
#     '182.45.62.119:808',
#     '182.34.18.20:808',
#     '36.249.29.172:808',
#     '60.167.133.60:808',
#     '183.32.233.21:808',
#     '175.155.24.53:808',
#     '59.62.121.23:808',
#     '218.29.111.106:9999',
#     '114.239.145.169:808',
#     '182.88.42.96:8123',
#     '175.155.141.35:808',
#     '110.83.46.86:808',
#     '115.213.155.71:8118',
#     '112.195.49.11:808',
#     '175.155.241.205:808',
#     '115.192.73.118:808',
#     '182.122.113.204:8118',
#     '113.58.233.44:808',
#     '123.55.185.104:808',
#     '49.86.62.204:808',
#     '114.239.151.48:808',
#     '119.5.218.189:808',
#     '121.226.174.130:808',
#     '115.203.83.177:808',
#     '114.237.209.12:33097',
#     '116.28.116.82:808',
#     '115.220.0.138:808',
#     '220.179.214.217:808',
#     '60.184.174.181:808',
#     '123.163.161.212:808',
#     '119.7.78.240:808',
#     '113.70.148.186:808',
#     '117.91.246.6:808',
#     '115.220.5.105:808',
#     '59.62.83.213:808',
#     '59.62.119.9:808',
#     '114.239.146.33:808',
#     '180.110.16.16:808',
#     '115.203.77.103:808',
#     '113.123.127.84:808',
#     '114.239.151.250:808',
#     '222.95.18.48:808',
#     '113.58.232.38:808',
#     '183.153.55.176:808',
#     '113.121.46.217:808',
#     '123.55.178.144:808',
#     '49.81.252.207:8118',
#     '180.122.21.248:33407',
#     '125.89.122.18:808',
#     '121.61.97.201:808',
#     '182.88.91.4:8123',
#     '115.207.80.24:808',
#     '114.239.145.61:808',
#     '123.139.56.238:9999',
#     '121.61.106.154:808',
#     '59.62.126.130:808',
#     '115.215.71.222:808',
#     '122.241.75.250:808',
#     '222.94.145.50:808',
#     '222.85.50.15:808',
#     '113.58.232.31:808',
#     '115.213.200.129:808',
#     '115.213.201.87:808',
#     '222.95.17.155:808',
#     '122.241.73.146:808',
#     '221.229.47.110:808',
#     '115.220.4.207:808',
#     '175.155.246.174:808',
#     '59.62.118.143:808',
#     '119.7.72.139:808',
#     '122.241.28.145:808',
#     '182.45.109.47:808',
#     '182.45.3.114:808',
#     '123.55.191.212:808',
#     '115.220.4.94:808',
#     '115.220.4.181:808',
#     '218.64.93.231:808',
#     '175.155.243.139:808',
#     '60.184.172.152:808',
#     '60.178.87.126:808',
#     '58.67.159.50:80',
#     '117.43.1.227:808',
#     '115.220.145.0:808',
#     '106.110.45.188:8118',
#     '60.167.21.103:808',
#     '183.153.36.173:808',
#     '113.236.35.113:808',
#     '60.178.87.11:808',
#     '175.155.141.187:808',
#     '115.203.77.20:808',
#     '123.163.161.49:808',
#     '117.43.1.33:808',
#     '222.89.74.112:808',
#     '110.73.28.67:8123',
#     '122.245.71.128:808',
#     '115.220.147.186:808',
#     '116.28.106.8:808',
#     '175.155.240.181:808',
#     '115.203.86.61:808',
#     '220.160.10.20:808',
#     '125.92.33.182:808',
#     '111.155.116.221:8123',
#     '115.220.144.112:808',
#     '114.239.150.17:808',
#     '119.5.34.135:808',
#     '115.203.69.214:808',
#     '115.213.253.225:808',
#     '182.35.37.199:80',
#     '115.151.0.206:808',
#     '115.203.86.71:808',
#     '121.61.111.103:808',
#     '222.94.150.179:808',
#     '61.160.208.221:8080',
#     '124.88.84.154:8080',
#     '114.239.1.101:808',
#     '175.155.143.233:808',
#     '115.207.99.79:808',
#     '222.95.23.174:808',
#     '180.118.242.230:808',
#     '60.172.124.96:808',
#     '49.86.62.169:808',
#     '115.192.78.112:808',
#     '180.118.240.79:808',
#     '114.232.154.72:808',
#     '113.69.252.63:808',
#     '115.215.70.217:808',
#     '183.149.48.96:808',
#     '175.155.246.102:808',
#     '123.55.94.82:808',
#     '123.169.84.112:808',
#     '175.155.136.89:808',
#     '116.28.108.210:808',
#     '113.121.244.210:808',
#     '221.229.44.74:808',
#     '117.43.1.142:808',
#     '120.38.14.211:808',
#     '119.7.81.235:808',
#     '175.155.245.72:808',
#     '175.155.247.149:808',
#     '221.237.154.57:9797',
#     '222.94.147.15:808',
#     '180.110.18.141:808',
#     '59.62.86.240:808',
#     '122.245.68.79:808',
#     '115.212.60.89:808',
#     '110.83.46.254:808',
#     '59.62.110.181:808',
#     '222.89.74.32:808',
#     '183.153.6.89:808',
#     '115.203.66.97:808',
#     '115.203.95.34:808',
#     '121.13.165.46:808',
#     '222.76.118.179:808',
#     '117.91.138.7:808',
#     '110.19.190.22:8080',
#     '59.62.166.175:808',
#     '60.184.175.176:808',
#     '183.153.29.54:808',
#     '117.43.0.126:808',
#     '175.155.154.153:808',
#     '115.207.82.255:808',
#     '122.5.130.171:808',
#     '115.220.7.40:808',
#     '123.169.84.13:808',
#     '36.249.24.79:808',
#     '180.118.242.25:808',
#     '113.121.22.229:808',
#     '119.5.217.173:808',
#     '115.207.83.227:808',
#     '123.163.143.120:808',
#     '175.155.234.66:808',
#     '123.163.164.224:808',
#     '175.155.141.143:808',
#     '115.221.112.90:808',
#     '114.238.42.209:808',
#     '115.202.172.80:808',
#     '115.151.1.50:808',
#     '120.83.97.33:808',
#     '115.215.68.140:808',
#     '113.122.150.201:808',
#     '114.238.22.183:808',
#     '60.167.135.13:808',
#     '115.203.69.198:808',
#     '113.69.179.2:808',
#     '183.153.16.53:808',
#     '113.121.21.130:808',
#     '113.121.245.66:808',
#     '123.169.88.132:808',
#     '123.163.166.111:808',
#     '123.163.132.56:808',
#     '114.99.21.155:808',
#     '123.163.71.126:808',
#     '113.123.36.52:808',
#     '123.163.160.148:808',
#     '115.203.70.205:808',
#     '175.155.25.24:808',
#     '122.241.74.15:808',
#     '115.202.237.30:808',
#     '115.203.84.219:808',
#     '221.229.45.220:808',
#     '122.5.132.106:808',
#     '115.220.145.182:808',
#     '144.255.123.23:808',
#     '116.28.122.21:808',
#     '122.245.66.16:808',
#     '175.155.241.34:808',
#     '175.155.242.223:808',
#     '115.215.69.218:808',
#     '183.153.11.200:808',
#     '123.55.95.167:808',
#     '115.203.199.58:808',
#     '182.87.187.101:808',
#     '122.245.69.188:808',
#     '222.76.118.181:808',
#     '175.155.155.189:808',
#     '117.43.0.49:808',
#     '123.163.164.9:808',
#     '222.76.118.238:808',
#     '113.68.8.64:9999',
#     '115.203.69.149:808',
#     '115.203.69.197:808',
#     '121.226.162.127:808',
#     '123.163.162.173:808',
#     '1.195.10.230:808',
#     '171.80.163.66:808',
#     '123.163.160.61:808',
#     '114.99.10.254:808',
#     '123.170.255.160:808',
#     '60.178.86.7:808',
#     '123.163.143.60:808',
#     '123.169.84.192:808',
#     '123.163.166.142:808',
#     '113.69.178.75:808',
#     '114.236.3.111:808',
#     '175.155.247.229:808',
#     '121.31.150.46:8123',
#     '114.230.98.23:808',
#     '114.230.124.72:808',
#     '175.155.139.242:808',
#     '115.202.188.4:808',
#     '123.163.161.34:808',
#     '115.220.148.140:808',
#     '1.192.247.108:8118',
#     '115.220.7.247:808',
#     '221.229.45.26:808',
#     '182.34.20.52:808',
#     '123.163.165.152:808',
#     '218.64.92.24:808',
#     '220.160.10.235:808',
#     '219.139.190.188:808',
#     '115.215.70.47:808',
#     '183.153.2.153:808',
#     '110.73.38.26:8123',
#     '171.38.153.3:8123',
#     '59.62.165.6:808',
#     '175.155.138.91:808',
#     '153.36.177.25:808',
#     '117.43.0.236:808',
#     '59.62.99.4:808',
#     '175.155.245.216:808',
#     '115.49.107.143:8118',
#     '175.43.106.82:808',
#     '171.36.63.15:8123',
#     '180.175.2.143:63000',
#     '113.58.235.48:808',
#     '222.94.150.157:808',
#     '121.61.100.131:808',
#     '110.72.27.59:8123',
#     '175.155.244.91:808',
#     '60.167.135.76:808',
#     '171.38.155.236:8123',
#     '115.213.202.231:808',
#     '115.220.1.116:808',
#     '222.94.151.121:808',
#     '175.155.68.78:808',
#     '114.238.161.142:808',
#     '222.94.148.242:808',
#     '123.169.84.196:808',
#     '115.203.85.34:808',
#     '121.62.186.23:808',
#     '123.169.87.226:808',
#     '36.249.27.87:808',
#     '113.93.185.82:808',
#     '114.230.123.181:808',
#     '182.45.177.183:808',
#     '113.71.115.120:808',
#     '183.153.27.1:808',
#     '117.43.1.89:808',
#     '119.5.0.24:808',
#     '183.153.28.94:808',
#     '183.153.3.235:808',
#     '113.123.127.171:808',
#     '183.153.1.225:808',
#     '1.68.140.187:808',
#     '115.220.2.18:808',
#     '119.90.248.245:9999',
#     '115.213.177.30:808',
#     '110.83.46.152:808',
#     '175.155.189.231:808',
#     '59.62.41.78:808',
#     '119.7.72.99:808',
#     '175.155.227.69:808',
#     '220.160.10.249:808',
#     '125.106.251.179:808',
#     '123.163.163.64:808',
#     '115.203.76.188:808',
#     '221.229.47.98:808',
#     '222.85.39.3:47954',
#     '115.213.200.226:808',
#     '175.155.243.126:808',
#     '222.95.20.211:808',
#     '182.32.168.236:808',
#     '171.13.36.186:808',
#     '175.155.240.21:808',
#     '180.118.240.18:808',
#     '123.55.188.28:808',
#     '115.213.203.49:808',
#     '221.229.46.142:808',
#     '113.122.5.247:808',
#     '183.153.57.205:808',
#     '183.153.62.206:808',
#     '115.220.144.4:808',
#     '183.157.191.137:80',
#     '123.55.177.103:808',
#     '49.83.8.165:808',
#     '183.158.9.56:34221',
#     '222.95.21.16:808',
#     '60.167.133.107:808',
#     '123.163.160.135:808',
#     '115.213.177.236:808',
#     '60.169.216.24:808',
#     '123.169.86.212:808',
#     '115.204.131.165:808',
#     '175.155.243.145:808',
#     '120.34.46.168:808',
#     '119.5.0.101:808',
#     '113.123.127.146:808',
#     '119.7.72.66:808',
#     '115.213.200.128:808',
#     '183.153.58.229:808',
#     '115.203.71.106:808',
#     '125.106.250.114:808',
#     '180.118.241.134:808',
#     '222.94.144.178:808',
#     '123.170.85.127:808',
#     '180.118.242.90:808',
#     '36.249.29.186:808',
#     '59.62.110.254:808',
#     '60.184.173.18:808',
#
# ]
#
#
# head = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')]
#
# ok_list = []
#
# global proxy_handler
#
# for i in range(0,len(proxies)):
#     try:
#         time.sleep(0.5)
#         proxy_handler = urllib.request.ProxyHandler({'http': proxies[i],'https':proxies[i]})
#         opener = urllib.request.build_opener(proxy_handler)
#         opener.addheaders = head
#
#         with opener.open('https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_' \
#                           '5743923782&luicode=10000011&lfid=100505' \
#                           '5743923782&featurecode=20000180&page=1',timeout=5) as f:
#
#         # f = opener.open('https://m.weibo.cn/')
#             a = f.read()
#
#             print(a)
#             ok_list.append(proxies[i])
#             print('ok_list ' + str(ok_list))
#             print('well ' + proxies[i])
#             # f.close()
#     except  (HTTPError) as err:
#         print(err.code)
#     except  (URLError) as err:
#         print('bad ' + proxies[i])
#         print(err.reason)
#     except (RemoteDisconnected) as error:
#         print('RemoteDisconnected')
#     except Exception as error:
#         print(error)
#
#
# print(ok_list)