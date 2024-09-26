a=int(input())
fees1=(2000*a)
fees2=(1500*a)
fees3=(1000*a)
fees4=(800*a)
if a<=2:
    print(fees1 + 0.05*fees1)
elif 2<a<10:
    print(fees2 + 0.05*fees2)
elif 9<a<13:
    print(fees3 + 0.05*fees3)
elif a<12:
    print(fees4 + 0.05*fees4)