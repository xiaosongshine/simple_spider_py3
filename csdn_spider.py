import requests        #导入requests包
from bs4 import BeautifulSoup
read_all = 0
for i in range(7):
 
    url = 'https://blog.csdn.net/xiaosongshine/article/list/%d'%(i+1)
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    data = soup.select('#articleMeList-blog > div.article-list > div > div.info-box.d-flex.align-content-center > p > span:nth-child(2)')
    ##Paging_04204215338304449 > ul > li.ui-pager
    for d in data:
        #print(d,d.text,type(d.text))
        read_all += eval(d.text)
 
print(read_all)