from datetime import datetime,timedelta
print("1周包含的总秒数：",timedelta(days=7).total_seconds())
d = datetime.now()
print("当前本地系统时间:",d)
print("1天后:",d + timedelta(days=1))
print("1天前:",d + timedelta(days=-1))
