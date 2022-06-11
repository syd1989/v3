# cron "55 13 * * *" 
# new Env('PY-59-20免券')
import json
import math
import random
import threading
import time
import requests,os
import datetime


#dt_ms = datetime.datetime.now().strftime('%H:%M:%S.%f') # 含微秒的日期时间，

starttime = 1654091999000 #需要精确到毫秒
#cookie格式：  'jfsdfhksj;'  只能放入一个cookie

#os.environ 获取环境变量
cookie =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[cookie[0],cookie[1],cookie[2],cookie[3],cookie[4],cookie[5],cookie[6],cookie[7],cookie[8],cookie[9],cookie[10],cookie[11]]
#print(mycookies)

ck = cookie[0]

print(ck)

#黄鸟包抓包4次url 全部复制进去，  任意一个链接的body复制进去（body为没有编码翻译的那个）。
url1 = 'https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22csTQSAnfQypSN7KeyCwJWthE6aV%22%2C%22from%22%3A%22H5node%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3Dm9a6teebr9iaa0lfc4m6sbb4a6351303%2CroleId%3D76337067%22%7D&client=wh5&clientVersion=1.0.0'
url2 = 'https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22csTQSAnfQypSN7KeyCwJWthE6aV%22%2C%22from%22%3A%22H5node%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3Dm9a6teebr9iaa0lfc4m6sbb4a6351303%2CroleId%3D76337067%22%7D&client=wh5&clientVersion=1.0.0'

body1 = '{"activityId":"csTQSAnfQypSN7KeyCwJWthE6aV","from":"H5node","scene":"1","args":"key=m9a6teebr9iaa0lfc4m6sbb4a6351303,roleId=76337067"}'
body2 = '{"activityId":"csTQSAnfQypSN7KeyCwJWthE6aV","from":"H5node","scene":"1","args":"key=m9a6teebr9iaa0lfc4m6sbb4a6351303,roleId=76337067"}'


# 一个链接能发三次 每次最多5链接
range_n = 6
range_sleep = 0.05 # 间隔时间
#elay_time = 0.6 #时间到后延迟600ms启动，可以根据网速更改



headers = {
        "Host": "api.m.jd.com",
        "cookie": ck,
        "charset": "UTF-8",
        "accept-encoding": "gzip,deflate",
        "user-agent": "okhttp/3.12.1;jdmall;android;version/11.0.2;build/96906;",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "content-length": "1574",
    }



def jdtime():
    #本地时间
    return int(time.time() * 1000)
    
if __name__ == '__main__':
    print('59-20抢券准备...')

    h = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")   +":00:00"
    print ("now time=",(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S") )
    print ("next hour=", h )

    #elif h in hour
    #mktime返回秒数时间戳，starttime为整点时间提前1.2秒
    starttime =int( time.mktime(time.strptime(h, "%Y-%m-%d %H:%M:%S")) * 1000) - 1200
    print("开始抢时间戳=",starttime)
    while True:
    if jdtime() >= starttime:
        res = requests.post(url=url1, headers=headers, data=body1).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        res = requests.post(url=url2, headers=headers, data=body2).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        res = requests.post(url=url1, headers=headers, data=body1).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        res = requests.post(url=url2, headers=headers, data=body2).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        res = requests.post(url=url1, headers=headers, data=body1).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        res = requests.post(url=url2, headers=headers, data=body2).json()
        print('请求时间：' + str(datetime.datetime.now()), res)
        time.sleep(range_sleep)
        break
    else:
        print('没到时间-现在为：' + jdtime())


