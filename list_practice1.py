l1= []
for i in range(5):
    num = int(input("Enter next no"))
    #l1 = []
    l1.append(num)

print(l1)
print("Print using for loop")
for idx in range(len(l1)):# idx is index of the element
    print(l1[idx])

print("Print using ANOTHER for loop")
for e in l1: # e will have one element at a time
    print(e)
