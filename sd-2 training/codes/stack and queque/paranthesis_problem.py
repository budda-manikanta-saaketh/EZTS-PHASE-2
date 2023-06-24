#get combination of parenthesis and check whether it is balanced or not
st=input("enter the string:")
li=[i for i in st]
li2=[]
if len(li)%2!=0:
    print(False)
elif li[0]==')' or li[0]=='}' or li[0]==']':
    print(False)
else:
    for i in range(len(li)):
        if li[i]=='(' or li[i]=='{' or li[i]=='[':
            li2.append(li[i])
        if li[i]==')' and li2[len(li2)-1]=='(':
            li2.pop()
            continue
        if li[i]==']' and li2[len(li2)-1]=='[':
            li2.pop()
            continue
        if li[i]=='}' and li2[len(li2)-1]=='{':
            li2.pop()
            continue
        if len(li2)==0:
            break
    if len(li2)==0:
        print(True)
    else:
        print(False)
        

