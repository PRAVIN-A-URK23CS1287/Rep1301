l=['L','J']
for i in l:
    x=ord(i)
    while True:
        y=x%2
        print(y,end="")
        x=int(x/2)
        if y==0:
            break
