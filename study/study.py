l =[1,2,3,4,5]

for num in range(1,6):
    print num

for num in xrange(1,11):
    print num

x= xrange(1,6)
print type(x)

if(type(x) is xrange):
    print 'type is xrange'

l=[]

#for letter in 'word':
#    l.append(letter)
#print l

l=[letter+'abc' for letter in 'word']
print l

l=[num for num in xrange(1,50) if num%3==0]
print l

st='Print every word in this sentence that has an even number of letters'
print [word for word in st.split() if len(word)%2==0]

l=[num for num in xrange(1,100) if num%3]

for num in xrange(1,100):
    if num%15==0:
        print 'FizzBuzz'
        continue
    elif num%5==0:
        print 'Buzz'
        continue
    elif num%3==0:
        print 'Fizz'
        continue
    else:
        print num

st ='Create a list of the first letters of every word in this string'
l=[word[0] for word in st.split()]
print l

range (0,11,2)
