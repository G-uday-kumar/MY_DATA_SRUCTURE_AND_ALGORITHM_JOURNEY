arr=[12,22,43,23,54,56]
lar_val=arr[0]
for num in arr:
    if num > lar_val:
        lar_val=num
print(lar_val)


arr1=[12,22,43,23,54,56]
lar_val1=arr1[0]
sec_lar_val1=arr1[1]
for num1 in arr1:
    if num1 > sec_lar_val1 and num1 < lar_val1:
        sec_lar_val1=lar_val1


print(sec_lar_val1)

