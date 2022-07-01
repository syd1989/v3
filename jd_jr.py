# cron "50 59 23 * * *" 
# new Env('PY京东金融抢券')
import json
import math
import random
import threading
import time
import requests,os
import datetime





#os.environ 获取环境变量
cookie =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[cookie[0],cookie[1],cookie[2],cookie[3],cookie[4],cookie[5],cookie[6],cookie[7],cookie[8],cookie[9],cookie[10],cookie[11]]
#print(mycookies)

ck = cookie[0]  #cookie格式： 只能放入一个cookie

starttime = 0 #需要精确到毫秒
range_n = 6
range_sleep = 3 # 间隔时间
#elay_time = 0.6 #时间到后延迟600ms启动，可以根据网速更改
atime=0
tq=1000   # 提前 于 整点的 时间，单位毫秒


#抓POST包获取URL,抓GET包获取body1，总览-第一行的URL点击进去，就是下发的内容。
url1 = 'https://jccamkt.jr.jd.com/mkt/m/activity/award/v2/receiveAward'

body1 = '{"cardId":92,"activityId":"202206296947817178245414912","activityType":29,"channelCode":"ICON2"}'


#抓POST包的headers

headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        'origin': 'https://jcca.jd.com/',
        "Referer": "https://jcca.jd.com/",
        "Cookie": ck,
        "User-Agent": "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

def jdtime():
    #本地时间
    return int(time.time() * 1000)
    
if __name__ == '__main__':
    print('金融-抢券准备...')
    print('时间间隔参数=',range_sleep)
    print('提前时间参数=',tq)
    h = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")   +":00:00"
    print ("now time=",(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S") )
    print ("next hour=", h )

    #elif h in hour
    #mktime返回秒数时间戳，starttime为整点时间提前1.2秒
    starttime =int( time.mktime(time.strptime(h, "%Y-%m-%d %H:%M:%S")) * 1000) - tq
    print("开始抢时间戳=",starttime)

    while True:
        if jdtime() >= starttime:
            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)
            
            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)
            
            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)

            res = requests.post(url=url1, headers=headers, data=body1).json()
            print('请求时间：' + str(datetime.datetime.now()), res)
            time.sleep(range_sleep)
            
            break
        else:
            if int(time.time() * 1000) - atime >= 5000:
                 atime = int(time.time() * 1000)
                 print(f'等待中，还差{int((starttime - int(time.time() * 1000)) / 1000)}秒开始抢券')
   



