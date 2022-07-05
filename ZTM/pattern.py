#WAP to geneate the following pattern.
# 1
# 1 3
# 1 3 5 
# 1 3 5 7
for i in range(3,10,2):
    for j in range(1,i,2):
        print(j,end=" ")
    print()
