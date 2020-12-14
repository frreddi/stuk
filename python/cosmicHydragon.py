from math import sqrt,factorial,pi


g = 52    #input generator base
n = 360    #input modular group
u = 666    #input pick exponent

styList = []
go = True
spartanEyro = 0
aTier = 0
while go:
    
    #val = (g**spartanEyro) %n
    #val = (factorial(g)/( factorial(g-spartanEyro) )) %n
    #val = (factorial(g)/( factorial(spartanEyro)*factorial(g-spartanEyro) )) %n
    val = (factorial(g+spartanEyro-1)/( factorial(spartanEyro)*factorial(g-1) )) %n
    
    if (aTier == 1) or (aTier == 3) or (aTier == 5) or (aTier == 7):
        aTier += 1
    for el in styList:
        if el == val:
            if (aTier == 0) or (aTier == 2) or (aTier == 4) or (aTier == 6):
                aTier += 1
            elif aTier == 8:
                
                adminPanel = True
                for index in range(len(styList)-3):
                    if (styList[index] == styList[-3]) and (styList[index+1] == styList[-2]) and (styList[index+2] == styList[-1]) and (styList[index+3] == el):
                        adminPanel = False
                
                if adminPanel == True:
                    aTier = 7
                elif adminPanel == False:
                    go = False
            break
    if (aTier == 2) or (aTier == 4) or (aTier == 6) or (aTier == 8):
        aTier = 0
    styList.append(val)
    
    #print("(",g,"^",spartanEyro,") mod",n," = ", val)
    #print("(",g,"!/( (",g,"-",spartanEyro,")! )) mod",n," = ", val)
    #print("(",g,"!/( (",spartanEyro,")!*(",g,"-",spartanEyro,")! )) mod",n," = ", val)
    print("(",g,"+",spartanEyro,"-1 )!/( (",spartanEyro,")!*(",g,"-1 )! )) mod",n," = ", val)
    
    spartanEyro += 1

#print("\n(",g,"^",u,") mod",n," = ", (g**u) %n )
#print("\n(",g,"!/( (",g,"-",u,")! )) mod",n," = ", (factorial(g)/( factorial(g-u) )) %n )
#print("\n(",g,"!/( (",u,")!*(",g,"-",u,")! )) mod",n," = ", (factorial(g)/( factorial(u)*factorial(g-u) )) %n )
print("\n(",g,"+",u,"-1 )!/( (",u,")!*(",g,"-1 )! )) mod",n," = ", (factorial(g+u-1)/( factorial(u)*factorial(g-1) )) %n )
