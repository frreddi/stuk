from random import randint;
from time import sleep;


tog = bool(1);
while tog==1:
    try:
        numb = int(0b110101111110101111110101111110101111110101111110101111);
        #numb = int(input("Input digits: "));
        tog = 0;
    except:
        print("Only whole numbers");
        continue;

length = int(len(str(bin(numb)))-2);
overflow = int(length%8);
byte = int((length-overflow)/8);
if byte<=0:
    byte = 1;
    overflow = 0;

while overflow>0:
    numb ^= 1<<((byte*8)+overflow-1);
    length = int(len(str(bin(numb)))-2);
    if length>8:
        overflow = int(length%8);
    else:
        overflow = -1;

numb ^= 1<<(byte*8);


while True:
    for n in range (0, byte):
        rand = randint(1, 50);
        if rand>36:
            randBit = randint(0, 7);
            numb ^= 1<<(randBit+(n*8));
    
    for n in range (0, rand):
        print(bin(numb));
        sleep(0.007);   #adjust for speed
