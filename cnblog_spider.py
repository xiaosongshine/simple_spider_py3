import requests        #导入requests包
from bs4 import BeautifulSoup
 
 
url = "https://www.cnblogs.com/xiaosongshine/default.html?page=2"
#页面为第一页时，无法显示总页数，所以选择访问第二页
 
htxt = requests.get(url)
 
soup=BeautifulSoup(htxt.text,'lxml')
 
data = soup.select("#homepage_top_pager > div > a")
 
for d in data:
    print(d)
 
MN = len(data)-2
#减去前一页与后一页标签
read_all = 0
for i in range(MN):
    url = "https://www.cnblogs.com/xiaosongshine/default.html?page=%d"%(i+1)
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    data = soup.select('#mainContent > div > div > div.postDesc > span.post-view-count')
 
    for d in data:
        #print(d,d.text[3:-1],type(d.text))
        read_all += eval(d.text[3:-1])
 
print(read_all)