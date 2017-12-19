import sys
import turtle
wn=turtle.Screen()
frank=turtle.Turtle()
drunk=turtle.Turtle()
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

mylist=[1,7,2,4,5,6,7,9,32,54,-88,-7]
mylist2=["hello","babab","sam","frank","newbe","conming","xbnhk"]
mylist3=["Dimah","Salma","Shell","aronson"]
def count_odd(lst):
    odd=0
    for i in lst:
        if i%2 == 1:
            odd += 1
    return odd
            
            


def sum_even(lst):
    sumeven=0
    for i in lst:
        if i%2==0:
            sumeven += i
    return sumeven
            
    
def sum_negative(lst):
    negasum=0
    for i in lst:
        if i < 0:
            negasum += i
    return negasum
    
def count_5(list):
    numword5=0
    for i in list:
        if len(i)==5:
            numword5 += 1
    return numword5

def sum_to_even(list):
    mysum=0
    for i in list:
        if i%2 == 0:
            break
        mysum += i
    return mysum

def before_sam(lst):
    count=0
    for i in lst:
        if i == "sam":
            count += 1
            break
        count += 1
    return count
            

def sqrt(n):
    approx = n/3
    while True:
        better = (approx + n/approx)/2
        print(better)
        if abs(approx-better)<0.001:
            return better
        approx = better

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



def test_suite():
    
    test(count_odd(mylist)== 6)
    test(sum_even(mylist)==10)
    test(sum_negative(mylist)==-95)
    test(count_5(mylist2)==5)
    test(sum_to_even(mylist)==8)
    test(before_sam(mylist2)==3)
    test(before_sam(mylist3)==4)

test_suite()

