from random import randint;
from time import sleep;
from math import *;


numb = int(0);
w = int(152);   #adjust for screen-width. minimum w >=66
numb ^= 1<<w;

count1 = {
    "echos": [0, 0, 0, 0, 0, 0, 0],
    "index": [0, 0, 0, 0, 0, 0, 0],
    "delay": [0, 0, 0, 0, 0, 0, 0],
    "draws": [0, 0, 0, 0, 0, 0, 0]
};
count2 = {
    "echos": [0, 0, 0, 0, 0],
    "index": [0, 0, 0, 0, 0],
    "delay": [0, 0, 0, 0, 0],
    "draws": [0, 0, 0, 0, 0]
};
count3 = {
    "echos": [0, 0],
    "index": [0, 0],
    "delay": [0, 0],
    "draws": [0, 0]
};
count4 = {
    "echos": [0],
    "index": [0],
    "delay": [7],
    "draws": [0]
};
count5 = {
    "echos": [0],
    "index": [0],
    "delay": [24],
    "draws": [0]
};
count6 = {
    "echos": [0],
    "index": [0],
    "delay": [7],
    "draws": [0]
};
x6 = int(0);
count7 = {
    "echos": [0],
    "index": [0],
    "delay": [6],
    "draws": [0]
};
x7 = int(0);
#x71 = int(1);
#x72 = int(1);
#tog7 = bool(0);
list7 = [49248, 254200, 520700, 1047550, 2097151, 2097151, 1048574, 524284, 131056, 65504, 32704, 7936, 3584, 1024];
count8 = {
    "echos": [0],
    "index": [0],
    "delay": [6],
    "draws": [0]
};
x8 = int(0);
list8 = [49248, 204952, 266500, 526850, 1049601, 0, 1048577, 524290, 393228, 65552, 32800, 24768, 4352, 2560, 1024];


while True:
    switchType = randint(1, 100);
    
    if switchType<=42:
        for n in range (0, len(count1["echos"])):
            if count1["echos"][n]<=0:
                count1["delay"][n] -= 1;
                if count1["delay"][n]<=0:
                    numbOfPrints = randint(1, 42);
                    randBit = randint(0, w-1);
                    count1["echos"][n] = numbOfPrints;
                    count1["index"][n] = randBit;
                    count1["delay"][n] = floor(numbOfPrints/2);
                    numb ^= 1<<count1["index"][n];
                    break;
    
    if switchType>42 and switchType<=66:
        for n in range (0, len(count2["echos"])):
            if count2["echos"][n]<=0:
                count2["delay"][n] -= 1;
                if count2["delay"][n]<=0:
                    numbOfPrints = randint(1, 127);
                    randBit = randint(1, w-2);
                    count2["echos"][n] = numbOfPrints;
                    count2["index"][n] = randBit;
                    count2["delay"][n] = floor(numbOfPrints/4);
                    numb ^= 1<<count2["index"][n];
                    break;
    
    if switchType>66 and switchType<=76:
        for n in range (0, len(count3["echos"])):
            if count3["echos"][n]<=0:
                count3["delay"][n] -= 1;
                if count3["delay"][n]<=0:
                    numbOfPrints = randint(1, 142);
                    randBit = randint(2, w-3);
                    count3["echos"][n] = numbOfPrints;
                    count3["index"][n] = randBit;
                    count3["delay"][n] = floor(numbOfPrints/4);
                    numb ^= 1<<count3["index"][n];
                    break;
    
    if switchType>76 and switchType<=85:
        for n in range (0, len(count4["echos"])):
            if count4["echos"][n]<=0:
                count4["delay"][n] -= 1;
                if count4["delay"][n]<=0:
                    numbOfPrints = 9;
                    randBit = randint(4, w-5);
                    count4["echos"][n] = numbOfPrints;
                    count4["index"][n] = randBit;
                    count4["delay"][n] = numbOfPrints*2;
                    break;
    
    if switchType>85 and switchType<=91:
        for n in range (0, len(count5["echos"])):
            if count5["echos"][n]<=0:
                count5["delay"][n] -= 1;
                if count5["delay"][n]<=0:
                    numbOfPrints = 43;
                    randBit = randint(33, w-33);
                    count5["echos"][n] = numbOfPrints;
                    count5["index"][n] = randBit;
                    count5["delay"][n] = numbOfPrints;
                    break;
    
    if switchType>91 and switchType<=94:
        for n in range (0, len(count6["echos"])):
            if count6["echos"][n]<=0:
                count6["delay"][n] -= 1;
                if count6["delay"][n]<=0:
                    numbOfPrints = randint(42, 94);
                    randBit = randint(0, w-37);
                    count6["echos"][n] = numbOfPrints;
                    count6["index"][n] = randBit;
                    count6["delay"][n] = numbOfPrints;
                    break;
    
    if switchType>94 and switchType<=98:
        for n in range (0, len(count7["echos"])):
            if count7["echos"][n]<=0:
                count7["delay"][n] -= 1;
                if count7["delay"][n]<=0:
                    numbOfPrints = randint(15, 94);
                    randBit = randint(0, w-21);
                    count7["echos"][n] = numbOfPrints;
                    count7["index"][n] = randBit;
                    count7["delay"][n] = numbOfPrints;
                    break;
    
    if switchType>98:
        for n in range (0, len(count8["echos"])):
            if count8["echos"][n]<=0:
                count8["delay"][n] -= 1;
                if count8["delay"][n]<=0:
                    numbOfPrints = randint(15, 94);
                    randBit = randint(0, w-21);
                    count8["echos"][n] = numbOfPrints;
                    count8["index"][n] = randBit;
                    count8["delay"][n] = numbOfPrints;
                    break;
    
    
    print(bin(numb));
    sleep(0.007);   #adjust for speed
    
    
    for n in range (0, len(count1["index"])):
        if count1["echos"][n]>0:
            count1["echos"][n] -= 1;
            if count1["echos"][n]<=0:
                numb ^= 1<<count1["index"][n];
    
    for n in range (0, len(count2["index"])):
        if count2["echos"][n]>0:
            count2["echos"][n] -= 1;
            if count2["draws"][n]<=0:
                if count2["echos"][n]<=0:
                    numb ^= 1<<count2["index"][n];
                elif count2["echos"][n]>85 and (4*count2["delay"][n])-count2["echos"][n]>17:
                    numb ^= 0b101<<(count2["index"][n]-1);
                    count2["draws"][n] = 1;
            elif count2["draws"][n]>=1 and count2["echos"][n]<17:
                numb ^= 0b101<<(count2["index"][n]-1);
                count2["draws"][n] = 0;
    
    for n in range (0, len(count3["index"])):
        if count3["echos"][n]>0:
            count3["echos"][n] -= 1;
            if count3["draws"][n]<=0:
                if count3["echos"][n]<=0:
                    numb ^= 1<<count3["index"][n];
                elif count3["echos"][n]>101 and (4*count3["delay"][n])-count3["echos"][n]>17:
                    numb ^= 0b101<<(count3["index"][n]-1);
                    count3["draws"][n] = 1;
            elif count3["draws"][n]==1 and count3["echos"][n]<85:
                numb ^= 0b10101<<(count3["index"][n]-2);
                count3["draws"][n] = 2;
            elif count3["draws"][n]==2 and count3["echos"][n]<42:
                numb ^= 0b10101<<(count3["index"][n]-2);
                count3["draws"][n] = 3;
            elif count3["draws"][n]>=3 and count3["echos"][n]<17:
                numb ^= 0b101<<(count3["index"][n]-1);
                count3["draws"][n] = 0;
    
    for n in range (0, len(count4["index"])):
        if count4["echos"][n]>0:
            count4["echos"][n] -= 1;
            if count4["echos"][n]>=8:
                numb ^= 0b111<<(count4["index"][n]-1);
            elif count4["echos"][n]==7:
                numb ^= 0b11111<<(count4["index"][n]-2);
            elif count4["echos"][n]==6:
                numb ^= 0b1000001<<(count4["index"][n]-3);
            elif count4["echos"][n]==5:
                numb ^= 0b101100110<<(count4["index"][n]-4);
            elif count4["echos"][n]==4:
                numb ^= 0b110101111<<(count4["index"][n]-4);
            elif count4["echos"][n]==3:
                numb ^= 0b11001001<<(count4["index"][n]-4);
            elif count4["echos"][n]==2:
                numb ^= 0b1000001<<(count4["index"][n]-3);
            elif count4["echos"][n]==1:
                numb ^= 0b11111<<(count4["index"][n]-2);
            elif count4["echos"][n]<=0:
                numb ^= 0b111<<(count4["index"][n]-1);
    
    for n in range (0, len(count5["index"])):
        if count5["echos"][n]>0:
            count5["echos"][n] -= 1;
            if count5["echos"][n]>=42:
                numb ^=                  0b000000000000000000000000000001111111100000000000000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]>=41:
                numb ^=                  0b000000000000000000000001111110000000011111100000000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]>=40:
                numb ^=                  0b000000000000000000001110000000000000000000011100000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==39:
                numb ^=                  0b000000000000000001110000000000000000000000000011100000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==38:
                numb ^=                  0b000000000000000110000000000000000000000000000000011000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==37:
                numb ^=                  0b000000000000011000000000000000000000000000000000000110000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==36:
                numb ^=                  0b000000000000100000000011111100000000001111110000000001000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==35:
                numb ^=                  0b000000000001000001111100000011110011110000001111100000100000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==34:
                numb ^=                  0b000000000010001110000000000000001100000000000000011100010000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==33:
                numb ^=                  0b000000000100110000000000000000000000000000000000000011001000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==32:
                numb ^=                  0b000000001001000000000000000000000000000000000000000000100100000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==31:
                numb ^=                  0b000000010010000000000000000000000000000000000000000000010010000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==30:
                numb ^=                  0b000000100100000000000000000000000000000000000000000000001001000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==29:
                numb ^=                  0b000000001000000000000000000000000000000000000000000000000100000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==28:
                numb ^=                  0b000001010000000000000000000000000000000000000000000000000010100000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==27:
                numb ^=                  0b000010100000000111111111111110000000011111111111111000000001010000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==26:
                numb ^=                  0b000100000000111000000000000001100001100000000000000111000000001000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==25:
                numb ^=                  0b010000111111000000000000000000011110000000000000000000111111000010  <<(count5["index"][n]-33);
            elif count5["echos"][n]==24:
                numb ^=                  0b111001111111000000000000000000111111000000000000000000111111100111  <<(count5["index"][n]-33);
            elif count5["echos"][n]==23:
                numb ^=                  0b000110000000100000000000000001100001100000000000000001000000011000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==22:
                numb ^=                  0b111100000000010000000000000010000000010000000000000010000000001111  <<(count5["index"][n]-33);
            elif count5["echos"][n]==21:
                numb ^=                  0b010000000000001000000000000101100001101000000000000100000000000010  <<(count5["index"][n]-33);
            elif count5["echos"][n]==20:
                numb ^=                  0b000110000000000111111111111000000000000111111111111000000000011000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==19:
                numb ^=                  0b000000000000000000000000000011010010110000000000000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==18:
                numb ^=                  0b000011000000000000000000000010111111010000000000000000000000110000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==17:
                numb ^=                  0b000001100000000000000000000000101101000000000000000000000001100000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==16:
                numb ^=                  0b000000110000000000000000000000000000000000000000000000000011000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==15:
                numb ^=                  0b000000011000000000011100000000000000000000001110000000000110000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==14:
                numb ^=                  0b000000001110000000011111111111111111111111111110000000011100000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==13:
                numb ^=                  0b000000000111000000000011111000000000000111110000000000111000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==12:
                numb ^=                  0b000000000001100000000000000111111111111000000000000001100000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==11:
                numb ^=                  0b000000000000111000000000000000000000000000000000000111000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==10:
                numb ^=                  0b000000000000011111111100000000000000000000001111111110000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==9:
                numb ^=                  0b000000000000000111011111111100000000001111111110111000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==8:
                numb ^=                  0b000000000000000000111011111111111111111111110111000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==7:
                numb ^=                  0b000000000000000000100111111011111111110111111001000000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==6:
                numb ^=                  0b000000000000000011000000000111111111111000000000110000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==5:
                numb ^=                  0b000000000001111100000000000000000000000000000000001111100000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==4:
                numb ^=                  0b000000000010000000000000000000000000000000000000000000010000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==3:
                numb ^=                  0b000000000010000000000000000000000000000000000000000000010000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==2:
                numb ^=                  0b000000000001111100000000000000000000000000000000001111100000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]==1:
                numb ^=                  0b000000000000000011111111111110000000011111111111110000000000000000  <<(count5["index"][n]-33);
            elif count5["echos"][n]<=0:
                numb ^=                  0b000000000000000000000000000001111111100000000000000000000000000000  <<(count5["index"][n]-33);
    
    for n in range (0, len(count6["index"])):
        if count6["echos"][n]>0:
            if count6["echos"][n]<count6["delay"][n]:
                numb ^= 1<<(count6["index"][n]+x6);
            count6["echos"][n] -= 1;
            if count6["echos"][n]>0:
                
                
                #x6 = count6["delay"][n]-count6["echos"][n];   #import fourier & pepe
                
                #x6 = count6["delay"][n]-count6["echos"][n];
                #x6 ^= 0b110;
                
                #x6 = count6["delay"][n]-count6["echos"][n];
                #x6 = floor( exp(x6/22) );
                
                #x6 = count6["delay"][n]-count6["echos"][n];
                #x6 = floor( 6*sin(x6*0.6) +6 );
                
                x6 = count6["delay"][n]-count6["echos"][n];
                x6 = floor( 6*sin(x6) + 6*sin(x6*0.6) + 6*sin(x6*0.36) +18 );
                
                
                numb ^= 1<<(count6["index"][n]+x6);
    
    for n in range (0, len(count7["index"])):
        if count7["echos"][n]>0:
            if count7["echos"][n]<count7["delay"][n]:
                numb ^= x7<<(count7["index"][n]);
            count7["echos"][n] -= 1;
            if count7["echos"][n]>0:
                
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                #x7 ^= 0b110;
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                #x7 = ceil( pow(2, x7) );
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                #x7 = floor( exp(x7/3) );
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                #x7 = floor( 6*sin(x7*0.7) );
                
                #x7 = count7["delay"][n]-count7["echos"][n];
                #x7 = floor( 6*sin(x7) + 6*sin(x7*0.7) + 6*sin(x7*0.49) +18 );
                
                #if tog7==0:
                #    x71 = x71+x72;
                #    x7 = x71;
                #    tog7=1;
                #elif tog7==1:
                #    x72 = x71+x72;
                #    x7 = x72;
                #    tog7=0;
                #if count7["echos"][n]==1:
                #    x71 = 1;
                #    x72 = 1;
                
                x7 = count7["delay"][n]-count7["echos"][n] -1;
                x7 = list7[x7%len(list7)];
                
                
                numb ^= x7<<(count7["index"][n]);
    
    for n in range (0, len(count8["index"])):
        if count8["echos"][n]>0:
            
            if count8["echos"][n]>(count8["delay"][n]%len(list8)):
                x8 = count8["delay"][n]-count8["echos"][n];
                x8 = list8[(x8%len(list8))];
            else:
                x8 = 0;
            if count8["echos"][n]==1:
                print("0b1"+"oHelloStanley"*(w//13));
            
            numb ^= x8<<(count8["index"][n]);
            count8["echos"][n] -= 1;
