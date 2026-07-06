dic={}
for i in range(65,91):
    dic[chr(i)]=chr(i+32)
print(dic)

d=["hai",88,"uday",55,"uday","kumar"]
for c in d:
    if type(c)==str:
        print(c[0]+c[-1])