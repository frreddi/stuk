

f = [0, 1];
highest = int(1);


while True:
    try:
        numb = int(input("Number in the Fibonacci sequence: "));
    except:
        print("Input a whole number");
        continue;
    
    if numb>highest:
        for n in range (highest, numb):
            f.append(f[n-1]+f[n]);
        highest = numb;
    
    if abs(numb)<=highest+1:
        print("Number", numb, "in the Fibonacci sequence:", f[numb], "\n");
        #print("Sequence:", f, "\n\n\n");
    else:
        print("Number is to low");
