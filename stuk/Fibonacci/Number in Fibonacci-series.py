
f = [0, 1];
numb = int(0);
highest = int(1);


while True:
    try:
        numb = abs(int(input("Number in the Fibonacci sequence: ")));
    except:
        print("Input digit");
        continue;
    
    if numb>highest:
        for n in range (highest, numb):
            f.append(f[n-1]+f[n]);
        highest = numb;
    
    print("Number", numb, "in the Fibonacci sequence:", f[numb], "\n");
    #print("Sequence:", f, "\n\n\n");
