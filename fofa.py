import requests,os

import time
import urllib
import base64
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}

def loadpage(email,key,targetsrting,end):
    ip_list = []
    #end = end +100
    #url_reg  = r'(https|http)?://'    
    for page in range(1,end+1):
        print("正在爬取第"+str(page)+"页：")       
        target=base64.b64encode(targetsrting.encode('utf-8')).decode("utf-8")
        #page="2" #翻页数
        size="1000" #每页返回记录数
        url="https://fofa.info/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+target+"&size="+size+"&page="+str(page)
        print(url)
        resp = requests.get(url)
        data_model = json.loads(resp.text)
        print(data_model)
        data_url=[]
        save=open('ip.txt','a+')
        for i in data_model['results']: #取结果列表
            for j in i[0:1]: #取结果列表中的每个列表的url,需要IP则改为[1:2]
                data_url.append(j)

        for i in data_url:
            save.write(i+"\n")
            print (i)
        save.close()

if __name__ == '__main__':
    os.system('del ip.txt')
    email="xxx@qq.com" #email
    key="xxx" #key
    email='xx@qq.com'
    key='xxx'
    targetsrting='region="TW"' #搜索关键字
    end = 100
    loadpage(email,key,targetsrting,end)  
    #time.sleep(1)