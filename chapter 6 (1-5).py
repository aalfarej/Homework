import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
    
# Exsersize 1

def turn_clockwise(direction):
    point=direction
    if point==("North"):
        return print("East")
    elif point==("East"):
        return print("South")
    elif point==("South"):
        return print("West")
    elif point==("West"):
        return print("North")
    else:
        return print("None")
#Exsersize 2

def day_name(number):
    if number== 0:
        return "Sunday"
    elif number==1:
        return "Monday"
    elif number==2:
        return "Tuesday"
    elif number==3:
        return "Wednesday"
    elif number==4:
        return "Thursday"
    elif number==5:
        return "Friday"
    elif number==6:
        return "Saturday"
    else:
        return None
    
#Exsersize 3


def day_num(dayname):
    if dayname=="Sunday":
        return 0
    elif dayname=="Monday":
        return 1
    elif dayname=="Tuesday":
        return 2
    elif dayname=="Wednesday":
        return 3
    elif dayname=="Thursday":
        return 4
    elif dayname=="Friday":
        return 5
    elif dayname=="Saturday":
        return 6
    else:
        return None
    
#Exsersize 4


def day_add(dayname,dayleave):
    sdaynum=day_num(dayname)
    ldaynum= (sdaynum + dayleave)%7
    return day_name(ldaynum)


#Exsersize 5 


def test_suite():
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    


test_suite()
    
    
