# swipe-tickets
2020年中国好声音杭州海选刷票，自己记录用

## IP代理（基于kuaidaili）
### 爬虫获取免费IP

``` bash
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
    
## vote方法需改写
