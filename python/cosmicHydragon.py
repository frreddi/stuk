from math import sqrt,factorial,pi

def go():
    g = 8    #input generator base, min0
    n = 360    #input modular group, min1
    u = 29    #input pick exponent, min0
    dif = 2    #input difficulty, min2
    
    dif -= 1
    spartanEyro = 0
    aTier = 0
    styList = []
    warMusic = False
    adminPanel = False
    while not adminPanel:
        
        #styList.append( (g**spartanEyro) %n )
        #styList.append( (spartanEyro**g) %n )  #plane duality
        #styList.append( (factorial(g)/( factorial(g-spartanEyro) )) %n )  #spartanEyro cannot exceed g, use larger g
        #styList.append( (factorial(spartanEyro+g)/( factorial(spartanEyro) )) %n )  #spartanEyro starts at 0, add g
        #styList.append( (factorial(g)/( factorial(spartanEyro)*factorial(g-spartanEyro) )) %n )  #spartanEyro cannot exceed g, use large g
        #styList.append( (factorial(spartanEyro+g)/( factorial(g)*factorial(spartanEyro) )) %n )  #spartanEyro starts at 0, add g
        #styList.append( (factorial(g+spartanEyro-1)/( factorial(spartanEyro)*factorial(g-1) )) %n )  #g min1, energy usage
        styList.append(  (factorial(spartanEyro+g)/( factorial(g)*factorial(spartanEyro) )) %n )  #spartanEyro starts at 0, add 1
        #...
        #styList.append( (factorial(g*spartanEyro)/( factorial(g)+factorial(spartanEyro) )) %n )
        #styList.append( (factorial((g+spartanEyro)**2)/( factorial(g)+factorial(spartanEyro) )) %n )
        #styList.append( (factorial(g**spartanEyro)/( factorial(g)+factorial(spartanEyro) )) %n )
        #styList.append( (factorial(spartanEyro**g)/( factorial(g)+factorial(spartanEyro) )) %n )
        
        if aTier%2 != 0:
            aTier += 1
        for elIndex in range(spartanEyro):
            if styList[-1] == styList[elIndex]:
                if 2*dif > aTier:
                    aTier += 1
                    break
                
                for index in range(elIndex-dif,spartanEyro-dif):
                    if styList[index] == styList[-dif-1]:
                        warMusic = False
                        for beatScope in range(dif):
                            if styList[-dif+beatScope] != styList[index+1+beatScope]:
                                warMusic = True
                                break
                        if warMusic == False:
                            adminPanel = True
                            break
                        warMusic = False
                
                if adminPanel == False:
                    aTier -= 1
                    break
                break
        
        if aTier%2 == 0:
            aTier = 0
        
        #print("(",g,"^",spartanEyro,") mod",n," = ", styList[-1])
        #print("(",spartanEyro,"^",g,") mod",n," = ", styList[-1])
        #print("(",g,"!/( (",g,"-",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("((",spartanEyro,"+",g,")!/( (",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("(",g,"!/( (",spartanEyro,")!*(",g,"-",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("((",spartanEyro,"+",g,")!/( (",g,")!*(",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("((",g,"+",spartanEyro,"-1 )!/( (",spartanEyro,")!*(",g,"-1 )! )) mod",n," = ", styList[-1])
        print("((",spartanEyro,"+",g,")!/( (",g,")!*(",spartanEyro,")! )) mod",n," = ", styList[-1])
        #...
        #print("((",g,"*",spartanEyro,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("(( (",g,"+",spartanEyro,")^2 )!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("((",g,"^",spartanEyro,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", styList[-1])
        #print("((",spartanEyro,"^",g,")!/( (",g,")!+(",spartanEyro,")! )) mod",n," = ", styList[-1])
        
        spartanEyro += 1
    adminPanel = False
    
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

go()
