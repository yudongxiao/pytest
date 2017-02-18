x=0
while x<10:
    print 'x is currently:',x
    x+=1
    if x==3:
        print 'Hey x equals 3!'
    else:
        print 'continuing...'
        continue
else:
    print 'All Done!'

for num in range(10):
    print num
