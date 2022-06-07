import requests,base64,json,os,time
from time import sleep
from multiprocessing import Pool, Manager


def forin():
    global list0
    page=1000
    b=0
    for i in range(10):
        headers = {
            "X-QuakeToken": "xxx"
        }

        data = {
            "query": "port:1080 And service: socks5 AND not response: username",
            "start": page*i,
            "size": page
        }

        response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        '''
        save=open('123.json','a+',encoding='utf-8')
        save.write(str(response.json()))
        save.close()
        '''
        s=response.json()
        #print(page*i,page)
        try:
            for a in range(len(s['data'])):
                b+=1
                print(b,s['data'][a]['ip'],s['data'][a]['port'])
                list0.append(s['data'][a]['ip'])
                list0.append(s['data'][a]['port'])
        except:
            print(s['data'][1])
            pass
    
def test_ip(ip,port):
    try:
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'} 
        proxy = {
            'http': 'socks5://'+ip+':'+port,
            'https': 'socks5://'+ip+':'+port
            }
        url = "http://www.baidu.com/"
        temp = time.time();
        req = requests.get(url, proxies=proxy,timeout=5)
        temp1 = time.time();
        if req.status_code == 200 and len(req.text) > 200 and 'baidu' in req.text:
            #print(req.text)
            str0=ip+':'+port+(25-len(ip+':'+port))*' '+str(temp1-temp)+'\n'
            print (str0,end='')
            save=open('p.txt','a+')
            save.write(str0)
            save.close()
            
    except:
        pass

def test_ip1(ip,port):
    try:
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'} 
        proxy = {
            'http': 'socks5://'+ip+':'+port,
            'https': 'socks5://'+ip+':'+port
            }
        url = "http://www.baidu.com/"
        temp = time.time();
        req = requests.get(url, proxies=proxy,timeout=5)
        temp1 = time.time();
        #print(req.text)
        if req.status_code == 200 and len(req.text) > 200 and 'baidu' in req.text:
            str0=ip+':'+port+(25-len(ip+':'+port))*' '+str(temp1-temp)+'\n'
            print (str0,end='')
            save=open('p.txt','a+')
            save.write(str0)
            save.close()
    except:
        pass


if __name__ == "__main__":
    while 1:
        
        try:
            list0=[]
            forin()
            print('run0 done!')
            p = Pool(60)
            for i in range(int(len(list0)/2)):
                p.apply_async(test_ip,args=(list0[2*i],str(list0[2*i+1])))
            p.close()
            p.join()

            os.system('del p.txt')

            print('run1 done!')
            p = Pool(60)
            for i in range(int(len(list0)/2)):
                p.apply_async(test_ip1,args=(list0[2*i],str(list0[2*i+1])))
            p.close()
            p.join()

            os.system('del p.txt')
            time.sleep(30*60)
        except:
            pass
    
    







