
# cron "55 9,21 * * *" 
# const $ = new Env('抢极速版全品卷15-5')
import json
import math
import random
import threading
import time
import requests,os
import datetime

'''
#9.9秒杀
10-2 7/10/16/20
key=99E9BFB397BB9E081C3D211644F4D63B80C6629BF10290DBE13C6C11E1DF025FE3774FB37875ED1B720ABB1A6023D3B4_bingo,roleId=3FE9EECAAA41B666E4FFAF79F20E21129412DAD4469A00C14E234FFC59430A3B03E9CF1047D2889AA3D9F3A3AC9845F06DD6177A62EF3A4A570EC8E5C227CE0E4892C7A1A2B984AB9B022706661B4828BA6ED364141E21A7499FE93EB659B4824F445AC4EAB78AF162CA2B7289EDF2DB3F8144DBC4D261FB9826BF7F88790CF94A2ADC829BEE300EB9E27DAD459EA19FE22F265CEE7EE1E0E926357D049A9C9A01413BFC73541208CCC10919AE1DD223_bingo,strengthenKey=4C8818C1732D1A7B9733D611F28BD8B57923ADE220C9B60370F65B533E02E0F8F7A8DB4211A7817EF606DDAD4FA3E67F_bingo
19-5 0/10/18/22
key=E72F2D6FD3B257AE6EAEEF81FEF44D9C3EFB9B5E0F0E11C4562D68BDA7BA69BF5C4E716FB9BBD7B1678E83551EA3A72E_bingo,roleId=3FE9EECAAA41B666E4FFAF79F20E21120520F1A5AFE5C9E8D77BD263F6726B9E3576C6C5571777201DA90CF204F2336AB211D7BA6D0E7255BAFF71BCC9ED7782F4BB5E97DDCA47183788BB228E79E0C34E78DF222617DBB46340CDD576D690369CEEB51EF2CC0DA24F159511AE4AD2EEF70B78A6287ED7D00634575733C0075CBA0ADD06A277A0DF84645DB74FF0C01DCED7EA5DCB5577E762C4029AD5172CE71951D9E209BD08E2DA0A722CF6411B58_bingo,strengthenKey=4C8818C1732D1A7B9733D611F28BD8B57923ADE220C9B60370F65B533E02E0F8E6A0FEFA632101D3D5409FE4F92580CF_bingo
#夏香节
5-2 9/12/18/22
key=BCE52145EC2FBDDE212899674C8CA1C12A3A133EEA5D70CB9D998AF6B3F4648C22AC20BFEB2B797D1292322C150A0DC2_bingo,roleId=3FE9EECAAA41B666E4FFAF79F20E211241BC51D1C03478640D4EF32FA22832B7C93468B462C8C368D7E33CA18F54891E8F724E3FA38C39E3AFF697601E6A963307103764559652634BA6CCE6381F1828DFFEA73CB1112D3B93F9141F71E772892890D12BAB366ADD8CB74520EFA0FDB0B46FCC528187867EF0EAB793451D2FFE1C4D4F8720CBC88786C9BFFE59122E55363C69842BD1673DD4A73213F87E6D0D714352B5F3FE5B0BCF0235EB9CB43C5C_bingo,strengthenKey=4C8818C1732D1A7B9733D611F28BD8B57923ADE220C9B60370F65B533E02E0F82F810FA48DCD7A31F76CAE44623F2470_bingo
15-8 9/12/15/18/20
key=DDF1B71D0AF91A8547973CE5362A890F18C8E73AAC10BA9179CE5D2D745E95AC9AC125029761397270C947AC9F5E11CE_bingo,roleId=3FE9EECAAA41B666E4FFAF79F20E2112EC5A32B22271AD04523B3C66AE5807591E0DB913F0F40F86F97AAA49D12C568D47FEEE50418AD25C6B23D81C476A40CB07BCCE74C4EDAD2E0D1BCF515F06DECE783A16EA99A0959CAC63BDF9BD9A9037450AB25EE84616EF9E65486A529F6690F93EA6903FF6754FD22FD39B43821B0041487D3996E0CF72C487DD107C4D0F13EA507700B35B495859747F1E700186EA385A46F6ED361FE40B11663D21263EB1_bingo,strengthenKey=4C8818C1732D1A7B9733D611F28BD8B57923ADE220C9B60370F65B533E02E0F823A5E9624E2105020B0FB67EE3BFC671_bingo
19-5 0/10/18/20
key=CB80DDB21929DB2DB9849A60F929CCB99B3BF927A75E71562ADB7CEC61846545338F6E4517C1973762A51B43E2C88518_bingo,roleId=3FE9EECAAA41B666E4FFAF79F20E21120520F1A5AFE5C9E8D77BD263F6726B9E5E06C7051840093D00E358BF32A400ED69C31825CC6E0B4002396D97E04CBE9B95BD50D3490D09DC4746C78A5C257455D11BB1F359F00BC8367524EC3D44EDDA221AD90D25402C0AED4BCE9EFBC506428188DEBB9A3B93AA72D7CF3C822077B7D4A2456215E02A8A3DA720FF426525BC40D44921C13A1FE2CDFEDBB98CF065955FEED95F578D1A7D0C8ED8051EBD5E53_bingo,strengthenKey=4C8818C1732D1A7B9733D611F28BD8B57923ADE220C9B60370F65B533E02E0F8E6A0FEFA632101D3D5409FE4F92580CF_bingo
'''

# 可以改的参数,当前参数19-5
args = 'key=751709DD793408174D56C44D3BFC3C434680AB42380C39D573683566316F1F090B3C468368A1FA0640C15E1A2A6BB25A_bingo%2CroleId%3D3FE9EECAAA41B666E4FFAF79F20E21122587E42E9489C92604E9B1CD426BF61F9DA8FF4F6F381F7CE14913B40C4A4E49DBD8A0F39C4428871CEA2BFB7AC136DBBC79AE321F4D5D092EFE0978EEEDB540EEE7D12BB491ECBE8EED47E3A2038461275DC7CE64BA016EE4FED74741BE686315495C99C4E9322C8F1B1AFD867E3599767D7054A4E0FC481F922E410D2C20FC568C5C67F6E2232124870EEC42166F6B_bingo%2CstrengthenKey%3D19F512DCD8EE34ABE9C4FB4A92C2F42A83880C27EA00E5A7DF564D095F19F994_bingo'


mycookies = ["",]


starttime = 1653094799000 
delay_time = 0.2
range_n = 20  # 线程个数20
range_sleep = 0.2  # 间隔时间

# 没用的参数
log_list = []
atime = 0
PUSH_PLUS_TOKEN = ''
title = '京东15-8抢券成功'
content = []

if "PUSH_PLUS_TOKEN" in os.environ and len(os.environ["PUSH_PLUS_TOKEN"]) > 1:
    PUSH_PLUS_TOKEN = os.environ["PUSH_PLUS_TOKEN"]


def get_log_list(num):
    global log_list
    try:
        for i in range(num):
            url = f'http://192.168.6.105:5889/log'
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
            print(f"账号{index + 1}：{res['subCodeMsg']}")
            if '成功' in res['subCodeMsg']:
                content.append(f"账号{cookie[90:-1]}：{res['subCodeMsg']}")
        else:
            print(f"账号{index + 1}：{res['errmsg']}")
    except:
        pass


def jdtime():
    url = 'http://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    try:
        res = requests.get(url=url, headers=headers, timeout=1).json()
        return int(res['currentTime2'])
    except:
        return 0


def use_thread(cookie, index):
    tasks = list()
    for i in range(range_n):
        tasks.append(threading.Thread(target=qiang_quan, args=(cookie, index * 50 + i, index)))
    print(f'账号{index + 1}：等待抢券')
    while True:
        #jdtime>=starttime时启动
        if jdtime() >= starttime:
            #starttime提前一秒，所以需要加上延迟
            time.sleep(delay_time)
            for task in tasks:
                task.start()
                time.sleep(range_sleep)
            for task in tasks:
                task.join()
            break

# push推送
def push_plus_bot(title, content):
    try:
        print("\n")
        if not PUSH_PLUS_TOKEN:
            print("PUSHPLUS服务的token未设置!!\n取消推送")
            return
        print("PUSHPLUS服务启动")
        url = 'http://pushplus.plus/send'
        data = {
            "token": PUSH_PLUS_TOKEN,
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=body, headers=headers).json()
        if response['code'] == 200:
            print('推送成功！')
        else:
            print('推送失败！')
            print(response)

    except Exception as e:
        print(e)




if __name__ == '__main__':
    print('极速版抢券准备...')

    h = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")   +":00:00"
    print ("now time=",(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S") )
    print ("下一个整点是：", h )
    #mktime返回秒数时间戳
    starttime =int( time.mktime(time.strptime(h, "%Y-%m-%d %H:%M:%S")) * 1000) - 1000
    print("time stamp=",starttime)        
    while True:
        if starttime - int(time.time() * 1000) <= 180000:
            break
        else:
            if int(time.time() * 1000) - atime >= 30000:
                atime = int(time.time() * 1000)
                print(f'等待获取log中，还差{int((starttime - int(time.time() * 1000)) / 1000)}秒')
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

    #发送通知
    if '成功' in content:
        push_plus_bot(title, content)
    else:
        print('抢券失败')
