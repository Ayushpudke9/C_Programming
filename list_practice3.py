# take a list l1 and print sum of 
# all numbers in the list
l1 = [10,34,23,56,78]
print("Addition of all elements is ")
total=0
for idx in range(len(l1)):
    total = total + l1[idx]

print(total)
print("Multiplication of all elements is ")
mult=1
for idx in range(len(l1)):
    mult = mult * l1[idx]
print(mult)
print("Minimum number in the list is .. ")
l1=[10,5,2,7,9,55,1,43]
min_num = l1[0]
for e in l1:
    if e < min_num:
        min_num = e
print(min_num) #1
print("Maximum number in the list is .. ")
l1=[10,5,2,7,9,55,1,43]
max_num = l1[0]
for e in l1:
    if e >  max_num:
        max_num = e
print(max_num)