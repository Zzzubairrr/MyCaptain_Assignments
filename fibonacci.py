n=int(input("number of terms : "))
n1,n2=0,1
c=0
if n<=0 :
    print("please enter a number")
elif n==1:
    print("fibonacci upto",n,":")
    print(n1)
else :
    print("fibonacci series:")
    while c < n :
        print(n1)
        nth = n1 + n2
        n1=n2
        n2=nth
        c+=1

