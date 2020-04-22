import unittest

#定义类.
class MostInfluFigureSurvey():
  #构造函数.
  def __init__(self,question):
    self.question = question
    self.answers = {}
  #显示调查问题.
  def show_question(self):
    print(self.question)
  #存储用户答案.
  def store_answer(self,new_answer):
    if new_answer in self.answers:
      self.answers[new_answer] = self.answers[new_answer] + 1
    else:
      self.answers[new_answer] = 1
  #显示调查结果.
  def show_results(self):
    print("调查结果:")
    #按照得票数由高到低排序.
    result = sorted(self.answers.items(),key=lambda x: x[1],reverse=True)
    #输出得票结果.
    for item in result:
      print(item)

#定义测试类.
class TestMostInfluFigureSurvey(unittest.TestCase):
  #创建被测试类的实例和相关变量.
  def setUp(self):
    question = "您认为全球最有影响的人是谁?"
    self.survey = MostInfluFigureSurvey(question)
    self.answers = {'穆罕默德':0,'牛顿':0,'释迦牟尼':0,'孔子':0,'圣保罗':0,
 		'蔡伦':0,'爱因斯坦':0,'马克思':0,'哥伦布':0,'伽利略':0}
  #测试调查结果.
  def test_user_answer(self):
    while True:
      answer = input("请输入您认为全球最有影响的人: ")
      if answer == 'q':
        break
      if answer in self.answers:
        self.answers[answer] = self.answers[answer] + 1 #名字在候选名单，票数加1.
      self.survey.store_answer(answer)
      for key,value in self.survey.answers.items():
        self.assertIn(key,self.answers)     		  #用户投票名字是否在候选名单.
        self.assertEqual(value,self.answers[key])  	  #候选人得票数是否正确.
    #显示调查结果.
    self.survey. show_results()

if __name__ == '__main__':
  unittest.main()
