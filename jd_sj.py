# cron "10 22 * * *" 
# new Env('py三时间比对')
import json
import math
import random
import threading
import time
import requests,os
import datetime
import ntplib   

#os.environ 获取环境变量
cookie =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[cookie[0],cookie[1],cookie[2],cookie[3],cookie[4],cookie[5],cookie[6],cookie[7],cookie[8],cookie[9],cookie[10],cookie[11]]
#print(mycookies)

#阿里在线获取时间
def jdtime1():
  ntp_server_url="ntp.aliyun.com"
  ntp = ntplib.NTPClient()
  ntpResponse = ntp.request(ntp_server_url)
  if (ntpResponse): 
      # calculate the ntp time and convert into microseconds
      ntp_time = int(ntpResponse.tx_time * 1000)
      return(ntp_time)

#京东时间

def jdtime2():
    url = 'http://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5'
    headers = {
        "Cookie": cookie[5],"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    try:
        res = requests.get(url=url, headers=headers, timeout=1).json()
        return int(res['currentTime2'])
    except:
        return 0

		#本地时间
def jdtime3():
    return int(time.time() * 1000)

a=jdtime1()
b=jdtime2()
c=jdtime3()

print("阿里在线",a)
print("京东时间",b)
print("本地时间",c)