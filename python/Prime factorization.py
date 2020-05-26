
while True:
    
    inputNumber=abs(int(input("\nProvide a positive whole number for prime factorization: ")))
    if inputNumber==0 or inputNumber==1:
        print(inputNumber, "is neither prime nor composite. Rulebending, are we?")
        continue
    number=inputNumber
    aList=[]
    
    for i in range (2, int(round(((number+1.001)/2)))):
        while number%i==0:
            number/=i
            aList.append(str(i))
    
    if aList==[]:
        print(inputNumber, "is a prime number ;D")
    else:
        print("Prime factorization gives:", inputNumber, "=", ' * '.join(aList))
g
