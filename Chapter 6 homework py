import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
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
    

    
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n%2 == 1:
        return True
    else:
        return False


def is_factor(f,n):
    if f <n or f == n:
        if n%f==0:
            return True
        else:
            return False
    else:
        return False

def is_multiple(a,b):
    return is_factor(b,a)
    
def f2c(f):
    c=(f-32)/1.8
    answer=round(c,0)
    return answer

def test_suite():
    test(is_even(3)==False)
    test(is_even(0)==True)
    test(is_odd(1234565434567897678)==False)
    test(is_odd(973428797987234993)==True)
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)



    
    

test_suite()
