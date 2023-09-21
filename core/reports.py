import os

successTests = []

errorTests = []
errorDescription = []


def setTest(testName,where):

  if(not testName):
    print("Put a name on test")
  if(not where):
    print("Put a where on test will to be")
  else:  
    if(where == 'success'):
      successTests.append(testName)
    else:
      errorTests.append(testName)
      

def setErrorDescription(description):
  if(not description):
    print("Put a description")
  else:
    errorDescription.append(description)  





def drawTests():

  # os.system('CLS')
  print('>----------------<')

  print(f"✔ PASSED TESTS | {len(successTests)}\n")
  for test in successTests:
    print(test)


  print('\n>----------------<\n')

  print(f"❌ TESTS FAILED | {len(errorTests)}\n")

  for i in range(0,len(errorTests) - 1):
    print("kkkkkkkkkkkkkk")
    print(f"{errorTests[0]} | {errorDescription[0]}")
  

  print('\n>----------------<')
 
