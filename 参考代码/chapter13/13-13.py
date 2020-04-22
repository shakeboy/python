from concurrent.futures import ThreadPoolExecutor
def ExecuteTask(task):
  print("执行: %s."%(task))
if __name__ == '__main__':
  taskList = []
  for i in range(5):
    taskList.append("任务" + str(i))
  with ThreadPoolExecutor(5) as executor:
    for task in taskList:
      future = executor.submit(ExecuteTask,task)
