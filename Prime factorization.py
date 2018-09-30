
while True:
    
    inputTall=abs(int(input("\nProvide a positive whole number: ")))
    tall=int(inputTall)
    aList=[]
    

    for i in range (2, tall):
        while tall%i==0:
            tall/=i
            aList.append(str(i))


    if aList==[] and inputTall!=0:
        print(inputTall, "is a prime number ;D")
    elif inputTall==0:
        print(inputTall, "can't be prime factorized!")
    else:
        print("Prime factorization gives:", inputTall, "=", ' * '.join(aList))
