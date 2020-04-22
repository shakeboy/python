import threadpool
def AddFunc(op1,op2):
  print("%d + %d = %d."%(op1,op2,op1+op2))
if __name__ == '__main__':
  opList1 = [1,2]
  opList2 = [3,4]
  opList3 = [5,6]
  opList=[(opList1,None),(opList2,None),(opList3,None)]
  pool = threadpool.ThreadPool(3)
  requests = threadpool.makeRequests(AddFunc,opList)
  [pool.putRequest(req) for req in requests]
  pool.wait()
