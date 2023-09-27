from pYAtlas.core import reports

class Test:

  reports = reports.Report()

  def __init__(self,testname,callback):
    self.testname = testname
    self.callback = callback
    
    if self.callback == True:
      self.reports.addtest(self.testname,'success')
    else:   
      self.reports.addtest(self.testname,'error')

    self.reports.drawTests()





class Expect:

  reports = reports.Report()

  def __init__(self,current):
    self.current = current

  def toBe(self,expected):
    if self.current != expected:
      self.reports.setErrorDescription(f'Expected: {expected} - Recived: {self.current}')
      return False
    else:
      return True
    
  def toEqual(self,expected):
    if type(self.current) != type(expected):
      self.reports.setErrorDescription(f'Type Error\nExpected: {type(expected)} - Recived: {type(self.current)} ')

 
