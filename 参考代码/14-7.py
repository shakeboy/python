import socket, time

if __name__ == '__main__':
  ad = dict()
  LocalIP = socket.gethostbyname(socket.gethostname())
  socket1 = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
  socket1.bind((LocalIP, 10000))
  socket1.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
  socket1.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)          # 打开混杂模式.
  start_time = time.time()
  # 接收数据包.
  while True:
    pocket = socket1.recvfrom(65565)
    host_ip = pocket[1][0]
    if host_ip != LocalIP:                                        # 过滤本机消息.
      ad[host_ip] = ad.get(host_ip,0) + 1
    end_time = time.time()
    print(end_time-start_time)
    if end_time-start_time >= 30:                                # 执行时间: 30秒.
      break
  socket1.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)        # 关闭混杂模式.
  socket1.close()
  if ad.items():
    print("本机IP为 %s, 接收数据包情况如下:"%LocalIP)
  else:
    print("没有接收到数据包。请检查网络是否连通！")
  for item in ad.items():
    print("远程计算机IP:%s, 发包数目:%d."%(item[0],item[1]))
