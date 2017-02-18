l =[1,2,3,4,5]

for num in range(1,6):
    print num

for num in xrange(1,11):
    print num

x= xrange(1,6)
print type(x)

if(type(x) is xrange):
    print 'type is xrange'