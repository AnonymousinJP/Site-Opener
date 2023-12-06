import os,schedule,time,webbrowser,datetime
import subprocess

timeVal="16:35"
url="https://XXXXXXXXXXXX.jp"

def task():
    webbrowser.open(url,new=1,autoraise=True)
    webbrowser.get('Safari')
schedule.every().day.at(timeVal).do(task)
while True:
    schedule.run_pending()
    time.sleep(1)

#example of crontab configuration
"""
0 9 * * * /Users/UserName/.venv/bin/python /Users/UserName/DirectoryName/doYourTask.py
# echo
"""
