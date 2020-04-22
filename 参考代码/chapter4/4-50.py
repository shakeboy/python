from collections import deque
q = deque(["李白","杜甫","王维"])  		     #创建一个队列.
q.append("韩愈")                 				#元素入队列.
q.append("白居易")               				#元素入队列.
print("出队列元素: ",q.popleft())    		#元素出队列.
print("出队列元素: ",q.popleft())    		#元素出队列.
print("队列剩余元素: ",q)          			#队列剩余元素.
