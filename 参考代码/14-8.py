import time,threadpool,socket

#扫描端口函数.
def scan_port(portList):
  global remote_host_ip
  try:
    soc = socket.socket(2,1)
    res = soc.connect_ex((remote_host_ip,portList))
    if res == 0:
      print('Port %s: OPEN'%portList)
      soc.close()
  except Exception as e:
    print("扫描端口异常:",e)

if __name__ == '__main__':
  remote_host = input("请输入远程主机域名: ")     	#需要进行端口扫描主机域名.
  remote_host_ip = ""
  try:
    remote_host_ip = socket.gethostbyname(remote_host)
    print('正在扫描远程主机 %s，请等候.' % remote_host_ip)
  except Exception as e:
    print("连接远程主机异常:%s."%repr(e))
  socket.setdefaulttimeout(1)    	#超时时间(秒).
  portList = []
  for i in range(0,1024):
    portList.append(i)
  start_time = time.time()
  pool = threadpool.ThreadPool(10)   	#创建线程池.
  reqs = threadpool.makeRequests(scan_port,portList)
  [pool.putRequest(req) for req in reqs]
  pool.wait()
  end_time = time.time()
  print("端口扫描时间: %d 秒."% (end_time-start_time))
