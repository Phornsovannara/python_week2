import random
A = random.randint(0,2)
a= int(A)
print(a)
Num = input( "Enter your number : ")
num = int(Num)

if(a==0 and num==0):
    print("=")
elif(a==1 and num==1):
    print("=")
elif(a==2 and num==2):
    print("=")
elif(a==0 and num==1):
    print("you win")
elif(a==0 and num==2):
    print("a is win")
elif(a==1 and num==2):
    print("you win")
elif(a==1 and num==0):
    print("a is win")
elif(a==2 and num==1):
    print("a is win")
elif(a==2 and num==0):
    print("you win")
else:
    print("..............")