﻿# cron "55 6,11,15 * * *" 
# new Env('PY极速【-3】')
import json
import math
import random
import threading
import time
import requests,os
import datetime


# 可以改的参数,当前参数15-5
args = 'key=00B0D3E7C6647F2DCBB27B83B407F64CE3B4DEFC1DA4E5A7E162A1F6BE48622224FDD1CB8ABD942923E6AD9A9ADDECB0_bingo,roleId=FDC4FE2CB6E8465BBB9D6363E08F77074127494A73563CF622D06B636ED63016F784DC6C22809244BB407156BA68832A94A000BBB29A02F8DFEE3F6F3AAEFAC35F2F40E295E2EFBBAFAC867171AA83A6D99B5D2E87FF1512E5A931CA9ACC0D4654790F5A47D7F67E28BBA5C811CDEF24C91ADB434A9ED554883A08F1BDEEB162C3DC6A81D998E0C3C415F6C5638C29FF2AF4550A13E2FC70FE2477828C92B40B_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42A4606A96C412625D97B008429129859D7_bingo'

#os.environ 获取环境变量
ck =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[ck[0],ck[1],ck[2]]
#print(mycookies)

starttime = 0  # 开始时间戳 13位 网址：https://tool.lu/timestamp/   5/8 5/7 23:59:58
delay_time = 0
range_n = 20  # 线程个数20
range_sleep = 0  # 间隔时间
tq = 1200   # 提前 于 整点的 时间，单位毫秒

# 没用的参数
log_list = []
atime = 0
title = '京东15-5抢券成功'
content = []



def get_log_list(num):
    global log_list
    try:
        for i in range(num):
            url = f'http://127.0.0.1:5889/log'
            res = requests.get(url=url).json()
            log_list.append(res)
    except:
        log_list = []
    return log_list


def randomString(e):
    t = "0123456789abcdef"
    a = len(t)
    n = ""
    for i in range(e):
        n = n + t[math.floor(random.random() * a)]
    return n


def Ua():
    UA = f'jdapp;iPhone;10.2.0;13.1.2;{randomString(40)};M/5.0;network/wifi;ADID/;model/iPhone8,1;addressid/2308460611;appBuild/167853;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;'
    return UA


def qiang_quan(cookie, i, index):
    url = 'https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        'origin': 'https://pro.m.jd.com',
        "Referer": "https://pro.m.jd.com/jdlite/active/3H885vA4sQj6ctYzzPVix4iiYN2P/index.html?lng=106.476617&lat=29.502674&sid=fbc43764317f538b90e0f9ab43c8285w&un_area=4_50952_106_0",
        "Cookie": cookie,
        "User-Agent": Ua()
    }

    body = json.dumps({"activityId": "vN4YuYXS1mPse7yeVPRq4TNvCMR",
                       "scene": "1",
                       "args": args,
                       "log": log_list[i]['log'],
                       "random": log_list[i]['random']}
                      )
    data = f"body={body}"
    try:
        res = requests.post(url=url, headers=headers, data=data).json()
        # print(res)
        if res['code'] == '0':
            print('请求时间：'+str(datetime.datetime.now()),f"账号{index + 1}：{res['subCodeMsg']}")
            if '成功' in res['subCodeMsg']:
                content.append(f"账号{cookie[90:-1]}：{res['subCodeMsg']}")
        else:
            print('请求时间：'+str(datetime.datetime.now()),f"账号{index + 1}：{res['errmsg']}")
    except:
        pass

'''

def jdtime():
    url = 'http://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5'
    headers = {
        "Cookie": cookie[9],"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    try:
        res = requests.get(url=url, headers=headers, timeout=1).json()
        return int(res['currentTime2'])
    except:
        return 0
'''

#获取系统时间：		
def getBdTime():
     #nt为现在时间，格式为 年月日时分秒
     nt = datetime.datetime.now()
     #ntdx为现在时间的 转换时间戳 的 对象，用于转换时间戳
     ntdx = nt.timetuple()
     #ntmc为现在时间的 秒时间戳
     ntmc = time.mktime(ntdx)
     #nthc为现在时间-毫秒时间戳  .microsecond属性返回给定Time对象2022-06-11 19:37:17.289437中的微秒值289437
     nthc = int(ntmc*1000 + nt.microsecond/1000)
     return(nthc)

def use_thread(cookie, index):
    tasks = list()
    for i in range(range_n):
        tasks.append(threading.Thread(target=qiang_quan, args=(cookie, index * 50 + i, index)))
    print(f'账号{index + 1}：等待抢券')
    while True:
        #jdtime>=starttime时启动
        if getBdTime() >= starttime:
            #starttime提前一秒，所以需要加上延迟
            time.sleep(delay_time)
            for task in tasks:
                task.start()
                time.sleep(range_sleep)
            for task in tasks:
                task.join()
            break

#下方为 主程序
if __name__ == '__main__':
    print('极速版抢券【2】...')
    print('时间间隔参数=',range_sleep)
    print('提前时间参数=',tq)
    h = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")   +":00:00"
    print ("now time=",(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S") )
    print ("next hour=", h )

    #elif h in hour
    #mktime返回秒数时间戳，starttime为整点时间提前tq秒,tq为提前时间
    starttime =int( time.mktime(time.strptime(h, "%Y-%m-%d %H:%M:%S")) * 1000) - tq
    print("开始抢时间戳=",starttime)
    while True:
        if starttime - getBdTime() <= 180000:
            break
        else:
            if getBdTime() - atime >= 30000:
                atime = getBdTime()
                print(f'等待获取log中，还差{int((starttime - getBdTime()) / 1000)}秒')
    get_log_list(len(mycookies) * 50)
    if len(log_list) != 0:
        print(f'{len(log_list)}条log获取完毕')
        threads = []
        for i in range(len(mycookies)):
            threads.append(
                threading.Thread(target=use_thread, args=(mycookies[i], i))
            )
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    else:
        print('暂无可用log')
