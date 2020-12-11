string = input().split()
print(string)
n = int(string[0])
h = int(string[1])
list1 = list(map(int, input().split()))
lat = 0
for student in list1:
    if student > h:
        lat += 2
    else:
        lat += 1
print(lat)