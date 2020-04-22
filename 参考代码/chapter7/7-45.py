import jieba.posseg as pseg
words = pseg.cut("中国人民是不可战胜的") 		#词性标注.
words1=pseg.POSTokenizer(tokenizer=pseg.dt)
for word,flag in words:
  print('%s %s' % (word,flag))
print(words1)