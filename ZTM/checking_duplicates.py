lst=[1,2,3,4,4,8,2,9,1]
duplicate=[]
for i in lst:
    if lst.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)