# gievn list l1 add 10 to every element
# store in new list
# display both lists

l1=[100,5,7,10,50]
new_list=[]
for e in l1:
    t = e+10
    new_list.append(t)
print(l1)
print(new_list)
new_list=[]
for idx in range(len(l1)):
    t = l1[idx]+10
    new_list.append(t)
print(l1)
print(new_list)

l1=[100,5,7,10,50]
l2=[ e for e in l1 ]
print(l2)