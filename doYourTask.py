import os,schedule,time,webbrowser,datetime,random
import subprocess
class DoTasks:
    def __init__(self,time,url):self.time=time;self.url=url
    def task(self):
        webbrowser.open(self.url,new=1,autoraise=True)
        webbrowser.get('Safari')
        schedule.every().day.at(self.time).do(self.task)
        while True:schedule.run_pending();time.sleep(1);return #returnでループ終了
doTasks0=DoTasks("00:00","https://任意のurl") #任意の時間, 任意のurl
doTasks1=DoTasks("00:00","https://任意のurl")
doTasks2=DoTasks("00:00","https://任意のurl")
def randNum():
    num=random.randrange(0,4) #乱数
    if num==0:doTasks0.task()
    elif num==1:doTasks1.task()
    elif num==2:doTasks2.task()
    elif num==3:doTasks2.task()
    else:pass
randNum()

#here is an example of crontab configuration
"""
0 9 * * * /Users/UserName/.venv/bin/python /Users/UserName/DirectoryName/doYourTask.py
"""
