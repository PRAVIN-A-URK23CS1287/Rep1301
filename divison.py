divinum=int(input("enter dividend:"))
divonum=int(input("enter divisor:"))
quotient=0
count=divinum
while divinum>0:
    quotient+=1
    divinum-=divonum
print("the quotient of",count,"&",divonum,"is",quotient)
