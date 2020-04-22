import re

r = "^China.*country$"

txt = "China is a great country"
x = re.search(r, txt)
print(x)
"""
元字符
元字符是具有特殊含义的字符：

字符 描述 示例 TIY 
[] 一组字符 "[a-m]" 试一试 
\\ 示意特殊序列（也可用于转义特殊字符） "\\d" 试一试 
. 任何字符（换行符除外） "he..o" 试一试 
^ 起始于 "^hello" 试一试 
$ 结束于 "world$" 试一试 
* 零次或多次出现 "aix*" 试一试 
+ 一次或多次出现 "aix+" 试一试 
{} 确切地指定的出现次数 "al{2}" 试一试 
| 两者任一 "falls|stays" 试一试 
() 捕获和分组 
"""

"""
RegEx 函数
re 模块提供了一组函数，允许我们检索字符串以进行匹配：

函数 描述 
findall 返回包含所有匹配项的列表 
search 如果字符串中的任意位置存在匹配，则返回 Match 对象 
split 返回在每次匹配时拆分字符串的列表 
sub 用字符串替换一个或多个匹配项 
"""

str = "China is a great country"
x = re.findall("a", str)
print(x)
