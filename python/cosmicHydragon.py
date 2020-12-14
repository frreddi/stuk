
g = 4   #input generator base
n = 1080    #input modular group
u = 42    #input pick exponent

styList = []
go = True
spartanEyro = 0
while go:
    
    val = (g**spartanEyro)%n
    for el in styList:
        if el == val:
            go = False
            break
    styList.append(val)
    
    print("(",g,"^",spartanEyro,") mod",n," = ",val)
    spartanEyro += 1

print("\n(",g,"^",u,") mod",n," = ",(g**u)%n)
