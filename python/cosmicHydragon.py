from math import sqrt,factorial,pi

g = 8    #input generator base, min0
n = 360    #input modular group, min1
u = 29    #input pick exponent, min0
dif = 2    #input difficulty, min2

dif -= 1
styList = []
go = True
spartanEyro = 0
aTier = 0
while go:
    
    #val = (g**spartanEyro) %n
    #val = (spartanEyro**g) %n    #plane duality
    #val = (factorial(g)/( factorial(g-spartanEyro) )) %n    #spartanEyro cannot exceed g, use larger g
    #val = (factorial(spartanEyro+g)/( factorial(spartanEyro) )) %n    #spartanEyro starts at 0, add g
    #val = (factorial(g)/( factorial(spartanEyro)*factorial(g-spartanEyro) )) %n    #spartanEyro cannot exceed g, use large g
    #val = (factorial(spartanEyro+g)/( factorial(g)*factorial(spartanEyro) )) %n    #spartanEyro starts at 0, add g
    #val = (factorial(g+spartanEyro-1)/( factorial(spartanEyro)*factorial(g-1) )) %n    #g min1, energy usage
    val  = (factorial(spartanEyro+g)/( factorial(g)*factorial(spartanEyro) )) %n    #spartanEyro starts at 0, add 1
    #...
    #val = (factorial(g*spartanEyro)/( factorial(g)+factorial(spartanEyro) )) %n
    #val = (factorial((g+spartanEyro)**2)/( factorial(g)+factorial(spartanEyro) )) %n
    #val = (factorial(g**spartanEyro)/( factorial(g)+factorial(spartanEyro) )) %n
    #val = (factorial(spartanEyro**g)/( factorial(g)+factorial(spartanEyro) )) %n
    
    if aTier%2 != 0:
        aTier += 1
    for elIndex in range(len(styList)):
        if styList[elIndex] == val:
            if aTier < 2*dif:
                aTier += 1
            elif aTier >= 2*dif:
                
                adminPanel = True
                for index in range(elIndex-dif,len(styList)-dif):
                    if styList[index] == styList[-dif]:
                        warMusic = True
                        for beatScope in range(dif-1):
                            if styList[index+1+beatScope] != styList[-dif+1+beatScope]:
                                warMusic = False
                                break
                        if (styList[index+dif] == styList[elIndex]) and (warMusic == True):
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
    #print("(",spartanEyro,"^",g,") mod",n," = ", val)
    #print("(",g,"!/( (",g,"-",spartanEyro,")! )) mod",n," = ", val)
    #print("((",spartanEyro,"+",g,")!/( (",spartanEyro,")! )) mod",n," = ", val)
    #print("(",g,"!/( (",spartanEyro,")!*(",g,"-",spartanEyro,")! )) mod",n," = ", val)
    #print("((",spartanEyro,"+",g,")!/( (",g,")!*(",spartanEyro,")! )) mod",n," = ", val)
    #print("((",g,"+",spartanEyro,"-1 )!/( (",spartanEyro,")!*(",g,"-1 )! )) mod",n," = ", val)
    print("((",spartanEyro,"+",g,")!/( (",g,")!*(",spartanEyro,")! )) mod",n," = ", val)
    #...
    #print("((",g,"*",spartanEyro,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", val)
    #print("(( (",g,"+",spartanEyro,")^2 )!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", val)
    #print("((",g,"^",spartanEyro,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", val)
    #print("((",spartanEyro,"^",g,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", val)
    
    spartanEyro += 1

#print("\n(",g,"^",u,") mod",n," = ", (g**u) %n )
#print("\n(",u,"^",g,") mod",n," = ", (u**g) %n )
#print("\n(",g,"!/( (",g,"-",u,")! )) mod",n," = ", (factorial(g)/( factorial(g-u) )) %n )
#print("\n((",u,"+",g,")!/( (",u,")! )) mod",n," = ", (factorial(u+g)/( factorial(u) )) %n )
#print("\n(",g,"!/( (",u,")!*(",g,"-",u,")! )) mod",n," = ", (factorial(g)/( factorial(u)*factorial(g-u) )) %n )
#print("\n((",u,"+",g,")!/( (",g,")!*(",u,")! )) mod",n," = ", (factorial(u+g)/( factorial(g)*factorial(u) )) %n )
#print("\n((",g,"+",u,"-1 )!/( (",u,")!*(",g,"-1 )! )) mod",n," = ", (factorial(g+u-1)/( factorial(u)*factorial(g-1) )) %n )
print("\n((",u,"+",g,")!/( (",g,")!*(",u,")! )) mod",n," = ", (factorial(u+g)/( factorial(g)*factorial(u) )) %n )
#...
#print("\n((",g,"*",u,")!/( (",g,")!+(",u,")! )) mod",n," = ", (factorial(g*u)/( factorial(g)+factorial(u) )) %n )
#print("\n(( (",g,"+",u,")^2 )!/( (",g,")!+(",u,")! )) mod",n," = ", (factorial((g+u)**2)/( factorial(g)+factorial(u) )) %n )
#print("\n((",g,"^",u,")!/( (",g,")!+(",u,")! )) mod",n," = ", (factorial(g**u)/( factorial(g)+factorial(u) )) %n )
#print("\n((",u,"^",g,")!/( (",g,")!+(",u,")! )) mod",n," = ", (factorial(u**g)/( factorial(g)+factorial(u) )) %n )
