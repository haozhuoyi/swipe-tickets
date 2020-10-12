import urllib.request
import urllib.parse
from lxml import etree
import ssl
import time
import random
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    Reptiles()

def Reptiles():
    global IParray
    global PORTarray
    global HTTParray
    IParray = []
    PORTarray = []
    HTTParray = []
    for i in range(10):
        IPurl = 'https://www.kuaidaili.com/free/intr/' + str(i + 1) + "/"
        request = urllib.request.Request(IPurl,method='GET')
        response = urllib.request.urlopen(request)
        htmlResponse = response.read().decode('utf8')
        # print(htmlResponse)
        html = etree.HTML(htmlResponse)
        getIPInfo(html)
        time.sleep(random.randint(2,4))
        print(i)
    print(IParray)
    print(PORTarray)
    print(HTTParray)
    vote()
    
def getIPInfo(html):
    IPresult = html.xpath('//td[@data-title="IP"]/text()')
    PORTresult = html.xpath('//td[@data-title="PORT"]/text()')
    HTTPresult = html.xpath('//td[@data-title="类型"]/text()')
    IParray.extend(IPresult)
    PORTarray.extend(PORTresult)
    HTTParray.extend(HTTPresult)

def vote():
    for i in range(len(IParray)):

        time.sleep(random.uniform(2,4))
        try:
            # nullproxy_handler = urllib.request.ProxyHandler({'http':'119.108.188.81:9000'})
            handlerIP = {'http':IParray[i] + ':' + PORTarray[i]}
            print(handlerIP)
            proxy_handler = urllib.request.ProxyHandler({'http':IParray[i] + ':' + PORTarray[i]})
            # nullproxy_handler = urllib.request.ProxyHandler({})
            opener = urllib.request.build_opener(proxy_handler)
            header = {
                'Content-Length':'8',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                'Host':'abc.xgsuu.cn',
                'Origin':'http://abc.xgsuu.cn',
                'Content-Type':'application/x-www-form-urlencoded',
                'Referer':'http://abc.xgsuu.cn/WeChat.php?m=Xue&c=MusicVote&a=info&fengxue=393&id=777&iid=34686',
                'Connection':'keep-alive',
                'X-Requested-With':'XMLHttpRequest',
                'Accept':'application/json, text/javascript, */*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6'
            }

            content = {
                'id':'34686'
            }

            url = 'http://abc.xgsuu.cn/WeChat.php?m=Xue&c=MusicVote&a=vote&fengxue=393&id=777'
            data = bytes(urllib.parse.urlencode(content), encoding='utf8')
            request = urllib.request.Request(url, data = data, headers = header,method='POST')
            response = opener.open(request, timeout=120)
        except:
            print("出错了")
        else:
            print(response.read().decode("utf8"))

    Reptiles()

if __name__ == '__main__':
    main()