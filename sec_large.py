arr1=[12,22,43,23,54,56]
lar_val1=arr1[0]
sec_lar_val1=arr1[0]
for num1 in arr1:
    if num1 > lar_val1:
        sec_lar_val1=lar_val1
        lar_val1=num1
    elif num1 < lar_val1 and num1 > sec_lar_val1:
        sec_lar_val1=num1

print("Second Large is:-",sec_lar_val1)

