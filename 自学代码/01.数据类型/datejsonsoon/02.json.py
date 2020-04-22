# JSON 是用于存储和交换数据的语法。
#
# JSON 是用 JavaScript 对象表示法（JavaScript object notation）编写的文本。
import json

# 一些json
x = '{"name":"bill","age":21,"address":"湖北省"}'
# 解析x
y = json.loads(x)
# 结果是字典
print(y)

# 若有 Python 对象，则可以使用 json.dumps() 方法将其转换为 JSON 字符串。
# Python 对象（字典）：
x = {
    "name": "Bill",
    "age": 63,
    "city": "Seatle"
}
# 转换为 JSON：
y = json.dumps(x)
# 结果是 JSON 字符串：
print(y)

# 可以转换成json对象的数据类型
"""
您可以把以下类型的 Python 对象转换为 JSON 字符串：
dict 
list 
tuple 
string 
int 
float 
True 
False 
None 
"""
print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""
当 Python 转换为 JSON 时，Python 对象会被转换为 JSON（JavaScript）等效项：
Python JSON
dict Object
list Array
tuple Array
str String
int Number
float Number
True true
False false
None null
"""
x = {
    "name": "Bill",
    "age": 63,
    "married": True,
    "divorced": False,
    "children": ("Jennifer", "Rory", "Phoebe"),
    "pets": None,
    "cars": [
        {"model": "Porsche", "mpg": 38.2},
        {"model": "BMW M5", "mpg": 26.9}
    ]
}

print(json.dumps(x))
# 您还可以定义分隔符，默认值为（", ", ": "），这意味着使用逗号和空格分隔每个对象，使用冒号和空格将键与值分开：
y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)
