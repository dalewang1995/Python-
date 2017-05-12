#-*-coding:utf8-*-
import  requests,sys,os,re,json
from bs4 import BeautifulSoup
class Spider:
    def __init__(self,stuname,stuid):
        self.url = 'http:www.xxx.com/xx.php'
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        self.s = requests.session()
        self.stuname = stuname
        self.content = ""
        self.stuid = stuid
        self.idict = {}
    def get_html(self):
        iparams = {'flag':1,'stuid':self.stuid,'stuname':self.stuname}
        iresponse = self.s.post(self.url,data=iparams,headers =self.header )
        self.content = iresponse.content

    def deal_html(self):
        #print self.content
        soup = BeautifulSoup(self.content,'html.parser')
        temp_list = soup.find_all("td")
        key_list = temp_list[0:11]+temp_list[22:33]
        value_list = temp_list[11:22]+temp_list[33:-1]
        for i in range(0,len(key_list)-1):
            ikey = key_list[i].string
            ivalue = value_list[i].string
            self.idict[ikey] =ivalue
        fl = open('111.txt', 'wb')
        for key in self.idict:
            print self.idict[key]
            b = json.dumps(self.idict[key])
            fl.write(b + '\n')
        fl.close()

    def main(self):
        self.get_html()
        self.deal_html()
if __name__ == '__main__':
    fl = open('data.txt', 'r')
    idata = fl.read()
    idata1 = idata.split(",")[0]
    idata2 = idata.split(",")[1]
    fl.close()
    stuname = r'姓名'
    #stuname = idata1
    #print stuname
    #stuid = idata2
    #print stuid
    stuid = '****9900'
    print stuname,stuid
    aa = Spider(stuname,stuid)
    aa.main()
