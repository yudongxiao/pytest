l=[1,2,3,4,5,6]
help(l.count)

def first_function(arg1,arg2):
    """
    Here is my docstring!
    :param arg1:
    :param arg2:
    :return:
    """
    print arg1+arg2

help(first_function)
first_function(1,2)

def is_prime(num):
    for n in xrange(2,num):
        if num%n==0:
            print 'it''s not a prime number'
            break
    else:
        print 'it''s a prime number'

is_prime(17)

square =lambda num:num**2
print square(4)


#global x
#print globals()

def vol(rad):
    return (4.0/3)*3.14*(rad**3)

print vol(15)

def ran_check(num,low,high):
    #check if numb is bettwn low and high
    if num in range(low, high):
        print "in range"
    else:
        print "the number is outside range"

st='Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(st):

    d={"upper":0,"lower":0}
    for word in st:
        if word.isupper():
            d["upper"]+=1
        elif word.islower():
            d["lower"]+=1
        else:
            pass
    print 'upper=',d["upper"]
    print 'loser=',d["lower"]

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


