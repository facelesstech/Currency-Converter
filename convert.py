import decimal
import os

def pick():
    os.system('clear')
    target = open("convert.txt")
    text = target.read()
    print '''\033[1;37m
                 _____
              .-'     `-.
            .'  .-"""-.-'
           /  .'
      .---' '--------.
       """:  :"""""""
    .-----'  '-----.
     """""\  \"""""
           \  `.
            '.  `-----.
              '-.____.'
  e88'Y88                                                            
 d888  'Y 8888 8888 888,8, 888,8,  ,e e,  888 8e   e88'888 Y8b Y888P 
C8888     8888 8888 888 "  888 "  d88 88b 888 88b d888  '8  Y8b Y8P  
 Y888  ,d Y888 888P 888    888    888   , 888 888 Y888   ,   Y8b Y   
  "88,d88  "88 88"  888    888     "YeeP" 888 888  "88,e8'    888    
                                                              888    
                                                              888    

  e88'Y88                                              d8                  
 d888  'Y  e88 88e  888 8e  Y8b Y888P  ,e e,  888,8,  d88    ,e e,  888,8, 
C8888     d888 888b 888 88b  Y8b Y8P  d88 88b 888 "  d88888 d88 88b 888 "  
 Y888  ,d Y888 888P 888 888   Y8b "   888   , 888     888   888   , 888    
  "88,d88  "88 88"  888 888    Y8P     "YeeP" 888     888    "YeeP" 888  

ver 0.1 alpha\033[0m
'''
    print "The current exchange rate is \033[1;31m%r\033[0m do you want to reset it?" % text
    print "1. Yes 2. No"
    question = raw_input("> ")
    if "1" in question:
        new()
    elif "2" in question:
        old()
    else:
        pick()

def new():
    target = open("convert.txt", "w")
    print "Enter the exchange rate now."
    rate = raw_input("> ")
    target.write(rate)
    target.close()
    old()
    
def old():
    text1 = os.stat("convert.txt").st_size
    if text1 <= 0:
        print "There is no exchange rate set."
        new()
    else:
        target = open("convert.txt")
        text = target.read()
        print "Enter amount here."
        amount = raw_input("> ")
        exchange = decimal.Decimal(text) * decimal.Decimal(amount)
        print "\033[1;31m%0.2f\033[0m" % exchange   
    
pick()
