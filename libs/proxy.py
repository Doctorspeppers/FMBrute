import requests
import bs4
from random import randrange
"""
@req array [{"url":[{"GET":{"param1":"data2","param2":"data2"}},{'user-agent': 'my-app/0.0.1'}]},
{"url2":[{"GET":{"param1":"data2","param2":"data2"}},{'user-agent': 'my-app/0.0.1'}]},
{"url3":[{"GET":{"param1":"data2","param2":"data2"}},{'user-agent': 'my-app/0.0.1'}]}]


"""
class proxy:
    def __init__(self,req=None,encoding="utf8",proxyAut=True):
        self.ordenedList = []
        self.proxyAut = proxyAut
        self.encoding = encoding
        self.req = req
        self.reqContent = []

    def getProxyList(self):
        r = requests.get("https://free-proxy-list.net/anonymous-proxy.html")
        html = bs4.BeautifulSoup(r.content, "html5lib")
        rows = html.find_all('tbody')
        rows = html.find_all('tr')
        rows_names = rows.pop(0)
        rows_names = [x.contents for x in rows_names.find_all("th")]
        rows = [x.find_all("td") for x in rows]
        content = []
        for row in rows:
            content.append([z.contents for z in row])
        for row in content:
            listing = {}
            size = len(row)
            if size == len(rows_names):
                for x,y in zip(rows_names,row):
                    if len(x) == len(y):
                        listing[x[0]] = y[0]
                self.ordenedList.append(listing)


    def doRequests(self):
        for especificRequistion in self.req:
            for url,params in especificRequistion.items():
                arrayParams = params[0]
                headers = params[1]
                Nrandom = randrange(0, len(self.ordenedList))
                if self.ordenedList[Nrandom]["Https"] == "no":
                    proxy = {"http":self.ordenedList[Nrandom]["IP Address"]+":"+self.ordenedList[Nrandom]["Port"]}
                else:
                    proxy = {"https":self.ordenedList[Nrandom]["IP Address"]+":"+self.ordenedList[Nrandom]["Port"]}
                for requestType,val in arrayParams.items():
                    print(requestType)
                    if requestType == "GET":
                        print(requestType)
                        thisrequest = requests.post(url=url,headers=headers,params=val, proxies=proxy)
                    elif requestType == "POST":
                        thisrequest = requests.post(url=url, headers=headers,data=val, proxies=proxy)
                    elif requestType == "PUT":
                        thisrequest = requests.put(url=url, headers=headers,data=val,proxies=proxy)
                    elif requestType == "DELETE":
                        thisrequest = requests.delete(url=url,headers=headers,data=val, proxies=proxy)
                    elif requestType == "HEAD":
                        thisrequest = requests.head(url=url,headers=headers,data=val, proxies=proxy)
                    elif requestType == "OPTIONS":
                        thisrequest = requests.options(url=url,headers=headers,data=val, proxies=proxy)
                    thisrequest.encoding = self.encoding
                    self.reqContent.append(thisrequest)


# test = [{"https://www.infoescola.com":[{"GET":{"":""}},{}]}]
# classse = proxy(test)
# classse.getProxyList()
# classse.doRequests()
# print(classse.reqContent[0].content)
####JUST A EXAMPLE

    
