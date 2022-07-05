#WAP to display the series  13, -23, 33, -43,.....

for i in range(1,10):
    num = 10
    num = num * i + 3
    if i % 2 == 0:
        print(-num,end=' ')
    else: 
        print(num,end=' ')