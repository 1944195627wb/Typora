import requests
import os
import json
import time
# 自动登录
file = r'd:\data.json'
def getInfo():
    print("请输入账号")
    accoutant = input()
    print("请输入密码")
    password = input()
    print("请输入运营商（1表示移动，2表示电信，3表示联通）")
    server = input()
    return accoutant,password,server

def connect():
    with open(file,'r') as f:
        data = json.load(f)
    f.close()
    url = "http://10.255.0.19/drcom/login"
    params={'callback':'dr1003','DDDDD':data['DDDDD'],'upass':data['upass'],'0MKKey':'123456'}
    res = requests.get(url,params=params)
    if res.status_code==200 :
        time.sleep(2)
        print("登陆成功")
    else:
        time.sleep(2)
        print("登陆失败")



if not os.path.exists(file):
    accoutant,password,server = getInfo()
    regex={'1':'cmcc','2':'aust','3':'unicom'}
    data={
       'DDDDD': accoutant+'@'+regex[server],
       'upass': password
    }
    with open(file,'w') as f:
       json.dump(data,f)
    f.close()
    connect()
else:
    connect()
    

