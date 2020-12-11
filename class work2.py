n = int(input())
list1 = list(map(int,input().split()))
ser = 0
dim = 0
i = 0
while i < n:
    scales = max(list1[0],list1[-1])
    if i % 2 == 0:
        ser += scales
    else:
        dim += scales
    i += 1
    list1.remove(scales)
print(ser,dim)