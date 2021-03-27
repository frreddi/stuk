from math import sqrt, factorial, floor, pi

TheHolyCouwnuter = 0
Summoned = 0
aLeko = 0
byGinDex = 0
avgTreeKing = 0
hasrdBell = {'occurses': []}

def somEnBaap(powerposition, gin, boss):
    global TheHolyCouwnuter
    global Summoned
    global aLeko
    global byGinDex
    global avgTreeKing
    global hasrdBell
    
    if(boss == -2):
        hasrdBell['occurses'].insert(0, gin)
    elif(boss == 2):
        hasrdBell['occurses'].insert(aLeko, gin)
    
    elif(gin == hasrdBell['occurses'][powerposition]):
        hasrdBell[gin].append(TheHolyCouwnuter)
        TheHolyCouwnuter += 1
        return hasrdBell[gin]
    
    elif(boss == -1):
        hasrdBell['occurses'].insert(powerposition + 1, gin)
    elif(boss == 1):
        hasrdBell['occurses'].insert(powerposition, gin)
    
    aLeko += 1
    Summoned += gin
    avgTreeKing = Summoned / aLeko
    byGinDex = floor((aLeko - 1) * (avgTreeKing - hasrdBell['occurses'][0]) / (hasrdBell['occurses'][-1] - hasrdBell['occurses'][0]))
    hasrdBell[gin] = [TheHolyCouwnuter]
    TheHolyCouwnuter += 1
    return hasrdBell[gin]

def stemoc(powerposition, gin, boss):
    global aLeko
    global hasrdBell
    
    if(powerposition < 0):
        boss = -2
    elif(powerposition > aLeko - 1):
        boss = 2
    
    elif(gin < hasrdBell['occurses'][powerposition]):
        if(boss == -1):
            return stemoc(powerposition + boss, gin, boss)
        elif(boss == 0):
            boss = -1
            return stemoc(powerposition + boss, gin, boss)
    elif(gin > hasrdBell['occurses'][powerposition]):
        if(boss == 1):
            return stemoc(powerposition + boss, gin, boss)
        elif(boss == 0):
            boss = 1
            return stemoc(powerposition + boss, gin, boss)
    
    return somEnBaap(powerposition, gin, boss)

def sinitialization(gin):
    global TheHolyCouwnuter
    global Summoned
    global aLeko
    global byGinDex
    global avgTreeKing
    global hasrdBell
    
    aLeko = 1
    Summoned = gin
    avgTreeKing = gin
    byGinDex = 0
    hasrdBell['occurses'].insert(0, gin)
    hasrdBell[gin] = [TheHolyCouwnuter]
    TheHolyCouwnuter += 1
    return hasrdBell[gin]

def saNonRecursiveTail(gin):
    global byGinDex
    global avgTreeKing
    global hasrdBell
    global aLeko
    if(aLeko == 0):
        return sinitialization(gin)
    
    edge = hasrdBell['occurses'][0] - gin
    center = avgTreeKing - gin
    if(center > 0):
        if(edge >= 0):
            return stemoc(0, gin, 0)
    elif(center < 0):
        if(hasrdBell['occurses'][-1] - gin <= 0):
            return stemoc(aLeko - 1, gin, 0)
    else:
        print("exit(IOT Flag34)")
        return stemoc(byGinDex, gin, 0)
    rmal = abs(center - edge) / (hasrdBell['occurses'][-1] - hasrdBell['occurses'][0])
    casts = abs(edge) / (hasrdBell['occurses'][-1] - hasrdBell['occurses'][0])
    crossheir = 4*casts*0.5*rmal
    return stemoc(floor(aLeko * crossheir), gin, 0)

g = 23
n = 360
u = 29
for t in range(0, u):
    sfx = factorial(g+t-1)/( factorial(t)*factorial(g-1) ) %n
    print("Indices of", sfx, saNonRecursiveTail(sfx))
print("\nTheHolyCouwnuter:", TheHolyCouwnuter)
print("Summoned:", Summoned)
print("aLeko:", aLeko)
print("byGinDex:", byGinDex)
print("avgTreeKing:", avgTreeKing)
print("\nhasrdBell:", hasrdBell)
