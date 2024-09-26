a=int(input())
b=int(input())
c=int(input())
x=int(input())
k=int(input())
y1=((a*(x**2))-(b*x)+c)
y2=(a*(x**2)+(b*x)+c)
if x>k:
    print (y1)
elif x==k:
    print("0")
else:
    print (y2)