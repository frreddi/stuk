from random import randint;
from time import sleep;
from math import floor;


numb = int(0);
w = int(152); #adjust for screen-width
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


while True:
    switchType = randint(1, 100);
    
    if switchType<=51:
        for n in range (0, len(count1["echos"])):
            if count1["echos"][n]<=0:
                count1["delay"][n] -= 1;
                if count1["delay"][n]<=0:
                    numbOfPrints = randint(1, 42);
                    randBit = randint(0, w-1);
                    count1["echos"][n] = numbOfPrints;
                    count1["index"][n] = randBit;
                    count1["delay"][n] = floor(numbOfPrints/4);
                    numb ^= 1<<count1["index"][n];
                    break;
    
    elif switchType>52 and switchType<=83:
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
    
    elif switchType>84:
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
    
    
    print(bin(numb));
    sleep(0.007);   #adjust for speed
    
    
    for n in range (0, len(count1["index"])):
        if count1["echos"][n]>0:
            count1["echos"][n] -= 1;
            if count1["echos"][n]<=0:
                numb ^= 0x1<<count1["index"][n];
    
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
