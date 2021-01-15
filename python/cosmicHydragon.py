from math import sqrt,factorial,pi


g = 13    #input generator base
n = 256    #input modular group
u = 42    #input pick exponent
dif = 3    #input difficulty

dif = 2*(dif-1)
styList = []
go = True
spartanEyro = 0
aTier = 0
while go:
    
    #val = (g**spartanEyro) %n
    #val = (factorial(g)/( factorial(g-spartanEyro) )) %n
    #val = (factorial(g)/( factorial(spartanEyro)*factorial(g-spartanEyro) )) %n
    val = (factorial(g+spartanEyro-1)/( factorial(spartanEyro)*factorial(g-1) )) %n
    
    if aTier%2 != 0:
        aTier += 1
    for el in styList:
        if el == val:
            if aTier < dif:
                aTier += 1
            elif aTier >= dif:
                
                adminPanel = True
                for index in range(len(styList)-int(dif/2)+1):
                    if styList[index] == styList[-int(dif/2)+1]:
                        warMusic = True
                        for beatScope in range(int(dif/2)-2):
                            if styList[index+1+beatScope] != styList[-int(dif/2)+2+beatScope]:
                                warMusic = False
                                break
                        if (styList[index+int(dif/2)-1] == el) and (warMusic == True):
                            adminPanel = False
                            break
                
                if adminPanel == True:
                    aTier -= 1
                elif adminPanel == False:
                    go = False
            break
    if aTier%2 == 0:
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
