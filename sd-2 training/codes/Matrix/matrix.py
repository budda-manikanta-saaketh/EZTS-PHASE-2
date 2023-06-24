#get 1 matrix as input and display same diagonal elements, non diagonal elements, upper diagonal and lower diagonal elements.
li=[]
diagonal=[]
ut=[]
lt=[]
r=int(input("enter no of rows:"))
c=int(input("enter no of coloums:"))
if(r==c):
    for i in range(r):
        li2=list(map(int,input().split(" ")))
        li.append(li2)
    for i in range(c):
        diagonal.append(li[i][i])
    for i in range(c):
        for j in range(c):
            if i<(r+c)/2 and i!=j:
                ut.append(li[i][j])
            if i>(r+c)/2 and i!=j:
                lt.append(li[i][j])
    print(diagonal)
    print(ut)
    print(lt)
else:
    print("not possible with rectangular matrix")
    