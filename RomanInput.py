import re
class Roman(object):
 # make a dictionary of Roman numerals and values
 roman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
 romanList = [
    (1000, "M"), (900, "CM"),
    (500, "D"), (400, "CD"), 
    (100, "C"), (90, "XC"), 
    (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"),
    (1, "I")
 ]
 wronginput = False
 returnInput = ""
 def __init__(self, expr):
  return self.startValidate(expr)
  
 def startValidate(self, expr):
  self.validateexpr(expr) 
  if self.istrue():
   return self.returnInput 
  expr = ''.join(expr)
  return self.romantoInt(expr)
     
 def istrue(self):
  return self.wronginput
 
 def validateexpr(self, expr): # validates roman expression
  expr = list(expr)
  for x in expr:
   if x not in self.roman.keys():
    self.returnInput = "Invalid Roman Expression.Contains Other Letter"
    self.wronginput = True
    return
  self.validateCorrectness(expr)
  return

 def validateCorrectness(self, expr) :
  pattern = re.compile("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
  if not pattern.match(''.join(expr)):
   self.returnInput = "Invalid Roman Expression.Order of letter is mismatch"
   self.wronginput = True
   return
  return
  
 def romantoInt(self, numeral):
    result = 0
    while numeral:
        preparse_length = len(numeral)
        groupresult = 0
        numeral = numeral.lstrip('( ')  # remove opening parens and spaces
        for value, rchar in self.romanList:
            while numeral.startswith(rchar):
                groupresult += value
                numeral = numeral[len(rchar):]
        if len(numeral) == preparse_length:
            # No valid numerals found, not a Roman numeral then
            raise ValueError(
                'ValueError: invalid literal for romanToInt: {!r}'.format(numeral))
        while numeral[:1] == ')':
            groupresult *= 4000
            numeral = numeral[1:]
        result += groupresult
    return result
  
 def intToRoman(self,integer):
    result = []
    parenscount = 0
    while integer:
        integer, num = divmod(integer, 4000)
        romanResult = ""
        for value, rchar in self.romanList:
            count, num = divmod(num, value)
            romanResult += count * rchar
        if romanResult:
            result.append('{}{}{}'.format(
                '(' * parenscount, romanResult, ')' * parenscount))
        parenscount += 1
    return ' '.join(result[::-1])

class TWex1(Roman):
 content = []
 inputs = []
 exprs = []
 fileinput = ""
 def __init__(self, fileinput):
  self.fileinput = fileinput
  self.startProcess()
  return

 def startProcess(self):
  self.fetchInput()
  self.processInput()
  
 def fetchInput(self): 
  with open(self.fileinput) as f:
   self.content = f.readlines()
  return 
 
 def processInput(self):
  statements = [ word.rstrip("\n") for i, word in enumerate(self.content) if word.find("?") == -1 and word.find("credits") == -1]
  expressions = [ word.rstrip("\n") for i, word in enumerate(self.content) if word.find("?") == -1 and word.find("credits") != -1]
  questions = [ word.rstrip("\n") for i, word in enumerate(self.content) if word.find("?") != -1 ]
  self.processStatements(statements)
  self.processExpressions(expressions)
  answers = self.processQuestions(questions)
  # self.displayOutput(answers)
  self.appendFile(answers)
  return
  
 def appendFile(self, answers):
  tmp = "\n\nTest Output:\n"
  for i in answers:
   tmp += i + "\n"
  with open(self.fileinput, "a") as myfile:
    myfile.write(tmp)
  print("Answers are appended in Input File :)")
  return
  
 # def displayOutput(self, answers):
  # print("Test Output:\n\n")
  # for i in answers:
   # print i , "\n"
  # return
  
 def processStatements(self,statements):
  statement = ';'.join(statements)
  self.inputs = dict(i.split(" is ") for i in statement.split(";"))
  return
  
 def processExpressions(self, expressions): #evaluating input expression and merging it with existing inputs dictionary.Now we got complete inputs
  key = []
  value = []
  for i in expressions:
   tmp = i.split(" is ")
   key.append(tmp[0])
   value.append(tmp[1])
  key = self.parsetoRoman(key)
  value = self.parsetoValue(value)
  self.evaluateExpr(key,value)
  self.inputs.update(dict(zip(key, value)))
  return
  
 def processQuestions(self, questions):#processing questions
  answers = []
  tmp_qns = []
  tempquestions = []
  k = 0
  
  for i in questions:
   temp = ""
   for j in i.split(" "):
	if j in self.inputs:
	 temp += " " + j 
   tmp_qns.append(temp.strip())
  tempquestions = tmp_qns[:]
  self.evaluateQns(tmp_qns, answers)
  
  # formatting answers
  for i , j in enumerate(questions):
   if not str(answers[i]).isdigit():
    continue
   elif j.find("Credits") == -1:
    answers[i] = tempquestions[i] + " is " + str(answers[i])
   else:
    answers[i] = tempquestions[i] + " is " + str(answers[i]) + " credits"  
  return answers
   
 def evaluateQns(self, tmp_qns, answers):
  for j, k in enumerate(tmp_qns):# to convert to roman numerals
   tmp = ""
   if k :
    for i in k.split(" "):
     if i in self.inputs and i not in ('Silver', 'Gold', 'Iron'):
      tmp += self.inputs[i] 
     else:
	  tmp+="*" + str(i)
    tmp_qns[j] = tmp
  # evaluating values of qns:
  for i in range(len(tmp_qns)):
   if not tmp_qns[i]:
    answers.append("I have no idea what you are talking about")
   elif tmp_qns[i].find("*") == -1:
    t = super(TWex1, self).__init__(tmp_qns[i])
    try:
     answers.append(int(t))
    except:
	 answers.append(t)
   else:
    tmp = tmp_qns[i].split("*")
    op1 = super(TWex1, self).__init__(tmp[0])#operand 1
    op2 = self.inputs[tmp[1]]
    try:
     answers.append(int(op1*op2))
    except:
	 answers.append(op1)
  return
  
 def evaluateExpr(self, key, value): #evaluating expression (can improve evaluating logic)
  for i in range(len(key)):
   tmp = key[i].split("*")
   key[i] = tmp[1] # assuming SIlver,GOld will come lastly(which can be updated)
   denominator = int(super(TWex1, self).__init__(tmp[0]))
   numerator = int(value[i]) 
   if numerator % denominator == 0:
    value[i] = int(numerator/denominator)
   else:
    value[i] = float(numerator)/float(denominator)
  return 
     
 def parsetoRoman(self, key):
  for j, k in enumerate(key):# to convert to roman numerals
   tmp = ""
   for i in k.split(" "):
    if i in self.inputs:
     tmp += self.inputs[i]
    else:
	 tmp+="*" + i
   key[j] = tmp
  return key
  
 def parsetoValue(self, value):
  for j, k in enumerate(value):# to convert to values
   tmp =0
   for s in k.split():
    if s.isdigit():
	 tmp =  int(s)
   value[j] = tmp
  return value

t = TWex1("C:\Users\PV02594\Desktop\inputtext.txt")
