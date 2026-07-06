prefix = [2, 6, 7, 14, 17, 23]
out=[]
for i in range(len(prefix)):
    if i==0:
        out.append(prefix[i])
    else:
        out.append(prefix[i]+prefix[i+1])
print(out)