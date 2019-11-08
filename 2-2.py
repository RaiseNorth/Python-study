a=int(input())
b=0
if a==2:
    b=1
elif a>2:
    i=2
    b=1
    while (i<a) :
        if a%i==0:b=0
        i+=1
if b==1 :print ("是")
else :print ("否")