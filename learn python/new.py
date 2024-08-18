a= int(input("enter your first no. :"))
b= int(input("enter your second no. :"))
c= input("enter your operator from +,-,*,/,**,%:")

if(c=="+"):
    print("the sum is :",a+b)
elif(c=="-"):   
    print("the diffrence is :",a-b)
elif(c=="*"):   
    print("the multiplication is :",a*b)
elif(c=="/"):   
    print("the division is :",a/b)
elif(c=="**"):
    print("the power is :",a**b)
elif(c=="%"):
    print("the remainder is :",a%b)
else:     
    print("choose the correct option :")    
