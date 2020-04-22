import socket
clientSocket = socket.socket() 	#创建套接字.
clientSocket.connect(('127.0.0.1',12345))  	#绑定套接字.
while True:
  send_data = input("客户端: ").strip()	#从键盘输入信息.
  if send_data == 'exit':
    print("客户端: 我要退出连接了！")
    break
  if len(send_data) == 0:
    continue
  clientSocket.send(bytes(send_data,encoding='utf8'))	#发送信息.
  recv_data = clientSocket.recv(1024)	#接收服务器信息.
  print("服务器：" + str(recv_data.decode()))	#输出信息.
clientSocket.close()     	#关闭连接.
