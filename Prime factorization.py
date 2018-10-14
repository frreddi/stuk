
while True:
    
    inputNumber=abs(int(input("\nProvide a positive whole number: ")))
    number=inputNumber
    halfNumber=round((inputNumber/2)+0.51)
    aList=[]


    for i in range (2, halfNumber):
        while number%i==0:
            number/=i
            aList.append(str(i))


    if aList==[] and inputNumber!=0:
        print(inputNumber, "is a prime number ;D")
    elif inputNumber==0:
        print(inputNumber, "can't be prime factorized!")
    else:
        print("Prime factorization gives:", inputNumber, "=", ' * '.join(aList))
