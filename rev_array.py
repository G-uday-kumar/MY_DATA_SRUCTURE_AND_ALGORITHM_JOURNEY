# arr1=[12,22,43,22,23,54,56]
# rev_are=[]
# length=len(arr1)
# for i in range(length-1,-1,-1):
#     rev_are.append(arr1[i])
# print("reversed array is:-",rev_are)
#
#



class student:
    def __init__(self,fees):
        self.fees = fees

    def __add__(self,other):
        return student(self.fees+other.fees)

    def __str__(self):
        return str(self.fees)


s1=student(75000)
s2=student(200000)
s3=student(100000)
s4=student(50000)
print(s1+s2+s3+s4)




































