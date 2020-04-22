#加密函数.
def encryFunc(encryString):
  decryString = ''
  for i in encryString:
    decryString = decryString + chr(ord(i) + 3)
  return decryString

#解密函数.
def decryFunc(decryString):
  encryString = ''
  for i in decryString:
    encryString = encryString + chr(ord(i) - 3)
  return encryString

if __name__ == '__main__':
  encryStr = input("请输入要加密的字符串: ")
  decryStr = encryFunc(encryStr)                  #调用字符串加密函数，返回密文.
  print("加密后的字符串:",decryStr)
  encryStr = decryFunc(decryStr)                  #调用字符串解密函数，返回明文.
  print("解密后的字符串:",encryStr)
