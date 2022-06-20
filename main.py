import os
import time
score = 0
def instrucions():
  print ("use google translate")
  question()

def intro():
  print ("This is a true and false quiz")
  print ("do you know how to play?")
  print ("jk you don't have a choice")
  question()
#Nate harris 5/24/22 ver 4
#create the questions and make a true or false 
def question():
  global socre
  print ("question 1")
  print ("'kura'")
  print ("does it mean school? true or false")
  question = input().lower()
  if question == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    
    time.sleep(1)
    os.system('clear')
    
    questio()
  else:
    print("not fax")
    print("")
    print("")
    
    

def questio():
 
  print ("question 2")
  print ("whakamaori")
  print ("does it mean translate? true or false")
  question2 = input().lower()
  if question2 == "true" or "t":
    print ("fax")
    
    print("")
    print("")
    time.sleep(1)
    os.system('clear')
    questi()
  else:
    print("not fax")
    print("")
    print("")
    questio()

def questi():

  print ("question 3")
  print ("'no te mea'")
  print ("does it mean tree? true or false")
  question3 = input().lower()
  if question3 == "true" or "t":
    print ("fax")
    print("")
    print("")
    time.sleep(1)
    os.system('clear')
    quest()
    
  else:
    print("not fax")
    print("")
    print("")
    
def quest():

  print ("question 4")
  print ("rakau")
  print ("does it mean wood? true or false")
  question4 = input().lower()
  if question4 == "true" or "t":
    print ("fax")
    print("")
    print("")
    time.sleep(1)
    os.system('clear')
    ques()
    
  else:
    print("not fax")
    print("")
    print("")

def ques():
  
  print ("question 5")
  print ("'hē'")
  print ("does it mean foot? true or false")
  question5 = input().lower()
  if question5 == "true" or "t":
    print ("fax")
    print("")
    print("")
    time.sleep(1)
    os.system('clear')
    que()
    
  else:
    print("not fax")
    print("")
    print("")

def que():
 
  print ("question 6")
  print ("'kupu o raro'")
  print ("does it mean bottom text? true or false")
  question1 = input().lower()
  if question1 == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    time.sleep(1)
    os.system('clear')
    
    qu()
  else:
    print("not fax")
    print("")
    print("")

def qu():
 
  print ("question 7")
  print ("'kuputuhi runga'")
  print ("does it mean top text? true or false")
  question1 = input().lower()
  if question1 == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    time.sleep(1)
    os.system('clear')
    
    q()
  else:
    print("not fax")
    print("")
    print("")

def q():
 
  print ("question 8")
  print ("'kaihe'")
  print ("does it mean forklift? true or false")
  question1 = input().lower()
  if question1 == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    time.sleep(1)
    os.system('clear')
    epic9()
    
  else:
    print("not fax")
    print("")
    print("")

def epic9():
 
  print ("question 9")
  print ("'kura'")
  print ("does it mean school? true or false")
  question1 = input().lower()
  if question1 == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    time.sleep(1)
    os.system('clear')
    epic2()
    
  else:
    print("not fax")
    print("")
    print("")

def epic2():
 
  print ("question 10")
  print ("'āniwhaniwha'")
  print ("does it mean lower? true or false")
  question1 = input().lower()
  if question1 == "true" or "t":
    print ("fax")
    
    print("score be like oooo")
    print("")
    time.sleep(1)
    os.system('clear')
    emd()
    
  else:
    print("not fax")
    print("")
    print("")
    intro()


def emd():
  print ("emd")
  print ("thank play")

intro()