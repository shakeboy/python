import re
phoneNumber = "400-669-5566#中国银行信用卡客服专线电话"
num1 = re.sub('#.*$',"",phoneNumber)
print("使用sub()替换结果:",num1)
num2 = re.subn('#.*$',"",phoneNumber)
print("使用subn()替换结果:",num2)
