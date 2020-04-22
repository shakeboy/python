import socket
serverSocket = socket.socket()    	#创建套接字.
serverSocket.bind(('127.0.0.1',12345))    	#绑定套接字.
serverSocket.listen(5)	#设置挂起的连接数.
print("等待客户端发起连接请求！")
while True:
  conn,addr = serverSocket.accept()    	#等待客户发起连接请求.
  print("客户端连接成功...")
  while True:
    try:
      recv_data = conn.recv(1024)	#接收信息.
      if len(recv_data) == 0:
        print("服务器: 好吧，我也退出连接！")
        break
      print("客户端：" + str(recv_data.decode()))
      send_data = "(阿甘)妈妈常常说，人生就如同一盒巧克力，你永远无法知道下一粒你会拿到什么。"
      conn.send(bytes(send_data,encoding='utf8'))    	#给客户端发送信息.
      print("服务器:" + send_data)
    except Exception:
      break
  conn.close()  	#关闭连接.
