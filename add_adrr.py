target=9
arrr=[2,4,7]
diiic={}
for i in range(len(arrr)):
    need=target-arrr[i]
    if need in diiic:
        print([diiic[need],i])
    diiic[arrr[i]]=i