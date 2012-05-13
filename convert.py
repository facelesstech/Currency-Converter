import decimal
import os

class start(object):

    def __init__(self):
        self.start = start
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
Ver 0.6 alpha
\033[0m              
'''
        
    def convert(self):
        target = open("convert.txt")
        rate = target.read()
        print "The rate is currently set at \033[1;36m%r\033[0m" % rate
        print "Set rate '1' use rate '2'"
        pick = raw_input("> ")
        if pick == "2":
            check = os.stat("convert.txt").st_size
            if check <= 0:
                print "There is no exchange rate set."
                print "Enter rate."
                exchange = raw_input("> ")
                target = open("convert.txt", "w")
                target.write(exchange)
                target = open("convert.txt")
                rate = target.read()
                print "Enter amount here"
                amount = raw_input("> ")
                final = decimal.Decimal(rate) * int(amount)
            else:    
                target = open("convert.txt")
                rate = target.read()
                print "Enter amount here"
                amount = raw_input("> ")
                final = decimal.Decimal(rate) * int(amount)
        elif pick == "1":
            target = open("convert.txt", "w")
            print "Enter rate"
            exchange = raw_input("> ")
            target.write(exchange)
            target.close()
            target = open("convert.txt")
            rate = target.read()
            print "Enter amount here"
            amount = raw_input("> ")
            final = decimal.Decimal(rate) * int(amount)
        else:
            print "Ether pick '1' or '2'"
            a = start()
            a.convert()
        return final
        
a = start()
print "\033[1;36m%0.2f\033[0m" % a.convert()
