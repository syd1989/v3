# cron "55 6 * * *" 
# new Env('PY-京东锦鲤')

# -*- coding: UTF-8 -*-
import json
import math
import random
import re
import time
# pip3 install requests
import requests

starttime = 1652351341000

#os.environ 获取环境变量
cookie =os.environ["JD_COOKIE"].split('&')
#split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
mycookies=[cookie[0],cookie[1],cookie[2],cookie[3],cookie[4],cookie[5],cookie[6],cookie[7],cookie[8],cookie[9],cookie[10],cookie[11]]
#print(mycookies)

cookies = [cookie[0],cookie[1],cookie[2],cookie[3],cookie[4],cookie[5],cookie[6],cookie[7],cookie[8],cookie[9],cookie[10],cookie[11]]
#print(mycookies)


#辅助参数
atime = 0
tag = 0
log_list = []


# 本地
def get_log_list1(num):
    global log_list
    try:
        for i in range(num):
            url = f'http://192.168.6.105:5889/log'
            res = requests.get(url=url).json()
            log_list.append(res)
    except:
        log_list = []
    return log_list

# 远程
def get_log_list(num):
    global log_list
    url = f'http://110.40.128.21:1998/newlog?func=jinli&num={num}'
    token = ''

    headers = {
        'Authorization': 'Bearer ' + token
    }
    res = requests.get(url=url,headers=headers).json()
    if res['code'] == '0':
        log_list = res['alog']
    else:
        print(res['msg'])
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
    UA = f'jdltapp;iPhone;3.1.0;{math.ceil(random.random() * 4 + 10)}.{math.ceil(random.random() * 4)};{randomString(40)}'

    return UA


def res_post(functionId, cookie, body, ua):
    url = f'https://api.m.jd.com/client.action/api?appid=jinlihongbao&functionId={functionId}&loginType=2&client=jinlihongbao&clientVersion=10.1.4&osVersion=-1'
    headers = {
        "Cookie": cookie,
        "origin": "https://h5.m.jd.com",
        "referer": "https://h5.m.jd.com/babelDiy/Zeus/2NUvze9e1uWf4amBhe1AV6ynmSuH/index.html",
        'Content-Type': 'application/x-www-form-urlencoded',
        "X-Requested-With": "com.jingdong.app.mall",
        "User-Agent": ua
    }
    data = f"body={json.dumps(body)}"
    try:
        res = requests.post(url=url, headers=headers, data=data).json()
        return res
    except:
        return -1


def launch_id(mycookie):
    user = log_list[random.randint(0, len(log_list) - 1)]
    body = {"followShop": 1,
            "random": user["random"],
            "log": user["log"],
            "sceneid": "JLHBhPageh5"
            }
    res = res_post('h5launch', mycookie, body, Ua())
    # print(res)
    if res != -1:
        if res['rtn_code'] == 403:
            print('h5launch,log失效，获取redPacketId失败')
            return -1
        elif res['rtn_code'] == 0:
            if res['data']['result']['status'] == 1:
                print('号黑了，锦鲤活动打不开了')
                return -1
            elif res['data']['result']['status'] == 2:
                redPacketId = get_id(mycookie)
                if redPacketId != -1 and redPacketId != 1:
                    return redPacketId
                else:
                    return -1
            else:
                redPacketId = res['data']['result']['redPacketId']
                return redPacketId
    else:
        print("h5launch,请求失败，获取redPacketId失败")
        return -1


def get_id(mycookie):
    res = res_post('h5activityIndex', mycookie, {"isjdapp": 1}, Ua())
    if res != -1:
        if res['rtn_code'] == 0:
            if res['data']['biz_code'] == 20002:
                print("已达拆红包数量限制")
                return 1
            else:
                redPacketId = res['data']['result']['redpacketInfo']['id']
                return redPacketId
        else:
            print('锦鲤活动未开启')
            return -1
    else:
        print("锦鲤活动未开启")
        return -1


def help1(redPacketId, pin):
    global tag
    for i in range(tag, len(cookies)):
        user = log_list[i]
        body = {"redPacketId": redPacketId, "followShop": 0,
                "random": user["random"],
                "log": user["log"],
                "sceneid": "JLHBhPageh5"
                }
        res = res_post('jinli_h5assist', cookies[i], body, Ua())
        # print(res)
        if res != -1:
            if res['rtn_code'] == 0:
                desc = res['data']['result']['statusDesc']
                print(f'账号{i}助力{pin}：{desc}')
                if 'TA的助力已满' in desc:
                    tag = i
                    return
            elif res['rtn_code'] == 403:
                print(f'账号{i}助力{pin}：助力失败，log失效')
    tag = len(cookies)


def reward(mycookie):
    sum = 0
    while True:
        user = log_list[random.randint(0, len(log_list) - 1)]
        body = {
            "random": user["random"],
            "log": user["log"],
            "sceneid": "JLHBhPageh5"
        }
        res = res_post('h5receiveRedpacketAll', mycookie, body, Ua())
        # print(res)
        if res != -1:
            if res['rtn_code'] == 0 and res['data']['biz_code'] == 0:
                print(f"{res['data']['biz_msg']}：{res['data']['result']['discount']}元")
                sum = sum + float(res['data']['result']['discount'])
                time.sleep(1)
            elif res['rtn_code'] == 0 and res['data']['biz_code'] == 10:
                print(res['data']['biz_msg'])
                break
            elif res['rtn_code'] == 403:
                print(f'reward, log失效')
                break
        else:
            continue
    print(f'共获得{sum}元红包')



if __name__ == '__main__':
    print('锦鲤准备...')
    while True:
        if starttime - int(time.time() * 1000) <= 120000:
            break
        else:
            if int(time.time() * 1000) - atime >= 30000:
                atime = int(time.time() * 1000)
                print(f'等待获取log中，还差{int((starttime - int(time.time() * 1000)) / 1000)}秒')

    get_log_list(200)
    if len(log_list) != 0:
        print(f'{len(log_list)}条log获取完毕')
        while True:
            if int(time.time() * 1000) >= starttime:
                for mycookie in mycookies:
                    redPacketId = launch_id(mycookie)
                    if redPacketId != -1:
                        ex = 'pt_pin=(.*);'
                        try:
                            pin = re.findall(ex, mycookie)[0]
                        except:
                            pin = ''
                        print(f"redPacketId：{redPacketId}")
                        help1(redPacketId, pin)

                for mycookie in mycookies:
                    reward(mycookie)
                break
    else:
        print('暂无可用log')
