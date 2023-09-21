from core import reports

class Test:

  def __init__(self,testname,callback):
    self.testname = testname
    self.callback = callback
    
    if self.callback == True:
      reports.setTest(self.testname,'success')
    else:   
      reports.setTest(self.testname,'error')

    reports.drawTests()


  
class Expect:
  def __init__(self,current):
    self.current = current

  def toBe(self,expected):
    
    if self.current != expected:
      print("Error")
      print(f"Expected: {expected}")
      print(f"Recived: {self.current}")
      reports.setErrorDescription(f'Expected: {expected} - Recived: {self.current}')
      return False
    
    else:
      print("Success")
      return True