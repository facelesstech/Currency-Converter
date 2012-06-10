import decimal
import os
class Convert(object):

    def __init__(self):
        self.start()
        
    def start(self):
        print '''\033[1;37m
 dP"Yb    .d   .d  dP"Yb    .d   .d  dP"Yb    .d     
dP   Yb .d88 .d88 dP   Yb .d88 .d88 dP   Yb .d88     
Yb   dP   88   88 Yb   dP   88   88 Yb   dP   88     
 YbodP    88   88  YbodP    88   88  YbodP    88     

 dP"Yb    .d   .d  dP"Yb    .d   .d   .d   .d     
dP   Yb .d88 .d88 dP   Yb .d88 .d88 .d88 .d88     
Yb   dP   88   88 Yb   dP   88   88   88   88     
 YbodP    88   88  YbodP    88   88   88   88     

 dP"Yb    .d   .d  dP"Yb    .d   .d   .d  dP"Yb      
dP   Yb .d88 .d88 dP   Yb .d88 .d88 .d88 dP   Yb     
Yb   dP   88   88 Yb   dP   88   88   88 Yb   dP     
 YbodP    88   88  YbodP    88   88   88  YbodP      

 dP"Yb    .d   .d  dP"Yb   dP"Yb    .d  dP"Yb    .d     
dP   Yb .d88 .d88 dP   Yb dP   Yb .d88 dP   Yb .d88     
Yb   dP   88   88 Yb   dP Yb   dP   88 Yb   dP   88     
 YbodP    88   88  YbodP   YbodP    88  YbodP    88     

 dP"Yb    .d   .d   .d   .d  dP"Yb   dP"Yb    .d 
dP   Yb .d88 .d88 .d88 .d88 dP   Yb dP   Yb .d88 
Yb   dP   88   88   88   88 Yb   dP Yb   dP   88 
 YbodP    88   88   88   88  YbodP   YbodP    88 

ver 0.2 beta\033[0m
'''        
        self.opentxt()
        print "Set rate press '1' or press '2' to use this rate \033[1;36m%r\033[0m" % self.rate
        pick = raw_input("> ")
        if pick == "1":
            self.convertset()
        elif pick == "2":
            self.justconvert()
        else:
            self.__init__()
    
    def opentxt(self):
        target = open("convert.txt")
        self.rate = target.read()        
        
    def opentxtwrite(self):
        target = open("convert.txt", "w")
        print "Enter rate now."
        rate = raw_input("> ")
        target.write(rate)
        
    def dothemath(self):
        check = os.stat("convert.txt").st_size
        if check <=0:
            print "There is no exchange rate set."
            self.opentxtwrite()
            self.justconvert()
        else:        
            print "Enter amount here"
            amount = raw_input("> ")
            final = decimal.Decimal(self.rate) * decimal.Decimal(amount)
            print "\033[1;36m%0.2f\033[0m" % final
        
        
    def convertset(self):
        self.opentxtwrite()
        self.opentxt()
        self.dothemath()
        exit()
        
    def justconvert(self):
        self.opentxt()
        self.dothemath()
        exit()
        
a = Convert()
a.start()
