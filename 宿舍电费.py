#date  2021-11-8
#copyright@ 紫薇斋609

import requests
import re
from datetime import date, timedelta

url = "http://192.168.84.3:9090/cgcSims/selectList.do"
yesterday = (date.today()+timedelta(days=-1)).strftime("%Y-%m-%d")
today = date.today().strftime("%Y-%m-%d")
#roomId需要自己去   http://192.168.84.3:9090/cgcSims  查一遍自己宿舍的roomId roomName
data = {"beginTime":yesterday,"client":"192.168.84.87","endTime":today,"roomId": "19414","roomName": "609+++++++++++++++++","type":"2"}


def getData(string):
	res= re.search(r"\t\d+.*\r",string)
	data = re.search(r"[\d\.]+",res.group())
	return data.group()

if __name__ == "__main__":
        r = requests.post(url,data)
        start = re.search("日期",r.text)
        ans = re.findall(r"<td[\s\S]*?/td>",r.text[start.end():-1])
        room = getData(ans[1])  #宿舍
        remainPower = getData(ans[2])  #剩余电量
        totaluse = getData(ans[3])   #总用电量
        totalPur = getData(ans[4])   #总购电量
        print("宿舍：",room)
        print("剩余电量：",remainPower)
        print("总用电量：",totaluse)
        print("总购电量：",totalPur)
        input()
        

        
        
        
        
        
