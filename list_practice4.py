l1 = [10,20,34,23,67,89]
num = int(input("Enter a number to be searched in l1"))
if num in l1:
    print(num, " is present in l1")
else:
    print(num, " is NOT present in l1")


l1 = [10,20,34,10,23,67,89,23,34,99]
# remove duplicate elements and put in new list
# new list should not have duplicate elements
l2=[]
for e in l1:
    # check if it is present in l2
    if e not in l2:
        l2.append(e)
print("Unique values in l1 are ")
print(l2)





