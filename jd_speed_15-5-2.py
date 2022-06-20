# cron "55 9,23 * * *" 
# new Env('PY极速卷15-5【2】')
import json
import math
import random
import threading
import time
import requests,os
import datetime

'''
#6月份KEY：

15-8 9,12,15,18,20
key=4C884367B622BB96ABD488103A5036F58B08100D4FEC967D97AA8854BC13AF4A50BE6F7B01529B9D56C52BEAB5EB5235_bingo,roleId=A921D0996A757D3D319487D17C0F25FE701307BE103D49F3D1562C7CF5D02F01F1043E437093D585B4730F630A66804F8AE429E9F2C40EE1F0580E482F388FEEF1F5A8A69753844555247364707E6E4159B29F3B419232040DE833D72925C80DF4315110A89299BBDAD305FC4D076A4D3DEDB438E19F7666BC135BFA5F266A42CE68623409ECB244532F4759F91B1AF05DEC49D77AE2E3F11EF07B9FC34F28511CD96B79AF1B4DC318DDFE29F10300B7_bingo,strengthenKey=B4CF90C71C84A203BD4F00A15A0D8EAB10847656370FB2FEA1F3FCE7E1A6F5CD89938B67BAED10AA94C72D5E8D031F0F_bingo

15-5  0 10 15 20
key=6E3ED4217CA5BA50CC868072587749279A819E91EC8217F49BC1DB9DC674DA27CF93291755C086262CF2BD2DADDD8138_bingo,roleId=A921D0996A757D3D319487D17C0F25FE0F6830D8485A69E35623B13BFBA59D1E7C2386D90F3D9D3A6D752ADCDEAB0529AA56BDE4467494DC5590AEB5C7C950D03EA337E197D9AF250FA7148376C8A9C2C7826A579EE8919B7B4F046F31A7F33771D69424BE2E31C4957568BC1183F08BD273D933A8092885B34900DD5088BE7BFAF8E88961C07BC6043362DEC0C9D912631C8651646624A0999D730E5CE836A91CC6E9E6E8434EE599FDF702E4461DC9_bingo,strengthenKey=B4CF90C71C84A203BD4F00A15A0D8EAB10847656370FB2FEA1F3FCE7E1A6F5CD010641A17BFFC13415D635F046619797_bingo

10-2  0 10 15 20
key=DF6500A60EBB047C1539292254D320D7E80F9297D19486370D6A0DD220E76A1CD91818B1BCEE491D10789D7765041113_bingo,roleId=A921D0996A757D3D319487D17C0F25FE01264B7B8DA4DBEF981EF390D1DC02E92308FBC1CF805C8B6550E0A1EED8671F5360D7210975255E5A17758A1D4815AB567D73B11DD737D321A8D6DAD3B6E47D59B713C5E6E22952565B387B52C6F791F414C5F814BD7A7E4CB08DFDC6E570FDEF6BE818DCC8CC7AE3C28B33AD315729E6E7BC4929591B8BC0D237B68DC09679FDA9AF263E3F1BDDF1A2D1470204BBF7FB7E95EEE2B0704726BF4B12A286159D_bingo,strengthenKey=B4CF90C71C84A203BD4F00A15A0D8EAB10847656370FB2FEA1F3FCE7E1A6F5CDA06C546612109C7525FADDFA012CDC51_bingo

'''

# 可以改的参数,当前参数15-5
args = 'key=6E3ED4217CA5BA50CC868072587749279A819E91EC8217F49BC1DB9DC674DA27CF93291755C086262CF2BD2DADDD8138_bingo,roleId=A921D0996A757D3D319487D17C0F25FE0F6830D8485A69E35623B13BFBA59D1E7C2386D90F3D9D3A6D752ADCDEAB0529AA56BDE4467494DC5590AEB5C7C950D03EA337E197D9AF250FA7148376C8A9C2C7826A579EE8919B7B4F046F31A7F33771D69424BE2E31C4957568BC1183F08BD273D933A8092885B34900DD5088BE7BFAF8E88961C07BC6043362DEC0C9D912631C8651646624A0999D730E5CE836A91CC6E9E6E8434EE599FDF702E4461DC9_bingo,strengthenKey=B4CF90C71C84A203BD4F00A15A0D8EAB10847656370FB2FEA1F3FCE7E1A6F5CD010641A17BFFC13415D635F046619797_bingo'

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
            url = f'http://192.168.5.238:5889/log'
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
    print('极速版抢券【1】...')
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
