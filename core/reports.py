import os

class Report:
  passedTests = []

  failedTests = []
  errorDescription = []


  def __init__(self):
    pass


  def addtest(self,testName,type):
    if(not testName):
      print("Put a name on test")
    if(not type):
      print("Put a type of a test")
    else:  
      if(type == 'success'):
        self.passedTests.append(testName)
      else:
        self.failedTests.append(testName)


  def setErrorDescription(self,description):
    if(not description):
      print("Put a description")
    else:
      self.errorDescription.append(description) 

  def drawTests(self):

    os.system('CLS')
    print('>----------------<')

    print(f"✔ PASSED TESTS | {len(self.passedTests)}\n")
    for test in self.passedTests:
      print(test)


    print('\n>----------------<\n')

    print(f"❌ TESTS FAILED | {len(self.failedTests)}\n")

    for i in range(0,len(self.failedTests)):
      print(f"{self.failedTests[i]} | {self.errorDescription[i]}")
      
    print('\n>----------------<') 