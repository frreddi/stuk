
f = [0, 1];
sumed = [0, 1];
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
            sumed.append(sumed[n]+f[n+1]);
        highest = numb;
    
    print("Number", numb, "in the Fibonacci sequence:", f[numb]);
    print("Sum after", numb, "Fibonacci numbers:", sumed[numb], "\n");
    #print("Sequence:", f);
    #print("Sum:", sumed, "\n\n\n");