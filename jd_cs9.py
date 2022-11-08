# cron "15 22 * * *" 
# new Env('PY超市券【全号-9券】')
import json
import math
import random
import threading
import time
import requests,os
import datetime

'''
#6月份KEY：
strengthenKey=B4CF90C71C84A203BD4F00A15A0D8EAB10847656370FB2FEA1F3FCE7E1A6F5CDA06C546612109C7525FADDFA012CDC51_bingo

'''

# 可以改的参数,当前参数15-5
args = 'key=473795C2E14A1F53F42B960A67F3E8C938C1F7B97EFC15808279AFB465F1D68A90D316BF3BDA376F716E773DAE7DBCBE_bingo,roleId=EB2D3DAD6C641DF34429B09F2E77E3D0261CF72A7F7518F5B5C850986A896E6419DD01861300BFC790EEDF8B9288908B86E4A03B02EB061F7534E0EFD5E23FADEF4F7388DF03B23E09A863386D4D8968D7FBFC29332F1AC5F73096D8D6F54021094F09D66CEE0C189C891029711D190130C0C02416697CD77F7C75C2D5154ECDA440FEA7501861D4EB8DEC55A46F3E370289549D9447A4E76C673C57FFBE6B60D5CB0A69DFEE7817E5818903327E2AD3_bingo,strengthenKey=36BDFAB8CB845823CA5CA7A772AEF9FB93AE2C2D454D5D8552BA5B8D4767277ABB6460D91B320C51D531FD9FCB4E0A3E_bingo'

#os.environ 获取环境变量
ck =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[ck[0],ck[1],ck[2],ck[3],ck[4],ck[5],ck[6],ck[7],ck[8],ck[9],ck[10],ck[11]]
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

    body = json.dumps({"activityId": "oTtXBgN2Toq1KfdLXUKKivNKVgA",
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
        tasks.append(threading.Thread(target=qiang_quan, args=(cookie, index * 20 + i, index)))
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
    print('立刻抢券【log获取+加载账号中】...')
    
    
    get_log_list(len(mycookies) * 20)
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
