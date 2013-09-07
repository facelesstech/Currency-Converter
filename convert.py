import decimal, os, sys

class Convert(object):
        
    def opentxt(self):
        target = open("convert.txt")
        self.rate = target.read()        
        
    def opentxtwrite(self):
        target = open("convert.txt", "w")
        print "Enter rate now."
        rate = raw_input("> ")
        #print "Writing to file"
        target.write(rate)
        
    def dothemath(self):        
        print "Enter amount here"
        amount = raw_input("> ")
        self.final = decimal.Decimal(self.rate) * decimal.Decimal(amount)

if __name__ == '__main__':
    start = Convert()
    print '''
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

ver 0.1 beta
'''        
start.opentxt()
check = os.stat("convert.txt").st_size
while check <= 0:
    print "There is no exchange rate set."
    start.opentxtwrite()
    start.opentxt()
    check = os.stat("convert.txt").st_size
    start.dothemath()
    print "> %.02f" % start.final
    sys.exit()
else:
    print "Set rate press '1' or press '2' to use this rate %r" % start.rate
    pick = raw_input("> ")
    if pick == "1":
        start.opentxt()
        start.opentxtwrite()
        start.dothemath()
        print "> %.02f" % start.final
    elif pick == "2":
        start.opentxt()
        start.dothemath()
        print "> %.02f" % start.final
    else:
        print "Something went wrong"
