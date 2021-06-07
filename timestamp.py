import os,time
from datetime import datetime

def changed_time(out_file):
    now = datetime.now()
    year,month,day = int(now.strftime("%Y")),int(now.strftime("%m")),int(now.strftime("%d"))
    hour,minute,second = int(now.strftime("%H")),int(now.strftime("%M")),int(now.strftime("%S"))
    date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    modTime = time.mktime(date.timetuple())

    os.utime(out_file,(modTime,modTime))
