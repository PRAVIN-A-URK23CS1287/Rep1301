import csv
fh=open('10th marks.csv','w',newline='')
stw=csv.writer(fh)
stw.writerow(['subject','grade','marks'])
for i in range(5):
    print('10th marks report for subject:',(i+1))
    sub=input('enter suject:')
    gdr=input('enter grade:')
    mks=input('enter marks:')
    l=[sub,gdr,mks]
    stw.writerow(l)
fh.close()
with open("10th marks.csv","r") as fh:
    fs=csv.reader(fh)
    for i in fs:
        print(i)
fh.close()
          
